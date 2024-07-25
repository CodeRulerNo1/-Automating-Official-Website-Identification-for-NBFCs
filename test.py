from bs4 import BeautifulSoup 
import requests 
import re 
import pandas as pd

def getHTMLdocument(url): 
	response = requests.get(url) 
	return response.text 

def search(query):	
    url_to_scrape = f"https://www.bing.com/search?q={query}"
    html_document = getHTMLdocument(url_to_scrape)        
    soup = BeautifulSoup(html_document, 'html.parser')                                                    
    for link in soup.find_all('a',attrs={'href': re.compile("^https://")}): 
        
        url=(link.get('href'))
        if  "stock" in url or"company" in url or "wikipedia" in url or url =="https://go.microsoft.com/fwlink/?linkid=868922" or url=="https://support.microsoft.com/topic/82d20721-2d6f-4012-a13d-d1910ccf203f" or any(url.startswith(prefix) for prefix in ["https://www.bingplaces","https://www.moneycontrol.""https://www.indiaratings","https://www.indiaratings","https://cleartax","https://opencorporates","https://www.instafinancials","https://www.indiafilings","https://ercsl.edelweissfin","https://www.quickcompany.in","https://economictimes.indiatimes","https://www.bloomberg","https://www.thecompanycheck.com","https://www.youtube","https://m.youtube","https://www.falconebiz","https://en.wikipedia","https://mycorporateinfo","https://www.99corporates","https://support.microsoft", "https://go.microsoft", "https://www.zaubacorp", "https://in.linkedin", "https://www.icra", "https://trendlyne", "https://www.crisil", "https://www.tofler"]) or url.endswith(".pdf"):
            continue
        return url
