from pulumi import ResourceOptions, Output
from pulumi_azure_native import keyvault, storage
from src.config import Config


config = Config()


class Secret(keyvault.Secret):
    def __init__(self, vault: keyvault.Vault, storage_account: storage.StorageAccount, secret: str,) -> None:
        super().__init__(
            secret_name=config.secret_name,
            resource_name=config.secret_name,
            resource_group_name=config.resource_group_name,
            vault_name=vault.name,
            properties=keyvault.SecretPropertiesArgs(
                value=secret,
            ),
            opts=ResourceOptions(parent=vault, depends_on=storage_account),
        )

        self.reference_string: Output = Output.all(
            vault.name,
            self.name,
        ).apply(lambda args: f"@Microsoft.KeyVault(SecretUri=https://{args[0]}.vault.azure.net/secrets/{args[1]})/")
