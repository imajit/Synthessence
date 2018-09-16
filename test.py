import requests
from bs4 import BeautifulSoup
import re
#import urllib.request

#Used headers/agent as the request timed out and asking for agent. Using following code you can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.zomato.com/ncr/top-restaurants",headers=headers)
content = response.content
print(content)
soup = BeautifulSoup(content,"html.parser")
#soup
top_rest = soup.find_all("div",attrs={"class": "bb0 collections-grid col-l-16"})
#print(top_rest)

list_tr = top_rest[0].find_all("div",attrs={"class": "col-s-8 col-l-1by3"})
list_rest =[]
for tr in list_tr:
    dataframe ={}
    dataframe["RestaurantName"] = (tr.find("div",attrs={"class": "res_title zblack bold nowrap"})).text.replace('\n', ' ')
    dataframe["RestaurantAddress"] = (tr.find("div",attrs={"class": "nowrap grey-text fontsize5 ttupper"})).text.replace('\n', ' ')
    dataframe["CuisineType"] = (tr.find("div",attrs={"class":"nowrap grey-text"})).text.replace('\n', ' ')
    list_rest.append(dataframe)
list_rest
import pandas
df = pandas.DataFrame(list_rest)
df.to_csv("zomato_res.csv",index=False)

