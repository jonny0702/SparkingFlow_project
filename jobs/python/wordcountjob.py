from pyspark.sql import SparkSession
#Setting a spar session
spark = SparkSession.builder.appName("PythonWordCount") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "2g") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.executor.heartbeatInterval", "60s") \
    .config("spark.network.timeout", "300s") \
    .getOrCreate()

text = "Hello Spark Hello Python Hello Airflow Hello Docker and Hello Yusuf"

words = spark.sparkContext.parallelize(text.split(" "))

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

results = wordCounts.collect()
for word, count in results:
    print(f"{word}: {count}")
spark.stop()