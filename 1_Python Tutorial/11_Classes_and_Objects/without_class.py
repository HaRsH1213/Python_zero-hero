import datetime
virat = {
    'first_name': 'virat',
    'last_name': 'kohli',
    'scores': [],
    'birth_year': 1988
}

virat['scores'].append(55)
virat['scores'].append(100)
virat['scores'].append(30)
virat['scores'].append(43)



Babar = {
    'first_name': 'Babar',
    'last_name': 'mula',
    'scores': [],
    'birth_year': 1938
}

Babar['scores'].append(0)
Babar['scores'].append(5)
Babar['scores'].append(10)
Babar['scores'].append(0)

def get_avg_scores(first_name):
    return sum(first_name['scores'])/len(first_name['scores'])


def get_currnet_age(first_name):
    current_date= datetime.datetime.now().year
    return current_date - first_name['birth_year']

print(f"Virat kohli avg score: {get_avg_scores(virat)}")
print(f"Virat kohli age is {get_currnet_age(virat)}")


print(f"Babar Mulla avg score: {get_avg_scores(Babar)}")
print(f"Babar Mulla age is {get_currnet_age(Babar)}")