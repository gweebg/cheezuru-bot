# CHEEZURU-BOT 

*guya-4koma* is a python script that automates the process of tweeting whenever a new chapter of Kaguya Sama 4koma is released.

## Installation

You can either use GIT to clone the repository or just download it as a zip.

```bash
git clone https://github.com/gweebg/cheezuru-bot
```
## How it works

The script uses python librarie [requests](https://requests.readthedocs.io/en/master/) and [BS4](https://pypi.org/project/beautifulsoup4/) to scrape information from [mangadex](https://mangadex.org/). 

In this case, it is scraping the episode number from [here](hhttps://mangadex.org/title/22151/kanojo-okarishimasu) and once it reaches it's goal, the script uses [tweepy](https://www.tweepy.org/) to tweet that a new chapter has released.
## Usage

# In case of hosting on Heroku:

I already made it so it was easy to deploy it there, so you only need to add the twitter credentials: 
```bash
# Add this #

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = "" 
CONSUMER_KEY = "" 
CONSUMER_SECRET = ""

# Each one of this is a single variable that you will need to add #
``` 
# In case of hosting on a machine:

To use the script you first need to add your Twitter developer credentials on the file *credentials.py*. 

Once that's done you can simply execute the script.

I recommend hosting on either a dedicated computer (Raspberry Pi) or on Heroku that works just fine. 

```python
# credentials.py

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""        # Add guya.moe twitter credentials here, never share this. #
CONSUMER_KEY = ""               # These are essential for the tweeting part. #
CONSUMER_SECRET = ""

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Contact me by:

- [Twitter](https://twitter.com/gweelherme)
- [Discord](https://discordapp.com/users/299252968882962432)

## License
[MIT](https://choosealicense.com/licenses/mit/)