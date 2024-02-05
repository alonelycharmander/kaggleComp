import pandas as pd 
import tensorflow 
dataset_df = pd.read_csv("train.csv")

#printin the head 
print(dataset_df.head(5))

#prints the columns withe the count and data type 
print(dataset_df.info())



