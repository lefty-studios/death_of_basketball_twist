import json
import random
year = 2019
age = 0
data = {
  "version": 33,
  "startingSeason": 2019,
}
data['players'] = []
players = []

def createPlayers(number, type, pos, id, teams):
  print("Hello from a function")
  for x in range(teams): #players
    if id == 0:
      teamid = x
    else:
      teamid = id  
    #print(year)
    for x in range(number):
      hgt = 0
      hgt = random.randint(10, 50)
      stre = 2
      spd = 2
      endu = 2
      thv = 2
      thp = 2
      tha = 2
      bsc = 2
      elu = 2
      rtr = 2
      hnd = 2
      rbk = 2
      pbk = 2
      pcv = 2
      tck = 2
      prs = 2
      rns = 2
      kpw = 2
      kac = 2
      ppw = 2
      pac = 2
      data['players'].append({
        "tid": teamid,
        "pos": pos,
        "ratings": [
            {
              "hgt": hgt,
              "stre": stre,
              "spd": spd,
              "endu": endu,
              "stre": stre,
              "spd": spd,
              "endu": endu,
              "thv": thv,
              "thp": thp,
              "tha": tha,
              "bsc": bsc,
              "elu": elu,
              "rtr": rtr,
              "hnd": hnd,
              "rbk": rbk, 
              "pbk": pbk,
              "pcv": pcv,
              "tck": tck,
              "prs": prs,
              "rns": rns,
              "kpw": kpw,
              "kac": kac,
              "ppw": ppw,
              "pac": pac
            }
          ],
    })

createPlayers(8, 0, "OL", 0, 32)
createPlayers(3, 1, "QB", 0, 32)
createPlayers(4, 3, "RB", 0, 32)
createPlayers(6, 3.5, "WR", 0, 32)
createPlayers(2, 3.5, "TE", 0, 32)
createPlayers(8, 2, "DL", 0, 32)
createPlayers(6, 2.25, "LB", 0, 32)
createPlayers(5, 2.5, "CB", 0, 32)
createPlayers(4, 2.5, "S", 0, 32)
createPlayers(1, 4, "K", 0, 32)
createPlayers(1, 4, "P", 0, 32)

createPlayers(8, 0, "OL", -1, 2)
createPlayers(3, 1, "QB", -1, 2)
createPlayers(4, 3, "RB", -1, 2)
createPlayers(6, 3.5, "WR", -1, 2)
createPlayers(2, 3.5, "TE", -1, 2)
createPlayers(8, 2, "DL", -1, 2)
createPlayers(6, 2.25, "LB", -1, 2)
createPlayers(5, 2.5, "CB", -1, 2)
createPlayers(4, 2.5, "S", -1, 2)
createPlayers(1, 4, "K", -1, 2)
createPlayers(1, 4, "P", -1, 2)




def createDraftPlayers(number, type, pos, draft, teams):
  print("Hello from a function")
  for x in range(50): #players
    teamid = -2
    year = 2018 + (x + 1)
    age = year - 19
    #print(year)
    for x in range(number):
      hgt = 0
      hgt = random.randint(10, 50)
      stre = 2
      spd = 2
      endu = 2
      thv = 2
      thp = 2
      tha = 2
      bsc = 2
      elu = 2
      rtr = 2
      hnd = 2
      rbk = 2
      pbk = 2
      pcv = 2
      tck = 2
      prs = 2
      rns = 2
      kpw = 2
      kac = 2
      ppw = 2
      pac = 2
      data['players'].append({
        "tid": -2,
        "pos": pos,
        "born": {"year": age},
        "draft": {"year": year},
        "ratings": [
            {
              "hgt": hgt,
              "stre": stre,
              "spd": spd,
              "endu": endu,
              "stre": stre,
              "spd": spd,
              "endu": endu,
              "thv": thv,
              "thp": thp,
              "tha": tha,
              "bsc": bsc,
              "elu": elu,
              "rtr": rtr,
              "hnd": hnd,
              "rbk": rbk, 
              "pbk": pbk,
              "pcv": pcv,
              "tck": tck,
              "prs": prs,
              "rns": rns,
              "kpw": kpw,
              "kac": kac,
              "ppw": ppw,
              "pac": pac
            }
          ],
    })

createDraftPlayers(random.randint(33, 35), 0, "OL", 0, 32)
createDraftPlayers(random.randint(33, 35), 1, "QB", 0, 32)
createDraftPlayers(random.randint(33, 35), 3, "RB", 0, 32)
createDraftPlayers(random.randint(33, 35), 3.5, "WR", 0, 32)
createDraftPlayers(random.randint(33, 35), 3.5, "TE", 0, 32)
createDraftPlayers(random.randint(33, 35), 2, "DL", 0, 32)
createDraftPlayers(random.randint(33, 35), 2.25, "LB", 0, 32)
createDraftPlayers(random.randint(33, 35), 2.5, "CB", 0, 32)
createDraftPlayers(random.randint(33, 35), 2.5, "S", 0, 32)
createDraftPlayers(random.randint(10, 10), 4, "K", 0, 32)
createDraftPlayers(random.randint(10, 10), 4, "P", 0, 32)


with open('fumble_dimension.json', 'w') as outfile:
    json.dump(data, outfile)