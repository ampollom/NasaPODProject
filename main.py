from datetime import datetime
from bs4 import BeautifulSoup
import requests
import urllib
from PIL import Image
import os

#print(os.getcwd())

#Retrieves html from NASA website
URL = "https://apod.nasa.gov/apod/"
current_datetime = datetime.now().strftime("(%Y.%m.%d)")
links = []

def parseUrl(URL):
    #requests and parses the page from the provided url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #checks for image and video tags
    image_tags = soup.find_all('img')
    video_tags = soup.find_all('iframe')

    #sends links to the appropriate method
    if len(video_tags) != 0:
        retriveVideoTags(video_tags, links)
    elif len(image_tags) != 0:
        retriveIMGTag(image_tags, links)
    else:
        print("Houston we have a problem")


    #print(soup)

    #retriveIMGTag(soup, links)
#print(page.text)

#prints the url for the video
def retriveVideoTags(video_tags, links):
    #video_tags = soup.find_all('iframe')
    for video_tag in video_tags:
        links.append(video_tag['src'])
        print("No image today, check out this video: " + links[0])


#Parses HTML and locates image tags
def retriveIMGTag(image_tags, links):
    #image_tags = soup.find_all('img')
    for image_tag in image_tags:
        links.append("https://apod.nasa.gov/apod/" + image_tag['src'])
    retreiveIMGFile(links)
#print(links)

#Collects and saves image with current date from link
def retreiveIMGFile(links):
    urllib.request.urlretrieve(links[0], 'images/nasapictureoftheday'+ current_datetime +'.png')

def displayImage():
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
#errors: what if the image is a video?
#send code to Github

parseUrl(URL)
#displayImage()
