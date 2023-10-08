# BitPlatform Interview Task2
I have been asked to get familiarized with the open source Infrastructure as Code tool, `pulumi`, along with the Azure Cloud platform.

To do that, I had to:
- Create a Blob Storage Account
- Create a Blob Container on the Storage Account
- Create a Key Vault
- Store Blob Storage connection string as a secret on the Key Vault
- Export a reference string of the Key Vault Secret containing the connection string

## How to Use
To use this project, after clonning and openning it on your favorite IDE, you should:
- Install Python3 (works with 3.11, official installer)
- [Windows] Install Visual Studio Build Tools (with C++ build tools)
- Install Azure CLI ([Windows] `winget install -e --id Microsoft.AzureCLI`)
- Install pullumi ([Windows] `winget install pulumi`)
- Create and login to a Pulumi account
- Create a virtual environment (`python3 -m venv venv`) and activate
- Install requirements (`pip install -r requirements.txt`)
- Create a `.env` from `.env.template` and fill in properly
- Create a stack with `pulumi stack init` and configure Pulumi to access your Azure Cloud Account:
    ```
    pulumi config set azure-native:clientId <clientID>
    pulumi config set azure-native:clientSecret <clientSecret> --secret
    pulumi config set azure-native:tenantId <tenantID>
    pulumi config set azure-native:subscriptionId <subscriptionId>
    pulumi config set azure-native:location <locationName>
    ```
- Finally `pulumi up` to create the described infrastructure

## Challenges
Throughout this activity, I hit the folllowing bumps in the road:
- Mistakenly installed Python 3.12, which at the time of writing this is in prerelease, and couldn't initalize a pulumi project with `pulumi new azure-python`; because the dependencies could not be built.
- Needed to install Visual Studio Build Tools along with C++ Build Tools to successfully install project dependencies. There was no mention of this in the documentation. I'm not sure, but maybe if I had installed a lower python version, packages were available and no build was required. But there was no mention of which python versions were supported in the documentation as well.
- Since I was provided with 2 different authentication information, I tried logging in to azure cloud CLI through web. I found it confusing at first.
- Logging in through Service Principal was shockingly twisted, since I was entering the credentials directly to the `Pulumi.prod.yml`, causing the password to be enterred in plain text and consequently, the authentication to fail. Unfortunately, no proper error was being displayed even with `debug` and `verbose` flags on (just that I should login through `az` and logging in through `az` with service principal ended up with a new error indicating that `pulumi` could not use that type of authentication)
- The documentation for Vault is apparently outdated, mentioning the `properties` attribute accepts the output of the `VaultPropertiesResponseArgs` function, however, the `VaultPropertiesArgs` function was needed ([link](https://www.pulumi.com/registry/packages/azure-native/api-docs/keyvault/vault/#create-a-new-vault-or-update-an-existing-vault))
- The Vault resource required the `tenant_id` to be directly passed and does not use the `tenant_id` in the stack yaml configuration, which befuddled me since `location` worked the other way.
- After creating the keyvault with full access and creating the secret in it, `pulumi destroy` started responding with error, indicating that the access was denied. Debugging this made me cry and took a lot of time; it felt like I was stuck in the matrix :-D, but eventually it became clear that the `object_id` in the project definition was not the `object_id` that keyvault expected for proper service principal access. I ended up obtaining it through `az ad sp show --id <appID>`. The positive side was that I got a little comfortable playing with the `az` tool.

## Final Words
I had fun playing with `Pulumi` and the Azure Cloud. The general notion behind the task and the amount of time it demanded was satisfying to me. However, task definition could be further improved to avoid confusion.

Generally, I could hardly find the solution to my issues through the documentation and the community searches, which was a letdown for such a fantastic tool.
