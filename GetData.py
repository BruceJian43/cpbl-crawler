import requests
import heapq as hp
from bs4 import BeautifulSoup
global team_p
global team_b
global l1
global l2
l1 = []
l2 = []
team_p = {}
team_b = {}

# get the team's resent siutaiton 
def situation(name,res):
	found = False
	if res.status_code == 200:
		print("連線程序完成1/5")
	else:
		print("伺服器連線失敗 請重試")
	resent = BeautifulSoup(res.text, 'html.parser')
	table = resent.table
	GB = 0
	row = table.find_all('tr')
	c = 0
	for r in row:
		c += 1
		if c > 1:
			data = r.find_all('td')
			c2 = 0
			for d in data:
				c2 += 1
				if c2 == 2:
					if d.string.split()[0] == name:
						found = True
					else:
						break
				if found == True:
					if c2 == 4:
						win = int(d.string.split('-')[0])
						tie = int(d.string.split('-')[1])
						lose = int(d.string.split('-')[2])
					if c2 == 5:
						winningRate = float(d.string)
					if c2 == 6:
						if d.string == "-":
							GB = 0
						else:
							GB = float(d.string)
					if c2 == 14:
						stk = d.string
		if found == True:
			break
	return win,tie,lose,winningRate,GB,stk,c-1
# get the latest game data
def latest(res):
	if res.status_code == 200:
		print("連線程序完成2/5")
	else:
		print("伺服器連線失敗 請重試")
	resent = BeautifulSoup(res.text, 'html.parser')
	table = resent.table
	row = table.find_all('tr')
	c = 0
	for r in row:
		c += 1
		if c == 2:
			data = r.find_all('td')
			j = 0
			for d in data:
				j += 1
				if j == 1:
					game_id = d.string
				if j == 2:
					position =  d.string
				elif j == 3:
					date = d.string
				elif j == 5:
					p1 = d.string
				elif j == 6:
					p1_s = d.string
				elif j == 7:
					p2 = d.string
				elif j == 8:
					p2_s = d.string
			break
	if p1 == '統一7-ELEVEn':
		p1 = '統一'
	if p2 == '統一7-ELEVEn':
		p2 = '統一'
	return position,date,p1,p1_s,p2,p2_s,game_id
def pitcherRank(url):
    win = []
    save = []
    hld = []
    res = requests.get(url, timeout = 5)
    if res.status_code == 200:
        print("連線程序完成3/5")
    else:
        print("伺服器連線失敗 請重試")
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.table
    row = table.find_all('tr')
    c = 0
    for r in row:
        c += 1
        if c > 1:
            data = r.find_all('td')
            j = 0
            for d in data:
                j += 1
                if j == 1:
                    name = d.string
                    for i in range(len(name)):
                        if name[i] == ' ':
                            name = name[i+1:]
                            break
                if j == 9:
                    hp.heappush(win,(-1*int(d.string),name))
                if j == 11:
                    hp.heappush(save,(-1*int(d.string),name))
                if j == 13:
                    hp.heappush(hld,(-1*int(d.string),name))
    return win,save,hld
def hitterRank(url):
    hit = []
    HR = []
    SB = []
    res = requests.get(url, timeout = 5)
    if res.status_code == 200:
        print("連線程序完成4/5")
    else:
        print("伺服器連線失敗 請重試")
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.table
    row = table.find_all('tr')
    c = 0
    for r in row:
        c += 1
        if c > 1:
            data = r.find_all('td')
            j = 0
            for d in data:
                j += 1
                if j == 1:
                    name = d.string
                    for i in range(len(name)):
                        if name[i] == ' ':
                            name = name[i+1:]
                            break
                if j == 8:
                    hp.heappush(hit,(-1*int(d.string),name))
                if j == 12:
                    hp.heappush(HR,(-1*int(d.string),name))
                if j == 15:
                    hp.heappush(SB,(-1*int(d.string),name))
    return hit,HR,SB
def game_box(game_id, game_date):
    global team_p
    global team_b
    global l1
    global l2
    len1 = 0
    len2 = 0
    url = 'http://www.cpbl.com.tw/games/box.html?&game_type=01&game_id=' + str(game_id) + '&game_date=' +str(game_date) + '&pbyear=2019'
    res = requests.get(url, timeout = 5)
    if res.status_code == 200:
        print("連線程序完成5/5")
    else:
        print("伺服器連線失敗 請重試")
    soup = BeautifulSoup(res.text, 'html.parser')
    cell = soup.find_all('div', class_ = "b_cell")
    k = 0
    for c in cell:
        k += 1
        if k == 2:
            name = c.find_all('span')
            j = 0
            for n in name:
                j += 1
                if j == 1:
                    pwin = n.string
                if j == 2:
                    plose = n.string
    table = soup.find_all('table')
    c = 0
    for t in table:
        c += 1
        if c == 4 or c == 5:
            j = 0
            data = t.find_all('tr')
            for d in data:
                #print(d)
                j += 1
                if(j > 1):
                    if d.td.find('a') != None:
                        box = d.find_all('td')
                        k = 0
                        for b in box:
                            k += 1
                            if k == 1:
                                name = b.a.string
                                global l2
                                l2.append(name)
                            if k == 2:
                                AB = b.string
                            if k == 3:
                                R = b.string
                            if k == 4:
                                H = b.string
                            if k == 5:
                                RBI = b.string
                            if k == 6:
                                BB = b.string
                            if k == 7:
                                SO = b.string
                            if k == 8:
                                SB = b.string
                            if k == 9:
                                AVG = b.string
                        if c == 4:
                            team_b[name] = [AB,R,H,RBI,BB,SO,SB,AVG]
                        if c == 5:
                            team_b[name] = [AB,R,H,RBI,BB,SO,SB,AVG]
        if c == 6 or c == 7:
            j = 0
            data = t.find_all('tr')
            for d in data:
                j += 1
                if(j > 1):
                    if d.td.find('a') != None:
                        box = d.find_all('td')
                        k = 0
                        for b in box:
                            k += 1
                            if k == 1:
                                name = b.a.string
                                global l1
                                l1.append(name)
                            if k == 2:
                                IP = b.string
                            if k == 3:
                                H = b.string
                            if k == 4:
                                R = b.string
                            if k == 5:
                                ER = b.string
                            if k == 6:
                                BB = b.string
                            if k == 7:
                                SO = b.string
                            if k == 8:
                                HR = b.string
                            if k == 9:
                                ERA = b.string
                            if k == 10:
                                WHIP = b.string
                        if c == 6:
                            team_p[name] = [IP,H,R,ER,BB,SO,HR,ERA,WHIP]
                        if c == 7:
                            team_p[name] = [IP,H,R,ER,BB,SO,HR,ERA,WHIP]
    return pwin, plose
def game_box2(game_id, game_date):
	global team_p
	global team_b
	global l1
	global l2
	len1 = 0
	len2 = 0
	url = 'http://www.cpbl.com.tw/games/box.html?&game_type=01&game_id=39&game_date=2019-04-20&pbyear=2019'
	#url = 'http://www.cpbl.com.tw/games/box.html?&game_type=01&game_id=' + str(game_id) + '&game_date=' +str(game_date) + '&pbyear=2019'
	res = requests.get(url, timeout = 5)
	if res.status_code == 200:
		print("連線程序完成5/5")
	else:
		print("伺服器連線失敗 請重試")
	soup = BeautifulSoup(res.text, 'html.parser')
	table = soup.find_all('table')
	c = 0
	for t in table:
		c += 1
		if c == 4 or c == 5:
			j = 0
			data = t.find_all('tr')
			for d in data:
				#print(d)
				j += 1
				if(j > 1):
					if d.td.find('a') != None:
						box = d.find_all('td')
						k = 0
						for b in box:
							k += 1
							if k == 1:
								name = b.a.string
								global l2
								l2.append(name)
							if k == 2:
								AB = b.string
							if k == 3:
								R = b.string
							if k == 4:
								H = b.string
							if k == 5:
								RBI = b.string
							if k == 6:
								BB = b.string
							if k == 7:
								SO = b.string
							if k == 8:
								SB = b.string
							if k == 9:
								AVG = b.string
						if c == 4:
							team_b[name] = [AB,R,H,RBI,BB,SO,SB,AVG]
						if c == 5:
							team_b[name] = [AB,R,H,RBI,BB,SO,SB,AVG]
		if c == 6 or c == 7:
			j = 0
			data = t.find_all('tr')
			for d in data:
				j += 1
				if(j > 1):
					if d.td.find('a') != None:
						box = d.find_all('td')
						k = 0
						for b in box:
							k += 1
							if k == 1:
								name = b.a.string
								global l1
								l1.append(name)
							if k == 2:
								IP = b.string
							if k == 3:
								H = b.string
							if k == 4:
								R = b.string
							if k == 5:
								ER = b.string
							if k == 6:
								BB = b.string
							if k == 7:
								SO = b.string
							if k == 8:
								HR = b.string
							if k == 9:
								ERA = b.string
							if k == 10:
								WHIP = b.string
						if c == 6:
							team_p[name] = [IP,H,R,ER,BB,SO,HR,ERA,WHIP]
						if c == 7:
							team_p[name] = [IP,H,R,ER,BB,SO,HR,ERA,WHIP]