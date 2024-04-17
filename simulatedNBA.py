import random
import csv
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.models import HoverTool

# Function to simulate a season for a team
def simulate_season():
    teams = [
        "Milwaukee Bucks", "Houston Rockets", "Dallas Mavericks", "LA Clippers", "New Orleans Pelicans",
        "Portland Trail Blazers", "Washington Wizards", "San Antonio Spurs", "Boston Celtics", "Phoenix Suns",
        "Los Angeles Lakers", "Minnesota Timberwolves", "Toronto Raptors", "Memphis Grizzlies", "Miami Heat",
        "Atlanta Hawks", "Brooklyn Nets", "Utah Jazz", "Denver Nuggets", "Philadelphia 76ers",
        "Oklahoma City Thunder", "Sacramento Kings", "Indiana Pacers", "Orlando Magic", "Detroit Pistons",
        "Cleveland Cavaliers", "Chicago Bulls", "Golden State Warriors", "New York Knicks", "Charlotte Hornets"
    ]
    season_data = {}

    for team in teams:
        G = random.randint(60, 82)
        FGM = random.randint(2500, 3500)
        FGA = random.randint(5000, 7000)
        _3PM = random.randint(600, 1200)
        _3PA = random.randint(1800, 3000)
        FTM = random.randint(1000, 2000)
        FTA = random.randint(1300, 2000)
        OREB = random.randint(500, 900)
        DREB = random.randint(1800, 2800)
        PTS = random.randint(6000, 9000)
        REB = random.randint(2500, 4000)
        AST = random.randint(1200, 2000)
        STL = random.randint(400, 800)
        BLK = random.randint(200, 600)
        TO = random.randint(800, 1200)
        PF = random.randint(1000, 1800)

        season_data[team] = {
            'G': G, 'FGM': FGM, 'FGA': FGA, '3PM': _3PM, '3PA': _3PA,
            'FTM': FTM, 'FTA': FTA, 'OREB': OREB, 'DREB': DREB,
            'PTS': PTS, 'REB': REB, 'AST': AST, 'STL': STL,
            'BLK': BLK, 'TO': TO, 'PF': PF
        }

    return season_data

# Simulate seasons and write data to a text file
with open('simulatedseasons.txt', 'w') as file:
    for _ in range(10):  # Simulate 10 seasons
        season_data = simulate_season()
        for team, stats in season_data.items():
            file.write(f"{team},{stats['G']},{stats['FGM']},{stats['FGA']},{stats['3PM']},{stats['3PA']},"
                       f"{stats['FTM']},{stats['FTA']},{stats['OREB']},{stats['DREB']},{stats['PTS']},"
                       f"{stats['REB']},{stats['AST']},{stats['STL']},{stats['BLK']},{stats['TO']},{stats['PF']}\n")

# Read data from the text file and create a dictionary
team_stats = {}
with open('simulatedseasons.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        team_name = data[0]
        team_stats[team_name] = {
            'G': int(data[1]), 'FGM': int(data[2]), 'FGA': int(data[3]),
            '3PM': int(data[4]), '3PA': int(data[5]), 'FTM': int(data[6]),
            'FTA': int(data[7]), 'OREB': int(data[8]), 'DREB': int(data[9]),
            'PTS': int(data[10]), 'REB': int(data[11]), 'AST': int(data[12]),
            'STL': int(data[13]), 'BLK': int(data[14]), 'TO': int(data[15]),
            'PF': int(data[16])
        }

# Generate visualizations
# Create hover tooltip
hover = HoverTool(tooltips=[("Value", "@top")])

# Get top 10 teams with highest FGM
top_10_FGM = sorted(team_stats.keys(), key=lambda x: team_stats[x]['FGM'], reverse=True)[:10]
FGM_teams = top_10_FGM[::-1]
FGM_values = [team_stats[team]['FGM'] for team in FGM_teams]

# Get top 10 teams with highest 3PM
top_10_3PM = sorted(team_stats.keys(), key=lambda x: team_stats[x]['3PM'], reverse=True)[:10]
_3PM_teams = top_10_3PM[::-1]
_3PM_values = [team_stats[team]['3PM'] for team in _3PM_teams]

# Get top 10 teams with highest REB
top_10_REB = sorted(team_stats.keys(), key=lambda x: team_stats[x]['REB'], reverse=True)[:10]
REB_teams = top_10_REB[::-1]
REB_values = [team_stats[team]['REB'] for team in REB_teams]

# Get top 10 teams with highest PTS
top_10_PTS = sorted(team_stats.keys(), key=lambda x: team_stats[x]['PTS'], reverse=True)[:10]
PTS_teams = top_10_PTS[::-1]
PTS_values = [team_stats[team]['PTS'] for team in PTS_teams]

# Create bar chart for top 10 teams with highest FGM with hover tooltip
p_FGM = figure(x_range=FGM_teams, title="Top 10 Teams with Highest FGM", toolbar_location=None, tools=[hover])
p_FGM.vbar(x=FGM_teams, top=FGM_values, width=0.9)
p_FGM.xaxis.major_label_orientation = "vertical"
p_FGM.xaxis.axis_label = "Team"
p_FGM.yaxis.axis_label = "Field Goals Made"

# Create bar chart for top 10 teams with highest 3PM with hover tooltip
p_3PM = figure(x_range=_3PM_teams, title="Top 10 Teams with Highest 3PM", toolbar_location=None, tools=[hover])
p_3PM.vbar(x=_3PM_teams, top=_3PM_values, width=0.9)
p_3PM.xaxis.major_label_orientation = "vertical"
p_3PM.xaxis.axis_label = "Team"
p_3PM.yaxis.axis_label = "3-Pointers Made"

# Create bar chart for top 10 teams with highest REB with hover tooltip
p_REB = figure(x_range=REB_teams, title="Top 10 Teams with Highest REB", toolbar_location=None, tools=[hover])
p_REB.vbar(x=REB_teams, top=REB_values, width=0.9)
p_REB.xaxis.major_label_orientation = "vertical"
p_REB.xaxis.axis_label = "Team"
p_REB.yaxis.axis_label = "Rebounds"

# Create bar chart for top 10 teams with highest PTS with hover tooltip
p_PTS = figure(x_range=PTS_teams, title="Top 10 Teams with Highest PTS", toolbar_location=None, tools=[hover])
p_PTS.vbar(x=PTS_teams, top=PTS_values, width=0.9)
p_PTS.xaxis.major_label_orientation = "vertical"
p_PTS.xaxis.axis_label = "Team"
p_PTS.yaxis.axis_label = "Points Scored"

# Display the plots in a grid layout
grid = gridplot([[p_FGM, p_3PM], [p_REB, p_PTS]])

# Show the grid layout
show(grid)
