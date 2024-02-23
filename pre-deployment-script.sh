rm -rf ./deployment_code
mkdir ./deployment_code
cp -f -r ./src/extract ./deployment_code/extract
sed -e s/src.//g -i ./deployment_code/extract/lambda_handler.py

cp -f -r ./src/transform ./deployment_code/transform
sed -e s/src.//g -i ./deployment_code/transform/lambda_handler.py
sed -e s/src.//g -i ./deployment_code/transform/fact_sales_order.py
sed -e s/src.//g -i ./deployment_code/transform/lambda_handler_demo.py

rm -rf terraform/transform/python
mkdir terraform/transform/python
pip install pandas -t terraform/transform/python/