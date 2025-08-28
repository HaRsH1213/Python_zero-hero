import datetime
class Tennisplayer:
    def __init__(self,fname, lname, birthdate):
        self.first_name = fname
        self.last_name = lname
        self.birthdate = birthdate
        self.ace = []

    def get_age(self):
        current_year= datetime.datetime.now().year
        return current_year - self.birthdate
    def get_avg_aces_per_match(self):
        return sum(self.ace)/len(self.ace)

    def add_ace(self,ace):
        return self.ace.append(ace)


class Cricketplayer:
    def __init__(self, fname, lname, birthdate):
        self.first_name = fname
        self.last_name = lname
        self.birthdate = birthdate
        self.score = []

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birthdate

    def get_average_score(self):
        return sum(self.score) / len(self.score)

    def add_score(self, score):
        return self.score.append(score)


virat = Cricketplayer('virat', 'kohli', 1988)
virat.add_score(37)
virat.add_score(23)
virat.add_score(85)

print("Age of viral kohli:", virat.get_age())
print("Average score of viral kohli:", virat.get_average_score())

roger = Tennisplayer('roger','federer',1981)
roger.add_ace(5)
roger.add_ace(7)

print("Age of roger federer:",roger.get_age())
print("His average ace per match:  ",roger.get_avg_aces_per_match())
