Architecture of Big Data Systems
LAB 1: Hadoop HDFS Basic Commands
Objective

To learn basic HDFS commands for creating directories, uploading files, viewing file contents, downloading files, copying files, moving files, renaming files, and deleting files.
1. Start Hadoop Services

Open Oracle VM VirtualBox, start Ubuntu, and open the terminal.

Command 1: Log in to MySQL

sudo mysql -u root -p

Purpose: Logs in to MySQL as the root user.

Command 2: Start HDFS and YARN

Open a new terminal and execute:

start-dfs.sh && start-yarn.sh

Purpose: Starts Hadoop's storage and resource-management services.
2. List HDFS Directories

Command:

hdfs dfs -ls /

Purpose: Displays all files and directories in the HDFS root directory.
3. Create a Directory

Command:

hdfs dfs -mkdir /practice_lab1

Purpose: Creates a directory named practice_lab1 in HDFS.

Verify the directory:

hdfs dfs -ls /

Purpose: Checks whether the directory was created successfully.
4. Upload a File to HDFS

Command:

hdfs dfs -put practice_lab.txt /practice_lab1

Purpose: Uploads the local file practice_lab.txt to HDFS.

Important: If the file already exists, Hadoop displays a File exists error.
5. Display File Contents

Command:

hdfs dfs -cat /practice_lab1/practice_lab.txt

Purpose: Displays the contents of the file stored in HDFS.

Sample output:

This is some random text for the abd lab
hello world
msis manipal
jai hind jai karanataka mate
kannadave satya kannadave nitya
I love my country India

6. Download a File from HDFS

Command:

hdfs dfs -get /practice_lab1/practice_lab.txt .

Purpose: Downloads the file to your current local directory.

The . represents the current directory.
7. Copy a File in HDFS

Command:

hdfs dfs -cp /practice_lab1/practice_lab.txt /tmp

Purpose: Copies the file to the HDFS /tmp directory without deleting the original.
8. Move a File in HDFS

Command:

hdfs dfs -mv /BDA2026ABD/DemoFile.txt /tmp

Purpose: Moves DemoFile.txt from /BDA2026ABD to /tmp.

Note: The source file must exist for this command to work.
9. Delete a File

Command:

hdfs dfs -rm /lab1

Purpose: Removes the specified HDFS path if it is a file or, depending on the Hadoop version, an empty directory.

Warning: Check the path before deleting anything.
10. Rename a File

Command:

hdfs dfs -mv /practice_lab1/practice_lab.txt /practice_lab1/practicw_lab1.txt

Purpose: Renames the file without downloading or uploading it again.

Verify the filename:

hdfs dfs -ls /practice_lab1

Purpose: Displays the files in the directory to verify the rename.
11. Common Errors
Error	Meaning
File exists	The destination file already exists.
No such file or directory	The specified path or filename is incorrect.
Permission denied	You do not have permission to access the destination.
hdfs: command not found	Hadoop is unavailable in the command environment or PATH.
Conclusion

In this lab, we learned how to use basic Hadoop HDFS commands to create directories, upload and download files, view file contents, copy files, move files, rename files, and delete files.

These commands provide a foundation for working with Hadoop and big data systems.
References

    Apache Hadoop Documentation
    HDFS Commands Guide
