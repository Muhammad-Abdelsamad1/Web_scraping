#Importing packages for the project
import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.wisdompetmed.com/")
#sanity check
response.url

#check server connection
response.status_code

#retrieve headers
response.headers

#retrieve content
response.content

soup = BeautifulSoup(response.text)
#use beutifulsoup to prettify 
print(soup.prettify())

#use find() to get first intance of vegetranine
soup.find("title")
#use find_all() instances of articles 
soup.find_all("article")

#find business phone number
print(soup.find("span", class_= "phone").text)

#find all featured testmonials
featured_testmonial = soup.find_all("div", class_= "quote")
for t in featured_testmonial:
    print(t.text)

#find all staff members
staff = soup.find_all("div", class_= "info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")
for s in staff:
    print(s.text)

  #finding all links

links = soup.find_all("a")
for a in links:
    print(a.text, a.get("href") )

#writing scrapping to text files
with open("wisdomweb.txt","w",encoding="utf-8") as f:
    f.write(soup.prettify())