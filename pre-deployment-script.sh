cp -f -r ./src/extract ./dummy_function
sed -e s/src.//g -i ./dummy_function/extract/lambda_handler.py