#import packages
from ast import Pass
import requests
import json

#url that links to the exchequer account (historical series) page on cso.ie
Url = "https://www.reddit.com/r/videogames/"

#function to acess the url and returns it as a json
def getAll():
    response = requests.get(Url)
    return response.json()

#function that creates a json file and puts in the data which is formated as a json
if __name__ == "__main__" :
    with open("cso.json", "wt") as fp: 
        print(json.dumps(getAll()), file = fp)