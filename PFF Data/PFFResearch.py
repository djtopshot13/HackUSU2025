import pandas as pd

BowlPlayoffTeamGPDict = {
    "OHIO STATE": 4,
    "NOTRE DAME": 4,
    "PENN STATE": 3,
    "TEXAS": 3, 
}
bowl_teams = ["S ALABAMA", "W MICHIGAN", "MEMPHIS", "W VIRGINIA", "W KENTUCKY", "ILLINOIS",
            "JAMES MADISON", "CAL", "UNLV", "GA SOUTHRN", "SM HOUSTON", "OHIO", "JVILLE ST",
            "TULANE", "FLORIDA", "COAST CAR", "UTSA", "N ILLINOIS", "FRESNO ST", "S FLORIDA", 
            "S JOSE ST", "PITTSBURGH", "TOLEDO", "RUTGERS", "KANSAS ST", "ARKANSAS ST", "BOWL GREEN", 
            "OKLAHOMA", "NAVY", "GA TECH", "VANDERBILT", "TEXAS TECH", "ARKANSAS", "SYRACUSE", "WASHINGTON ST", 
            "TEXAS A&M", "USC", "N CAROLINA", "BOSTON COL", "NEBRASKA", "LA LAFAYET", "TCU", "IOWA ST", 
            "MIAMI OH", "COLO ST", "E CAROLINA", "NC STATE", "COLORADO", "LA TECH", "ARMY", "IOWA", 
            "MISSOURI", "ALABAMA", "MICHIGAN", "LOUISVILLE", "WASHINGTON", "S CAROLINA", "ILLINOIS", 
            "BAYLOR", "LSU", "DUKE", "OLE MISS", "N TEXAS", "TEXAS ST", "MINNESOTA", "VA TECH", 
            "BUFFALO", "LIBERTY", "BYU", "MIAMI FL", "GEORGIA", "CLEMSON", "SMU", "TENNESSEE",
            "INDIANA", "ARIZONA ST", "BOISE ST", "OREGON"]
P5ConfDict = { 
    "ACC": {
        "Boston College": "BOSTON COL",
        "California": "CAL",
        "Clemson": "CLEMSON",
        "Duke": "DUKE",
        "Florida State": "FLORIDA ST",
        "Georgia Tech": "GA TECH",
        "Louisville": "LOUISVILLE",
        "Miami (FL)": "MIAMI FL",
        "North Carolina": "N CAROLINA",
        "NC State": "NC STATE",
        "Wake Forest": "WAKE",
        "Notre Dame": "NOTRE DAME",
        "Pittsburgh": "PITTSBURGH",
        "Syracuse": "SYRACUSE",
        "Southern Methodist": "SMU",
        "Stanford": "STANFORD",
        "Syracuse": "SYRACUSE",
        "Virginia": "VIRGINIA",
        "Virginia Tech": "VA TECH",
        "Wake Forest": "WAKE",
    },
    "SEC": {
        "Alabama": "ALABAMA",
        "Arkansas": "ARKANSAS",
        "Auburn": "AUBURN",
        "Florida": "FLORIDA",
        "Georgia": "GEORGIA",
        "Kentucky": "KENTUCKY",
        "LSU": "LSU",
        "Mississippi State": "MISS ST",
        "Missouri": "MISSOURI",
        "Oklahoma": "OKLAHOMA",
        "Mississippi": "OLE MISS",
        "South Carolina": "S CAROLINA",
        "Tennessee": "TENNESSEE",
        "Texas": "TEXAS",
        "Texas A&M": "TEXAS A&M",
        "Vanderbilt": "VANDERBILT"        
    },
    "Big 12": {
        "Arizona": "ARIZONA",
        "Arizona State": "ARIZONA ST",
        "Baylor": "BAYLOR",
        "Brigham Young": "BYU",
        "Central Florida": "UCF",
        "Cincinnati": "CINCINNATI",
        "Colorado": "COLORADO",
        "Houston": "HOUSTON",
        "Iowa State": "IOWA ST",
        "Colorado": "COLORADO",
        "Iowa State": "IOWA ST",
        "Kansas": "KANSAS",
        "Kansas State": "KANSAS ST",
        "Oklahoma State": "OKLAHOMA ST",
        "Texas Christian": "TCU",
        "Texas Tech": "TEXAS TECH",
        "Utah": "UTAH",
        "West Virginia": "W VIRGINIA",
        
    },
    "Big Ten": {
        "Illinois": "ILLINOIS",
        "Indiana": "INDIANA",
        "Iowa": "IOWA",
        "Maryland": "MARYLAND",
        "Michigan": "MICHIGAN",
        "Michigan State": "MICH ST",
        "Minnesota": "MINNESOTA",
        "Nebraska": "NEBRASKA",
        "Northwestern": "NWESTERN",
        "Ohio State": "OHIO STATE",
        "Oregon": "OREGON",
        "Penn State": "PENN STATE",
        "Purdue": "PURDUE",
        "Rutgers": "RUTGERS",
        "UCLA": "UCLA",
        "USC": "USC",
        "Washington": "WASHINGTON",
        "Wisconsin": "WISCONSIN"
    },
    "Pac-12": {
        "Oregon State": "OREGON ST",
        "Washington State": "WASH ST"
    }
}
G5ConfDict = {
    "MW": {
        "Air Force": "AIR FORCE",
        "Boise State": "BOISE ST",
        "Colorado State": "COLO ST",
        "Fresno State": "FRESNO ST",
        "Hawaii": "HAWAII",
        "Nevada": "NEVADA",
        "New Mexico": "NEW MEX ST",
        "San Diego State": "S Diego ST",
        "San Jose State": "S JOSE ST",
        "Nevada-Las Vegas": "UNLV",
        "Utah State": "UTAH ST",
        "Wyoming": "WYOMING"
    },
    "AAC": {
        "Alabama at Birmingham": "UAB",
        "UNC Charlotte": "CHARLOTTE",
        "East Carolina": "E CAROLINA",
        "Florida Atlantic": "FAU",
        "Memphis": "MEMPHIS",
        "North Texas": "N TEXAS",
        "Rice": "RICE",
        "South Florida": "S FLORIDA",
        "Temple": "TEMPLE",
        "Texas at San Antonio": "UTSA",
        "Tulane": "TULANE",
        "Tulsa": "TULSA",
        "Wichita State": "WICHITA ST"
    },
    "Sunbelt":
    {
        "Appalachian State": "APP ST",
        "Arkansas State": "ARKANSAS ST",
        "Coastal Carolina": "COAST CAR",
        "Georgia Southern": "GA SOUTHRN",
        "Georgia State": "GA STATE",
        "Louisiana": "LA LAFAYET",
        "Louisiana Monroe": "LA MONROE",
        "Marshall": "MARSHALL",
        "Old Dominion": "DOMINION",
        "South Alabama": "S ALABAMA",
        "Southern Mississippi": "SO MISS",
        "Texas State": "TEXAS ST",
        "Troy": "TROY"
    },
    "MAC":
    {
        "Akron": "AKRON",
        "Ball State": "BALL ST",
        "Bowling Green": "BOWL GREEN",
        "Buffalo": "BUFFALO",
        "Central Michigan": "C MICHIGAN",
        "Eastern Michigan": "E MICHIGAN",
        "Kent State": "KENT STATE",
        "Miami (OH)": "MIAMI OH",
        "Northern Illinois": "N ILLINOIS",
        "Ohio": "OHIO",
        "Toledo": "TOLEDO",
        "Western Michigan": "W MICHIGAN"
    },
    "CUSA":
    {
        "Florida International": "FIU",
        "Jacksonville State": "JVILLE ST",
        "Kennesaw State": "KENNESAW",
        "Liberty": "LIBERTY",
        "Louisiana Tech": "LA TECH",
        "Middle Tennessee": "MIDDLE TN",
        "New Mexico State": "NEW MEX STATE",
        "Sam Houston State": "SM HOUSTON",
        "Texas at El Paso": "UTEP",
        "Western Kentucky": "W KENTUCKY"
    }
}

P5Ddf = pd.read_csv('Power 5 Data/Power 5 Defense Grades.csv')
P5Odf = pd.read_csv('Power 5 Data/Power 5 Offense Grades.csv')
P5Sdf = pd.read_csv('Power 5 Data/Power 5 ST Grades.csv')
G5Ddf = pd.read_csv('Group 5 Data/Group 5 Defense Grades.csv') 
G5Odf = pd.read_csv('Group 5 Data/Group 5 Offense Grades.csv')
G5Sdf = pd.read_csv('Group 5 Data/Group 5 ST Grades.csv')
PFFdf = pd.read_csv('MW Data/pff-data.csv')

def generateConfCols(df, confDict):
    # Create a mapping dictionary
    team_to_conf = {}
    for conf, teams in confDict.items():
        for team, team_name in teams.items():
            team_to_conf[team] = conf
            team_to_conf[team_name] = conf
    
    # Use the mapping to create the 'Conf' column
    df['Conf'] = df['Team'].map(team_to_conf)
    
    # If you want to insert it at a specific location (e.g., index 8)
    conf_col = df.pop('Conf')
    df.insert(loc=8, column='Conf', value=conf_col)
    
    return df
    
P5Ddf = generateConfCols(P5Ddf, P5ConfDict)
P5Ddf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
P5Ddf.to_csv('Power 5 Data/Power 5 Defense Grades.csv', index=False)
P5Odf = generateConfCols(P5Odf, P5ConfDict)
P5Odf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
P5Odf.to_csv('Power 5 Data/Power 5 Offense Grades.csv', index=False)
P5Sdf = generateConfCols(P5Sdf, P5ConfDict)
P5Sdf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
P5Sdf.to_csv('Power 5 Data/Power 5 ST Grades.csv', index=False)

G5Ddf = generateConfCols(G5Ddf, G5ConfDict)
G5Ddf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
G5Ddf.to_csv('Group 5 Data/Group 5 Defense Grades.csv', index=False)
G5Odf = generateConfCols(G5Odf, G5ConfDict)
G5Odf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
G5Odf.to_csv('Group 5 Data/Group 5 Offense Grades.csv', index=False)
G5Sdf = generateConfCols(G5Sdf, G5ConfDict)
G5Sdf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
G5Sdf.to_csv('Group 5 Data/Group 5 ST Grades.csv', index=False)

PFFdf = generateConfCols(PFFdf, G5ConfDict)
PFFdf.sort_values(by=['S', 'Conf', 'Team', 'Name'], inplace=True)
PFFdf.to_csv('MW Data/pff-data.csv', index=False)

