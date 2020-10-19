from datetime import datetime as dt


def main(spark):
    df = spark.read.json('/opt/nifi/year=*/')
    df = df.filter(f'day <= {dt.now().strftime("%d")}')
    df.write.mode('append').parquet('/opt/nifi/data_flow')


def read_data(spark):
    df = spark.read.parquet('/opt/nifi/data_flow')
    df.show()
