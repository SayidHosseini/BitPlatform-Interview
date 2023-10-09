from typing import Dict, List, Self
from decouple import config as env
from pulumi_azure_native import keyvault


class Config:
    _env = None

    def __new__(cls) -> Self:
        if cls._env is None:
            cls._env = super(Config, cls).__new__(cls)
            cls._env.resource_group_name: str = env("RESOURCE_GROUP_NAME")
            cls._env.storage_account_name: str = env("STORAGE_ACCOUNT_NAME")
            cls._env.blob_container_name: str = env("BLOB_CONTAINER_NAME")
            cls._env.vault_name: str = env("VAULT_NAME")
            cls._env._vault_access_policy_oid: str = env(
                "VAULT_ACCESS_POLICY_OBJECT_ID")
            cls._env.vault_tenant_id: str = env("VAULT_TENANT_ID")
            cls._env.vault_access_policy: List[Dict] = [{
                "tenantId": cls._env.vault_tenant_id,
                "objectId": cls._env._vault_access_policy_oid,
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
            cls._env.secret_name: str = env("SECRET_NAME")

            cls._check_integrity(cls)
        return cls._env

    def _check_integrity(self):
        if not (self._env.resource_group_name
                and self._env.storage_account_name
                and self._env.blob_container_name
                and self._env.vault_name
                and self._env._vault_access_policy_oid
                and self._env.vault_tenant_id
                and self._env.secret_name):
            print("At least one environment variable not provided!")
            import sys
            sys.exit(1)
