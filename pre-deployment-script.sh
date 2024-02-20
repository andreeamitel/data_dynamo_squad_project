cp -f -r ./src/extract ./deployment_code
sed -e s/src.//g -i ./deployment_code/extract/lambda_handler.py