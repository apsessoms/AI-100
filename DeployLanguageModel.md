# Deploying Language Models in Azure AI Foundry


Deploying a language model in Azure AI involves selecting the right model for your use case and following best practices for deployment, security, and scalability.

## 1. Choosing a Language Model

Azure AI offers several pre-trained language models, including OpenAI GPT, Azure OpenAI Service, and custom models. Consider the following when choosing a model:

| Model Type                | Use Case Examples                | Notes                                  |
|---------------------------|----------------------------------|----------------------------------------|
| GPT-3 / GPT-4 (OpenAI)    | Chatbots, summarization, Q&A     | Powerful, general-purpose, large scale |
| Custom Fine-tuned Model   | Domain-specific tasks            | Requires training data and tuning      |
| Azure Cognitive Services  | Translation, entity recognition  | Pre-built for specific tasks           |

Take a look at the **details** tab for each model to understand its capabilities and limitations.

![Model Details](https://i.imgur.com/v0XonxD.png)

**Additionally** view the **benchmarks** tab to compare performance metrics across different models in similiar tasks.
![Model Benchmarks](https://i.imgur.com/CTMUM6y.png)

- **Assess your requirements:** Do you need general language understanding, or a model fine-tuned for your domain?
- **Consider cost and latency:** Larger models are more expensive and slower.
- **Check compliance needs:** Some models offer region or compliance options.

## 2. Preparing for Deployment

Before deploying, ensure you have:

- An Azure subscription with access to Azure AI services.
- The required resource group and region selected.
- Proper access permissions (Owner or Contributor role).

## 3. Deploying a Language Model

### Using Azure Portal

1. Go to [Azure Foundry Portal](https://ai.azure.com/)
2. Select the **gpt-4o** chat completion model
3. Select **use this model** and create a project name using good naming conventions. 

![Create Project](https://i.imgur.com/MFFW0W9.png)

4. Review and select **Create** and wait for the project to be created. By using the default **global standard deployment**, the tokens per minute rate limit of 50k will be applied. By limiting TPM you can avoid over-using quota available in your subscription.


### Using Azure CLI

```bash
# Example: Deploying Azure OpenAI resource
az cognitiveservices account create \
  --name my-openai-resource \
  --resource-group my-resource-group \
  --kind OpenAI \
  --sku S0 \
  --location eastus
```
## 4. Accessing the Deployed Model
If your chat playground did not open, simply click on the **Open in playground** button to start testing your deployed model. In the **setup** pane, type in the prompt "You are an AI assistant that helps solve problems." and click on **Apply Changes**. 

![Open in Playground](https://i.imgur.com/HuJqyPU.png)

In the chat window, enter the following prompt to test the model:

```I have a github repo that is not syncing locally to my computer. I have already updated the application but it is still not working. I need to make sure the changes I make locally sync to github and vice versa. Can you help me troubleshoot this? ```

+ Review the response and then type in the following prompt to continue the conversation:

```how do i know what version is the latest? it only showed me what is installed locally?```

When you review the response, you can see that the model is able to walk through the steps to figure out the version.

![Chat Response](https://i.imgur.com/mfdLDE3.png)



## 5. Try a different model

In the left hand navigation bar, under **my assets** click on **Models & endpoints**.
In the **model deployment** tap, click on the deploy model drop down list and select **deploy base model** as seen below.

![Deploy Base Model](https://i.imgur.com/iDdsCwZ.png)

In the search box, type "Phi-4-mini-instruct" and click confirm. Repeat the steps for creating a project and using good naming conventions. Click **deploy**. 

![Select Model](https://i.imgur.com/P8bVcoI.png)

Type in the same prompt as before and see how the response differs.

```I have a github repo that is not syncing locally to my computer. I have already updated the application but it is still not working. I need to make sure the changes I make locally sync to github and vice versa. Can you help me troubleshoot this? ```

Ask the follow up question again:

```how do i know what version is the latest? it only showed me what is installed locally?```

When you review the response, you can see that the model is able to walk through the steps to figure out the version, but it is not able to tell you what the latest version is.

## Which one is better at math?

To compare the two models on their math capabilities, you can ask both models the same math question and evaluate their responses. For example, you can ask:

```I have 53 socks in my drawer: 21 identical blue, 15 identical black and 17 identical red. The lights are out, and it is completely dark. How many socks must I take out to make 100 percent certain I have at least one pair of black socks?```

When I ran it, you can see that with phi-4-mini-instruct, it got the answer wrong. But with gpt-4o, it got the answer correct.
![Math Comparison](https://i.imgur.com/om5N0zx.png)

You have successfully deployed two different models and compared their responses to the same prompts.

## References

- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Azure CLI Documentation](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices)