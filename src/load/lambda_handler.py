from pg8000.native import Connection

def lambda_handler():
    """
    This function is responsible for periodically scheduling an update of the data warehouse by taking the parquet file from the processed bucket.

    Args:
    event:
        a valid S3 PutObject event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
    context:
        a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    
    Functionality:
    get database connection from secrets manager
    get parquet data from processed bucket
    load data to RDS
    """
    conn = Connection(
            host = "nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com",
            port = "5432",
            user = "project_team_0",
            password = "Z4s1r0ZGJjJUGC",
            database="postgres",
        )
    response = conn.run("SELECT * FROM project_team_0;")
    return response
    
print(lambda_handler())