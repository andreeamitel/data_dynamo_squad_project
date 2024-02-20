import pandas as pd
import awswrangler as wr
import warnings




def python_to_parquet(table_data, bucket_name, timestamp_key):
    """
    Arg: 
    - table_data - new data created from unit functions in correct schema, form of python list of dictionaries
    - s3 - client - connection to s3
    - bucket_name - name of processed bucket 
    - file_key - name of key we are writing to
    Functionality: 
    - converts table to parquet format 
    - writes converted table to s3 processed bucket
    """
    # Suppress specific FutureWarning from awswrangler module
    warnings.filterwarnings("ignore", message="promote has been superseded by promote_options='default'.", category=FutureWarning, module="awswrangler")
    table_name = list(table_data.keys())[0]
    dataframe = pd.DataFrame(table_data[table_name])
    wr.s3.to_parquet(dataframe, path=f"s3://{bucket_name}/{timestamp_key}/{table_name}.parquet", index=False)
    

    

