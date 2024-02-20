rm -rf ./deployment_code
mkdir ./deployment_code
cp -f -r ./src/extract ./deployment_code/extract
sed -e s/src.//g -i ./deployment_code/extract/lambda_handler.py