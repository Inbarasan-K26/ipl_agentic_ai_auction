import random

players = [

**Batsman**
{"name":"Virat Kohli","role":"Batsman","runs":7263,"wickets":4,"rating":95,"price":2.0},
{"name":"Rohit Sharma","role":"Batsman","runs":6211,"wickets":15,"rating":92,"price":2.0},
{"name":"Shubman Gill","role":"Batsman","runs":2790,"wickets":0,"rating":90,"price":1.8},
{"name":"KL Rahul","role":"Batsman","runs":4163,"wickets":0,"rating":89,"price":1.9},
{"name":"Faf du Plessis","role":"Batsman","runs":4200,"wickets":0,"rating":90,"price":1.8},
{"name":"David Warner","role":"Batsman","runs":6397,"wickets":0,"rating":92,"price":2.0},
{"name":"Shreyas Iyer","role":"Batsman","runs":3000,"wickets":0,"rating":88,"price":1.7},
{"name":"Ruturaj Gaikwad","role":"Batsman","runs":2500,"wickets":0,"rating":88,"price":1.7},
{"name":"Devdutt Padikkal","role":"Batsman","runs":1800,"wickets":0,"rating":84,"price":1.5},
{"name":"Yashasvi Jaiswal","role":"Batsman","runs":1600,"wickets":0,"rating":86,"price":1.6},

** Wicket Keepers
{"name":"MS Dhoni","role":"Wicket-Keeper","runs":5082,"wickets":0,"rating":90,"price":1.8},
{"name":"Jos Buttler","role":"Wicket-Keeper","runs":3223,"wickets":0,"rating":91,"price":2.0},
{"name":"Sanju Samson","role":"Wicket-Keeper","runs":3800,"wickets":0,"rating":88,"price":1.8},
{"name":"Rishabh Pant","role":"Wicket-Keeper","runs":2900,"wickets":0,"rating":90,"price":1.9},
{"name":"Ishan Kishan","role":"Wicket-Keeper","runs":2400,"wickets":0,"rating":87,"price":1.7},

**All Rounders
{"name":"Hardik Pandya","role":"All-Rounder","runs":2309,"wickets":53,"rating":91,"price":2.1},
{"name":"Ravindra Jadeja","role":"All-Rounder","runs":2692,"wickets":152,"rating":93,"price":2.0},
{"name":"Andre Russell","role":"All-Rounder","runs":2300,"wickets":96,"rating":92,"price":2.0},
{"name":"Glenn Maxwell","role":"All-Rounder","runs":2800,"wickets":35,"rating":90,"price":1.9},
{"name":"Ben Stokes","role":"All-Rounder","runs":2900,"wickets":28,"rating":90,"price":2.0},

**Bowlers
{"name":"Jasprit Bumrah","role":"Bowler","runs":50,"wickets":145,"rating":94,"price":2.2},
{"name":"Mohammed Shami","role":"Bowler","runs":200,"wickets":127,"rating":90,"price":1.9},
{"name":"Rashid Khan","role":"Bowler","runs":350,"wickets":149,"rating":94,"price":2.2},
{"name":"Yuzvendra Chahal","role":"Bowler","runs":100,"wickets":187,"rating":91,"price":2.0},
{"name":"Bhuvneshwar Kumar","role":"Bowler","runs":300,"wickets":170,"rating":90,"price":1.9},

]

* Generate extra players to reach 200
roles = ["Batsman","Bowler","All-Rounder","Wicket-Keeper"]

for i in range(len(players)+1,201):

    players.append({
        "name":f"Domestic_Player_{i}",
        "role":random.choice(roles),
        "runs":random.randint(0,4000),
        "wickets":random.randint(0,150),
        "rating":random.randint(65,88),
        "price":round(random.uniform(0.5,2.0),2)
    })
