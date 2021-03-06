# Import needed modules
import sys
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobClient
import os

# Import needed credentials
credential = AzureCliCredential()
subscription_id = os.environ["SUBSCRIPTION_ID"]
resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

# Program code 
print("Tämä on tiedoston nimi: ",
    sys.argv[0])
print(f"Annoit rivimääräksi: ",
    sys.argv[1])

count = int(sys.argv[1])  

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=katastorage01;AccountKey=9IOHn5FyJAiKdp4MqgDx1Q7iQAxeHYUzIFxY/iXEaDOga6tzi1vRpUBsUtYgcEAGo0Ue87ER2FTpPQ9bZfFMJQ==;EndpointSuffix=core.windows.net", container_name="katablobtentti", blob_name="checkpoint.txt")

with open("checkpoint2.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)

with open("checkpoint2.txt", "r") as f:
    for i in range(count):
        rivi = f.readline()
        rivi = rivi.replace("\n", "")
        lista = []
        lista.append(rivi)
        sortattu = (sorted(lista, key=len))
        print(sortattu)



