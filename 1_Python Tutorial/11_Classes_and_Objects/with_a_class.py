import datetime
class CricketPlayer:
    def __init__(self,first_name, lname, birthdate, team ):
        self.first_name = first_name
        self.last_name = lname
        self.birth_year = birthdate
        self.team= team
        self.scores = []


    def add_score(self,score):
        return self.scores.append(score)

    def avg_score(self):
        return sum(self.scores)/len(self.scores)
    def get_current_age(self):
        current_Year = datetime.datetime.now().year
        return current_Year - self.birth_year
    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player from {self.team}"

    def __lt__(self, other):
        self_avg_score = self.avg_score()
        other_avg_score = other.avg_score()
        return self_avg_score < other_avg_score
    def __eq__(self, other):
        self_age = self.get_current_age()
        other_age = other.get_current_age()
        return self_age==other_age


virat =CricketPlayer('Virat','Kohli',1988,'India')
virat.add_score(100)
virat.add_score(67)
virat.add_score(45)
virat.add_score(34)
print(virat)
print(f"Name: {virat.first_name} {virat.last_name}")
print(f"Virat age: {virat.get_current_age()}")
print(f"His avg score in the last {len(virat.scores)} matches: {virat.avg_score()}")
print(f"He playing for the team: {virat.team}")



Babar =CricketPlayer('Babar','Mulla',1923,'Bikharistan')
Babar.add_score(10)
Babar.add_score(0)
Babar.add_score(0)
Babar.add_score(5)
print(Babar)
print(f"Name: {Babar.first_name} {Babar.last_name}")
print(f"His age: {Babar.get_current_age()}")
print(f"His avg score in the last {len(Babar.scores)} matches: {Babar.avg_score()}")
print(f"He playing for the team: {Babar.team}")



print(Babar<virat)
print(Babar==virat)