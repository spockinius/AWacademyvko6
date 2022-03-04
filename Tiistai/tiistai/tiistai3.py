from azure.mgmt.network import NetworkManagementClient
from azure.identity import AzureCliCredential
credential = AzureCliCredential()

def vnetjasubnet():
    GROUP_NAME = 'kata-rg'
    VNET_NAME = 'katanvnetti'
    LOCATION = 'westeurope'
    SUBNET_NAME = 'katansubbari'

    network_client = NetworkManagementClient(credential, '397dc614-480f-46f5-a35f-d4e5d10d1095')

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