import requests

# Log into AoC, open devtools, go to the "Application" tab, and click on "cookies" on the left panel. Copy the session token from the AoC cookie.
SESSION_TOKEN = ""

def data(day):
	return requests.get("https://adventofcode.com/2020/day/{}/input".format(day), cookies={ 'session': SESSION_TOKEN })
