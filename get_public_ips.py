# Get Public IPs in an Azure resource group
import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient

from msrestazure.azure_exceptions import CloudError

RG_NAME="upskill-challenge"

# You will want to supply the values in this function as environment variables
def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id

credentials, subscription_id = get_credentials()
network_client = NetworkManagementClient(credentials, subscription_id)

def get_public_ips_by_rg():
    try:
        print(f'Getting pulbic IPs in Resource Group {RG_NAME}')
        public_ips = network_client.public_ip_addresses.list(RG_NAME)
        for ip in public_ips:
            print(f'{ip.ip_address}')
    except CloudError:
        print('Could not get the public IPs:\n{}'.format(traceback.format_exc()))
    else:
        print(f'\nGot all public IP addresses for {RG_NAME}')

if __name__ == "__main__":
    get_public_ips_by_rg()
