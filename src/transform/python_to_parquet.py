import pandas as pd
import awswrangler as wr
import warnings


def python_to_parquet(dict_df, bucket_name, timestamp_key):
    """
    Arg:
    - table_data - new data created from unit functions in correct schema,
    form of python list of dictionaries
    - s3 - client - connection to s3
    - bucket_name - name of processed bucket
    - file_key - name of key we are writing to
    Functionality:
    - converts table to parquet format
    - writes converted table to s3 processed bucket
    """
    warnings.filterwarnings(
        "ignore",
        message="promote has been superseded by promote_options='default'.",
        category=FutureWarning,
        module="awswrangler",
    )
    table_name = list(dict_df.keys())[0]
    wr.s3.to_parquet(
        dict_df[table_name],
        path=f"s3://{bucket_name}/{table_name}/{timestamp_key}.parquet",
        index=False,
    )
