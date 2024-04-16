import csv

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

# Initialize dictionaries to store the team with the maximum value for each statistic
max_stats_teams = {stat: {'team': '', 'value': 0} for stat in team_stats['Milwaukee Bucks'].keys()}

# Iterate through team_stats dictionary to find the team with the maximum value for each statistic
for team, stats in team_stats.items():
    for stat, value in stats.items():
        if value > max_stats_teams[stat]['value']:
            max_stats_teams[stat]['team'] = team
            max_stats_teams[stat]['value'] = value

# Print the teams with the maximum value for each statistic
for stat, data in max_stats_teams.items():
    print(f"{stat}: {data['team']} ({data['value']})")
