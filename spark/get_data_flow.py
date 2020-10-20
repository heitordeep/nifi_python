from datetime import datetime as dt


def create_parquet(spark):
    df = spark.read.json('/opt/nifi/output')
    df = df.filter(df['day'] == dt.now().strftime('%d'))
    df.write.mode('append').parquet('/opt/nifi/trusted')


def read_data(spark):
    df = spark.read.parquet('/opt/nifi/trusted')
    df.orderBy(df['day']).show(truncate=False)
