#!/bin/bash


python3 query.py --data_name store_sales --units 500
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

python3 query.py --data_name store_sales --units 550
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

python3 query.py --data_name store_sales --units 600
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/


python3 query.py --data_name store_sales --units 700
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

python3 query.py --data_name store_sales --units 800
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

python3 query.py --data_name store_sales --units 900
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

python3 query.py --data_name store_sales --units 1000
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/
