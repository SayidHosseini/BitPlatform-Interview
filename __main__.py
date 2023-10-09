import pulumi
from src.storage_account import StorageAccount
from src.blob_container import BlobContainer
from src.vault import Vault
from src.secret import Secret


class Main():
    def __init__(self):
        sa = StorageAccount().object
        BlobContainer(sa)
        vault = Vault()
        secret = Secret(vault, sa, sa.connection_string).object

        pulumi.export("secret_reference", secret.reference_string)


Main()
