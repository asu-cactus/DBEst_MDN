#!/bin/bash

mv ../dbestwarehouse_temp/store_sales/store_sales_500.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 500
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

mv ../dbestwarehouse_temp/store_sales/store_sales_550.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 550
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

mv ../dbestwarehouse_temp/store_sales/store_sales_600.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 600
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

mv ../dbestwarehouse_temp/store_sales/store_sales_700.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 700
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

mv ../dbestwarehouse_temp/store_sales/store_sales_800.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 800
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

mv ../dbestwarehouse_temp/store_sales/store_sales_900.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 900
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/

mv ../dbestwarehouse_temp/store_sales/store_sales_1000.dill* ../dbestwarehouse/
python3 query.py --data_name store_sales --units 1000
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/store_sales/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/store_sales/