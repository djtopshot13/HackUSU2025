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

PFF = pd.read_csv('Power 5 Data/Power 5 Offense Grades.csv')
