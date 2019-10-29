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

for x in range(30): #players
  teamid = x
  #print(year)
  for x in range(15):
    hgt = 0
    hgt = random.randint(0, 100)
    statToChange = 0
    statToChange = random.randint(0, 14)
    stre = 2
    spd = 2
    jmp = 2
    endu = 2
    ins = 2
    dnk = 2
    ft = 2
    fg = 2
    tp = 2
    oiq = 2
    diq = 2
    drb = 2
    pss = 2
    reb = 2
    if statToChange == 0:
        stre = 99
    elif statToChange == 1:
        spd = 99
    elif statToChange == 2:
        jmp = 99
    elif statToChange == 3:
        endu = 99 
    elif statToChange == 4:
        ins = 99
    elif statToChange == 5:
        dnk = 99
    elif statToChange == 6:
        ft = 99
    elif statToChange == 7:
        fg = 99  
    elif statToChange == 8:
        tp = 99
    elif statToChange == 9:
        oiq = 99
    elif statToChange == 10:
        diq = 99
    elif statToChange == 11:
        drb = 99
    elif statToChange == 12:
        pss = 99
    elif statToChange == 13:
        reb = 99
    elif statToChange == 14:
        reb = 99
    data['players'].append({
 #     "firstName": "Draft",
 #     "lastName": "Prospect",
      "tid": teamid,
      "ratings": [
          {
            "hgt": hgt,
            "stre": stre,
            "spd": spd,
            "jmp": jmp,
            "endu": endu,
            "ins": ins,
            "dnk": dnk,
            "ft": ft,
            "fg": fg,
            "tp": tp,
            "oiq": oiq,
            "diq": diq,
            "drb": drb,
            "pss": pss,
            "reb": reb
          }
        ],
  })

for x in range(50): #draft prospects
  year = 2018 + (x + 1)
  age = year - 19
  for x in range(71):
    hgt = 0
    hgt = random.randint(0, 100)
    statToChange = 0
    statToChange = random.randint(0, 14)
    stre = 2
    spd = 2
    jmp = 2
    endu = 2
    ins = 2
    dnk = 2
    ft = 2
    fg = 2
    tp = 2
    oiq = 2
    diq = 2
    drb = 2
    pss = 2
    reb = 2
    if statToChange == 0:
        stre = 99
    elif statToChange == 1:
        spd = 99
    elif statToChange == 2:
        jmp = 99
    elif statToChange == 3:
        endu = 99 
    elif statToChange == 4:
        ins = 99
    elif statToChange == 5:
        dnk = 99
    elif statToChange == 6:
        ft = 99
    elif statToChange == 7:
        fg = 99  
    elif statToChange == 8:
        tp = 99
    elif statToChange == 9:
        oiq = 99
    elif statToChange == 10:
        diq = 99
    elif statToChange == 11:
        drb = 99
    elif statToChange == 12:
        pss = 99
    elif statToChange == 13:
        reb = 99
    elif statToChange == 14:
        reb = 99
    data['players'].append({
 #     "firstName": "Draft",
 #     "lastName": "Prospect",
      "tid": -2,
      "ratings": [
          {
            "hgt": hgt,
            "stre": stre,
            "spd": spd,
            "jmp": jmp,
            "endu": endu,
            "ins": ins,
            "dnk": dnk,
            "ft": ft,
            "fg": fg,
            "tp": tp,
            "oiq": oiq,
            "diq": diq,
            "drb": drb,
            "pss": pss,
            "reb": reb
          }
      ],
      "born": {"year": age},
      "draft": {"year": year},
  })

else:
  print("Finally finished!")
with open('death_of_basketball.json', 'w') as outfile:
    json.dump(data, outfile)