from datetime import datetime
from bs4 import BeautifulSoup
import requests
import urllib
from PIL import Image
import os

#print(os.getcwd())

#Retrieves html from NASA website
URL = "https://apod.nasa.gov/apod/"
page = requests.get(URL)
current_datetime = datetime.now().strftime("(%Y.%m.%d)")

#print(page.text)

#Parses HTML and locates image tags
soup = BeautifulSoup(page.content, "html.parser")
image_tags = soup.find_all('img')
links = []
for image_tag in image_tags:
    links.append("https://apod.nasa.gov/apod/" + image_tag['src'])

#print(links)

#Collects and saves image with current date from link
urllib.request.urlretrieve(links[0], 'images/nasapictureoftheday'+ current_datetime +'.png')

#Opens image from saved file
dimensions = (1926, 2000)
i = Image.open('images/nasapictureoftheday'+ current_datetime +'.png')
i.thumbnail(dimensions)
i.show()

#use beautiful soup to get dimensions
#investigate setting up Azure as storage
#investigate deleting images
#clean up code into methods
#figure out how to include explanation with image

