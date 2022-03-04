from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
import os

credential = AzureCliCredential()
subscription_id = os.environ["SUBSCRIPTION_ID"]
resource_client = ResourceManagementClient(credential, subscription_id)

# Create client
# # For other authentication approaches, please see: https://pypi.org/project/azure-identity/
resource_client = ResourceManagementClient(
    credential=AzureCliCredential(),
    subscription_id = os.environ["SUBSCRIPTION_ID"]
  )
storage_client = StorageManagementClient(
    credential=AzureCliCredential(),
    subscription_id = os.environ["SUBSCRIPTION_ID"]
  )

def newstrg():
    SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
    GROUP_NAME = "kata-rg"
    STORAGE_ACCOUNT = "katastrg"
    BLOB_CONTAINER = "blobcontainerkata"

  # - init depended resources -
  # Create storage account
    storage_client.storage_accounts.begin_create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        {
          "sku": {
            "name": "Standard_GRS"
          },
          "kind": "StorageV2",
          "location": "eastus",
          "encryption": {
            "services": {
              "file": {
                "key_type": "Account",
                "enabled": True
              },
              "blob": {
                "key_type": "Account",
                "enabled": True
              }
            },
            "key_source": "Microsoft.Storage"
          },
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
    ).result()
    # - end -
    blob_container = storage_client.blob_containers.create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER,
        {}
    )
    print("Create blob container:\n{}".format(blob_container))

def getblob():
    SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
    GROUP_NAME = "kata-rg"
    STORAGE_ACCOUNT = "katastrg2"
    BLOB_CONTAINER = "blobcontainerkata"    

    blob_container = storage_client.blob_containers.get(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER
    )
    print("Get blob container:\n{}".format(blob_container))
    
def uploadblob():
  from azure.storage.blob import BlobClient

  blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=katastrg2;AccountKey=dXIfiq+zJ2qM+JF+Ken3i078jyAJMyeMybgByHTgULktJxmgDt4KMADmycziSOm/0l0z53/HPCkP+ASts1kX6Q==;EndpointSuffix=core.windows.net", container_name="blobcontainerkata", blob_name="kata_blob2")

  with open("date.txt", "rb") as data:
    blob.upload_blob(data) 


def dwlnblob():
  from azure.storage.blob import BlobClient

  blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=katastrg2;AccountKey=dXIfiq+zJ2qM+JF+Ken3i078jyAJMyeMybgByHTgULktJxmgDt4KMADmycziSOm/0l0z53/HPCkP+ASts1kX6Q==;EndpointSuffix=core.windows.net", container_name="blobcontainerkata", blob_name="kata_blob2")

  with open("./date1.txt", "wb") as my_blob:
      blob_data = blob.download_blob()
      blob_data.readinto(my_blob)

def listblobs():
  from azure.storage.blob import ContainerClient

  container = ContainerClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=katastrg2;AccountKey=dXIfiq+zJ2qM+JF+Ken3i078jyAJMyeMybgByHTgULktJxmgDt4KMADmycziSOm/0l0z53/HPCkP+ASts1kX6Q==;EndpointSuffix=core.windows.net", container_name="blobcontainerkata")

  blob_list = container.list_blobs()
  for blob in blob_list:
    print(blob.name + '\n')  

def deleteblob():
  GROUP_NAME = "kata-rg"
  STORAGE_ACCOUNT = "katastrg2"
  BLOB_CONTAINER = "blobcontainerkata"

  blob_container = storage_client.blob_containers.delete(
      GROUP_NAME,
      STORAGE_ACCOUNT,
      BLOB_CONTAINER
    )
  print("Delete blob container.\n")
  


def deletefile():
  from azure.storage.blob import BlobClient

  blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=katastrg2;AccountKey=dXIfiq+zJ2qM+JF+Ken3i078jyAJMyeMybgByHTgULktJxmgDt4KMADmycziSOm/0l0z53/HPCkP+ASts1kX6Q==;EndpointSuffix=core.windows.net", container_name="blobcontainerkata", blob_name="kata_blob")

  with open("kata_blob", "wb") as f:
    f = blob.delete_blob()
    #blob_data.readinto(my_blob)
              
  print("Delete blob file.\n")


deletefile()