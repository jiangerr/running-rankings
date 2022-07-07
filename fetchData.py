import numpy as np
import requests
import util.constants
from Race import Race
from tqdm import tqdm
import pickle


def fetch_data():

    brief_race_list = (requests.get(util.constants.BRIEF_RACE_LIST)).json()
    max_id = int(brief_race_list['results'][0]['id']) + 1

    races = []
    race_results = []

    for i in tqdm(range(1, max_id)):
        response = requests.get(util.constants.RACE_INSTANCE + str(i))
        response_JSON = response.json()
        if response.status_code == '200':
            race = Race(response_JSON)
            races.append(race)
            JSON_results = response_JSON['xc_results']
            results = createResults(JSON_results)
            race_results.append(results)

    results_dict = dict(zip(races, race_results))

    with open('data/data.pickle', 'wb') as handle:
        pickle.dump(results_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def createResults(JSON_results):
    numRacers = len(JSON_results)
    results = np.zeros((numRacers, 2))
    for i in range(numRacers):
        results[i, 0] = JSON_results[i]["runner"]["firstname"] + " " + JSON_results[i]["runner"]["lastname"]
        results[i, 1] = JSON_results[i]["time"]
    return results