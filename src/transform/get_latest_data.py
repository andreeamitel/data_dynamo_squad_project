import json


def get_latest_data(last_updated, s3, ingested_bucket_name):
    updated_data_dict = {}
    objs = s3.list_objects(Bucket=ingested_bucket_name)
    for obj in objs["Contents"]:
        if obj["Key"].split("/")[1] == last_updated:
            up_data = s3.get_object(Bucket=ingested_bucket_name, Key=obj["Key"])
            decode_data = up_data["Body"].read().decode("utf-8")
            updated_data_dict[obj["Key"].split("/")[0]] = json.loads(decode_data)

    return updated_data_dict
