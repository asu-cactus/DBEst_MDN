#!/bin/bash

python3 query.py --data_name flights --units 380
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/flights/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/flights/

python3 query.py --data_name flights --units 400
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/flights/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/flights/

python3 query.py --data_name flights --units 450
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/flights/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/flights/

python3 query.py --data_name flights --units 470
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/flights/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/flights/

python3 query.py --data_name flights --units 500
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/flights/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/flights/

python3 query.py --data_name flights --units 550
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/flights/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/flights/
