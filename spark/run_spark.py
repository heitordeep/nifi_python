import findspark

findspark.init()

if __name__ == "__main__":
    import get_data_flow
    from pyspark.sql import SparkSession

    spark = (
        SparkSession.builder.master('local')
        .appName('generator_data_flow')
        .config("spark.executor.memory", '1gb')
        .getOrCreate()
    )

    get_data_flow.main(spark)
    get_data_flow.read_data(spark)
