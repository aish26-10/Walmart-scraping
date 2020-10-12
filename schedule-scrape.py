#beginning of code
import urllib.request
import re
import schedule
import time
import smtplib
from datetime import datetime

def job():
    
    htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Great-Value-Whole-Milk-1-Gallon-128-Fl-Oz/10450114")
    htmltext = htmlfile.read()
    regex1 = re.findall(r'<span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
    print ("Walmart's Great Value,:",regex1)
    review1 = re.findall(r'<span class="seo-avg-rating" itemprop="ratingValue">(.*?)</span>',str(htmltext))
    print ("Walmart's Greatvalue",review1)
    
schedule.every(1).day.at("10:29").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

# To clear all functions, in console type
# schedule.clear()
#end of code
