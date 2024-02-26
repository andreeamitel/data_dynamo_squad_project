import json


def get_latest_data(ingested_bucket_name, s3, last_updated):
    updated_data_dict = {}
    print("GLD - start")
    objs = s3.list_objects(Bucket=ingested_bucket_name)
    print(objs)
    for obj in objs["Contents"]:
        print("GLD - for loop")
        print(obj)
        if obj["Key"] != "Last_Ingested.txt":
            if obj["Key"].split("/")[1][:-5] == last_updated:
                print("get_latest_data - in if")
                up_data = s3.get_object(Bucket=ingested_bucket_name, Key=obj["Key"])
                decode_data = up_data["Body"].read().decode("utf-8")
                updated_data_dict[obj["Key"].split("/")[0]] = json.loads(decode_data)
    print("GLD before return")
    return updated_data_dict
