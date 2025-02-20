This folder contains Python code

Update the configuration values to include the  **endpoint** and a **key** from the Azure Language resource you created (available on the **Keys and Endpoint** page for your Azure AI Language resource in the Azure portal). The file should already contain the project and deployment names for your text classification model.

Save the `.env`configuration file.

```bash
AI_SERVICE_ENDPOINT="your_ai_language_service_endpoint"
AI_SERVICE_KEY="your_ai_language_service_key"
PROJECT=ClassifyLab
DEPLOYMENT=articles
```

Expected result should be:

```bash
test0.txt was classified as 'Entertainment' with confidence score 0.32.
test1.txt was classified as 'Entertainment' with confidence score 0.32.
test2.txt was classified as 'Sports' with confidence score 0.34.
test3.txt was classified as 'News' with confidence score 0.28.
```