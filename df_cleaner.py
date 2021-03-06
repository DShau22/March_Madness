"""
Manual functions for cleaning the dataframes so that data is consistent
and standardized
"""

import pandas as pd

def handle_kenpom_csvs(df):
    df['TeamName'] = df['TeamName'].replace("St\.", "St", regex=True)
    df['TeamName'] = df['TeamName'].replace("Saint Joseph's", "St Joseph's PA")
    df['TeamName'] = df['TeamName'].replace("Saint Mary's", "St Mary's CA")
    df['TeamName'] = df['TeamName'].replace("Saint", "St", regex = True)
    df['TeamName'] = df['TeamName'].replace("Abilene Christian", "Abilene Chr")
    df['TeamName'] = df['TeamName'].replace("Albany", "Albany NY")
    df['TeamName'] = df['TeamName'].replace("American", "American Univ")
    df['TeamName'] = df['TeamName'].replace("Arkansas Little Rock", "Ark Little Rock")
    df['TeamName'] = df['TeamName'].replace("Arkansas Pine Bluff", "Ark Pine Bluff")
    df['TeamName'] = df['TeamName'].replace("Bethune Cookman", "Bethune-Cookman")
    df['TeamName'] = df['TeamName'].replace("Birmingham Southern", "Birmingham So")
    df['TeamName'] = df['TeamName'].replace("Boston University", "Boston Univ")
    df['TeamName'] = df['TeamName'].replace("Cal Poly", "Cal Poly SLO")
    df['TeamName'] = df['TeamName'].replace("Central Michigan", "C Michigan")
    df['TeamName'] = df['TeamName'].replace("Central Connecticut", "Central Conn")
    df['TeamName'] = df['TeamName'].replace("Charleston Southern", "Charleston So")
    df['TeamName'] = df['TeamName'].replace("Coastal Carolina", "Coastal Car")
    df['TeamName'] = df['TeamName'].replace("College of Charleston", "Col Charleston")
    df['TeamName'] = df['TeamName'].replace("Eastern Illinois", "E Illinois")
    df['TeamName'] = df['TeamName'].replace("Eastern Kentucky", "E Kentucky")
    df['TeamName'] = df['TeamName'].replace("Eastern Michigan", "E Michigan")
    df['TeamName'] = df['TeamName'].replace("Eastern Washington", "E Washington")
    df['TeamName'] = df['TeamName'].replace("Fairleigh Dickinson", "F Dickinson")
    df['TeamName'] = df['TeamName'].replace("Florida Atlantic", "FL Atlantic")
    df['TeamName'] = df['TeamName'].replace("George Washington", "G Washington")
    df['TeamName'] = df['TeamName'].replace("Georgia Southern", "Ga Southern")
    df['TeamName'] = df['TeamName'].replace("Illinois Chicago", "IL Chicago")
    df['TeamName'] = df['TeamName'].replace("Kent St", "Kent")
    df['TeamName'] = df['TeamName'].replace("Loyola Marymount", "Loy Marymount")
    df['TeamName'] = df['TeamName'].replace("Loyola Chicago", "Loyola-Chicago")
    df['TeamName'] = df['TeamName'].replace("Maryland Eastern Shore", "MD E Shore")
    df['TeamName'] = df['TeamName'].replace("Middle Tennessee", "MTSU")
    df['TeamName'] = df['TeamName'].replace("Mississippi Valley St", "MS Valley St")
    df['TeamName'] = df['TeamName'].replace('Mount St Mary\'s', 'Mt St Mary\'s')
    df['TeamName'] = df['TeamName'].replace("Northern Illinois", "N Illinois")
    df['TeamName'] = df['TeamName'].replace("North Carolina A&T", "NC A&T")
    df['TeamName'] = df['TeamName'].replace("North Carolina St", "NC State")
    df['TeamName'] = df['TeamName'].replace("North Carolina Central", "NC Central")
    df['TeamName'] = df['TeamName'].replace("North Dakota St", "N Dakota St")
    df['TeamName'] = df['TeamName'].replace("Northern Kentucky", "N Kentucky")
    df['TeamName'] = df['TeamName'].replace("Prairie View A&M", "Prairie View")
    df['TeamName'] = df['TeamName'].replace("South Carolina St", "S Carolina St")
    df['TeamName'] = df['TeamName'].replace("Southeastern Louisiana", "SE Louisiana")
    df['TeamName'] = df['TeamName'].replace("Southeast Missouri St", "SE Missouri St")
    df['TeamName'] = df['TeamName'].replace("Stephen F. Austin", "SF Austin")
    df['TeamName'] = df['TeamName'].replace("Tennessee Martin", "TN Martin")
    df['TeamName'] = df['TeamName'].replace("Troy St", "Troy")
    df['TeamName'] = df['TeamName'].replace("Texas Southern", "TX Southern")
    df['TeamName'] = df['TeamName'].replace("VCU", "VA Commonwealth")
    df['TeamName'] = df['TeamName'].replace("Western Carolina", "W Carolina")
    df['TeamName'] = df['TeamName'].replace("Western Illinois", "W Illinois")
    df['TeamName'] = df['TeamName'].replace("Western Kentucky", "WKU")
    df['TeamName'] = df['TeamName'].replace("Western Michigan", "W Michigan")
    return df

def handle_sr_csvs(df):
    df['School'] = df['School'].replace(' NCAA', '', regex=True)
    df['School'] = df['School'].replace('(State)', 'St', regex=True)
    df['School'] = df['School'].replace('St\.', 'St', regex=True)
    df['School'] = df['School'].replace('Albany (NY)', 'Albany NY')
    df['School'] = df['School'].replace('Boston University', 'Boston Univ')
    df['School'] = df['School'].replace('Central Michigan', 'C Michigan')
    df['School'] = df['School'].replace('(Eastern)', 'E', regex=True)
    df['School'] = df['School'].replace('Louisiana St', 'LSU')
    df['School'] = df['School'].replace('North Carolina St', 'NC State')
    df['School'] = df['School'].replace('Southern California', 'USC')
    df['School'] = df['School'].replace('University of California', 'California', regex=True)
    df['School'] = df['School'].replace('American', 'American Univ')
    df['School'] = df['School'].replace('Arkansas-Little Rock', 'Ark Little Rock')
    df['School'] = df['School'].replace('Arkansas-Pine Bluff', 'Ark Pine Bluff')
    df['School'] = df['School'].replace('Bowling Green St', 'Bowling Green')
    df['School'] = df['School'].replace('Brigham Young', 'BYU')
    df['School'] = df['School'].replace('Cal Poly', 'Cal Poly SLO')
    df['School'] = df['School'].replace('Centenary (LA)', 'Centenary')
    df['School'] = df['School'].replace('Central Connecticut St', 'Central Conn')
    df['School'] = df['School'].replace('Charleston Southern', 'Charleston So')
    df['School'] = df['School'].replace('Coastal Carolina', 'Coastal Car')
    df['School'] = df['School'].replace('College of Charleston', 'Col Charleston')
    df['School'] = df['School'].replace('Cal St Fullerton', 'CS Fullerton')
    df['School'] = df['School'].replace('Cal St Sacramento', 'CS Sacramento')
    df['School'] = df['School'].replace('Cal St Bakersfield', 'CS Bakersfield')
    df['School'] = df['School'].replace('Cal St Northridge', 'CS Northridge')
    df['School'] = df['School'].replace('East Tennessee St', 'ETSU')
    df['School'] = df['School'].replace('Detroit Mercy', 'Detroit')
    df['School'] = df['School'].replace('Fairleigh Dickinson', 'F Dickinson')
    df['School'] = df['School'].replace('Florida Atlantic', 'FL Atlantic')
    df['School'] = df['School'].replace('Florida Gulf Coast', 'FL Gulf Coast')
    df['School'] = df['School'].replace('Florida International', 'Florida Intl')
    df['School'] = df['School'].replace('George Washington', 'G Washington')
    df['School'] = df['School'].replace('Georgia Southern', 'Ga Southern')
    df['School'] = df['School'].replace('Gardner-Webb', 'Gardner Webb')
    df['School'] = df['School'].replace('Illinois-Chicago', 'IL Chicago')
    df['School'] = df['School'].replace('Kent St', 'Kent')
    df['School'] = df['School'].replace('Long Island University', 'Long Island')
    df['School'] = df['School'].replace('Loyola Marymount', 'Loy Marymount')
    df['School'] = df['School'].replace('Loyola (MD)', 'Loyola MD')
    df['School'] = df['School'].replace('Loyola (IL)', 'Loyola-Chicago')
    df['School'] = df['School'].replace('Massachusetts', 'MA Lowell')
    df['School'] = df['School'].replace('Maryland-Eastern Shore', 'MD E Shore')
    df['School'] = df['School'].replace('Miami (FL)', 'Miami FL')
    df['School'] = df['School'].replace('Miami (OH)', 'Miami OH')
    df['School'] = df['School'].replace('Missouri-Kansas City', 'Missouri KC')
    df['School'] = df['School'].replace('Monmouth', 'Monmouth NJ')
    df['School'] = df['School'].replace('Mississippi Valley St', 'MS Valley St')
    df['School'] = df['School'].replace('Montana St', 'MTSU')
    df['School'] = df['School'].replace('Northern Colorado', 'N Colorado')
    df['School'] = df['School'].replace('North Dakota St', 'N Dakota St')
    df['School'] = df['School'].replace('Northern Illinois', 'N Illinois')
    df['School'] = df['School'].replace('Northern Kentucky', 'N Kentucky')
    df['School'] = df['School'].replace('North Carolina A&T', 'NC A&T')
    df['School'] = df['School'].replace('North Carolina Central', 'NC Central')
    df['School'] = df['School'].replace('Pennsylvania', 'Penn')
    df['School'] = df['School'].replace('South Carolina St', 'S Carolina St')
    df['School'] = df['School'].replace('Southern Illinois', 'S Illinois')
    df['School'] = df['School'].replace('UC-Santa Barbara', 'Santa Barbara')
    df['School'] = df['School'].replace('Southeastern Louisiana', 'SE Louisiana')
    df['School'] = df['School'].replace('Southeast Missouri St', 'SE Missouri St')
    df['School'] = df['School'].replace('Stephen F. Austin', 'SF Austin')
    df['School'] = df['School'].replace('Southern Methodist', 'SMU')
    df['School'] = df['School'].replace('Southern Mississippi', 'Southern Miss')
    df['School'] = df['School'].replace('Southern', 'Southern Univ')
    df['School'] = df['School'].replace('St Bonaventure', 'St Bonaventure')
    df['School'] = df['School'].replace('St Francis (NY)', 'St Francis NY')
    df['School'] = df['School'].replace('Saint Francis (PA)', 'St Francis PA')
    df['School'] = df['School'].replace('St John\'s (NY)', 'St John\'s')
    df['School'] = df['School'].replace('Saint Joseph\'s', 'St Joseph\'s PA')
    df['School'] = df['School'].replace('Saint Louis', 'St Louis')
    df['School'] = df['School'].replace('Saint Mary\'s (CA)', 'St Mary\'s CA')
    df['School'] = df['School'].replace('Mount St Mary\'s', 'Mt St Mary\'s')
    df['School'] = df['School'].replace('Saint Peter\'s', 'St Peter\'s')
    df['School'] = df['School'].replace('Texas A&M-Corpus Christian', 'TAM C. Christian')
    df['School'] = df['School'].replace('Texas Christian', 'TCU')
    df['School'] = df['School'].replace('Tennessee-Martin', 'TN Martin')
    df['School'] = df['School'].replace('Texas-Rio Grande Valley', 'UTRGV')
    df['School'] = df['School'].replace('Texas Southern', 'TX Southern')
    df['School'] = df['School'].replace('Alabama-Birmingham', 'UAB')
    df['School'] = df['School'].replace('UC-Davis', 'UC Davis')
    df['School'] = df['School'].replace('UC-Irvine', 'UC Irvine')
    df['School'] = df['School'].replace('UC-Riverside', 'UC Riverside')
    df['School'] = df['School'].replace('Central Florida', 'UCF')
    df['School'] = df['School'].replace('Louisiana-Lafayette', 'ULL')
    df['School'] = df['School'].replace('Louisiana-Monroe', 'ULM')
    df['School'] = df['School'].replace('Maryland-Baltimore County', 'UMBC')
    df['School'] = df['School'].replace('North Carolina-Asheville', 'UNC Asheville')
    df['School'] = df['School'].replace('North Carolina-Greensboro', 'UNC Greensboro')
    df['School'] = df['School'].replace('North Carolina-Wilmington', 'UNC Wilmington')
    df['School'] = df['School'].replace('Nevada-Las Vegas', 'UNLV')
    df['School'] = df['School'].replace('Texas-Arlington', 'UT Arlington')
    df['School'] = df['School'].replace('Texas-San Antonio', 'UT San Antonio')
    df['School'] = df['School'].replace('Texas-El Paso', 'UTEP')
    df['School'] = df['School'].replace('Virginia Commonwealth', 'VA Commonwealth')
    df['School'] = df['School'].replace('Western Carolina', 'W Carolina')
    df['School'] = df['School'].replace('Western Illinois', 'W Illinois')
    df['School'] = df['School'].replace('Western Kentucky', 'WKU')
    df['School'] = df['School'].replace('Western Michigan', 'W Michigan')
    df['School'] = df['School'].replace('Abilene Christian', 'Abilene Chr')
    df['School'] = df['School'].replace('Montana State', 'Montana St')
    df['School'] = df['School'].replace('Central Arkansas', 'Cent Arkansas')
    df['School'] = df['School'].replace('Houston Baptist', 'Houston Bap')
    df['School'] = df['School'].replace('South Dakota St', 'S Dakota St')
    df['School'] = df['School'].replace('Maryland-Eastern Shore', 'MD E Shore')
    return df
