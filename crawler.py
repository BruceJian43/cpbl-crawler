from tkinter import font
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
from GetData import *


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
select_image1 = tk.PhotoImage(file = './asset/logo_01.gif')
select_image2 = tk.PhotoImage(file = './asset/logo_02.gif')
select_image3 = tk.PhotoImage(file = './asset/logo_03.gif')
select_image4 = tk.PhotoImage(file = './asset/logo_04.gif')

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
			#the game is tie
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
