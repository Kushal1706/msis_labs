Architecture of Big Data Systems
LAB 1: Hadoop HDFS Basic Commands
1. Start the Environment
Open Oracle VM VirtualBox.
Start the Ubuntu virtual machine.
Open the terminal.

Command: Login to MySQL

# Log in to MySQL as the root user
sudo mysql -u root -p


Command: Start Hadoop Services

Open a new terminal and execute:

# Start HDFS and YARN services
start-dfs.sh && start-yarn.sh

2. View the HDFS Root Directory

Command:

# Display all files and directories in the HDFS root directory
hdfs dfs -ls /


Explanation: Lists all files and directories available in HDFS.

3. Create a Directory

Command:

# Create a directory named practice_lab1 in HDFS
hdfs dfs -mkdir /practice_lab1


Verify the directory:

# List the root directory to check whether practice_lab1 exists
hdfs dfs -ls /


Explanation: Creates a new directory in HDFS.

4. Upload a File to HDFS

Command:

# Upload practice_lab.txt from the local system to HDFS
hdfs dfs -put practice_lab.txt /practice_lab1


Explanation: Uploads the local file practice_lab.txt into the HDFS directory /practice_lab1.

Note: If the file already exists, Hadoop displays a File exists error.

5. View the Contents of a File

Command:

# Display the contents of the file stored in HDFS
hdfs dfs -cat /practice_lab1/practice_lab.txt


Explanation: Displays the contents of the file directly in the terminal.

Output:

This is some random text for the abd lab
hello world
msis manipal
jai hind jai karanataka mate
kannadave satya kannadave nitya
I love my country India

6. Download a File from HDFS

Command:

# Download the file from HDFS to the current local directory
hdfs dfs -get /practice_lab1/practice_lab.txt .


Explanation: Downloads the file from HDFS to your current local directory.

Note: Choose a local directory where you have permission to save files.

7. Copy a File in HDFS

Command:

# Copy the file to the HDFS /tmp directory
hdfs dfs -cp /practice_lab1/practice_lab.txt /tmp


Explanation: Creates a copy of the file in /tmp. The original file remains unchanged.

8. Move a File in HDFS

Command:

# Move DemoFile.txt from BDA2026ABD to the /tmp directory
hdfs dfs -mv /BDA2026ABD/DemoFile.txt /tmp


Explanation: Moves the file to /tmp and removes it from its original location.

Note: The source file must exist for the command to work.

9. Delete a File or Directory

Command:

# Remove the HDFS path named lab1
hdfs dfs -rm /lab1


Explanation: Removes the specified file or an empty directory, depending on the Hadoop version.

Note: Always verify the path before deleting anything.

10. Rename a File

Command:

# Rename practice_lab.txt to practicw_lab1.txt
hdfs dfs -mv /practice_lab1/practice_lab.txt /practice_lab1/practicw_lab1.txt


Explanation: Changes the filename without downloading or uploading the file again.

Verify the new filename:

# List the files in practice_lab1
hdfs dfs -ls /practice_lab1

11. Common Errors
Error	Reason
File exists	The destination file already exists.
No such file or directory	The specified file or path does not exist.
Permission denied	You do not have permission to access the destination.
hdfs: command not found	Hadoop is not available in the command environment or PATH.
Conclusion

In this lab, we learned basic Hadoop HDFS commands for creating directories, uploading and downloading files, viewing file contents, copying files, moving files, renaming files, and deleting files.

These commands provide a foundation for working with Hadoop and big data systems.

References
Apache Hadoop Documentation
HDFS Commands Guide
