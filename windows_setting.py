import tkinter as tk
from tkinter import font

import cpbl_info
import get_data

selected = -1
selected_team = -1

def selecting_finished(window):
    global selected
    selected = 1
    window.destroy()

def selecting_event(event, box_list, logos, window, canvas):
    global selected_team
    value = box_list.get(box_list.curselection())
    ret = -1
    ret = cpbl_info.TEAM_LIST.index(value)
    if ret != -1:
        selected_team = ret
        canvas.create_image(50, 10, image=logos[ret], anchor='nw')
        canvas.place(x=170, y=70)
        button = tk.Button(window, text="OK", command= lambda: selecting_finished(window), height=2, width=6).place(x=165, y=220, anchor='nw')

def init_window(window, size=(300, 400)):
	window.title('CPBL CRAWLER')
	window.geometry(str(size[0]) + 'x' + str(size[1]))
	window.resizable(0, 0)
	window.configure(bg='white')

def init_selecting_team_window(window):
    selecting_team_window_width = 400
    selecting_team_window_height = 300
    init_window(window, size=(selecting_team_window_width, selecting_team_window_height))

    canvas = tk.Canvas(width=300, height=200, bg='white', bd=0, highlightthickness=0, relief='ridge')
    Font = font.Font(family='Microsoft JhengHei', size=15)

    team_list = tk.StringVar()
    team_list.set(cpbl_info.TEAM_LIST)

    team_logos = [tk.PhotoImage(file=path) for path in cpbl_info.TEAM_LOGO_PATH]

    team_selection_box = tk.Listbox(window, listvariable=team_list, width=13, height=4, font=Font)
    team_selection_box.place(x=40, y=80)
    team_selection_box.bind('<<ListboxSelect>>', lambda e: selecting_event(e, team_selection_box, team_logos, window, canvas))

    title = tk.Label(window, text="選擇欲查詢球隊名稱", font=Font, bg='white')
    title.place(x=100, y=25)

def init_result_window(window):
    
    result_window_width = 800
    result_window_height = 600
    init_window(window, size=(result_window_width, result_window_height))

    bar = tk.Label(window, width=result_window_width, height=6, bg=cpbl_info.TEAM_BAR_COLOR[selected_team])
    bar.place(x=0, y=0)

    team_logos = [tk.PhotoImage(file=path) for path in cpbl_info.TEAM_LOGO_PATH]

    selected_team_logo = tk.Label(window, image=team_logos[selected_team])
    selected_team_logo.photo = team_logos[selected_team]
    selected_team_logo.grid(row=0, column=0)

    Copyright = tk.Label(window, text='資料來源:中華職棒大聯盟全球資訊網', font=('Microsoft JhengHei', 15, 'bold'), bg='white')
    Copyright.place(x=400, y=550)

def add_current_standing(window):
    res = get_data.get_current_standing_data(selected_team)

    each_title_width, each_title_height = 12, 3
    standing_string = ""
    for i in range(len(cpbl_info.STANDING_DATA_TITLE)):
        standing_string += cpbl_info.STANDING_DATA_TITLE[i] + ":" + res[i] + "   "
    standing = tk.Label(window, text=standing_string, wraplengt=500, bg=cpbl_info.TEAM_BAR_COLOR[selected_team], fg='white', font = ('Microsoft JhengHei',17,'bold'))
    standing.place(x=225, y=20)

def add_team_ranking(window):
    hitters_ranking = get_data.get_current_ranking(selected_team, is_hitter=True)
    pitchers_ranking = get_data.get_current_ranking(selected_team, is_hitter=False)
    
    ranking = [hitters_ranking, pitchers_ranking]
    x, y = 50, 340
    for i in range(2):
        if i == 0:
            size = len(hitters_ranking)
            title = cpbl_info.HITTER_RANKING_TITLE
        else:
            size = len(pitchers_ranking)
            title = cpbl_info.PITCHER_RANKING_TITLE
        for j in range(size):
            top3 = ""
            for k in range(3):
                top3 += ranking[i][j][k][0] + " " + str(ranking[i][j][k][1]) + '\n'
            current_text = title[j] + '\n' + top3
            current_title = tk.Label(window, text=current_text, font=('Microsoft JhengHei',15,'bold'), bg='white')
            current_title.place(x=x, y=y)
            x += 110


    





