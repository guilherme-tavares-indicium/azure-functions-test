# Load libraries
from azure.storage.blob import BlobClient
import pandas as pd
from dotenv import dotenv_values

config = dotenv_values(".env")

# Define parameters
connectionString = config["CONNECTION_STRING"]
containerName = "output"
outputBlobName	= "iris_setosa.csv"

# Establish connection with the blob storage account
blob = BlobClient.from_connection_string(conn_str=connectionString, container_name=containerName, blob_name=outputBlobName)

# Load iris dataset from the task node
df = pd.read_csv("iris.csv")

# Take a subset of the records
df = df[df['Species'] == "setosa"]

# Save the subset of the iris dataframe locally in task node
df.to_csv(outputBlobName, index = False)

with open(outputBlobName, "rb") as data:
    blob.upload_blob(data)