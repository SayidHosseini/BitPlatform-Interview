from pulumi_azure_native import keyvault
from src.config import Config


config = Config()


class Vault:
    def __new__(self) -> keyvault.Vault:
        return keyvault.Vault(
            resource_name=config.vault_name,
            vault_name=config.vault_name,
            resource_group_name=config.resource_group_name,
            properties=keyvault.VaultPropertiesArgs(
                tenant_id=config.vault_tenant_id,
                enabled_for_disk_encryption=True,
                enabled_for_template_deployment=True,
                soft_delete_retention_in_days=14,
                enable_rbac_authorization=False,
                sku=keyvault.SkuArgs(
                    family="A",
                    name=keyvault.SkuName.STANDARD,
                ),
                access_policies=config.vault_access_policy[0],
            ),
        )
