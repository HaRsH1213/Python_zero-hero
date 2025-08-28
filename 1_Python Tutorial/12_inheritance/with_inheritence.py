import datetime
class Players:
    def __init__(self,fname, lname, birthyear):
        self.first_name = fname
        self.last_name = lname
        self.birthyear = birthyear

    def get_current_age_(self):
        current_year= datetime.datetime.now().year
        return current_year - self.birthyear

class Tennisplayer(Players):
    def __init__(self,fname, lname, birthyear):
        super().__init__(fname,lname,birthyear)
        self.ace=[]

    def avg_acc(self):
        return sum(self.ace)/len(self.ace)

    def add_ace(self,ace):
        return self.ace.append(ace)

class CricketPlayer(Players):
    def __init__(self,fname, lname, birthyear):
        super().__init__(fname,lname,birthyear)
        self.score=[]

    def avv_score(self):
        return sum(self.score)/len(self.score)

    def add_score(self,score):
        return self.score.append(score)




virat = CricketPlayer('virat', 'kohli', 1988)
virat.add_score(37)
virat.add_score(23)
virat.add_score(85)

print("Age of viral kohli:", virat.get_current_age_())
print("Average score of viral kohli:", virat.avv_score())

roger = Tennisplayer('roger','federer',1981)
roger.add_ace(5)
roger.add_ace(7)

print("Age of roger federer:",roger.get_current_age_())
print("His average ace per match:  ",roger.avg_acc())



