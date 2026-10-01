import json

#agents = {"name":"Banana","country": "Belgium",
#          "level": 9,"skills": "being yellow"}
#print(agents)
#print(agents["name"])
#print(agents["skills"])
#agents["diet"] = "vegitarian"

#print(agents["diet"])
agents = [
     {"name":"Banana","country": "Belgium",
          "level": 9,"skills": "being yellow"},
     {
         "name": "Shadow",
         "country": "Netherlands",
         "level": 4,
         "skills": ["hacking", "disguise"]
     },

     {
         "name": "Falcon",
         "country": "Japan",
         "level": 5,
         "skills": ["driving", "surveillance"]
     },

     {
         "name": "Ghost",
         "country": "Brazil",
         "level": 3,
         "skills": ["languages", "infiltration"]
     } ]
def search():
    a = input('what name do you search? — ')
    for agent in agents:
        if agent['name']==a:
            print(agent)



def open():
    with open("agent.json", "r") as file:
        agent = json.load(file)
    return agent
    
def close():
    with open("Agents.json", "w") as file:
        json.dump(agents, file, indent=4)
while True:
    choise = int(input())
    if choise == 1:
        search()

#agent_list = open()

