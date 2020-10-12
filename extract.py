#beginning of code
#idea is to analyse Vitamin D whole milk 1 gallon prices across different stores
#Price of Walmart Greatvalue, Kroger, Target Good and Gather, 
#Price of brand Dairypure at Walmart, Dollargeneral and Vons to check for differences
import urllib.request
import re
import time
from datetime import datetime
from selenium import webdriver
e_path = r"C:\Users\aishr\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe"
browser = webdriver.Firefox(executable_path=e_path)

print ("Prices of 1 Gallon Vitamin D Milk across stores in West Lafayette")
# Python 3 version
print ("Prices on",str(datetime.now()))

# product "Walmart Great Value Whole Milk, 1 Gallon,"
htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Great-Value-Whole-Milk-1-Gallon-128-Fl-Oz/10450114")
htmltext = htmlfile.read()
regex1 = re.findall(r'<span class="hide-content display-inline-block-m"><span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
print ("Walmart's Great Value,:",regex1)
review1 = re.findall(r'<span class="seo-avg-rating" itemprop="ratingValue">(.*?)</span>',str(htmltext))
print ("Walmart's Greatvalue",review1)

# product "Kroger Whole Milk, 1 Gallon,"
browser.get('https://www.pay-less.com/p/kroger-vitamin-d-whole-milk/0001111040101')
regex2 = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div[3]/label[1]/div/div/div[2]/data/span')
print("Kroger Whole Milk" ,regex2.text)

# product "Target Whole Milk, 1 Gallon,"
browser.get('https://www.target.com/p/vitamin-d-whole-milk-1gal-good-38-gather-8482/-/A-13276134')
regex3 = browser.find_element_by_xpath('//*[@id="viewport"]/div[4]/div/div[2]/div[2]/div[1]/div[1]/div[1]')
print("Target Whole Milk" ,regex3.text)
review3 = browser.find_element_by_xpath('//*[@id="viewport"]/div[4]/div/div[2]/div[2]/div[1]/div[2]/div/a[1]/span[1]/span')
print ("Targets Good and Gathe reviewr",review3.text)

# product "Dairypure Whole Milk at Walmart, 1 Gallon,"
htmlfile = urllib.request.urlopen("https://www.walmart.com/ip/Garelick-Farms-Dairy-Pure-Vitamin-D-Whole-Milk-1-Gallon-128-Fl-Oz/46491786")
htmltext = htmlfile.read()
regex5 = re.findall(r'<span class="price display-inline-block arrange-fit price price--stylized"><span class="visuallyhidden">(.*?)</span>',str(htmltext))
print ("Walmart's Dairypure,:",regex5)
review5 = re.findall(r'<span class="seo-avg-rating" itemprop="ratingValue">(.*?)</span>out of<span class="seo-best-rating" itemprop="bestRating">5</span>',str(htmltext))
print ("Walmart's Dairypure",review5)

# product "Dairypure Whole Milk at Dollargeneral, 1 Gallon,"
browser.get('https://www.dollargeneral.com/dairypure-vitamin-d-whole-milk-1-gallon.html')
regex6 = browser.find_element_by_xpath('//*[@id="product-price-85372"]/span')
print("Dairypure at Dollargeneral" ,regex6.text)
#end of code
