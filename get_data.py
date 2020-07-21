import requests
import heapq as hp
from bs4 import BeautifulSoup

import cpbl_info

def find_target_title_index_from_thead(target_list, thead):
    title_idx = []
    idx = 0
    for th in thead.find_all('th'):
        if th.has_attr('title'):
            if th['title'] in target_list:
                title_idx.append(idx)
        idx += 1
    return title_idx

def get_current_standing_data(selected_team):
    response = requests.get(cpbl_info.STANDING_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    standing_raw_data_title = soup.table.tr
    target_standing_title_idx = find_target_title_index_from_thead(cpbl_info.STANDING_DATA_TITLE, standing_raw_data_title)

    res = []
    team_name_idx = cpbl_info.STANDING_DATA_TITLE.index('球隊')
    replaced_char = ['\r', '\n', '\t', ' ']
    for team_data in standing_raw_data_title.next_siblings:
        if type(team_data) == type(standing_raw_data_title):
            current_idx = 0
            for td in team_data.find_all('td'):
                if current_idx in target_standing_title_idx:
                    res.append(*td.contents)
                current_idx += 1
            for char in replaced_char:
                res[team_name_idx] = res[team_name_idx].replace(char, '')
            if res[team_name_idx] == cpbl_info.TEAM_LIST[selected_team]:
                break
            else:
                res.clear()
    return res

def get_current_ranking(selected_team, is_hitter):
    if is_hitter:
        url = cpbl_info.HITTER_RANKING_URL[selected_team]
        target_title = cpbl_info.HITTER_RANKING_TITLE
    else:
        url = cpbl_info.PITCHER_RANKING_URL[selected_team]
        target_title = cpbl_info.PITCHER_RANKING_TITLE

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ranking_data_title = soup.table.thead
    target_ranking_title_idx = find_target_title_index_from_thead(target_title, ranking_data_title)

    ranking_data = soup.table
    ranking = []
    for i in range(len(target_ranking_title_idx)):
        ranking.append([])
    for player in ranking_data.find_all('tr'):
        if player.td != None:
            current_idx = 0
            player_name = player.td.a.contents[0].split(' ')[1]
            for td in player.find_all('td'):
                if current_idx in target_ranking_title_idx:
                    ranking[target_ranking_title_idx.index(current_idx)].append((player_name, int(td.contents[0])))
                current_idx += 1
    for i in range(len(target_ranking_title_idx)):
        ranking[i] = sorted(ranking[i], key=lambda tup: tup[1], reverse=True)

    return ranking