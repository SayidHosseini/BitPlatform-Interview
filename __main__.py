import pulumi
from storage_account import StorageAccount
from blob_container import BlobContainer
from vault import Vault
from secret import Secret


class Main():
    def __init__(self):
        storage_account = StorageAccount().object
        BlobContainer(storage_account)
        vault = Vault()
        secret = Secret(vault, storage_account, storage_account.connection_string).object

        pulumi.export("secret_reference", secret.reference_string)


Main()
