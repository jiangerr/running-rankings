from unicodedata import name


class Race:
    # id = 0
    # date, name, section, tfrrs_url, location, sex = ''

    def __init__(self, raceJSON):
        self.id = int(raceJSON['id'])
        self.date = raceJSON['date']
        self.name = raceJSON['meet_name']
        self.section = raceJSON['section']
        self.tfrrs_url = raceJSON['tfrrs_url']
        self.location = raceJSON['location']
        self.sex = raceJSON['sex']

    def __str__(self):
        tostring = "Name: " + self.name + "\n"
        tostring = tostring + "Date: " + self.date + "\n"
        tostring = tostring + "Location: " + self.location + "\n"
        tostring = tostring + "ID: " + str(self.id) + "\n"
        tostring = tostring + "Section: " + self.section + "\n"
        tostring = tostring + "tfrrs url: " + self.tfrrs_url + "\n"
        tostring = tostring + "Sex: " + self.sex + "\n"
        return tostring
