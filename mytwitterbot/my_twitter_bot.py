import tweepy
import schedule
import time
import os

print('this is my twitter bot')
def get_auth_key():
    CONSUMER_KEY = 'bYAfLbk9SG4F7MYOOUt5nkaRP'
    CONSUMER_SECRET ='QuH4NkDGTayxuipGrv2Avz8mNGEeucaqJE2MjGjpVK3Ql2xfRk'
    ACCESS_KEY = '1152952023936933888-XqXOZ3ytt3SyKiljfIf07lSgmlAgt7'
    ACCESS_SECRET = 'Aqvysd7ajtrEIs7iBqbF7ULPwF9UyCCOCSlONQyflAO0s'

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

FILE_NAME = 'morningquotes.txt'

def read():
    with open(FILE_NAME,'r') as f:
        line=f.readline().strip()

    with open(FILE_NAME,'r') as f:
        lines=f.readlines()

    with open(FILE_NAME,'w') as f:
        f.write( ''.join( lines[1:] ) )
    return line

def quotes_of_day():
    api = get_auth_key()
    print("Got the API token")
    line = read()
    print("Read the line from the file")
    api.update_status(line+" #morningvibes #morningquotes")
    print("status update is done!")
os.environ['TZ'] = 'Asia/Kolkata'
schedule.every().day.at("09:00").do(quotes_of_day)
print("schdeduled")

while True:
    schedule.run_pending()
    time.sleep(60)