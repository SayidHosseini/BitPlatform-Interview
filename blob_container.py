from pulumi_azure_native import storage
from pulumi import ResourceOptions
from config import envs as config


class BlobContainer:
    def __init__(self, storage_account: storage.StorageAccount) -> None:
        storage.BlobContainer(
            config.blob_container_name,
            account_name=storage_account.name,
            resource_group_name=config.resource_group_name,
            public_access=storage.PublicAccess.NONE,
            opts=ResourceOptions(parent=storage_account),
        )
