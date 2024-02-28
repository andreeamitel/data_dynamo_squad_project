import json
import pandas as pd

def get_latest_data(ingested_bucket_name, s3, last_updated):
    updated_data_list = []
    objs = s3.list_objects(Bucket=ingested_bucket_name)
    dict_dfs ={}
    for obj in objs["Contents"]:

        if obj["Key"] != "Last_Ingested.txt":
            if obj["Key"].split("/")[1][:-5] == last_updated:
                table_name = obj["Key"].split("/")[0]
                up_data = s3.get_object(
                    Bucket=ingested_bucket_name, Key=obj["Key"])
                decode_data = up_data["Body"].read().decode("utf-8")
                df = pd.DataFrame(json.loads(decode_data)[table_name])
                dict_dfs[table_name] = df
    return dict_dfs
