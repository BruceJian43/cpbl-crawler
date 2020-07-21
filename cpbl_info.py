# TEAM INFROMATION

TEAM_NUM = 4
TEAM_LIST = ['中信兄弟', '樂天', '統一7-ELEVEn', '富邦']
TEAM_CODE = ['E02', 'AJL011', 'L01', 'B04']
TEAM_BAR_COLOR = ['DarkGoldenrod4', 'Crimson', 'gray16', 'purple4']
TEAM_LOGO_PATH = ['asset/E02_logo.gif', 'asset/AJL011_logo.png', 'asset/L01_logo.gif', 'asset/B04_logo.gif']


STANDING_URL = 'http://www.cpbl.com.tw/standing/season/2020.html?&year=2020&season=0'
STANDING_DATA_TITLE = ['排名', '球隊', '勝-和-敗', '勝率', '勝差', '連勝/連敗']

HITTER_RANKING_URL = ['http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team={team_code}&year=2020&grade=1&syear=2020'.format(team_code=code) for code in TEAM_CODE]
PITCHER_RANKING_URL = ['http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team={team_code}&year=2020&grade=2&syear=2020'.format(team_code=code) for code in TEAM_CODE]
HITTER_RANKING_TITLE = ['安打', '全壘打', '盜壘']
PITCHER_RANKING_TITLE = ['勝場', '救援成功', '中繼點']