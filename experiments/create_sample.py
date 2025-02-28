import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Create a sample of a dataset")
parser.add_argument("--data_name", type=str, help="The name of the dataset")
args = parser.parse_args()
data_name = args.data_name
df = pd.read_csv(f"../dbestwarehouse/{data_name}_sum.csv")
df.sample(frac=0.1, random_state=42).to_csv(f"../dbestwarehouse/{data_name}_sum_sample.csv", index=False)