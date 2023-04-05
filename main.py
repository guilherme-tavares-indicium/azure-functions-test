# Load libraries
from azure.storage.blob import BlobClient
import pandas as pd
import os
from datetime import datetime

# Define parameters
now = datetime.now() # current date and time
connectionString = os.environ.get("CONNECTION_STRING")
containerName = "output"
outputBlobName	= f"iris_setosa_v4_{now}.csv"

# Establish connection with the blob storage account
blob = BlobClient.from_connection_string(conn_str=connectionString, container_name=containerName, blob_name=outputBlobName)

# Load iris dataset
df = pd.read_csv("iris.csv")

# Take a subset of the records
df = df[df['Species'] == "setosa"]

# Save the subset of the iris dataframe locally in task node
df.to_csv(outputBlobName, index = False)

with open(outputBlobName, "rb") as data:
    blob.upload_blob(data, overwrite=True)

print("hi from the code")