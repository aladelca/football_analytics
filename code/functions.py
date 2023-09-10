import pandas as pd
import numpy as np
import requests
from variables import *


### Alianza Lima
###leagueId = 281
###teamId = 2553

url = "https://api-football-v1.p.rapidapi.com/v3/teams"

querystring = {"league":"281","season":"2023"}

headers = {
	"X-RapidAPI-Key": apiKey,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


def getTeamId(teamName, response):
    '''
    teamName (string) = Name of the team
    response (json) = Request file
    '''
    teamList = response.json()['response']
    for i in range(len(teamList)):
        if teamList[i]['team']['name'] == teamName:
            return teamList[i]['team']['id']

id = getTeamId('Alianza Lima', response)

#{"league":"281","season":"2023","team":"2553"})
def getTeamStats(url,headers, teamId, season, leagueId):

    querystring = {"league":leagueId,"season":season,"team":teamId}

    print(querystring)

    response = requests.get(url, headers=headers, params=querystring)

    playedMatches = pd.DataFrame(response.json()['response']['fixtures'])

    keys = ['for','against']

    dfGoals = pd.DataFrame()
    for i in keys:
        dfGoals[i] = list(response.json()['response']['goals'][i]['total'].values())

    dfGoals.index = list(response.json()['response']['goals'][i]['total'].keys())
    return playedMatches, dfGoals

print(getTeamStats("https://api-football-v1.p.rapidapi.com/v3/teams/statistics", headers, 2553,2023,281))