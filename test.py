
## Start Spark , pyspark 

import findspark

findspark.init()
import pyspark

from pyspark.sql import SparkSession

## create Session and cache objects

spark = SparkSession.builder.getOrCreate()
df_jul= spark.read.csv('C:/GIT/Nasa/access_log_Jul95.txt', sep = ' ')
df_jul = df_jul.cache()
df_Aug= spark.read.csv('C:/GIT/Nasa/access_log_Aug95.txt', sep = ' ')
df_Aug = df_Aug.cache()


df_jul.show()
df_Aug.show()


## convert into SQL table approach

df_jul.registerTempTable("NasaJul")
df_Aug.registerTempTable("NasaAug")


total_host_num_Jul = spark.sql("SELECT count(*) count FROM NasaJul").first()['count']
total_host_num_AUg = spark.sql("SELECT count(*) count FROM NasaAug").first()['count']

## Total records per file

print(total_host_num_Jul)
print(total_host_num_AUg)



## First Question Total of unique hosts

Unique_host_num_Jul = spark.sql("SELECT count(distinct(_c0)) count FROM NasaJul").first()['count']
Unique_host_num_Aug = spark.sql("SELECT count(distinct(_c0)) count FROM NasaAug").first()['count']

print(Unique_host_num_Jul)
print(Unique_host_num_Aug)

## Second Question Total of errors =404

total_error_404_Jul = spark.sql("SELECT count(*) count  FROM NasaJul Where _c6='404'").first()['count']
total_error_404_Aug = spark.sql("SELECT count(*) count  FROM NasaAug Where _c6='404'").first()['count']

print(total_error_404_Jul)
print(total_error_404_Aug)

## Third Question Top 5 Total of errors =404

Top5host_error_404_Jul = spark.sql("SELECT _c0 host,count(*) count FROM NasaJul Where _c6='404' group by _c0 order by 2 desc")
Top5host_error_404_Aug = spark.sql("SELECT _c0 host,count(*) count FROM NasaAug Where _c6='404' group by _c0 order by 2 desc")

Top5_Jul = Top5host_error_404_Jul.take(5)

Top5_Aug = Top5host_error_404_Aug.take(5)


def Top5(row,month):

   for i in range(0,len(row)):
    print(month,row[i][0],"-",row[i][1])


Top5(Top5_Jul,'Top5 Jul')
Top5(Top5_Aug ,'Top5 Aug')

## Fourth Question  Total of errors per day =404

error_per_day_Jul = spark.sql("SELECT substring(_c3,2,11) dia,count(*) FROM NasaJul Where _c6='404' group by 1 order by 1")
error_per_day_Aug = spark.sql("SELECT substring(_c3,2,11) dia,count(*) FROM NasaAug Where _c6='404' group by 1 order by 1")


error_per_day_Jul.show()

error_per_day_Aug.show()


## Fifth Question  Total of bytes

total_bytes_Jul = spark.sql("SELECT sum(CAST(_c7 AS DOUBLE)) sumTotal FROM NasaJul ").first()['sumTotal']
total_bytes_Aug = spark.sql("SELECT sum(CAST(_c7 AS DOUBLE)) sumTotal FROM NasaAug ").first()['sumTotal']

print(total_bytes_Jul)
print(total_bytes_Aug)
