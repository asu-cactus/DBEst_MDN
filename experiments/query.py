#
# Created by Qingzhi Ma on Thu Jun 04 2020
#
# Copyright (c) 2020 Department of Computer Science, University of Warwick
# Copyright 2020 Qingzhi Ma
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SELECT unique_carrier, COUNT(dep_delay) FROM flights GROUP BY unique_carrier;
# hive -e "SELECT unique_carrier, COUNT(*) FROM flights GROUP BY unique_carrier" > flights_group.csv

# hive -e "SELECT unique_carrier, AVG(dep_delay) FROM flights WHERE distance >=  300  AND distance <= 1000 GROUP BY unique_carrier" > flights_avg1.csv
# hive -e "SELECT unique_carrier, AVG(dep_delay) FROM flights WHERE distance >= 1000  AND distance <= 1500 GROUP BY unique_carrier" > flights_avg2.csv
# hive -e "SELECT unique_carrier, AVG(dep_delay) FROM flights WHERE distance >= 1500  AND distance <= 2000 GROUP BY unique_carrier" > flights_avg3.csv
# hive -e "SELECT unique_carrier, SUM(dep_delay) FROM flights WHERE distance >=  300  AND distance <= 1000 GROUP BY unique_carrier" > flights_sum1.csv
# hive -e "SELECT unique_carrier, SUM(dep_delay) FROM flights WHERE distance >= 1000  AND distance <= 1500 GROUP BY unique_carrier" > flights_sum2.csv
# hive -e "SELECT unique_carrier, SUM(dep_delay) FROM flights WHERE distance >= 1500  AND distance <= 2000 GROUP BY unique_carrier" > flights_sum3.csv

# hive -e "SELECT unique_carrier, COUNT(*) FROM flights WHERE dep_delay>=1000 AND dep_delay<=1200 AND origin_state_abr='LA'  GROUP BY unique_carrier" > flights_one_model_1_x.csv

from dbestclient.executor.executor import SqlExecutor
import numpy as np
import pandas as pd

import pdb
import argparse
import os
from time import perf_counter

EPS = 1e-6

def parse_args():
    parser = argparse.ArgumentParser(description="Create a sample of a dataset")
    parser.add_argument("--data_name", type=str, required=True, help="The name of the dataset")
    parser.add_argument("--units", type=int, default=200, help="The number of units to sample")
    args = parser.parse_args()
    return args 

class Query1:
    def __init__(self, args):
        self.sql_executor = SqlExecutor()

        self.task_type = "sum"
        self.ratio = 0.1
        self.units = args.units
        self.data_name = args.data_name

        if args.data_name == "pm25":
            self.dep = "pm25"
            self.indep = "PRES"
        elif args.data_name == "ccpp":
            self.dep = "PE"
            self.indep = "RH"
        elif args.data_name == "flights":
            self.dep = "TAXI_OUT"
            self.indep = "DISTANCE"
        elif args.data_name == "store_sales":
            self.dep = "wholesale_cost"
            self.indep = "list_price"
        else:
            raise ValueError(f"Invalid data name: {args.data_name}")

        self.mdl_name = f"{self.data_name}_{self.units}"
        self.datafile = f"{self.data_name}_{self.task_type}_sample.csv"
        # self.query_path = f"../../DeepMappingAQP/query/{self.data_name}_{self.task_type}_1D.npz"
        self.query_path = f"../../DeepMappingAQP/query/{self.data_name}_{self.task_type}_1D_nonzeros.npz"

    def build_model(self):
        self.sql_executor.execute(f"set n_mdn_layer_node_reg={self.units}")          # 20
        self.sql_executor.execute(f"set n_mdn_layer_node_density={self.units}")      # 30
        self.sql_executor.execute("set n_hidden_layer=2")                 # 2
        self.sql_executor.execute("set n_gaussians_reg=10")                # 
        self.sql_executor.execute("set n_gaussians_density=10")            # 10
        self.sql_executor.execute("set n_epoch=10")                       # 20
        self.sql_executor.execute("set device='gpu'")
        self.sql_executor.execute(
            f"create table {self.mdl_name}({self.dep} real, {self.indep} real) from {self.datafile} method uniform size {self.ratio}"
        )

    def workload(
        self,
        n_jobs: int = 1,
        nqueries: int = 1000,   
    ):
        # Load dataframe from save_path if exists
        save_path = f"results/{self.data_name}_results.csv"
        if os.path.exists(save_path):
            df = pd.read_csv(save_path)
        else:
            df = pd.DataFrame(columns=["units", "query_percent", "avg_rel_err", "avgtime"])

        self.sql_executor.execute("set n_jobs=" + str(n_jobs) + '"')
        # Load queries
        results = []
        
        npzfile = np.load(self.query_path)
        for query_percent in npzfile.keys():
            queries = npzfile[query_percent][:nqueries]
            start = perf_counter()
            total_rel_error = 0.0
  
            for query in queries:
                lb, ub, y = query

                y_pred = self.sql_executor.execute(
                    f"select {self.task_type}({self.dep} real) from {self.mdl_name} where {lb}<{self.indep}<={ub}"
                )["dummy"]
                rel_error = np.absolute(y_pred - y) / (y + EPS)
                total_rel_error += rel_error

            avg_rel_error = total_rel_error / len(queries)
            avg_time = (perf_counter() - start) / len(queries)
            results.append({"units": self.units, "query_percent": query_percent,"avg_rel_err": round(avg_rel_error,4), "avgtime": round(avg_time,4)})
        #Conver results to pandas dataframe and save to csv
        
        # Append results to dataframe
        df = df.append(results, ignore_index=True)
        df.to_csv(save_path, index=False)


if __name__ == "__main__":
    args  = parse_args()
    query1 = Query1(args)

    # query1.build_model(mdl_name="flights_1m_binary_small",encoder="binary")
    # # query1.build_model(mdl_name="flights_1m_onehot",encoder="onehot")
    # # query1.build_model(mdl_name="flights_1m_embedding",encoder="embedding")
    # query1.workload("flights_5m_binary",result2file="experiments/flights/results/mdn5m/")


    query1.build_model()
    # query1.build_one_model("flight_one_model_embedding",encoder="embedding")
    query1.workload()
