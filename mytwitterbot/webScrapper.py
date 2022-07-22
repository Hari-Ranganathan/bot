import requests
from bs4 import BeautifulSoup
from datetime import date
import calendar
import tweepy
from twilio.rest import Client

def get_quote():
    url = 'https://www.brainyquote.com/quote_of_the_day'
    quote=''
    response = requests.get(url)
    try:
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text.encode('UTF-8'), 'html.parser')
            quote = soup.find('a', attrs={'title':'view quote'}).find('img').attrs['alt']
        else:
            send_message(response.status_code,response.reason)
    except Exception as inst:
        send_message(500,inst.with_traceback)
    return quote

def get_hashtag():
    day=calendar.day_name[date.today().weekday()]
    hashtag = '#'+ day +'Motivation #'+ day +'Thoughts'
    return hashtag

def get_auth_key():
    CONSUMER_KEY = ''
    CONSUMER_SECRET =''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def quotes_of_day():
    api = get_auth_key()
    print("Got the API token")
    quote = get_quote()
    hashtag = get_hashtag()
    line = quote +' '+hashtag
    print("Done Web Scrapping")
    api.update_status(line+" #morningvibes #morningquotes")
    print("status update is done!")

def send_message(status:int,reason:str):
    twilio_sid=''
    auth_token=''

    whatsapp_client = Client(twilio_sid,auth_token)

    contact_directory = {'mine':'+919952597675'}

    for key,value in contact_directory.items():
        alert_msg = whatsapp_client.messages.create(
            body= status +','+reason,
            from_='whatsapp:+14155238886',
            to='whatsapp:'+value
        )
    print(alert_msg.sid)

quotes_of_day()
