This folder contains Python code

Update the configuration values to include the  **region** and a **key** from the **Azure Speech service** resource you created.

Save the `.env` configuration file.

```python
SPEECH_KEY="your_speech_service_key"
SPEECH_REGION="eastus"
```

# translator_from_file.py

Use this if you want to tried an audio file, you can use `station.wav`

# translator_microphone.py

Use this if there is an microphone device available