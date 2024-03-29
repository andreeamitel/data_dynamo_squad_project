import json
import boto3


def convert_and_write_data(
    list_of_selection, table_name, bucket_name, new_ingesting_time
):
    """
    This function should convert the data from a list of dictionaries to
    json, write it in a file and put it in the ingested-bucket.

    Args:\n
        list of dictionaries
        table_name(str)

    Returns:\n
        None
    """

    file_name = f"{table_name}/{new_ingesting_time}.json"
    s3 = boto3.client("s3")
    table_dict = {table_name: list_of_selection}
    if list_of_selection is None:
        table_dict = {}
    s3.put_object(
        Body=f"{json.dumps(table_dict)}",
        Bucket=bucket_name,
        Key=f"{file_name}",
    )
