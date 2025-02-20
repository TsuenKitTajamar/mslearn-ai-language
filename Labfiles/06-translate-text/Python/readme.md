This folder contains Python code

Update the configuration values to include the  **region** and a **key** from the Azure Language resource you created.

Save the `.env`configuration file.

```bash
TRANSLATOR_KEY="your_translator_Service_Key"
TRANSLATOR_REGION="your_service_region"
``` 

# text-translation

This should be the output:
```bash
-------------
review1.txt

Good Hotel and staff
The Royal Hotel, London, UK
3/2/2018
Clean rooms, good service, great location near Buckingham Palace and Westminster Abbey, and so on. We thoroughly enjoyed our stay. The courtyard is very peaceful and we went to a restaurant which is part of the same group and is Indian ( West coast so plenty of fish) with a Michelin Star. We had the taster menu which was fabulous. The rooms were very well appointed with a kitchen, lounge, bedroom and enormous bathroom. Thoroughly recommended.
Language: en

-------------
review2.txt

Tired hotel with poor service
The Royal Hotel, London, United Kingdom
5/6/2018
This is a old hotel (has been around since 1950's) and the room furnishings are average - becoming a bit old now and require changing. The internet didn't work and had to come to one of their office rooms to check in for my flight home. The website says it's close to the British Museum, but it's too far to walk.
Language: en

-------------
review3.txt

Good location and helpful staff, but on a busy road.
The Lombard Hotel, San Francisco, USA
8/16/2018
We stayed here in August after reading reviews. We were very pleased with location, just behind Chestnut Street, a cosmopolitan and trendy area with plenty of restaurants to choose from. The
Marina district was lovely to wander through, very interesting houses. Make sure to walk to the San Francisco Museum of Fine Arts and the Marina to get a good view of Golden Gate bridge and the city. On a bus route and easy to get into centre. Rooms were clean with plenty of room and staff were friendly and helpful. The only down side was the noise from Lombard Street so ask to have a room furthest away from traffic noise.
Language: en

-------------
review4.txt

Very noisy and rooms are tiny
The Lombard Hotel, San Francisco, USA
9/5/2018
Hotel is located on Lombard street which is a very busy SIX lane street directly off the Golden Gate Bridge. Traffic from early morning until late at night especially on weekends. Noise would not be so bad if rooms were better insulated but they are not. Had to put cotton balls in my ears to be able to sleep--was too tired to enjoy the city the next day. Rooms are TINY. I picked the room because it had two queen size beds--but the room barely had space to fit them. With family of four in the room it was tight. With all that said, rooms are clean and they've made an effort to update them. The hotel is in Marina district with lots of good places to eat, within walking distance to Presidio. May be good hotel for young stay-up-late adults on a budget

Language: en

-------------
review5.txt

Un hôtel agréable
L'Hotel Buckingham, Londres, UK
J’adore cet hôtel. Le personnel est très amical et les chambres sont confortables.
Language: fr

Translation:
A pleasant hotel
The Buckingham Hotel, London, UK
I love this place. The staff is very friendly and the rooms are comfortable.
```

# translate.py

This should be the output:

```bash
Enter a target language code for translation (for example, 'en' | 'de' | 'fr'):
de

Enter text to translate ('quit' to exit):hola estoy haciendo un test con azure
'hola estoy haciendo un test con azure' was translated from es to de as 'Hallo, ich mache einen Test mit Azure'.
```
```python
Enter a target language code for translation (for example, 'en' | 'de' | 'fr'):
fr

Enter text to translate ('quit' to exit):This a test. I'm using Azure translator service.
'This a test. I'm using Azure translator service.' was translated from en to fr as 'C’est un test. J’utilise le service de traduction Azure.'.
```

135 languages are supported.
[Check the official Azure documentation](https://learn.microsoft.com/azure/ai-services/translator/language-support#translation)
