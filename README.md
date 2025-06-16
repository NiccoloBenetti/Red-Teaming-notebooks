# Red-Teaming-notebooks README
Red Teaming Notebooks

## Conda Environment Installation
```
conda create -n redTA-env python=3.12 -y
conda activate redTA-env
pip install -r ./infra/requirements.txt
jupyter kernelspec uninstall redTA-env -y
python -m ipykernel install --user --name=redTA-env
```

## Credentials should be stored in `../config/credentials_my.env` as follows
```
AZURE_TENANT_ID = "***"
AZURE_SUBSCRIPTION_ID = "***"
AZURE_HUB_RESOURCE_GROUP_NAME = "***"
AZURE_HUB_PROJECT_NAME = "***"
AZURE_PJ_PROJECT_ENDPOINT = "https://<aifoundry_name>.services.ai.azure.com/api/projects/<project_name>"
AZURE_PJ_MODEL_ENDPOINT = "https://<aifoundry_name>.cognitiveservices.azure.com/openai/deployments/<deployment_name>-4o/chat/completions?api-version=2025-01-01-preview"
AZURE_PJ_MODEL_NAME = "***"
AZURE_PJ_MODEL_API_KEY = "***"

# SEMANTIC KERNEL FOR AZURE OPENAI
GLOBAL_LLM_SERVICE="AzureOpenAI"

AZURE_OPENAI_ENDPOINT = https://***.openai.azure.com/
AZURE_OPENAI_API_KEY = "***" 

MODEL_DEPLOYMENT_NAME = "***" # e.g. gpt-40 or gpt-4.1
```
