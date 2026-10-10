# Architecture of Big Data Systems

## LAB 1: Hadoop HDFS Basic Commands

### Objective
To learn basic Hadoop Distributed File System (HDFS) commands, such as 
creating directories, uploading files, viewing file contents, copying files, 
moving files, renaming files, and deleting files.

### 1. Start the Environment

- Open Oracle VM VirtualBox.
- Start the Ubuntu virtual machine.
- Open the terminal.

Log in to MySQL as the root user

sudo mysql -u root -p


Open another terminal and start Hadoop services:

Start HDFS and YARN services

start-dfs.sh && start-yarn.sh


### 2. View the HDFS Root Directory

List all files and directories in the HDFS root directory

hdfs dfs -ls /


**Explanation:** Displays the directories available in HDFS, such as `/tmp` and `/user`.

### 3. Create a Directory

Create a new directory named practice_lab1 in HDFS

hdfs dfs -mkdir /practice_lab1


Verify the directory:

Check whether the directory was created

hdfs dfs -ls /


**Explanation:** Creates a directory in HDFS where we can store files.

### 4. Upload a File to HDFS

Upload practice_lab.txt from the local system to HDFS

hdfs dfs -put practicelab.txt /practicelab1


**Explanation:** Transfers the local file `practice_lab.txt` into the HDFS directory `/practice_lab1`.

**Note:** If the file already exists, Hadoop displays a `File exists` error.

### 5. View File Contents

Display the contents of the file stored in HDFS

hdfs dfs -cat /practicelab1/practicelab.txt


**Explanation:** Displays the text stored in the file directly in the terminal.

### 6. Download a File from HDFS

Download the file to the current local directory

hdfs dfs -get /practicelab1/practicelab.txt .


**Explanation:** Copies the file from HDFS to the local system.

**Note:** Use a local directory where you have permission to save files.

### 7. Copy a File in HDFS

Copy the file from practice_lab1 to the HDFS /tmp directory

hdfs dfs -cp /practicelab1/practicelab.txt /tmp


**Explanation:** Creates a copy of the file in `/tmp`. The original file remains unchanged.

### 8. Move a File in HDFS

Move DemoFile.txt from BDA2026ABD to the /tmp directory

hdfs dfs -mv /BDA2026ABD/DemoFile.txt /tmp


**Explanation:** Moves the file to `/tmp` and removes it from its original location.

**Note:** The source file must exist for the command to work.

### 9. Delete a File or Directory

Remove the HDFS path named lab1

hdfs dfs -rm /lab1


**Explanation:** Deletes the specified file or an empty directory, depending on the Hadoop version.

**Note:** Verify the path before deleting anything.

### 10. Rename a File

Rename the file in HDFS

hdfs dfs -mv /practicelab1/practicelab.txt /practicelab1/practicwlab1.txt


**Explanation:** Changes the filename without downloading or uploading the file again.

Verify the new filename:

Display the files inside practice_lab1

hdfs dfs -ls /practice_lab1


### Common Errors

Error	Reason
File exists	The destination file already exists.
No such file or directory	The filename or path is incorrect.
Permission denied	You do not have permission to access the destination.
hdfs: command not found	Hadoop is not available in the command environment or PATH.
Conclusion

In this lab, we learned the basic HDFS commands used to manage files and directories.

We practiced creating directories, uploading and downloading files, viewing file contents, copying files, moving files, renaming files, and deleting files.

These commands provide a foundation for working with Hadoop and big data systems.
References

    Apache Hadoop Documentation
    HDFS Commands
