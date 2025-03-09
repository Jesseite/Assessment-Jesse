import os
from azure.storage.blob import BlobServiceClient

# Retrieve environment variables
storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")
storage_account_key = os.getenv("STORAGE_ACCOUNT_KEY")
connection_string = os.getenv("CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")

def uploadtoBlobStorage(file_path):
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        file_name = os.path.basename(file_path)
        
        # Create a BlobClient
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        # Upload the file
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded '{file_name}' to container '{container_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

uploadtoBlobStorage(r"C:\Users\jesse\anonymized_file.csv")