# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/snmp' resources
# =============================================


class SysSnmpSchema(MetaParser):

    schema = {}


class SysSnmp(SysSnmpSchema):
    """ To F5 resource for /mgmt/tm/sys/snmp
    """

    cli_command = "/mgmt/tm/sys/snmp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
