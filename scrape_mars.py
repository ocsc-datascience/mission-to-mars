#!/usr/bin/env python3
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd


def scrape():

   # chrome driver
   executable_path = {'executable_path': '/Users/cott/tmp/chromedriver'}
   browser = Browser('chrome', **executable_path, headless=True)
   
   mars_dict = {}

   # scrape NASA Mars News Site
   target_url = "https://mars.nasa.gov/news/"
   browser.visit(target_url)
   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')
   main = soup.find('ul', class_='item_list')
   news_items = main.find_all('li',class_="slide")
   mars_news = {}
   mars_news['date'] = news_items[0].find('div',class_="list_date").text.strip()
   mars_news['title'] = news_items[0].find('div',class_="content_title").text.strip()
   mars_news['shorttext'] = news_items[0].find('div',class_="article_teaser_body").text.strip()
   print(mars_news)
   mars_dict['mars_news'] = mars_news

   
   # scrape JPL Mars Space Images - Featured Image
   target_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
   browser.visit(target_url)
   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')
   main = soup.find('ul', class_='articles')
   slide = main.find('li', class_='slide')
   fancybox = slide.find('a',class_='fancybox')
   featured_image_url = "https://www.jpl.nasa.gov"+fancybox['data-fancybox-href']
   print(featured_image_url)
   mars_dict['featured_image_url'] = featured_image_url

   # scrape Mars weather twitter
   target_url = "https://twitter.com/marswxreport?lang=en"
   browser.visit(target_url)
   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')
   stream = soup.find('div', class_='stream')
   item = stream.find('li', class_='js-stream-item')
   tweet = item.find('div',class_='js-tweet-text-container')
   mars_weather = tweet.text
   print(mars_weather)
   mars_dict['mars_weather'] = mars_weather

   
   target_url = "https://space-facts.com/mars/"
   tables = pd.read_html(target_url)
   df = tables[0]
   df.rename(columns={0:'Quantity', 1:'Value'},inplace=True)
   mars_facts_string = df.to_html(index=False,header=True,border=0)
   print(mars_facts_string)

   mars_dict['mars_facts'] = mars_facts_string
   
   # get Mars hemisphere images by checking out https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
   # Not sure if it makes sense to serve 20 MBs-size pictures...
   # Also saving lower-res thumbnail urls.
   hemisphere_image_urls = [
      {"title": "Valles Marineris Hemisphere", "lr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg",
        "hr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
       {"title": "Cerberus Hemisphere", "lr_img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg",
        "hr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
       {"title": "Schiaparelli Hemisphere", "lr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg",
        "hr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
       {"title": "Syrtis Major Hemisphere", "lr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg",
        "hr_img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
   ]

   mars_dict['mars_hemisphere_image_urls'] = hemisphere_image_urls

   return mars_dict



if __name__ == "__main__":
    # execute only if run as a script
    scrape()


