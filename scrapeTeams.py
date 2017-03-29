import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://espn.go.com/nba/teams'
r = requests.get(url)
#html = r.content

soup = BeautifulSoup(r.text, 'lxml')
tables = soup.find_all('ul', class_='medium-logos')

outfile = open("./teams.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Team", "Prefix_1", "Prefix_2", "URL"])

teams = []
prefix_1 = []
prefix_2 = []
teams_urls = []
for table in tables:
    #print("Found following table: " + table.text)
    lis = table.find_all('li')
    for li in lis:
        #print("Found the following li from the table: " + li.h5.a.text)
        info = li.h5.a

        #info.text.replace('&nbsp;', '')
        #print("li after replacing &nbsp;: " + info.text)

        #infoText = ' '.join(info.text.split()) + '\n'
        #print("infoTText after ' '.join: " + infoText)

        teams.append(info.text)

        url = info['href']
        #print("Found the following url from the table: " + url)
        teams_urls.append(url)

        prefix_1_string = url.split('/')[-2]
        prefix_1_string = prefix_1_string.upper()
        prefix_1.append(prefix_1_string)
        #print("Prefix_1 split url '/' -2: " + url.split('/')[-2])

        prefix_2_string = url.split('/')[-1]
        prefix_2_string = prefix_2_string.upper()
        prefix_2.append(prefix_2_string)
        #print("Prefix_2 split url '/' -1: " + url.split('/')[-1])
        writer.writerow([info.text, prefix_1_string, prefix_2_string, url])

#writer.writerows(teams)

dic = {'url': teams_urls, 'prefix_2': prefix_2, 'prefix_1': prefix_1}
teams = pd.DataFrame(dic, index=teams)
teams.index.name = 'team'
print(teams)
