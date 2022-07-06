from unicodedata import name


class Race:
    id = 0
    date, name, section, tfrrs_url, location, sex = ''

    def __init__(self, raceJSON):
        self.date = raceJSON.date
        self.name = raceJSON.name
        self.section = raceJSON.section
        self.tfrrs_url = raceJSON.tfrrs_url
        self.location = raceJSON.location
        self.sex = raceJSON.sex
