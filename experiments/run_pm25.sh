#!/bin/bash

python3 query.py --data_name pm25 --units 380
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/pm25/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/pm25/

python3 query.py --data_name pm25 --units 400
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/pm25/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/pm25/

python3 query.py --data_name pm25 --units 450
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/pm25/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/pm25/

python3 query.py --data_name pm25 --units 470
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/pm25/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/pm25/

python3 query.py --data_name pm25 --units 500
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/pm25/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/pm25/

python3 query.py --data_name pm25 --units 550
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/pm25/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/pm25/
