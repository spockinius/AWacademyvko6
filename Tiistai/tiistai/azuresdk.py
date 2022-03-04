# Import the needed credential and management objects from the libraries.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
import os

credential = AzureCliCredential()
subscription_id = os.environ["SUBSCRIPTION_ID"]
resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)
#container_client = ContainerClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

# Provision the resource group.
def newrg(name: str, location: str):
    rg_result = resource_client.resource_groups.create_or_update(
        name,
        {
            "location": location
        }
    )
    print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

# Retrieve the list of resource groups
def listrgs():
    group_list = resource_client.resource_groups.list()
    # Show the groups in formatted output
    column_width = 40
    print("Resource Group".ljust(column_width) + "Location")
    print("-" * (column_width * 2))

    for group in list(group_list):
        print(f"{group.name:<{column_width}}{group.location}")

# To update the resource group, repeat the call with different properties, such
# as tags:
def updaterg(rgname: str, key: str, value: str):
    rg_result = resource_client.resource_groups.create_or_update(
        rgname,
        {
            "location": "westeurope",
            "tags": { key : value }
        }
    )
    print(f"Updated resource group {rg_result.name} with tags")

# Make a new storage account
def newstorage(rgname: str, storagename: str, location: str):
    storage_client.storage_accounts.begin_create(
        rgname,
        storagename,
        {
          "sku": {
            "name": "Standard_GRS"
          },
          "kind": "StorageV2",
          "location": location,
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
    print(f"New storage account named {storagename} created in RG {rgname}, in location {location}")

# Create new blob storage
def newblob(rgname: str, storagename: str, blobname: str):
    blob_container = storage_client.blob_containers.create(
        rgname,
        storagename,
        blobname,
        {}
    )
    print(f"Created blob storage named {blobname} into RG {rgname} under storage account {storagename}")

# List blob containters
def listblobs(rgname: str, storagename: str, blobname: str):
    blob_container = storage_client.blob_containers.get(
        rgname,
        storagename,
        blobname
    )
    print(f"Get blob container: \n name: {blob_container.name}, \n type: {blob_container.type}")

# Upload blob file
def uploadblob(connectionstring: str, filename: str, container: str, blobname: str):
  blob = BlobClient.from_connection_string(conn_str=connectionstring, container_name=container, blob_name=blobname)

  with open(filename, "rb") as f:
    blob.upload_blob(f)
  print(f"File {filename} has been uploaded to storageaccount {blobname}")

# Download blob file
def downloadblob(connectionstring: str, containername: str, azurefile: str, localfile: str):
    blob = BlobClient.from_connection_string(conn_str=connectionstring, container_name=containername, blob_name=azurefile)

    with open(localfile, "wb") as f:
      blobdata = blob.download_blob()
      blobdata.readinto(f)
    print(f"Blob file named {azurefile} has now been downloaded into local file named {localfile}")

# List blobs
def listblobs():
    from azure.storage.blob import ContainerClient

    container = ContainerClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=katastorage01;AccountKey=9IOHn5FyJAiKdp4MqgDx1Q7iQAxeHYUzIFxY/iXEaDOga6tzi1vRpUBsUtYgcEAGo0Ue87ER2FTpPQ9bZfFMJQ==;EndpointSuffix=core.windows.net", container_name="katanblobi")

    blob_list = container.list_blobs()
    for blob in blob_list:
        print(blob.name + '\n')  

# Create vnet and subnet

def vnetjasubnet(rgname, vnetname, location, subnetname):
    GROUP_NAME = rgname
    VNET_NAME = vnetname
    LOCATION = location
    SUBNET_NAME = subnetname

    async_vnet_creation = network_client.virtual_networks.begin_create_or_update(
        GROUP_NAME,
        VNET_NAME,
        {
            'location': LOCATION,
            'address_space': {
                'address_prefixes': ['10.0.0.0/16']
            }
        }
    )
    async_vnet_creation.wait()

    # Create Subnet
    async_subnet_creation = network_client.subnets.begin_create_or_update(
        GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME,
        {'address_prefix': '10.0.0.0/24'}
    )
    subnet_info = async_subnet_creation.result()

def listvm(rgname):
    GROUP_NAME = rgname
    result_create = compute_client.virtual_machines.list(
        GROUP_NAME,
    )
    for re in result_create:
        print(re.name)

def startvm(rgname, vmname):
    GROUP_NAME = rgname
    VM_NAME = vmname
    # Start the VM
    print('\nStart VM')
    async_vm_start = compute_client.virtual_machines.begin_start(
        GROUP_NAME, VM_NAME)
    async_vm_start.wait()

def stopvm(rgname, vmname):
    GROUP_NAME = rgname
    VM_NAME = vmname
    # Stop the VM
    print('\nStop VM')
    async_vm_stop = compute_client.virtual_machines.begin_power_off(
        GROUP_NAME, VM_NAME)
    async_vm_stop.wait()

if __name__ == "__main__":
    listblobs()

