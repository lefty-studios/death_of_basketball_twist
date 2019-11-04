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
    hgt = random.randint(20, 75)
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
    bk = 2
    pbk = 2
    pcv = 2
    tck = 2
    prs = 2
    rns = 2
    kpw = 2
    kac = 2
    ppw = 2
    pac = 2
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
	if playerType == 0: #lineman
        focusStat = 0
		focusStat = random.randint(0, 1)
		if focusStat == 0:
			bk = 99
		elif focusStat == 1:
			pbk = 99
	elif playerType == 1: #quarterback
		focusStat = 0
		focusStat = random.randint(0, 2)
		if focusStat == 0:
			thv = 99
		elif focusStat == 1:
			thp = 99
		elif focusStat == 2:
			tha = 99
	elif playerType == 2: #defensive player
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
	elif playerType == 3: #Rushing / Receiving
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
	elif playerType == 4: #kicker
    
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