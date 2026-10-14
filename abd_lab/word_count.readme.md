 public class testWordCount {

  	public static class testWordCountMapper extends Mapper<LongWritable, Text, IntWritable, IntWritable> {
  		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
  					String line = value.toString();
  					StringTokenizer tokenizer = new StringTokenizer (line);
  
  					while (tokenizer.hasMoreTokens() ) {
  						//value.set(String.valueOf(tokenizer.nextToken().length()));						
  						context.write(new IntWritable(tokenizer.nextToken().length()), new IntWritable(1));
  					}
  		}
	}

	public static class testWordCountReducer extends Reducer <IntWritable, IntWritable, IntWritable, IntWritable > {
  		public void reduce(IntWritable key, Iterable<IntWritable> values, Context context) 
  			throws IOException, InterruptedException {
  				int sum = 0;
  				for (IntWritable x: values) {
  					sum += x.get();
  				}
  				context.write(key, new IntWritable(sum) );
		}
		
	public static class maxMapper extends Mapper<IntWritable, IntWritable, IntWritable, IntWritable>{
  		public void map(Iterable<IntWritable> key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
  			int maxx = 0;
  			for (IntWritable x: key) {
  				if(x.get()>maxx) {
  					maxx = x.get();
  				}
  			}
  			context.write(new IntWritable(maxx),new IntWritable(maxx));
  		}
	}
	
	public static class maxReducer extends Reducer <IntWritable, IntWritable, IntWritable, IntWritable > {
  		public void reduce(IntWritable key, Iterable<IntWritable> values, Context context) 
  			throws IOException, InterruptedException {
  				context.write(new IntWritable(0), new IntWritable(0));
  		}
	}

	public static void main(String[] args) throws Exception{
  		// TODO Auto-generated method stub
  		Configuration conf = new Configuration();
  		
  		Job job = Job.getInstance(conf, "my count");
  
  		job.setJarByClass(testWordCount.class);
  		job.setMapperClass(maxMapper.class);
  		job.setReducerClass(maxReducer.class);
  
  		job.setOutputKeyClass(IntWritable.class);
  		job.setOutputValueClass(IntWritable.class);
  
  		FileInputFormat.addInputPath(job, new Path(args[0]));
  		
  		FileOutputFormat.setOutputPath(job, new Path(args[1]));
  
  		System.exit(job.waitForCompletion(true) ? 0: 1);

	}

}}
