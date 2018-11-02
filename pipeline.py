import findspark
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

findspark.init("C:\My Softwares\pyspark\spark-2.3.1-bin-hadoop2.7")

spark = SparkSession.builder.getOrCreate()
#Read csv into a pyspark dataframe and infer schema as well
sparkDF = spark.read.format('csv').options(header='true', inferSchema='true').load('language_dataset.csv')

#Remove duplicate rows present in the dataframe
sparkDF=sparkDF.dropDuplicates()

#Remove null rows present in the dataframe
sparkDF=sparkDF.dropna()

#Select the required columns from the datafram and put it in another dataframe
language_dataset=sparkDF.select('uid','predicted_gender','predicted_age','streams')

#Connect to mysql and write the dataframe into the table with same schema
language_dataset.write.format('jdbc').options(
      url='jdbc:mysql://localhost/mysql',
      driver='com.mysql.jdbc.Driver',
      dbtable='Language_Data',
      user='root@vatsal',
      password='Vatsal123').mode('append').save()
    
