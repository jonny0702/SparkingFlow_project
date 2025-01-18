from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

text = "Hello Spark, Hello python, and docker"

words = spark.sparkContext.parallelize(text.split(","))

# Sumamos las ocurrencias de cada palabra lambda key, value
wordsCounts = words.map( lambda word: (word,1)).reduceByKey(lambda a, b: a + b)

for countWords in wordsCounts.collect():
    print(countWords[0], countWords[1])

spark.stop()