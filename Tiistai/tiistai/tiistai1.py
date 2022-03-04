from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os

credential = AzureCliCredential()
subscription_id = os.environ["SUBSCRIPTION_ID"]
resource_client = ResourceManagementClient(credential, subscription_id)

def listrgs():
# Retrieve the list of resource groups
    group_list = resource_client.resource_groups.list()
# Show the groups in formatted output
    column_width = 40
    print("Resource Group".ljust(column_width) + "Location")
    print("-" * (column_width * 2))

    for group in list(group_list):
        print(f"{group.name:<{column_width}}{group.location}")

def creatergs():

    # Provision the resource group.
    rg_result = resource_client.resource_groups.create_or_update(
        "KatanExample-rg",
        {
            "location": "centralus"
        }
    )

    print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

    # To update the resource group, repeat the call with different properties, such
    # as tags:
    rg_result = resource_client.resource_groups.create_or_update(
        "KatanExample-rg",
        {
            "location": "centralus",
            "tags": { "environment":"test", "department":"tech" }
        }
    )
    print(f"Updated resource group {rg_result.name} with tags")


if __name__ == "__main__":
    creatergs()