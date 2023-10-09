from pulumi import Output
from pulumi_azure_native import storage
from src.config import Config


config = Config()


class StorageAccount(storage.StorageAccount):
    def __init__(self) -> None:
        super().__init__(
            config.storage_account_name,
            resource_group_name=config.resource_group_name,
            sku=storage.SkuArgs(
                name=storage.SkuName.STANDARD_LRS,
            ),
            kind=storage.Kind.STORAGE_V2,
            allow_blob_public_access=False,
            enable_https_traffic_only=True,
        )

        primary_access_key: Output = Output.all(
            config.resource_group_name,
            self.name,
        ).apply(lambda args: storage.list_storage_account_keys(
            resource_group_name=args[0],
            account_name=args[1]
        )).apply(lambda keys: keys.keys[0].value)

        self.connection_string: Output = Output.all(self.name, primary_access_key).apply(
            lambda args: f"DefaultEndpointsProtocol=https;AccountName={args[0]};AccountKey={args[1]};EndpointSuffix=core.windows.net"
        )
