##python

#http requests
import requests
#web scraper
from bs4 import BeautifulSoup 
# sendmail
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now = datetime.datetime.now()

#email content placeholder

content = ''

#extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker News stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
