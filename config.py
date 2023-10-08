from typing import Dict, List
from decouple import config as env
from pulumi_azure_native import keyvault


class config:
    def __init__(self) -> None:
        self.resource_group_name : str = env("RESOURCE_GROUP_NAME")
        self.storage_account_name : str = env("STORAGE_ACCOUNT_NAME")
        self.blob_container_name : str = env("BLOB_CONTAINER_NAME")
        self.vault_name : str = env("VAULT_NAME")
        self.__vault_access_policy_oid : str = env("VAULT_ACCESS_POLICY_OBJECT_ID")
        self.vault_tenant_id : str = env("VAULT_TENANT_ID")
        self.vault_access_policy : List[Dict] = [{
            "tenantId": self.vault_tenant_id,
            "objectId": self.__vault_access_policy_oid,
            "permissions": keyvault.PermissionsArgs(
                certificates=[
                    "get",
                    "list",
                    "delete",
                    "create",
                    "import",
                    "update",
                    "managecontacts",
                    "getissuers",
                    "listissuers",
                    "setissuers",
                    "deleteissuers",
                    "manageissuers",
                    "recover",
                    "purge",
                ],
                keys=[
                    "encrypt",
                    "decrypt",
                    "wrapKey",
                    "unwrapKey",
                    "sign",
                    "verify",
                    "get",
                    "list",
                    "create",
                    "update",
                    "import",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge",
                ],
                secrets=[
                    "get",
                    "list",
                    "set",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge",
                ],
            ),
        }],
        self.secret_name : str = env("SECRET_NAME")


envs = config()
