#!/bin/bash

python3 query.py --data_name ccpp --units 350
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/ccpp/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/ccpp/

python3 query.py --data_name ccpp --units 400
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/ccpp/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/ccpp/

python3 query.py --data_name ccpp --units 450
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/ccpp/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/ccpp/

python3 query.py --data_name ccpp --units 500
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/ccpp/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/ccpp/


python3 query.py --data_name ccpp --units 550
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/ccpp/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/ccpp/

python3 query.py --data_name ccpp --units 600
mv ../dbestwarehouse/*.dill ../dbestwarehouse_temp/ccpp/
mv ../dbestwarehouse/*.pt ../dbestwarehouse_temp/ccpp/

