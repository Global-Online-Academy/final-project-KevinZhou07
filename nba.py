import csv
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.models import HoverTool

# Open and read the CSV file
with open('SEASON 2019-20 STATS OF NBA BOTH CONFERENCE  - 1.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    team_stats = {}
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Extract team name
        team_name = row[1]
        
        # Convert numerical values from strings to integers
        stats = [int(val) for val in row[2:]]
        
        # Create dictionary entry for team if it doesn't exist
        if team_name not in team_stats:
            team_stats[team_name] = {}
        
        # Assign each statistic to its corresponding key in the dictionary
        team_stats[team_name]['G'] = stats[0]
        team_stats[team_name]['FGM'] = stats[1]
        team_stats[team_name]['FGA'] = stats[2]
        team_stats[team_name]['3PM'] = stats[3]
        team_stats[team_name]['3PA'] = stats[4]
        team_stats[team_name]['FTM'] = stats[5]
        team_stats[team_name]['FTA'] = stats[6]
        team_stats[team_name]['OREB'] = stats[7]
        team_stats[team_name]['DREB'] = stats[8]
        team_stats[team_name]['PTS'] = stats[9]
        team_stats[team_name]['REB'] = stats[10]
        team_stats[team_name]['AST'] = stats[11]
        team_stats[team_name]['STL'] = stats[12]
        team_stats[team_name]['BLK'] = stats[13]
        team_stats[team_name]['TO'] = stats[14]
        team_stats[team_name]['PF'] = stats[15]

# Get top 10 ranked teams
top_10_ranked = [
    "Milwaukee Bucks", "Houston Rockets", "Dallas Mavericks", "LA Clippers", "New Orleans Pelicans",
    "Portland Trail Blazers", "Washington Wizards", "San Antonio Spurs", "Boston Celtics", "Phoenix Suns"
]

# Get top 10 teams with highest FGM
top_10_FGM = sorted(team_stats.keys(), key=lambda x: team_stats[x]['FGM'], reverse=True)[:10]

# Get top 10 teams with highest 3PM
top_10_3PM = sorted(team_stats.keys(), key=lambda x: team_stats[x]['3PM'], reverse=True)[:10]

# Get top 10 teams with highest REB
top_10_REB = sorted(team_stats.keys(), key=lambda x: team_stats[x]['REB'], reverse=True)[:10]

# Get top 10 teams with highest PTS
top_10_PTS = sorted(team_stats.keys(), key=lambda x: team_stats[x]['PTS'], reverse=True)[:10]

# Create hover tooltip
hover = HoverTool(tooltips=[("Value", "@top")])

# Create bar chart for top 10 ranked teams with hover tooltip
ranked_values = [team_stats[team]['G'] for team in top_10_ranked]

p_ranked = figure(x_range=top_10_ranked, title="Top 10 Ranked Teams", toolbar_location=None, tools=[hover])
p_ranked.vbar(x=top_10_ranked, top=ranked_values, width=0.9)
p_ranked.xaxis.major_label_orientation = "vertical"
p_ranked.xaxis.axis_label = "Team"
p_ranked.yaxis.axis_label = "Games Played"

# Create bar chart for top 10 teams with highest FGM with hover tooltip
FGM_teams = top_10_FGM[::-1]
FGM_values = [team_stats[team]['FGM'] for team in FGM_teams]

p_FGM = figure(x_range=FGM_teams, title="Top 10 Teams with Highest FGM", toolbar_location=None, tools=[hover])
p_FGM.vbar(x=FGM_teams, top=FGM_values, width=0.9)
p_FGM.xaxis.major_label_orientation = "vertical"
p_FGM.xaxis.axis_label = "Team"
p_FGM.yaxis.axis_label = "Field Goals Made"

# Create bar chart for top 10 teams with highest 3PM with hover tooltip
_3PM_teams = top_10_3PM[::-1]
_3PM_values = [team_stats[team]['3PM'] for team in _3PM_teams]

p_3PM = figure(x_range=_3PM_teams, title="Top 10 Teams with Highest 3PM", toolbar_location=None, tools=[hover])
p_3PM.vbar(x=_3PM_teams, top=_3PM_values, width=0.9)
p_3PM.xaxis.major_label_orientation = "vertical"
p_3PM.xaxis.axis_label = "Team"
p_3PM.yaxis.axis_label = "3-Pointers Made"

# Create bar chart for top 10 teams with highest REB with hover tooltip
REB_teams = top_10_REB[::-1]
REB_values = [team_stats[team]['REB'] for team in REB_teams]

p_REB = figure(x_range=REB_teams, title="Top 10 Teams with Highest REB", toolbar_location=None, tools=[hover])
p_REB.vbar(x=REB_teams, top=REB_values, width=0.9)
p_REB.xaxis.major_label_orientation = "vertical"
p_REB.xaxis.axis_label = "Team"
p_REB.yaxis.axis_label = "Rebounds"

# Create bar chart for top 10 teams with highest PTS with hover tooltip
PTS_teams = top_10_PTS[::-1]
PTS_values = [team_stats[team]['PTS'] for team in PTS_teams]

p_PTS = figure(x_range=PTS_teams, title="Top 10 Teams with Highest PTS", toolbar_location=None, tools=[hover])
p_PTS.vbar(x=PTS_teams, top=PTS_values, width=0.9)
p_PTS.xaxis.major_label_orientation = "vertical"
p_PTS.xaxis.axis_label = "Team"
p_PTS.yaxis.axis_label = "Points Scored"

# Display the plots in a grid layout
grid = gridplot([[p_ranked, p_FGM], [p_3PM, p_REB], [None, p_PTS]])

# Show the grid layout
show(grid)
