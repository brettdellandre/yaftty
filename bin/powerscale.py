from pprint import pprint
import urllib3
import sys
import isi_sdk_9_1_0 as isi_sdk
from isi_sdk_9_1_0.rest import ApiException

urllib3.disable_warnings()

isiuser = "none"
if("--isi-user" in  sys.argv):
    isiuser = sys.argv[sys.argv.index("--isi-user") + 1]
isipassword = "none"
if("--isi-password" in  sys.argv):
    isipassword = sys.argv[sys.argv.index("--isi-password") + 1]
isimgmtip = "none"
if("--isi-mgmt-ip" in  sys.argv):
    isimgmtip = sys.argv[sys.argv.index("--isi-mgmt-ip") + 1]

# configure username and password
configuration = isi_sdk.Configuration()
configuration.username = isiuser
configuration.password = isipassword
configuration.verify_ssl = False


# configure host
configuration.host = "https://" + isimgmtip + ":8080"
api_client = isi_sdk.ApiClient(configuration)
protocols_api = isi_sdk.ProtocolsApi(api_client)
network_api = isi_sdk.NetworkApi(api_client)

# get all exports
sort = "description"
limit = 50
dir = "ASC"
try:
    api_response_nfs_exports = protocols_api.list_nfs_exports(sort=sort, limit=limit, dir=dir)
    pprint(api_response_nfs_exports)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s") % e

# get all networking interfaces
sort = "id"
limit = 50
dir = "ASC"
try:
    api_response_network = network_api.get_network_interfaces(sort=sort, limit=limit, dir=dir)
    pprint(api_response_network)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_subnets_subnet_pools: %s") % e