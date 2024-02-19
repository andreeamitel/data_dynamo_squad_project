import pandas as pd
import awswrangler as wr



def python_to_parquet(table_data, s3, bucket_name, file_key):
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
    table_name = list(table_data.keys())[0]
    dataframe = pd.DataFrame(table_data[table_name])
    wr.s3.to_parquet(dataframe, path=f"s3://{bucket_name}/{file_key}/{table_name}.parquet", index=False)
    

    

