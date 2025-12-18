# Getting to know Azure AI Foundry

**Azure AI Foundry** is where you build, store, and connect all of your AI applications. Things like language models, image analyzers, document processors, or language translators. If you're wondering what a **SDK** is, it stands for Software Development Kit and it lets you use Azure AI Foundry from your own code. Instead of traditional clickops in the portal, the SDK lets you do all of the same things automatically and repeatably through code. 

## Common Analgy
If you have ever built a website on **Wix Studio** or **WordPress**, you know that you can drag and drop components to build your site. With SDKs, you can do the same thing but using common programming languages like Python, JavaScript, or C#.

## Connecting to a Azure AI Foundry Project

The first task in any Azure AI Foundry SDK code is to connect it to a **project**. The project has a unique **endpoint** and keys to include:
+ **Project Endpoint** - This is used to access project connections, agents, and model within the resource
+ **API Endpoint** - This is for Azure OpenAIs APIs
+ **Azure AI Endpoint** - For Azure AI Services APIS (Vision & Language)

Each Azure AI Foundry project can connect to other services (Azure Storage, Azure OpenAI, or Azure AI Search). These are called **connections.** They’re basically links your project uses to talk to those services. 

## Chat Client Tutorial

At the time of this writing, everyone has used ChatGPT and typed in prompts to engage in a conversation. You can use the Azure AI Foundry SDK to retriever a project client, get an authenticated OpenAI chat client for any models in the projects Azure AI Foundry resource. No more juggling around multiple sets of API keys! This makes it easy to write code that interacts with the model in YOUR project. 

1. 