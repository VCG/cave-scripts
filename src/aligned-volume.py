from caveclient.auth import AuthClient
from caveclient.infoservice import InfoServiceClient
from dotenv import dotenv_values

config = dotenv_values("./.env")

server = "https://global.brain-wire-test.org"
datastack_name = "h01_c3_flat"
token = config["TOKEN"]

auth = AuthClient(server_address=server, token=token)
infoclient = InfoServiceClient(
    server_address=server,
    auth_client=auth,
    api_version="latest",
)
aligned_volume_names = infoclient.get_aligned_volumes()

print(aligned_volume_names)
