This folder contains Python code

Update the configuration values to include the  **endpoint** and a **key** from the Azure Language resource you created (available on the **Keys and Endpoint** page for your Azure AI Language resource in the Azure portal). The file should already contain the project and deployment names for your custom entity model.

Save the `.env`configuration file.

```bash
AI_SERVICE_ENDPOINT="your_ai_language_service_endpoint"
AI_SERVICE_KEY="your_ai_language_service_key"
PROJECT=CustomEntityLab
DEPLOYMENT=AdEntities
```

Expected result should be:

```python
test1.txt
        Entity 'Bluetooth earbuds' has category 'ItemForSale' with confidence score of '0.87'
        Entity '$100' has category 'Price' with confidence score of '0.96'
        Entity 'Sacramento, CA' has category 'Location' with confidence score of '0.89'


test2.txt
        Entity 'Dog harness' has category 'ItemForSale' with confidence score of '0.91'
        Entity '$20' has category 'Price' with confidence score of '0.99'
        Entity 'Tucson' has category 'ItemForSale' with confidence score of '0.44'
        Entity 'AZ' has category 'Location' with confidence score of '0.94'


test3.txt
        Entity 'Gaming laptop' has category 'ItemForSale' with confidence score of '1.0'
        Entity '$800' has category 'ItemForSale' with confidence score of '0.8'
        Entity 'Austin, TX' has category 'Location' with confidence score of '0.86'


test4.txt
        Entity 'Bicycle' has category 'ItemForSale' with confidence score of '0.72'
        Entity '$150' has category 'Price' with confidence score of '0.79'
        Entity 'Portland' has category 'Location' with confidence score of '0.74'


test5.txt
        Entity 'Coffee maker' has category 'ItemForSale' with confidence score of '0.8'
        Entity '$50' has category 'Price' with confidence score of '0.9'
        Entity 'Seattle, WA' has category 'Location' with confidence score of '0.93'
```