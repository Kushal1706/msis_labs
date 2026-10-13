# LAB PROGRAM: IMPLEMENTATION OF MAPREDUCE USING HADOOP

## AIM
To implement a MapReduce program using Java in Eclipse and execute it
on Hadoop to process a text file stored in HDFS.

---

## STEP 1: CREATE DIRECTORIES IN HDFS

Open the terminal and execute the following commands to create the
required input directory.

    hdfs dfs -mkdir -p /mrjobs/input


Check whether the directory has been created:

    hdfs dfs -ls /mrjobs


Create a text file named `word.txt` on your local system.

    Example content for `word.txt`:
    hello world hello hadoop mapreduce program hadoop mapreduce


Upload the text file to HDFS:

    hdfs dfs -put word.txt /mrjobs/input/


Verify that the file has been uploaded successfully:

    hdfs dfs -ls /mrjobs/input


**Note:** Do not create the output directory in advance.
Hadoop will automatically create it when the MapReduce program runs.

---

## STEP 2: OPEN ECLIPSE WORKSPACE

  1. Open Eclipse IDE.
  2. Select the workspace directory.
  3. If the workspace directory is already selected, click Continue or Launch.
  4. Wait for Eclipse to load the workspace.
  
  ---

## STEP 3: CREATE A JAVA PROJECT

  1. Click File → New → Java Project.
  2. Enter the project name.
  
     Example: `WordCountProject`
  
  3. Click Next.
  4. Click Finish.
  5. If a module-info.java prompt appears, you can avoid creating a
     module descriptor for this Hadoop project.
  
  ---

## STEP 4: CREATE A SOURCE FOLDER
  
  1. Right-click the Java project.
  2. Select New → Source Folder.
  3. Enter the source folder name.
  
     Example: `src`
  
  4. Click Finish.
  
  ---

## STEP 5: CREATE A JAVA PACKAGE

  1. Right-click the `src` folder.
  2. Select New → Package.
  3. Enter the package name.
  
     Example: `com.hadoop.mapreduce`
  
  4. Click Finish.
  
  ---

## STEP 6: CREATE A JAVA CLASS
  
  1. Right-click the package you created.
  2. Select New → Class.
  3. Enter the class name.
  
     Example: `WordCount`
  
  4. Select the option:
  
     `public static void main(String[] args)`

5. Click Finish.

---

## STEP 7: WRITE THE MAPREDUCE PROGRAM

Replace the contents of the generated Java class with the following
WordCount MapReduce program.

  File name: `WordCount.java`
  
  package com.hadoop.mapreduce;
  
  import java.io.IOException; import java.util.StringTokenizer;
  
  import org.apache.hadoop.conf.Configuration; import org.apache.hadoop.fs.Path; import org.apache.hadoop.io.IntWritable; import org.apache.hadoop.io.Text; import org.apache.hadoop.mapreduce.Job; import org.apache.hadoop.mapreduce.Mapper; import org.apache.hadoop.mapreduce.Reducer; import org.apache.hadoop.mapreduce.lib.input.FileInputFormat; import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
  
  public class WordCount {
  
  public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
  
  private final static IntWritable one = new IntWritable(1); private Text word = new Text();
  
  public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
  
  StringTokenizer itr = new StringTokenizer(value.toString());
  
  while (itr.hasMoreTokens()) { word.set(itr.nextToken()); context.write(word, one); } } }
  
  public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
  
  private IntWritable result = new IntWritable();
  
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
  
  int sum = 0;
  
  for (IntWritable val : values) { sum += val.get(); }
  
  result.set(sum); context.write(key, result); } }
  
  public static void main(String[] args) throws Exception {
  
  if (args.length != 2) { System.err.println( "Usage: WordCount <input path> <output path>"); System.exit(2); }
  
  Configuration conf = new Configuration();
  
  Job job = Job.getInstance(conf, "word count");
  
  job.setJarByClass(WordCount.class);
  
  job.setMapperClass(TokenizerMapper.class); job.setCombinerClass(IntSumReducer.class); job.setReducerClass(IntSumReducer.class);
  
  job.setOutputKeyClass(Text.class); job.setOutputValueClass(IntWritable.class);
  
  FileInputFormat.addInputPath(job, new Path(args[0])); FileOutputFormat.setOutputPath(job, new Path(args[1]));
  
  System.exit(job.waitForCompletion(true) ? 0 : 1); } }


Save the program using:

  `Ctrl + S`

---

## STEP 8: ADD HADOOP JAR FILES
  
  1. Right-click the Java project.
  2. Select Build Path → Configure Build Path.
  3. Open the Libraries tab.
  4. Click Add External JARs.

### Add the Hadoop MapReduce JAR

Navigate to the Hadoop installation directory.

Open the `share/hadoop/mapreduce` folder.

Select:

  `hadoop-mapreduce-client-core-3.2.1.jar`

Click Open.

### Add the Hadoop Common JAR

Click Add External JARs again.

Navigate to the `share/hadoop/common` folder.

Select:

  `hadoop-common-3.2.1.jar`

Click Open.

5. Click Apply and Close.

  **Important:** Depending on your Hadoop installation, additional
  Hadoop JAR files may be required. If compilation or execution fails
  because of missing dependencies, add the required JAR files from the
  appropriate Hadoop directories.
  
  ---

## STEP 9: RESOLVE JAVA IMPORT ERRORS

  1. Check the Java program for red-underlined errors.
  2. Hover over an unresolved class name.
  3. Select the appropriate import suggestion, if available.
  4. Repeat for other unresolved Hadoop classes.
  5. Save the file.

Ensure that the following imports are present:

  - `org.apache.hadoop.conf.Configuration`
  - `org.apache.hadoop.fs.Path`
  - `org.apache.hadoop.io.IntWritable`
  - `org.apache.hadoop.io.Text`
  - `org.apache.hadoop.mapreduce.Job`
  - `org.apache.hadoop.mapreduce.Mapper`
  - `org.apache.hadoop.mapreduce.Reducer`
  - `org.apache.hadoop.mapreduce.lib.input.FileInputFormat`
  - `org.apache.hadoop.mapreduce.lib.output.FileOutputFormat`

**Note:** Import suggestions will work only when the required JAR files
and their dependencies are available in the project's build path.

---

## STEP 10: EXPORT THE JAVA PROJECT AS A JAR FILE
  
  1. Right-click the Java project.
  2. Select Export.
  3. Expand Java.
  4. Select JAR file.
  5. Click Next.
  6. Select the project and source files that should be exported.
  7. Specify the destination path.

   Example:

   `/home/<username>/eclipse-workspace/wordcount.jar`

   Replace `<username>` with your Linux username.

8. Click Finish.

The JAR file will be created at the specified destination.

**Important:** Export a standard JAR containing the compiled class files.
Do not select a source-only JAR.

---

## STEP 11: VERIFY THE JAR FILE

Open the terminal and navigate to your Eclipse workspace.

Example:

  cd ~/eclipse-workspace


List the files:

  ls


Verify that the JAR file exists:

  ls -l wordcount.jar


If your JAR file has a different name, replace `wordcount.jar`
with your actual JAR file name.

---

## STEP 12: EXECUTE THE MAPREDUCE PROGRAM

Before running the program, ensure that Hadoop is configured properly
and its required services are running.

Execute the following command from the terminal:

  hadoop jar jar_name.jar package_name.java_class_name /mrjobs/input/word.txt(it has to be created in the hdfs before only) /mrjobs/output/output_name


### Command Explanation

- `hadoop jar`: Executes a Hadoop application packaged as a JAR.
- `wordcount.jar`: The exported JAR file.
- `com.hadoop.mapreduce.WordCount`: The fully qualified Java class name.
- `/mrjobs/input/word.txt`: The input file stored in HDFS.
- `/mrjobs/output`: The output directory to be created in HDFS.

**Important:** The output directory must not already exist.
If it exists from a previous execution, remove it before running
the program again.

To remove the previous output directory, execute:

  hdfs dfs -rm -r /mrjobs/output


Run this removal command only when the directory already exists and
you intend to replace its contents.

---

## STEP 13: VIEW THE OUTPUT

After the MapReduce job completes successfully, execute:
  
  hdfs dfs -ls /mrjobs/output


The output directory should contain a file such as:

  `part-r-00000`

Display the result:
  
  hdfs dfs -cat /mrjobs/output/part-r-00000


### Expected Output

For the sample input:
  
  hello world hello hadoop mapreduce program hadoop mapreduce


The output should be similar to:

  hadoop 2 hello 2 mapreduce 2 program 1 world 1


The exact order of the words may vary.

---

## STEP 14: RESULT

Thus, the MapReduce WordCount program was successfully implemented
using Java in Eclipse and executed on Hadoop.

The program reads a text file from HDFS, counts the occurrences of
each word, and stores the results in the HDFS output directory.

---

## IMPORTANT NOTES
  
  1. Ensure that the input text file exists in HDFS before executing
     the program.
  2. The input and output paths must be HDFS paths.
  3. The output directory must not exist before job execution.
  4. The JAR file must contain the compiled Java class files.
  5. Use the fully qualified class name when running the Hadoop command.
  6. If the package name or class name changes, update the execution
     command accordingly.
  7. If the program fails with missing-class errors, check the Hadoop
     JAR files and dependencies in the Eclipse build path.
  8. Make sure the Hadoop version used for compilation is compatible
     with the Hadoop installation used for execution.
