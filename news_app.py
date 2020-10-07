from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
import happybase
from datetime import datetime


def SaveRecord(corona):
    server = "localhost"
    table_name = "corona"
    pool = happybase.ConnectionPool(size=300, host=server)

    with pool.connection() as connection:
        connection.table(table_name).put(bytes(str(datetime.now()), 'utf-8'), {"corona_frequency:count": str(corona)})

# create spark configuration
conf = SparkConf()
conf.setAppName("CoronaTrendApp")
# create spark context with the above configuration
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
# create the Streaming Context from the above spark context with interval size 2 seconds
ssc = StreamingContext(sc, 2)
# setting a checkpoint to allow RDD recovery
ssc.checkpoint("checkpoint_CoronaApp")
# read data from port 9999
dataStream = ssc.socketTextStream("localhost",9999)

corona = dataStream.filter(lambda x: "corona" in x).count()
corona.foreachRDD(SaveRecord)

ssc.start()
ssc.awaitTermination()


