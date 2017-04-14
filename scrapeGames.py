import csv
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

year = 2017
teams = pd.read_csv('teams.csv')
BASE_URL = 'http://espn.go.com/nba/team/schedule/_/name/{0}/year/{1}/{2}'

match_id = []
dates = []
home_team = []
home_team_score = []
visit_team = []
visit_team_score = []

for index, row in teams.iterrows():
    _team, url = row['Team'], row['URL']
    #print _team;
    r = requests.get(BASE_URL.format(row['Prefix_1'], year, row['Prefix_2']))
    table = BeautifulSoup(r.text, "lxml").table
    #print table;
    for row in table.find_all('tr')[1:]: #Remove header
        columns = row.find_all('td')
        #print columns;
        try:
            _home = True if columns[1].li.text == 'vs' else False
            print _home
            #_other_team = columns[1].find_all('a')[1].text
            #print _other_team
            #_score = columns[2].a.text.split(' ')[0].split('-')
            #print _score
            #_won = True if columns[2].span.text == 'W' else False
            #print won
        except Exception as e:
            pass # Not all columns row are a match, it's OK
            # print(e)
