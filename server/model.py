import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

class Model:

    def __init__(self):
        self.df = pd.read_csv (r'/Users/amanjalan/Downloads/UMichMLTrial(2).csv')
        self.clean()

    def clean(self):

        self.df.rename(columns = {'Did you get into the University of Michigan?':'Accepted'},inplace = True)
        self.df.rename(columns = {'What was the nature of your application to the University of Michigan?':'EA/RA','If you took the SAT, what was your score out of 1600 (Ex. 1500)?':'SAT','If you took the ACT, what was your score out of 36 (Ex. 34)?':'ACT'},inplace = True)
        self.df.rename(columns = {'Where would you rank yourself academically in class?':'Rank','What College within the University of Michigan did you apply to?':'College'},inplace = True)
        self.df.rename(columns = {'How many SAT Subject Test Scores were submitted with a score of >= 700?':'SAT II'},inplace = True)
        self.df.rename(columns = {'How many AP Test Scores were submitted with a score of >= 3?':'AP', 'How many IB Test Scores were submitted with a score of >= 5?':'IB', 'What gender identity do you most identify with?':'Gender','What was your residency status when you applied to the University of Michigan?':'Residency Status', 'Were you considered a legacy (i.e. your parents or siblings went to the University of Michigan)?':'Legacy', 'Were you considered a first-generation college student (i.e. you were the first in your family to go to college)?':'First-Gen', 'Did you ask for Financial Aid?':'Financial Aid'}, inplace = True)
        self.df.rename(columns = {'Were you a part of Student government at your school?':'Student Gov','Did you have any notable leadership positions in high school (i.e. President/Vice-President of a club)?':'Leadership', 'Please indicate your ethnicity?':'Ethnicity','Were you a member of a Sports team in high school (Dedicated 100+ hours)?':'Sports','Did you volunteer in high school (Dedicated 100+ hours)?':'Volunteer','Did you participate in the performing arts (dance, drama and other forms of artistic expressions) while in high school (100+ hours)?':'Performing Arts',"If you'd like to be considered for the Amazon gift card raffle, please enter an email id that we can send the gift card to (Optional)":'Email'}, inplace = True)
        ScamEntry = (self.df['SAT'].isnull() & self.df['ACT'].isnull()) 
        ScamIndices = self.df[ScamEntry].index        
        self.df.drop(ScamIndices, inplace = True)
        self.df.reset_index(drop=True, inplace = True)
        self.df.drop(df.index[641],inplace = True)        
        self.df.reset_index(drop=True, inplace = True)
        self.df.drop(df.index[636],inplace = True)
        self.df.reset_index(drop=True, inplace = True)    

        ScoreTemp = df['SAT'].dropna()
        ScoreTempIndex = ScoreTemp[ScoreTemp%10 != 0].index
        self.df.drop(ScoreTempIndex, inplace = True)
        self.df.reset_index(drop=True, inplace = True)

        Lottery = self.df['Email']
        Lottery.dropna(inplace = True)
        Lottery.reset_index(drop=True, inplace = True)
        self.df.drop('Email',axis = 1,inplace = True)
        
        self.df['ConvertedAct'] = self.df.SAT.apply(self.ConvertScore)
        self.df['ACT'] = self.df.ACT.apply(self.ActFix) 
        self.df['Standardized Score'] = self.df.apply(self.ChooseScore, axis = 1)
        self.df.drop(['SAT','ACT','ConvertedAct'], axis = 1, inplace = True)        
                
        self.df.drop(['NormStan','Fare_boxcox'], axis = 1, inplace = True)
        self.categorical_features=[feature for feature in self.df.columns if self.df[feature].dtype=='O']
        self.categorical_features.remove('Accepted')

        for feature in self.categorical_features:
            temp = self.df.groupby(feature)['Accepted'].count()/len(df)
            temp_df = temp[temp > 0.01].index
            self.df[feature] = np.where(self.df[feature].isin(temp_df), self.df[feature], 'Rare_Var')
        
        for feature in self.categorical_features:
            self.df[feature] = pd.factorize(self.df[feature])[0]
        '''    
        feature_scale=[feature for feature in self.df.columns if feature not in ['Accepted']]
        scaler=MinMaxScaler()
        scaler.fit(df[feature_scale])
        self.df = pd.concat([self.df[['Accepted']].reset_index(drop=True), pd.DataFrame(scaler.transform(self.df[feature_scale]), columns=feature_scale)],axis=1)
        self.df = self.df.sample(frac=1).reset_index(drop=True)
        self.df['Accepted'] = self.df.Accepted.map({'Yes':1, 'No':0}) 

        X_train, X_test, y_train, y_test = train_test_split(self.df.drop(columns = 'Accepted'), df['Accepted'], test_size=0.3, random_state = 9)
        feature_sel_model = SelectFromModel(Lasso(alpha=0.005, random_state=0))
        ''' 

    def train(self):
        pass

    def test(self):
        pass

    def ConvertScore(self,SatScore):
    if (np.isnan(SatScore)):
        return 0
    elif (SatScore >= 1570 and SatScore <= 1600):
        return 36
    elif (SatScore >= 1530 and SatScore <= 1560):
        return 35
    elif (SatScore >= 1490 and SatScore <= 1520):
        return 34
    elif (SatScore >= 1450 and SatScore <= 1480):
        return 33
    elif (SatScore >= 1420 and SatScore <= 1440):
        return 32
    elif (SatScore >= 1390 and SatScore <= 1410):
        return 31
    elif (SatScore >= 1360 and SatScore <= 1380):
        return 30
    elif (SatScore >= 1330 and SatScore <= 1350):
        return 29
    elif (SatScore >= 1300 and SatScore <= 1320):
        return 28
    elif (SatScore >= 1260 and SatScore <= 1290):
        return 27
    elif (SatScore >= 1230 and SatScore <= 1250):
        return 26
    elif (SatScore >= 1200 and SatScore <= 1220):
        return 25
    elif (SatScore >= 1160 and SatScore <= 1190):
        return 24
    elif (SatScore >= 1130 and SatScore <= 1150):
        return 23
    elif (SatScore >= 1100 and SatScore <= 1120):
        return 22
    elif (SatScore >= 1060 and SatScore <= 1090):
        return 21
    elif (SatScore >= 1030 and SatScore <= 1050):
        return 20
    elif (SatScore >= 990 and SatScore <= 1020):
        return 19
    elif (SatScore >= 960 and SatScore <= 980):
        return 18
    elif (SatScore >= 920 and SatScore <= 950):
        return 17
    elif (SatScore >= 880 and SatScore <= 910):
        return 16
    elif (SatScore >= 830 and SatScore <= 870):
        return 15
    elif (SatScore >= 780 and SatScore <= 820):
        return 14
    elif (SatScore >= 730 and SatScore <= 770):
        return 13
    elif (SatScore >= 690 and SatScore <= 720):
        return 12
    elif (SatScore >= 650 and SatScore <= 680):
        return 11
    elif (SatScore >= 620 and SatScore <= 640):
        return 10
    elif (SatScore >= 590 and SatScore <= 610):
        return 9
    else:
        return 0 

    def ActFix(self,Score):
        if (np.isnan(Score)):
            return 0
        else:
            return Score

    def ChooseScore(self,row):
        if (row.ACT >= row.ConvertedAct):
            return row.ACT
        else:
            return row.ConvertedAct
