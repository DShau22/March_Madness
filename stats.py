"""
Contains all the functions that get different stats given a Pandas df
"""
import pandas as pd
import numpy as np
import os

from df_cleaner import handle_kenpom_csvs
from df_cleaner import handle_sr_csvs

data_dir = "./Data"
kaggle_dir = os.path.join(data_dir, "Kaggle")
kenpom_dir = os.path.join(data_dir, "Kenpom")
sr_dir = os.path.join(data_dir, "Sports_ref")

class Stats():

    def __init__(self, pds):
        self.teams_pd = pds["teams_pd"]
        self.team_conferences_pd = pds["team_conferences_pd"]
        self.kenpom_pd = handle_kenpom_csvs(pds["kenpom_pd"])
        self.sr_pd = handle_sr_csvs(pds["sr_pd"])

    def test(self):
        print("this is a test")

    def getTeamName(self, team_id):
        '''
        Testing TeamName getter:
        >>> getTeamName(1105)
        'Alabama A&M'
        '''
        assert len(self.teams_pd.loc[self.teams_pd["TeamID"] == team_id].index) != 0, "can't find team Name :("

        return self.teams_pd.loc[self.teams_pd["TeamID"] == team_id].values[0][1]

    def getTeamID(self, team_name):
        '''
        Testing TeamID getter:
        >>> getTeamID('North Carolina')
        1314
        '''
        assert len(self.teams_pd.loc[self.teams_pd["TeamName"] == team_name].index) != 0, "can't find team ID :("

        return self.teams_pd.loc[self.teams_pd['TeamName'] == team_name].values[0][0]

    def checkPower6(self, team_name, year):
        '''
        Testing power6 checker:
        >>> checkPower6("Stanford", "2002")
        1
        '''
        power_six = ['sec', 'acc', 'big_east', 'pac_twelve', 'pac_ten', 'big_ten', 'big_twelve']
        assert len(year) == 4, "Year format must be the ending year, and a string; eg: '2002'"

        team_id = self.getTeamID(team_name)
        year_conference_pd = self.team_conferences_pd[self.team_conferences_pd['Season'] == int(year)]

        if len(year_conference_pd[year_conference_pd['TeamID'] == team_id]) == 0:
            return "missing"
        elif year_conference_pd[year_conference_pd["TeamID"] == team_id].values[0][2] in power_six:
            return 1
        else:
            return 0

    """
    Four Factors Defensive Statistics
    """
    def getOppEfg(self, team_name, season):
        '''
        >>> getOppEfg("Alabama", "2002")
        0.460177
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "defense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][2]/100

    def getOppTOPercentage(self, team_name, season):
        '''
        >>> getOppTOPercentage("Auburn", "2002")
        0.237027
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "defense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][4]/100

    def getOppORPercentage(self, team_name, season):
        '''
        >>> getOppORPercentage("Auburn", "2002")
        0.37560000000000004
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "defense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][6]/100

    def getOppFTRate(self, team_name, season):
        '''
        >>> getOppFTRate("Auburn", "2003")
        0.295782
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "defense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][8]/100

    """
    Four Factors Offensive Statistics
    """

    def getEfg(self, team_name, season):
        '''
        >>> getEfg("Auburn", "2002")
        0.470159
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "offense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][2]/100

    def getTOPercentage(self, team_name, season):
        '''
        >>> getTOPercentage("Auburn", "2002")
        0.252061
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "offense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][4]/100

    def getORPercentage(self, team_name, season):
        '''
        >>> getORPercentage("Auburn", "2002")
        0.352195
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "offense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][6]/100

    def getFTRate(self, team_name, season):
        '''
        >>> getFTRate("Auburn", "2002")
        0.379048
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Four_Factors", "offense" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][8]/100

    """
    Height and Experience and Bench stats
    """

    def getSize(self, team_name, season):
        '''
        >>> getSize("Auburn", "2007")
        76.83
        '''
        if(int(season) < 2007):
            return 0
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Height_experience", "height" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][2]

    def getEffectiveHeight(self, team_name, season):
        '''
        >>> getEffectiveHeight("Auburn", "2007")
        -1.18
        '''
        if(int(season) < 2007):
            return 0
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Height_experience", "height" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][14]

    def getExperience(self, team_name, season):
        '''
        >>> getExperience("Auburn", "2007")
        1.14
        '''
        if(int(season) < 2007):
            return 0
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Height_experience", "height" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][16]

    def getBenchMin(self, team_name, season):
        '''
        >>> getBenchMin("Auburn", "2007")
        29.75
        '''
        if(int(season) < 2007):
            return 0
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Height_experience", "height" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][18]

    """
    General Statistics
    """

    def get2PtFGPercentage(self, team_name, season):
        '''
        >>> get2PtFGPercentage("Auburn", "2002")
        0.468809
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][2]/100


    def get3PtFGPercentage(self, team_name, season):
        '''
        >>> get3PtFGPercentage("Auburn", "2002")
        0.31528
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][4]/100

    def getFTPercentage(self, team_name, season):
        '''
        >>> getFTPercentage("Auburn", "2002")
        0.592965
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][6]/100

    def getBlockPercentage(self, team_name, season):
        '''
        >>> getBlockPercentage("Auburn", "2002")
        0.13434200000000002
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][8]/100

    def getOpp2PtFGPercentage(self, team_name, season):
        '''
        >>> getOpp2PtFGPercentage("Auburn", "2002")
        0.44661900000000004
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][10]/100

    def getOpp3PtFGPercentage(self, team_name, season):
        '''
        >>> getOpp3PtFGPercentage("Auburn", "2002")
        0.302
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][12]/100

    def getOppFTPercentage(self, team_name, season):
        '''
        >>> getOppFTPercentage("Auburn", "2002")
        0.681135
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][14]/100

    def getOppBlockPercentage(self, team_name, season):
        '''
        >>> getOppBlockPercentage("Auburn", "2002")
        0.069943
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][16]/100

    def getAssistRate(self, team_name, season):
        '''
        >>> getAssistRate("Auburn", "2002")
        0.5629740000000001
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][22]/100

    def getOppAssistRate(self, team_name, season):
        '''
        >>> getOppAssistRate("Auburn", "2002")
        0.534456
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][24]/100

    def getStealRate(self, team_name, season):
        '''
        >>> getStealRate("Auburn", "2002")
        0.1148
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][26]

    def getOppStealRate(self, team_name, season):
        '''
        >>> getOppStealRate("Auburn", "2002")
        0.1198
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][28]

    def getDefensiveFingerprint(self, team_name, season):
        '''
        >>> getDefensiveFingerprint("Auburn", "2002")
        5.5
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Misc_stats", "misc" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][30]

    """
    Point Distributions
    """

    def getPointPercentageFromFT(self, team_name, season):
        '''
        >>> getPointPercentageFromFT("Auburn", "2002")
        0.19291599999999998
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Point_distributions", "pointdist" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][2] / 100

    def getPointPercentageFrom2pt(self, team_name, season):
        '''
        >>> getPointPercentageFrom2pt("Auburn", "2002")
        0.5405989999999999
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Point_distributions", "pointdist" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][4] / 100

    def getPointPercentageFrom3pt(self, team_name, season):
        '''
        >>> getPointPercentageFrom3pt("Auburn", "2002")
        0.26648499999999997
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Point_distributions", "pointdist" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][6] / 100

    def getOppPointPercentageFromFT(self, team_name, season):
        '''
        >>> getOppPointPercentageFromFT("Auburn", "2002")
        0.218767
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Point_distributions", "pointdist" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][8] / 100

    def getOppPointPercentageFrom2pt(self, team_name, season):
        '''
        >>> getOppPointPercentageFrom2pt("Auburn", "2002")
        0.538338
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Point_distributions", "pointdist" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][10] / 100

    def getOppPointPercentageFrom3pt(self, team_name, season):
        '''
        >>> getOppPointPercentageFrom3pt("Auburn", "2002")
        0.242895
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"
        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "Point_distributions", "pointdist" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][12] / 100

    """
    Summaries
    """

    def getTempo(self, team_name, season):
        '''
        >>> getTempo("Auburn", "2002")
        71.2696
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][2]

    def getAdjTempo(self, team_name, season):
        '''
        >>> getAdjTempo("St John's", "2002")
        69.1465
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][4]

    def getOffensiveEfficiency(self, team_name, season):
        '''
        >>> getOffensiveEfficiency("Auburn", "2002")
        92.1664
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][6]

    def getAdjOffensiveEfficiency(self, team_name, season):
        '''
        >>> getAdjOffensiveEfficiency("Auburn", "2002")
        98.6419
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][8]

    def getDefensiveEfficiency(self, team_name, season):
        '''
        >>> getDefensiveEfficiency("Auburn", "2002")
        93.4108
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][10]

    def getAdjDefensiveEfficiency(self, team_name, season):
        '''
        >>> getAdjDefensiveEfficiency("Auburn", "2002")
        92.0288
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][12]

    def getAdjEfficiencyMargin(self, team_name, season):
        '''
        >>> getAdjEfficiencyMargin("Auburn", "2002")
        6.613110000000001

        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.kenpom_pd = pd.read_csv(os.path.join(kenpom_dir, "summaries", "summary" + season[2:] + ".csv"))
        if len(self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].index) == 0:
            return "missing"
        return self.kenpom_pd.loc[self.kenpom_pd["TeamName"] == team_name].values[0][14]

    """
    Sports Reference Basic Statistics
    """

    def getNumWins(self, team_name, season):
        '''
        >>> getNumWins("Mt St Mary's", '2017')
        20
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        this.self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][3]

    def getWinPercentage(self, team_name, season):
        '''
        >>> getWinPercentage("Air Force", "2002")
        0.321
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][5]

    def getSRS(self, team_name, season):
        '''
        >>> getSRS("Air Force", "2002")
        -0.95
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][6]

    def getPpg(self, team_name, season):
        '''
        >>> getPpg("Air Force", "2002")
        57.32142857142857
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][14] / self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][2]

    def getOppPpg(self, team_name, season):
        '''
        >>> getOppPpg("Air Force", "2002")
        61.5
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][15] / self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][2]


    def getFtm(self, team_name, season):
        '''
        >>> getFtm("Air Force", "2002")
        331
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][24]

    def getFgPercent(self, team_name, season):
        '''
        >>> getFgPercent("St John's", "2002")
        0.401
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][20]

    def get3pPercent(self, team_name, season):
        '''
        >>> get3pPercent("St John's", "2002")
        0.287
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][23]

    def get3pm(self, team_name, season):
        '''
        >>> get3pm("St John's", "2002")
        139
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][21]

    def getFtPercent(self, team_name, season):
        '''
        >>> getFtPercent("Air Force", "2002")
        0.7120000000000001
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_basic.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][26]

    """
    Advanced Sports Reference Statistics
    """

    def getTrueShooting(self, team_name, season):
        '''
        >>> getTrueShooting("Air Force", "2004")
        0.607
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_adv.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][21]

    def getTotalReboundPercent(self, team_name, season):
        '''
        >>> getTotalReboundPercent("Air Force", "2004")
        43.4
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_adv.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][22]

    def getTotalReboundPercent(self, team_name, season):
        '''
        >>> getTotalReboundPercent("Air Force", "2004")
        43.4
        '''
        assert len(season) == 4, "Season format must be the ending year, and a string; eg: '2002'"

        self.sr_pd = pd.read_csv(os.path.join(sr_dir, season + "_adv.csv"), skiprows=1)
        if len(self.sr_pd.loc[self.sr_pd["School"] == team_name].index) == 0:
            return "missing"
        return self.sr_pd.loc[self.sr_pd["School"] == team_name].values[0][22]
