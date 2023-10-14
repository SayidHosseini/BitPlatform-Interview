# Task 1
Consider a retail company that has a sales website hosted on on-promises. The company is intended to move to a new office soon. Also, they need to migrate some of their infrastructure resources to the Microsoft Azure cloud. The team is using the .NET platform and Microsoft SQL database.
Now, please read below their requirements and write your suggestions for each item. Note that there might not be a single correct answer to each question. What matters is how you approach the problem and provide suggestions according to your knowledge, experience, and more importantly, your
research on the problem. So, make sure to research each question within the scope of infrastructure and Azure cloud (e.g., using Azure [documentation](https://docs.microsoft.com/en-us/azure/?product=popular)) before writing your suggestions.

#### 1.4) What solutions/methods do you suggest having Web Application Firewall?
I think we can go with the `Azure Web Application Firewall` solution which centrally protects web applications from different types of threats and vulnerabilities and can be integrated with other Microsoft services such as `Azure Application Gateway`, `Azure Front Door` and `Azure CDN` to handle production load requirements.

#### 1.5) The team is decided to use Azure Firewall coupled with an Azure Firewall Policy resource to ensure further security. There are two types of rules that can be defined in Azure Firewall Policy: network rules and application rules. What are the differences between these two types of rules? Provide a couple of examples for each.
The two type of rules go hand-in-hand to provide full security to the infrastructure. Network rules focus on controlling traffic flow between network segments (such as Virtual or on-premises networks), while application rules are designed to control access to specific websites or services at the application layer (based on domain names and URLs). An example network rules would be "Allowing inbound traffic to port 80 and 443" and application rule could be "Denying all HTTP traffic to web application at secure.example.com".

#### 1.6) Suggest an Azure resource/service for each of the following requirements:
- **Hosting a .NET website** -> `Azure App Service`

    Key factors: _Automatic scaling, High availability, Built-in security, Easy deployment_
- **A database for transactional data and user credentials** -> `Azure SQL Database`

    Key factors: _High performance, Scalability, Reliability, Security_

- **A space/storage for archiving logs, image, and video** -> `Azure Blob Storage`

    Key factors: _Low cost, High durability, Easy access_

- **A database for semi-structure and unstructured data** -> `Azure Cosmos DB`

    Key factors: _Scalability, Performance, Reliability, Global distribution_


#### 1.7) The retail website has a high traffic on weekends. What is your suggestion to handle this load just on Saturday and Sunday? Please consider the cost issue.
Depending on the website, we may use `Azure Autoscaling` to scale out VMs/Pods in case of consistant high demands of CPU/RAM/QueueLength. For this to work, we either need `Azure Load Balancing` or to cut costs further, `DNS Load Balancing`. Of course using `Azure CDN` could help us deliver a better quality by using caching, smart routing and etc.

If further improvement is required, we might need to put our innovation cap on and try to utilize `Azure Functions` to offload some of the tasks in our web application. This is only possible for tasks that don't require a continuously running server.

#### 1.8) The team needs to implement a central data hub to handle a huge amount of streaming logs generated from a specific source and deliver them to various clients, such as monitoring resources, applications, etc. What solutions do you suggest to implement this data hub? If suggested more than one solution, please give a short comparison as well.
It is possible to use `Azure Event Hubs` or `Azure Kafka on HDInsight` for receiving huge amount of streaming data from multiple sources and distributing them to several resources; if the data needs to be processed and then delivered to the destination resources, we may use `Azure Stream Analytics`. Both of the mentioned services will do the job, however `Azure Event Hub` is specialized for real-time data ingestion and distribution and requires less configurations to work but `Azure Kafka on HDInsight` is general-purpose, provides a lot of flexibilty, more granular control over the streaming data and naturaly, demands more complexity to be overseen.

#### 1.9) The team is required to find a secure solution to store credentials, e.g., keys, secrets, and certificates, used by their applications for authentication and authorization purposes. What solutions do you suggest?
I think the obvious choice would be `Azure Key Vault`. It is a centralized, highly secure, and fully managed service designed for this exact purpose. It provides fine-grained permissions. Also, it seamlessly integrates with a wide range of Azure services and applications, including `Virtual Machines`, `Azure Functions`, `Azure App Service`, `Azure Logic Apps`; and last but not least, supports .NET.
