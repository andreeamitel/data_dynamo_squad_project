rm -rf ./deployment_code
mkdir ./deployment_code
cp -f -r  ./src/extract ./deployment_code/
sed -e s/src.//g -i ./deployment_code/extract/lambda_handler.py

cp -f -r ./src/transform ./deployment_code/
sed -e s/src.//g -i ./deployment_code/transform/lambda_handler.py
sed -e s/src.//g -i ./deployment_code/transform/fact_sales_order.py

cp -f -r ./src/load ./deployment_code/
sed -e s/src.//g -i ./deployment_code/load/lambda_handler.py
