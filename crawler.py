from tkinter import font
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import requests
import heapq as hp
from bs4 import BeautifulSoup

# declare the global variables we use 
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
def init_window(window, l, w):
	window.title('CPBL CRAWLER')
	window.geometry(str(l) + 'x' + str(w))
	window.resizable(0,0)
	window.configure(bg = 'white')
def p1_finish():
	global phase1_Finish
	phase1_Finish = True
	window.destroy()
def select_event(event):
	global value
	value = team_selection.get(team_selection.curselection())
	if value == '統一獅':
		canvas.create_image(50, 10, image = select_image1, anchor = 'nw')
		canvas.place(x = 150, y = 60)
		button1 = tk.Button(window, text="OK", command = p1_finish, height = 2, width = 6).place(x = 165, y = 200, anchor = 'nw')
	elif value == '兄弟象':
		canvas.create_image(50, 10, image = select_image2, anchor = 'nw')
		canvas.place(x = 150, y = 60)
		button1 = tk.Button(window, text="OK", command = p1_finish, height = 2, width = 6).place(x = 165, y = 200, anchor = 'nw')
	elif value == 'Lamigo桃猿':
		canvas.create_image(50, 10, image = select_image4, anchor = 'nw')
		canvas.place(x = 150, y = 60)
		button1 = tk.Button(window, text="OK", command = p1_finish, height = 2, width = 6).place(x = 165, y = 200, anchor = 'nw')
	elif value == '富邦悍將':
		canvas.create_image(50, 10, image = select_image3, anchor = 'nw')
		canvas.place(x = 150, y = 60)
		button1 = tk.Button(window, text="OK", command = p1_finish, height = 2, width = 6).place(x = 165, y = 200, anchor = 'nw')
def SelectFunc1(event):
	global select_p
	small_window = tk.Tk()
	init_window(small_window,550,200)
	Title = tk.Label(small_window,text = '今日' + select_p.get(), font = ('Microsoft JhengHei',15,'bold'))
	Title.place(x = 0, y = 10)
	IP_title = tk.Label(small_window, text = '局數: ' + team_p[select_p.get()][0]+ ' 被安打: '+team_p[select_p.get()][1] +
											'  失分: '+team_p[select_p.get()][2]+'  自責分: '+team_p[select_p.get()][3]
									, font = ('Microsoft JhengHei',15,'bold'), bg ='white')
	IP_title.place(x = 20, y = 60)
	IP2_title = tk.Label(small_window, text = '四壞: '+ team_p[select_p.get()][4] + ' 三振: '+ team_p[select_p.get()][5] +
										'  被全壘打: ' +team_p[select_p.get()][6]+'  ERA: '+team_p[select_p.get()][7] + '  WHIP: '+team_p[select_p.get()][8]
										,font = ('Microsoft JhengHei',15,'bold'), bg ='white')
	IP2_title.place(x = 20, y = 120)
	small_window.mainloop()
def SelectFunc2(event):
	global select_b
	small_window = tk.Tk()
	init_window(small_window,550,200)
	Title = tk.Label(small_window,text = '今日' + select_b.get(), font = ('Microsoft JhengHei',15,'bold'))
	Title.place(x = 0, y = 10)
	IP_title = tk.Label(small_window, text = '打數: ' + team_b[select_b.get()][0]+ ' 得分: '+team_b[select_b.get()][1] +
											'  安打: '+team_b[select_b.get()][2]+'  打點: '+team_b[select_b.get()][3]
									, font = ('Microsoft JhengHei',15,'bold'), bg ='white')
	IP_title.place(x = 20, y = 60)
	IP2_title = tk.Label(small_window, text = '四壞: '+ team_b[select_b.get()][4] + ' 三振: '+ team_b[select_b.get()][5] +
										'  盜壘: ' +team_b[select_b.get()][6]+'  打擊率: '+team_b[select_b.get()][7]
										,font = ('Microsoft JhengHei',15,'bold'), bg ='white')
	IP2_title.place(x = 20, y = 120)
	small_window.mainloop()
# main 
global window
window = tk.Tk() # creat window
init_window(window,400,300)
Font = font.Font(family = 'Microsoft JhengHei', size = 15)
team_list = tk.StringVar()
team_list.set(('統一獅','兄弟象','Lamigo桃猿','富邦悍將'))
global select_image1
global select_image2
global select_image3	
global select_image4
select_image1 = tk.PhotoImage(file = 'logo_01.gif')
select_image2 = tk.PhotoImage(file = 'logo_02.gif')
select_image3 = tk.PhotoImage(file = 'logo_03.gif')
select_image4 = tk.PhotoImage(file = 'logo_04.gif')
global canvas
title = tk.Label(window, text = "選擇欲查詢球隊名稱", font = Font, bg = 'white')
title.place(x = 100, y = 25)
canvas = tk.Canvas(width = 300, height = 200, bg = 'white', bd = 0, highlightthickness=0, relief='ridge')
team_selection = tk.Listbox(window, listvariable = team_list, width = 10, height = 4, font = Font)
team_selection.place(x = 40, y = 80)
team_selection.bind('<<ListboxSelect>>', select_event)
warn = tk.Label(window, text = "近日伺服器不穩定" + '\n' + '若出現超時請重試', font = ('Microsoft JhengHei',12,'bold'), bg = 'white')
warn.place(x = 125, y = 250)

global phase1_Finish
global select_p
global select_b
phase1_Finish = False
window.mainloop()
if phase1_Finish == True:
	global window2
	window2 = tk.Tk()
	init_window(window2,800,600)
	bigfont = font.Font(family="Microsoft JhengHei",size = 15)
	window2.option_add("*TCombobox*Listbox*Font", bigfont)
	logo1 = tk.PhotoImage(file = 'logo_01.gif')
	logo2 = tk.PhotoImage(file = 'logo_02.gif')
	logo3 = tk.PhotoImage(file = 'logo_03.gif')
	logo4 = tk.PhotoImage(file = 'logo_04.gif')
	canvas2 = tk.Canvas(width = 300, height = 200, bg = 'white', bd = 0, highlightthickness=0, relief='ridge')
	if value == '統一獅':
		name = '統一7-ELEVEn'
		canvas2.create_image(50, 50, image = logo1)
		canvas2.place(x = 0, y = 0)
		bar = tk.Label(window2, width = 570, height = 6, bg = 'gray16')
		bar.place(x = 110, y = 0)
		res1 = requests.get("http://www.cpbl.com.tw/standing/season/?&season=1", timeout = 5)
		win,tie,lose,winningRate,GB,stk,rank = situation(name,res1)
		board = "戰績：" + str(win) + '勝' + str(tie) + '和' + str(lose) + '敗    ' + '勝率:' + str(winningRate) + "   目前連" + stk + '場'
		board2 = "目前排名:" + str(rank) + "   勝差:" + str(GB)
		sit = tk.Label(window2, width = 50, height = 2, bg = 'gray16', text = board, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit.place(x = 110, y = 0)
		sit2 = tk.Label(window2, width = 50, height = 1, bg = 'gray16', text = board2, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit2.place(x = 110, y = 55)
		latest_url = 'http://www.cpbl.com.tw/web/team_dayscore.php?&team=L01'
		res2 = requests.get(latest_url, timeout = 5)
		position,date,p1,p1_s,p2,p2_s,game_id = latest(res2)
		title_resent = tk.Label(window2, text = "News：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		title_resent.place(x = 50, y = 120)
		latest_table = tk.Label(window2, text = '地點:' + position + '\n' + '日期' + date, fg = 'black', font = ('Microsoft JhengHei',15,'bold'), width = 25)
		latest_table.place(x = 50, y = 160)
		player_search = tk.Label(window2, text = '查詢該場次球員表現', font = ('Microsoft JhengHei',15,'bold'), width = 25)
		pitcher = tk.Label(window2, text = '投手', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		batter = tk.Label(window2, text = '打者', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		player_search.place(x = 400, y = 160)
		pitcher.place(x = 400, y = 210)
		batter.place(x = 550, y = 210)
		if int(p1_s) > int(p2_s):
			color1 = 'red'
			color2 = 'black'
		elif int(p1_s) < int(p2_s):
			color2 = 'red'
			color1 = 'black'
		score_table1 = tk.Label(window2, text = p1 + ' ' + p1_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color1)
		score_table1.place(x = 95, y = 220)
		score_table2 = tk.Label(window2, text = p2 + ' ' + p2_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color2)
		score_table2.place(x = 95, y = 250)
		team_rank = tk.Label(window2, text = "球隊各項排行榜：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		team_rank.place(x = 50,y = 300)
		pitcherData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team=L01&year=2019&grade=2&syear=2019'
		hitterData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&team=L01&gameno=01'
		winner, saver, holder = pitcherRank(pitcherData)
		win_title = tk.Label(window2, text = '勝投:', font = ('Microsoft JhengHei',15,'bold'))
		win_title.place(x = 50, y = 340)
		p1 = hp.heappop(winner)
		p2 = hp.heappop(winner)
		p3 = hp.heappop(winner)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		win_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		win_rank.place(x = 50, y = 370)
		save_title = tk.Label(window2, text = '救援:', font = ('Microsoft JhengHei',15,'bold'))
		save_title.place(x = 160, y = 340)
		p1 = hp.heappop(saver)
		p2 = hp.heappop(saver)
		p3 = hp.heappop(saver)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		save_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		save_rank.place(x = 160, y = 370)
		hld_title = tk.Label(window2, text = '中繼:', font = ('Microsoft JhengHei',15,'bold'))
		hld_title.place(x = 270, y = 340)
		p1 = hp.heappop(holder)
		p2 = hp.heappop(holder)
		p3 = hp.heappop(holder)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hld_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hld_rank.place(x = 270, y = 370)
		hit, HR, SB = hitterRank(hitterData)
		hit_title = tk.Label(window2, text = '安打:', font = ('Microsoft JhengHei',15,'bold'))
		hit_title.place(x = 380, y = 340)
		p1 = hp.heappop(hit)
		p2 = hp.heappop(hit)
		p3 = hp.heappop(hit)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hit_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hit_rank.place(x = 380, y = 370)
		HR_title = tk.Label(window2, text = '全壘打:', font = ('Microsoft JhengHei',15,'bold'))
		HR_title.place(x = 490, y = 340)
		p1 = hp.heappop(HR)
		p2 = hp.heappop(HR)
		p3 = hp.heappop(HR)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		HR_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		HR_rank.place(x = 490, y = 370)
		SB_title = tk.Label(window2, text = '盜壘:', font = ('Microsoft JhengHei',15,'bold'))
		SB_title.place(x = 600, y = 340)
		p1 = hp.heappop(SB)
		p2 = hp.heappop(SB)
		p3 = hp.heappop(SB)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		SB_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		SB_rank.place(x = 600, y = 370)
		if int(p1_s) != int(p2_s) :
			pwin, plose = game_box(game_id,date)
			p_player = tk.Label(window2, text = pwin + '\n' + plose, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
			p_player.place(x = 220, y = 225)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		else:
			game_box2(game_id,date)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		Copyright = tk.Label(window2, text = '資料來源:中華職棒大聯盟全球資訊網',font = ('Microsoft JhengHei',15,'bold'), bg = 'white' )
		Copyright.place(x = 400,y = 550)


	elif value == '兄弟象':
		name = '中信兄弟'
		canvas2.create_image(50, 50, image = logo2)
		canvas2.place(x = 0, y = 0)
		bar = tk.Label(window2, width = 570, height = 6, bg = 'DarkGoldenrod4')
		bar.place(x = 110, y = 0)
		res1 = requests.get("http://www.cpbl.com.tw/standing/season/?&season=1", timeout = 5)
		win,tie,lose,winningRate,GB,stk,rank = situation(name,res1)
		board = "戰績：" + str(win) + '勝' + str(tie) + '和' + str(lose) + '敗    ' + '勝率:' + str(winningRate) + "   目前連" + stk + '場'
		board2 = "目前排名:" + str(rank) + "   勝差:" + str(GB)
		sit = tk.Label(window2, width = 50, height = 2, bg = 'DarkGoldenrod4', text = board, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit.place(x = 110, y = 0)
		sit2 = tk.Label(window2, width = 50, height = 1, bg = 'DarkGoldenrod4', text = board2, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit2.place(x = 110, y = 55)
		latest_url = 'http://www.cpbl.com.tw/web/team_dayscore.php?&team=E02'
		res2 = requests.get(latest_url, timeout = 5)
		position,date,p1,p1_s,p2,p2_s,game_id = latest(res2)
		title_resent = tk.Label(window2, text = "News：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		title_resent.place(x = 50, y = 120)
		latest_table = tk.Label(window2, text = '地點:' + position + '\n' + '日期' + date, fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		latest_table.place(x = 50, y = 160)
		player_search = tk.Label(window2, text = '查詢該場次球員表現', font = ('Microsoft JhengHei',15,'bold'), width = 25)
		pitcher = tk.Label(window2, text = '投手', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		batter = tk.Label(window2, text = '打者', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		player_search.place(x = 400, y = 160)
		pitcher.place(x = 400, y = 210)
		batter.place(x = 550, y = 210)
		if int(p1_s) > int(p2_s):
			color1 = 'red'
			color2 = 'black'
		elif int(p1_s) < int(p2_s):
			color2 = 'red'
			color1 = 'black'
		score_table1 = tk.Label(window2, text = p1 + ' ' + p1_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color1)
		score_table1.place(x = 95, y = 220)
		score_table2 = tk.Label(window2, text = p2 + ' ' + p2_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color2)
		score_table2.place(x = 95, y = 250)
		team_rank = tk.Label(window2, text = "球隊各項排行榜：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		team_rank.place(x = 50,y = 300)
		pitcherData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team=E02&year=2019&grade=2&syear=2019'
		hitterData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&team=E02&gameno=01'
		winner, saver, holder = pitcherRank(pitcherData)
		win_title = tk.Label(window2, text = '勝投:', font = ('Microsoft JhengHei',15,'bold'))
		win_title.place(x = 50, y = 340)
		p1 = hp.heappop(winner)
		p2 = hp.heappop(winner)
		p3 = hp.heappop(winner)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		win_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		win_rank.place(x = 50, y = 370)
		save_title = tk.Label(window2, text = '救援:', font = ('Microsoft JhengHei',15,'bold'))
		save_title.place(x = 160, y = 340)
		p1 = hp.heappop(saver)
		p2 = hp.heappop(saver)
		p3 = hp.heappop(saver)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		save_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		save_rank.place(x = 160, y = 370)
		hld_title = tk.Label(window2, text = '中繼:', font = ('Microsoft JhengHei',15,'bold'))
		hld_title.place(x = 270, y = 340)
		p1 = hp.heappop(holder)
		p2 = hp.heappop(holder)
		p3 = hp.heappop(holder)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hld_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hld_rank.place(x = 270, y = 370)
		hit, HR, SB = hitterRank(hitterData)
		hit_title = tk.Label(window2, text = '安打:', font = ('Microsoft JhengHei',15,'bold'))
		hit_title.place(x = 380, y = 340)
		p1 = hp.heappop(hit)
		p2 = hp.heappop(hit)
		p3 = hp.heappop(hit)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hit_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hit_rank.place(x = 380, y = 370)
		HR_title = tk.Label(window2, text = '全壘打:', font = ('Microsoft JhengHei',15,'bold'))
		HR_title.place(x = 490, y = 340)
		p1 = hp.heappop(HR)
		p2 = hp.heappop(HR)
		p3 = hp.heappop(HR)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		HR_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		HR_rank.place(x = 490, y = 370)
		SB_title = tk.Label(window2, text = '盜壘:', font = ('Microsoft JhengHei',15,'bold'))
		SB_title.place(x = 600, y = 340)
		p1 = hp.heappop(SB)
		p2 = hp.heappop(SB)
		p3 = hp.heappop(SB)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		SB_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		SB_rank.place(x = 600, y = 370)
		if int(p1_s) != int(p2_s) :
			pwin, plose = game_box(game_id,date)
			p_player = tk.Label(window2, text = pwin + '\n' + plose, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
			p_player.place(x = 220, y = 225)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		else:
			game_box2(game_id,date)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		Copyright = tk.Label(window2, text = '資料來源:中華職棒大聯盟全球資訊網',font = ('Microsoft JhengHei',15,'bold'), bg = 'white' )
		Copyright.place(x = 400,y = 550)
	elif value == 'Lamigo桃猿':
		name = 'Lamigo'
		canvas2.create_image(50, 50, image = logo4)
		canvas2.place(x = 0, y = 0)
		bar = tk.Label(window2, width = 570, height = 6, bg = 'navy')
		bar.place(x = 110, y = 0)
		res1 = requests.get("http://www.cpbl.com.tw/standing/season/?&season=1", timeout = 5)
		win,tie,lose,winningRate,GB,stk,rank = situation(name,res1)
		board = "戰績：" + str(win) + '勝' + str(tie) + '和' + str(lose) + '敗    ' + '勝率:' + str(winningRate) + "   目前連" + stk + '場'
		board2 = "目前排名:" + str(rank) + "   勝差:" + str(GB)
		sit = tk.Label(window2, width = 50, height = 2, bg = 'navy', text = board, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit.place(x = 110, y = 0)
		sit2 = tk.Label(window2, width = 50, height = 1, bg = 'navy', text = board2, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit2.place(x = 110, y = 55)
		latest_url = 'http://www.cpbl.com.tw/web/team_dayscore.php?&team=A02'
		res2 = requests.get(latest_url, timeout = 5)
		position,date,p1,p1_s,p2,p2_s,game_id = latest(res2)
		title_resent = tk.Label(window2, text = "News：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		title_resent.place(x = 50, y = 120)
		latest_table = tk.Label(window2, text = '地點:' + position + '\n' + '日期' + date, fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		latest_table.place(x = 50, y = 160)
		player_search = tk.Label(window2, text = '查詢該場次球員表現', font = ('Microsoft JhengHei',15,'bold'), width = 25)
		pitcher = tk.Label(window2, text = '投手', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		batter = tk.Label(window2, text = '打者', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		player_search.place(x = 400, y = 160)
		pitcher.place(x = 400, y = 210)
		batter.place(x = 550, y = 210)
		if int(p1_s) > int(p2_s):
			color1 = 'red'
			color2 = 'black'
		elif int(p1_s) < int(p2_s):
			color2 = 'red'
			color1 = 'black'
		score_table1 = tk.Label(window2, text = p1 + ' ' + p1_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color1)
		score_table1.place(x = 95, y = 220)
		score_table2 = tk.Label(window2, text = p2 + ' ' + p2_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color2)
		score_table2.place(x = 95, y = 250)
		team_rank = tk.Label(window2, text = "球隊各項排行榜：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		team_rank.place(x = 50,y = 300)
		pitcherData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team=A02&year=2019&grade=2&syear=2019'
		hitterData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&team=A02&gameno=01'
		winner, saver, holder = pitcherRank(pitcherData)
		win_title = tk.Label(window2, text = '勝投:', font = ('Microsoft JhengHei',15,'bold'))
		win_title.place(x = 50, y = 340)
		p1 = hp.heappop(winner)
		p2 = hp.heappop(winner)
		p3 = hp.heappop(winner)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		win_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		win_rank.place(x = 50, y = 370)
		save_title = tk.Label(window2, text = '救援:', font = ('Microsoft JhengHei',15,'bold'))
		save_title.place(x = 160, y = 340)
		p1 = hp.heappop(saver)
		p2 = hp.heappop(saver)
		p3 = hp.heappop(saver)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		save_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		save_rank.place(x = 160, y = 370)
		hld_title = tk.Label(window2, text = '中繼:', font = ('Microsoft JhengHei',15,'bold'))
		hld_title.place(x = 270, y = 340)
		p1 = hp.heappop(holder)
		p2 = hp.heappop(holder)
		p3 = hp.heappop(holder)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hld_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hld_rank.place(x = 270, y = 370)
		hit, HR, SB = hitterRank(hitterData)
		hit_title = tk.Label(window2, text = '安打:', font = ('Microsoft JhengHei',15,'bold'))
		hit_title.place(x = 380, y = 340)
		p1 = hp.heappop(hit)
		p2 = hp.heappop(hit)
		p3 = hp.heappop(hit)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hit_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hit_rank.place(x = 380, y = 370)
		HR_title = tk.Label(window2, text = '全壘打:', font = ('Microsoft JhengHei',15,'bold'))
		HR_title.place(x = 490, y = 340)
		p1 = hp.heappop(HR)
		p2 = hp.heappop(HR)
		p3 = hp.heappop(HR)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		HR_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		HR_rank.place(x = 490, y = 370)
		SB_title = tk.Label(window2, text = '盜壘:', font = ('Microsoft JhengHei',15,'bold'))
		SB_title.place(x = 600, y = 340)
		p1 = hp.heappop(SB)
		p2 = hp.heappop(SB)
		p3 = hp.heappop(SB)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		SB_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		SB_rank.place(x = 600, y = 370)
		if int(p1_s) != int(p2_s) :
			pwin, plose = game_box(game_id,date)
			p_player = tk.Label(window2, text = pwin + '\n' + plose, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
			p_player.place(x = 220, y = 225)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		else:
			game_box2(game_id,date)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		Copyright = tk.Label(window2, text = '資料來源:中華職棒大聯盟全球資訊網',font = ('Microsoft JhengHei',15,'bold'), bg = 'white' )
		Copyright.place(x = 400,y = 550)
	else:
		name = '富邦'
		canvas2.create_image(50, 50, image = logo3)
		canvas2.place(x = 0, y = 0)
		bar = tk.Label(window2, width = 570, height = 6, bg = 'purple4')
		bar.place(x = 110, y = 0)
		res1 = requests.get("http://www.cpbl.com.tw/standing/season/?&season=1", timeout = 5)
		win,tie,lose,winningRate,GB,stk,rank = situation(name,res1)
		board = "戰績：" + str(win) + '勝' + str(tie) + '和' + str(lose) + '敗    ' + '勝率:' + str(winningRate) + "   目前連" + stk + '場'
		board2 = "目前排名:" + str(rank) + "   勝差:" + str(GB) 
		sit = tk.Label(window2, width = 50, height = 1, bg = 'purple4', text = board, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit.place(x = 110, y = 15)
		sit2 = tk.Label(window2, width = 50, height = 1, bg = 'purple4', text = board2, fg = 'white', font = ('Microsoft JhengHei',15,'bold'))
		sit2.place(x = 110, y = 55)
		latest_url = 'http://www.cpbl.com.tw/web/team_dayscore.php?&team=B04'
		res2 = requests.get(latest_url, timeout = 5)
		position,date,p1,p1_s,p2,p2_s,game_id = latest(res2)
		title_resent = tk.Label(window2, text = "News：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		title_resent.place(x = 50, y = 120)
		latest_table = tk.Label(window2, text = '地點:' + position + '\n' + '日期' + date, fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		latest_table.place(x = 50, y = 160)
		player_search = tk.Label(window2, text = '查詢該場次球員表現', font = ('Microsoft JhengHei',15,'bold'), width = 25)
		pitcher = tk.Label(window2, text = '投手', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		batter = tk.Label(window2, text = '打者', font = ('Microsoft JhengHei',15,'bold'), width = 6)
		player_search.place(x = 400, y = 160)
		pitcher.place(x = 400, y = 210)
		batter.place(x = 550, y = 210)
		if int(p1_s) > int(p2_s):
			color1 = 'red'
			color2 = 'black'
		elif int(p1_s) < int(p2_s):
			color2 = 'red'
			color1 = 'black'
		score_table1 = tk.Label(window2, text = p1 + ' ' + p1_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color1)
		score_table1.place(x = 95, y = 220)
		score_table2 = tk.Label(window2, text = p2 + ' ' + p2_s, bg = 'white', font = ('Microsoft JhengHei',15,'bold'), fg = color2)
		score_table2.place(x = 95, y = 250)
		team_rank = tk.Label(window2, text = "球隊各項排行榜：", fg = 'black', font = ('Microsoft JhengHei',15,'bold'))
		team_rank.place(x = 50,y = 300)
		pitcherData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team=B04&year=2019&grade=2&syear=2019'
		hitterData = 'http://www.cpbl.com.tw/web/team_playergrade.php?&team=B04&gameno=01'
		winner, saver, holder = pitcherRank(pitcherData)
		win_title = tk.Label(window2, text = '勝投:', font = ('Microsoft JhengHei',15,'bold'))
		win_title.place(x = 50, y = 340)
		p1 = hp.heappop(winner)
		p2 = hp.heappop(winner)
		p3 = hp.heappop(winner)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		win_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		win_rank.place(x = 50, y = 370)
		save_title = tk.Label(window2, text = '救援:', font = ('Microsoft JhengHei',15,'bold'))
		save_title.place(x = 160, y = 340)
		p1 = hp.heappop(saver)
		p2 = hp.heappop(saver)
		p3 = hp.heappop(saver)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		save_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		save_rank.place(x = 160, y = 370)
		hld_title = tk.Label(window2, text = '中繼:', font = ('Microsoft JhengHei',15,'bold'))
		hld_title.place(x = 270, y = 340)
		p1 = hp.heappop(holder)
		p2 = hp.heappop(holder)
		p3 = hp.heappop(holder)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hld_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hld_rank.place(x = 270, y = 370)
		hit, HR, SB = hitterRank(hitterData)
		hit_title = tk.Label(window2, text = '安打:', font = ('Microsoft JhengHei',15,'bold'))
		hit_title.place(x = 380, y = 340)
		p1 = hp.heappop(hit)
		p2 = hp.heappop(hit)
		p3 = hp.heappop(hit)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		hit_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		hit_rank.place(x = 380, y = 370)
		HR_title = tk.Label(window2, text = '全壘打:', font = ('Microsoft JhengHei',15,'bold'))
		HR_title.place(x = 490, y = 340)
		p1 = hp.heappop(HR)
		p2 = hp.heappop(HR)
		p3 = hp.heappop(HR)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		HR_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		HR_rank.place(x = 490, y = 370)
		SB_title = tk.Label(window2, text = '盜壘:', font = ('Microsoft JhengHei',15,'bold'))
		SB_title.place(x = 600, y = 340)
		p1 = hp.heappop(SB)
		p2 = hp.heappop(SB)
		p3 = hp.heappop(SB)
		t = p1[1] + ' ' + str(int(p1[0])*(-1)) + '\n' + p2[1] + ' ' + str(int(p2[0])*(-1)) + '\n'  + p3[1] + ' ' + str(int(p3[0])*(-1)) + '\n'
		SB_rank = tk.Label(window2, text = t, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
		SB_rank.place(x = 600, y = 370)
		if int(p1_s) != int(p2_s) :
			pwin, plose = game_box(game_id,date)
			p_player = tk.Label(window2, text = pwin + '\n' + plose, font = ('Microsoft JhengHei',15,'bold'), bg = 'white')
			p_player.place(x = 220, y = 225)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		else:
			game_box2(game_id,date)
			select_p = ttk.Combobox(window2,value = l1, width = 10)
			select_p.place(x = 400, y = 245 )
			select_b = ttk.Combobox(window2,value = l2, width = 10)
			select_p.bind("<<ComboboxSelected>>", SelectFunc1)
			select_b.place(x = 550, y = 245)
			select_b.bind("<<ComboboxSelected>>", SelectFunc2)
		Copyright = tk.Label(window2, text = '資料來源:中華職棒大聯盟全球資訊網',font = ('Microsoft JhengHei',15,'bold'), bg = 'white' )
		Copyright.place(x = 400,y = 550)

	window2.mainloop()
