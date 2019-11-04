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

def createPlayers(number, type, pos, draft, teams):
  print("Hello from a function")
  for x in range(teams): #players
    if draft == -2:
      teamid = -2
    else:
      teamid = x
    #print(year)
    for x in range(number):
      hgt = 0
      hgt = random.randint(20, 75)
      stre = 15
      spd = 15
      endu = 15
      thv = 15
      thp = 15
      tha = 15
      bsc = 15
      elu = 15
      rtr = 15
      hnd = 15
      bk = 15
      pbk = 15
      pcv = 15
      tck = 15
      prs = 15
      rns = 15
      kpw = 15
      kac = 15
      ppw = 15
      pac = 15
      playerType = type
      statToChange = 0
      statToChange = random.randint(0, 3)
      if statToChange == 0:
          stre = 99
      elif statToChange == 1:
          spd = 99
      elif statToChange == 2:
          endu = 99 
      elif statToChange == 3:
          spd = 99 
      if playerType == 0:
        focusStat = 0
        focusStat = random.randint(0, 1)
        if focusStat == 0:
          bk = 99
          stre = 75
        elif focusStat == 1:
          pbk = 99
          stre = 75
      elif playerType == 1:
        focusStat = 0
        focusStat = random.randint(0, 2)
        if focusStat == 0:
          thv = 99
        elif focusStat == 1:
          thp = 99
        elif focusStat == 2:
          tha = 99
      elif playerType == 2:
        focusStat = 0
        focusStat = random.randint(0, 2)
        if focusStat == 0:
          tck = 99
        elif focusStat == 1:
          prs = 99
        elif focusStat == 2:
          rns = 99
      elif playerType == 2.25:
        focusStat = 0
        focusStat = random.randint(0, 3)
        if focusStat == 0:
          tck = 99
        elif focusStat == 1:
          prs = 99
        elif focusStat == 2:
          rns = 99
        elif focusStat == 3:
          pac = 99    
      elif playerType == 2.5:
        focusStat = 0
        focusStat = random.randint(0, 3)
        if focusStat == 0:
          tck = 99
          pac = 50  
        elif focusStat == 1:
          prs = 99
          pac = 50 
        elif focusStat == 2:
          rns = 99
          pac = 50  
        elif focusStat == 2:
          pac = 99   
          tck = 20 
      elif playerType == 3:
        focusStat = 0
        focusStat = random.randint(0, 2)
        if focusStat == 0:
          bsc = 99
          stre = 25
          elu = 25
          hnd = 25
        elif focusStat == 1:
          elu = 99
          stre = 25
          hnd = 25
          bsc = 25
        elif focusStat == 2:
          hnd = 99
          elu = 25
          stre = 25
          hnd = 25
        elif focusStat == 3 and stre < 99:
          stre = 30
      elif playerType == 3.5:
        focusStat = 0
        focusStat = random.randint(0, 3)
        if focusStat == 0:
          bsc = 99
          rtr = 25
        elif focusStat == 1:
          elu = 99
          rtr = 25
        elif focusStat == 2:
          rtr = 99
        elif focusStat == 3:
          hnd = 99
          rtr = 25    
      elif playerType == 4:
        focusStat = 0
        focusStat = random.randint(0, 1)
        if focusStat == 0:
          kpw = 99
          ppw = 99
        elif focusStat == 1:
          kac = 99
          pac = 99
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
              "bk": bk, 
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
createPlayers(2, 3, "TE", 0, 32)
createPlayers(8, 2, "DL", 0, 32)
createPlayers(6, 2.25, "LB", 0, 32)
createPlayers(5, 2.5, "CB", 0, 32)
createPlayers(4, 2.5, "S", 0, 32)
createPlayers(1, 4, "K", 0, 32)
createPlayers(1, 4, "P", 0, 32)

def createDraftPlayers(number, type, pos, draft, teams):
  print("Hello from a function")
  for x in range(50): #players
    teamid = -2
    year = 2018 + (x + 1)
    age = year - 19
    #print(year)
    for x in range(number):
      hgt = 0
      hgt = random.randint(20, 75)
      stre = 15
      spd = 15
      endu = 15
      thv = 15
      thp = 15
      tha = 15
      bsc = 15
      elu = 15
      rtr = 15
      hnd = 15
      bk = 15
      pbk = 15
      pcv = 15
      tck = 15
      prs = 15
      rns = 15
      kpw = 15
      kac = 15
      ppw = 15
      pac = 15
      playerType = type
      statToChange = 0
      statToChange = random.randint(0, 3)
      if statToChange == 0:
          stre = 99
      elif statToChange == 1:
          spd = 99
      elif statToChange == 2:
          endu = 99 
      elif statToChange == 3:
          spd = 99 
      if playerType == 0:
        focusStat = 0
        focusStat = random.randint(0, 1)
        if focusStat == 0:
          bk = 99
          stre = 75
        elif focusStat == 1:
          pbk = 99
          stre = 75
      elif playerType == 1:
        focusStat = 0
        focusStat = random.randint(0, 2)
        if focusStat == 0:
          thv = 99
        elif focusStat == 1:
          thp = 99
        elif focusStat == 2:
          tha = 99
      elif playerType == 2:
        focusStat = 0
        focusStat = random.randint(0, 2)
        if focusStat == 0:
          tck = 99
        elif focusStat == 1:
          prs = 99
        elif focusStat == 2:
          rns = 99
      elif playerType == 2.25:
        focusStat = 0
        focusStat = random.randint(0, 3)
        if focusStat == 0:
          tck = 99
        elif focusStat == 1:
          prs = 99
        elif focusStat == 2:
          rns = 99
        elif focusStat == 3:
          pac = 99    
      elif playerType == 2.5:
        focusStat = 0
        focusStat = random.randint(0, 3)
        if focusStat == 0:
          tck = 99
          pac = 50  
        elif focusStat == 1:
          prs = 99
          pac = 50 
        elif focusStat == 2:
          rns = 99
          pac = 50  
        elif focusStat == 2:
          pac = 99   
          tck = 20 
      elif playerType == 3:
        focusStat = 0
        focusStat = random.randint(0, 2)
        if focusStat == 0:
          bsc = 99
          stre = 25
          elu = 25
          hnd = 25
        elif focusStat == 1:
          elu = 99
          stre = 25
          hnd = 25
          bsc = 25
        elif focusStat == 2:
          hnd = 99
          elu = 25
          stre = 25
          hnd = 25
          bsc = 25
      elif playerType == 3.5:
        focusStat = 0
        focusStat = random.randint(0, 3)
        if focusStat == 0:
          bsc = 99
          rtr = 25
        elif focusStat == 1:
          elu = 99
          rtr = 25
        elif focusStat == 2:
          rtr = 99
        elif focusStat == 3:
          hnd = 99
          rtr = 25    
      elif playerType == 4:
        focusStat = 0
        focusStat = random.randint(0, 1)
        if focusStat == 0:
          kpw = 99
          ppw = 99
        elif focusStat == 1:
          kac = 99
          pac = 99
      data['players'].append({
        "tid": teamid,
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
              "bk": bk, 
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

createDraftPlayers(random.randint(10, 35), 0, "OL", 0, 32)
createDraftPlayers(random.randint(10, 35), 1, "QB", 0, 32)
createDraftPlayers(random.randint(10, 35), 3, "RB", 0, 32)
createDraftPlayers(random.randint(10, 35), 3.5, "WR", 0, 32)
createDraftPlayers(random.randint(10, 35), 3, "TE", 0, 32)
createDraftPlayers(random.randint(10, 35), 2, "DL", 0, 32)
createDraftPlayers(random.randint(10, 35), 2.25, "LB", 0, 32)
createDraftPlayers(random.randint(10, 35), 2.5, "CB", 0, 32)
createDraftPlayers(random.randint(10, 35), 2.5, "S", 0, 32)
createDraftPlayers(random.randint(5, 10), 4, "K", 0, 32)
createDraftPlayers(random.randint(5, 10), 4, "P", 0, 32)


with open('death_of_football.json', 'w') as outfile:
    json.dump(data, outfile)
