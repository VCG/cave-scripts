from caveclient import CAVEclient
from dotenv import dotenv_values

config = dotenv_values("./.env")

server = "https://global.brain-wire-test.org"
datastack_name = "h01_c3_flat"
token = config["TOKEN"]
# renew using https://global.brain-wire-test.org/auth/api/v1/create_token

client = CAVEclient(server_address=server, datastack_name=datastack_name, auth_token=token)

table_name = "test_table"
description = """
This is a test table to demonstrate table creation and annotation upload.
The data in this table is random and should not be used for analysis.
This table was create by Jakob Troidl
"""

client.annotation.create_table(table_name=table_name,
                               schema_name="bound_tag",
                               description=description,
                               voxel_resolution=[1, 1, 1])
