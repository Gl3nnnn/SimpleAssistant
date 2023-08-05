import requests
import pywhatkit as kit
from decouple import config

NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
