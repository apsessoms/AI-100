# Creating an AI Solution in Azure AI Foundry

1. Go to the [Azure AI Foundry portal at](https://ai.azure.com/). Sign in using your Azure credentials. You should see the home page of the Azure AI Foundry portal.

![Azure AI Foundry Portal](https://i.imgur.com/KabjlrT.png)

**Projects** provide a workspace for AI development. We will start by choosing a model we want to work with. 

## How do I know which model to choose?
You can choose from a variety of models based on your project requirements. Here are some common use cases and the corresponding models you might consider:
+ **gpt-5**: Best for complex reasoning, detailed writing, coding, and research. Use when you need **high-accuracy** and **deep understanding**. 
    + Slower and more expensive. 💡

+ **gpt-5-mini / gpt-5-nano**: Lighter, faster versions of GPT-5 that is good for **chatbots, quick responses, and lightweight applications**. 
    + Lower cost, but also less powerful than the full GPT-5.💡

+ **grok-code-fast-1**: A coding-focused model.

    + Best for code generation, debugging, or explaining programming concepts.

+ **DeepSeek-R1-0528**: A reasoning-focused model (from another developer).

    + Useful for math, logic-heavy tasks, or step-by-step problem solving.

## Quick Guide (How to Choose)

✅ Need depth and accuracy? → gpt-5

⚡ Need speed & cost savings? → gpt-5-mini / gpt-5-nano

💬 Need great conversations? → gpt-5-chat

💻 Need coding help? → grok-code-fast-1

🧠 Need strong reasoning? → DeepSeek-R1

2. Click on **Create an agent**. Search for **gpt-4o** model & review the details. Select **Use this model** and create a name for your project. It is important to follow good naming schemes so you can easily identify your projects later. Make sure you use the correct region and resource group for your project. Click **Create project**.
![Create Project](https://i.imgur.com/8plrwps.png)

Reducing the tokens used can help reduce costs and over-using the quota available. Once your project is created, you will see the project dashboard.

![Project Dashboard](https://i.imgur.com/hGlfQxj.png)

**Resource**: This is where the Azure AI Foundry resource was created to support your project. **Project**: The project level relates to your individual project where you can add and manage specific resrouces. 

Click on the **resource group** under Project Details to open the Azure portal and see all the resources created to support your Azure Ai Foundry project. 
![Azure Portal](https://i.imgur.com/NEKPJMa.png)    

3. You can close the Azure Portal and return to the Azure AI Foundry portal. Under **overview**, click on **endpoints.**
    + This is where you can find the endpoints that client applications will use to connect to the project and the models including the AI services involved. 

![Endpoints](https://i.imgur.com/WMnE60K.png)

Here you will see the endpoints and authorization keys that you can bake into your application code to access Azure AI foundry projects, Azure OpenAI, and other Azure AI services.


4. Test a generative AI model. In the lefthand menu, click on **playground** and open the **chat playground**. Check to make sure you see the **gpt-4o** model selected in the deployment dropdown.

In the **Setup** section, give the model the following instructions:

```You are a highly trained business coach. Your role is to help organizations align their strategy, structure, and people. Provide clear, actionable guidance that balances long-term vision with practical steps. Always focus on clarity, accountability, and measurable outcomes.```

In the query section, ask the model the following question:

```Where can I start with improving the strategy of my wholesale real estate company?```

View the response from the model. Lab complete. You have successfully created an AI project in Azure AI Foundry and tested a generative AI model. 