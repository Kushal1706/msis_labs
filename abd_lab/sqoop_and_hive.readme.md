# Sqoop & Hive Lab: MySQL ↔ HDFS ↔ Hive
 
Hands-on lab covering data transfer between **MySQL** and **HDFS** using **Apache Sqoop**, and loading that data into **Apache Hive**.
 
**Environment:** Ubuntu VM (VirtualBox) · Hadoop · Sqoop 1.4.7 · Hive 3.1.2 · MySQL 5.7
 
---
 
## Workflow
 
```
MySQL  ──(sqoop import)──▶  HDFS  ──(load data inpath)──▶  Hive
MySQL  ◀──(sqoop export)──  HDFS
```
 
## Contents
 
1. [Start Hadoop services](#1-start-hadoop-services)
2. [MySQL setup](#2-mysql-setup)
3. [Sqoop import (MySQL → HDFS)](#3-sqoop-import-mysql--hdfs)
4. [Sqoop export (HDFS → MySQL)](#4-sqoop-export-hdfs--mysql)
5. [Hive (HDFS → Hive)](#5-hive-hdfs--hive)
6. [Common errors and fixes](#6-common-errors-and-fixes)
> **Note:** Replace `your_password` with your MySQL password. Using `-P` instead of `--password` is safer, as it prompts you for the password instead of exposing it in the command.
 
---
 
## 1. Start Hadoop services
 
```bash
start-dfs.sh && start-yarn.sh
```
 
Check that everything is running:
 
```bash
jps
```
 
---
 
## 2. MySQL setup
 
Open the MySQL shell:
 
```bash
sudo mysql -u root -p
```
 
### Create database and tables
 
```sql
SHOW DATABASES;
CREATE DATABASE school;
USE school;
 
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  city VARCHAR(20)
);
 
CREATE TABLE teachers (
  teacher_id INT PRIMARY KEY,
  teacher_name VARCHAR(30),
  subject VARCHAR(20)
);
 
CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(20),
  teacher_id INT,
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);
```
 
### Insert sample data
 
```sql
INSERT INTO students VALUES
  (1,'kushal',22,'chithradurga'),
  (2,'name1',934,'fgg'),
  (3,'name2',35,'sdfgsd');
 
INSERT INTO teachers VALUES
  (101,'ramesh','database'),
  (102,'deepak rao','abd');
 
INSERT INTO courses VALUES
  (201,'my_sql',101),
  (202,'spark',102);
```
 
### Verify
 
```sql
SHOW TABLES;
SELECT * FROM students;
DESCRIBE students;
```
 
### Create a user for Sqoop
 
```sql
GRANT ALL PRIVILEGES ON *.* TO 'kushal'@'localhost' IDENTIFIED BY 'your_password';
```
 
### Create the target database for export (used in Section 4)
 
```sql
CREATE DATABASE exportfromhdfs;
USE exportfromhdfs;
 
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(50),
  age INT
);
```
 
---
 
## 3. Sqoop import (MySQL → HDFS)
 
### List tables in a database
 
```bash
sqoop list-tables \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password
```
 
### Import a single table (`--target-dir`)
 
Writes the data directly into the given directory.
 
```bash
sqoop import \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --table students \
  --target-dir '/test-order'
```
 
### Import a single table (`--warehouse-dir`)
 
Creates a **subfolder named after the table** inside the given directory (`/school/teachers`).
 
```bash
sqoop import \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --table teachers \
  --warehouse-dir '/school'
```
 
### Import all tables
 
```bash
sqoop import-all-tables \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --warehouse-dir '/practice_lab_table'
```
 
### Import all tables except some
 
```bash
sqoop import-all-tables \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --warehouse-dir '/school_except' \
  --exclude-tables teachers
```
 
### Import with a filter (`--where`)
 
```bash
sqoop import \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --table teachers \
  --target-dir '/teachers_partial' \
  --where "subject='database'"
```
 
### Import selected columns (`--columns`)
 
```bash
sqoop import \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --table students \
  --columns student_id,name \
  --warehouse-dir '/school_col'
```
 
### Import using a single mapper (`-m 1`)
 
```bash
sqoop import \
  --connect jdbc:mysql://localhost/school?useSSL=false \
  --username kushal --password your_password \
  --table teachers \
  --target-dir '/school_teachers1' \
  -m 1
```
 
### Check the imported data in HDFS
 
```bash
hdfs dfs -ls /school_col/students
hdfs dfs -cat /school_col/students/part-m-*
```
 
---
 
## 4. Sqoop export (HDFS → MySQL)
 
Export HDFS data (`/school_col/students`, which has `student_id,name`) into the MySQL table `exportfromhdfs.students`.
 
```bash
sqoop export \
  --connect jdbc:mysql://localhost/exportfromhdfs?useSSL=false \
  --username kushal --password your_password \
  --table students \
  --export-dir '/school_col/students'
```
 
Verify in MySQL:
 
```sql
USE exportfromhdfs;
SELECT * FROM students;
```
 
```
+------------+--------------+------+
| student_id | student_name | age  |
+------------+--------------+------+
|          1 | kushal       | NULL |
|          2 | name1        | NULL |
|          3 | name2        | NULL |
+------------+--------------+------+
```
 
> `age` is `NULL` because the exported HDFS data only contained two columns.
 
---
 
## 5. Hive (HDFS → Hive)
 
Open Hive:
 
```bash
hive
```
 
### Create and select a database
 
```sql
CREATE DATABASE hive_test_db1;
USE hive_test_db1;
```
 
### Create a table
 
Hive does not enforce primary or foreign keys, so create a plain table that matches the comma-separated files Sqoop wrote.
 
```sql
CREATE TABLE courses (
  course_id INT,
  course_name STRING,
  teacher_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```
 
### Load data from HDFS
 
```sql
LOAD DATA INPATH '/school_except/courses' INTO TABLE hive_test_db1.courses;
```
 
> `LOAD DATA INPATH` **moves** the files from the HDFS source path into the Hive warehouse; they will no longer exist at the original location.
 
### Query
 
```sql
SELECT * FROM courses;
```
 
---
 
## 6. Common errors and fixes
 
| Error | Cause | Fix |
|---|---|---|
| `Unrecognized argument: --pasword` | Typo in option name | Use `--password` |
| `No manager for connect string: jdbc:mysql:localhost/...` | Missing `//` in the JDBC URL | Use `jdbc:mysql://localhost/...` |
| SQL syntax error near `==` | `--where` uses SQL, not Java/Python | Use `=` : `--where "teacher_id=102"` |
| SQL syntax error near `)` with `subject=database` | String value not quoted | Use `--where "subject='database'"` |
| `Input path does not exist` on export | Wrong HDFS path | Check with `hdfs dfs -ls /` |
| `Path is not a file: /school/teachers` | `--export-dir` pointed at a directory containing sub-directories | Point to the directory that directly contains `part-m-*` files |
| `Unknown database 'exportfromhdfs'` | Database not created yet | Create it in MySQL first |
| Job fails: export of `teachers` data into `students` table | Table structure doesn't match the data | Export data into a table with matching columns |
| `Invalid Constraint syntax ENABLE/ENFORCED` in Hive | Hive doesn't support enforced PK/FK | Create the table without constraints |
| `Database already exists` in Hive | Name already used | Use another name or `CREATE DATABASE IF NOT EXISTS ...` |
| `bad substitution` / HBase / HCatalog warnings | Optional components not configured | Safe to ignore for this lab |
 
---
 
## Quick reference
 
| Task | Command |
|---|---|
| Import one table | `sqoop import --table <t> --target-dir <dir>` |
| Import under a parent dir | `sqoop import --table <t> --warehouse-dir <dir>` |
| Import all tables | `sqoop import-all-tables --warehouse-dir <dir>` |
| Skip tables | `--exclude-tables <t1,t2>` |
| Filter rows | `--where "<condition>"` |
| Select columns | `--columns col1,col2` |
| Single mapper | `-m 1` |
| Export to MySQL | `sqoop export --table <t> --export-dir <dir>` |
| Load into Hive | `LOAD DATA INPATH '<hdfs_path>' INTO TABLE <t>;` |
