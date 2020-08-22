import pandas
import pickle
import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.model_selection import train_test_split

def act_fix(score):
    if (np.isnan(score)):
        return 0
    else:
        return score

def choose_score(row):
    if (row.ACT >= row.ConvertedAct):
        return row.ACT
    else:
        return row.ConvertedAct

def convert_score(satscore):
    if (np.isnan(satscore)):
        return 0
    elif (satscore >= 1570 and satscore <= 1600):
        return 36
    elif (satscore >= 1530 and satscore <= 1560):
        return 35
    elif (satscore >= 1490 and satscore <= 1520):
        return 34
    elif (satscore >= 1450 and satscore <= 1480):
        return 33
    elif (satscore >= 1420 and satscore <= 1440):
        return 32
    elif (satscore >= 1390 and satscore <= 1410):
        return 31
    elif (satscore >= 1360 and satscore <= 1380):
        return 30
    elif (satscore >= 1330 and satscore <= 1350):
        return 29
    elif (satscore >= 1300 and satscore <= 1320):
        return 28
    elif (satscore >= 1260 and satscore <= 1290):
        return 27
    elif (satscore >= 1230 and satscore <= 1250):
        return 26
    elif (satscore >= 1200 and satscore <= 1220):
        return 25
    elif (satscore >= 1160 and satscore <= 1190):
        return 24
    elif (satscore >= 1130 and satscore <= 1150):
        return 23
    elif (satscore >= 1100 and satscore <= 1120):
        return 22
    elif (satscore >= 1060 and satscore <= 1090):
        return 21
    elif (satscore >= 1030 and satscore <= 1050):
        return 20
    elif (satscore >= 990 and satscore <= 1020):
        return 19
    elif (satscore >= 960 and satscore <= 980):
        return 18
    elif (satscore >= 920 and satscore <= 950):
        return 17
    elif (satscore >= 880 and satscore <= 910):
        return 16
    elif (satscore >= 830 and satscore <= 870):
        return 15
    elif (satscore >= 780 and satscore <= 820):
        return 14
    elif (satscore >= 730 and satscore <= 770):
        return 13
    elif (satscore >= 690 and satscore <= 720):
        return 12
    elif (satscore >= 650 and satscore <= 680):
        return 11
    elif (satscore >= 620 and satscore <= 640):
        return 10
    elif (satscore >= 590 and satscore <= 610):
        return 9
    else:
        return 0

def cleaning(data):

    df = pd.DataFrame(data, columns = ["What College within the University of Michigan did you apply to?","What was the nature of your application to the University of Michigan?","If you took the SAT, what was your score out of 1600 (Ex. 1500)?","If you took the ACT, what was your score out of 36 (Ex. 34)?","Where would you rank yourself academically in class?","How many SAT Subject Test Scores were submitted with a score of >= 700?","How many AP Test Scores were submitted with a score of >= 3?","How many IB Test Scores were submitted with a score of >= 5?","What gender identity do you most identify with?","Please indicate your ethnicity?","What was your residency status when you applied to the University of Michigan?","Were you considered a legacy (i.e. your parents or siblings went to the University of Michigan)?","Were you considered a first-generation college student (i.e. you were the first in your family to go to college)?","Did you ask for Financial Aid?","Were you a part of Student government at your school?","Did you have any notable leadership positions in high school (i.e. President/Vice-President of a club)?","Were you a member of a Sports team in high school (Dedicated 100+ hours)?","Did you volunteer in high school (Dedicated 100+ hours)?","Did you participate in the performing arts (dance, drama and other forms of artistic expressions) while in high school (100+ hours)?","If you'd like to be considered for the Amazon gift card raffle, please enter an email id that we can send the gift card to (Optional)"]) 


    df.rename(columns = {'What was the nature of your application to the University of Michigan?':'EA/RA','If you took the SAT, what was your score out of 1600 (Ex. 1500)?':'SAT','If you took the ACT, what was your score out of 36 (Ex. 34)?':'ACT'},inplace = True)

    df.rename(columns = {'Where would you rank yourself academically in class?':'Rank','What College within the University of Michigan did you apply to?':'College'},inplace = True)

    df.rename(columns = {'How many SAT Subject Test Scores were submitted with a score of >= 700?':'SAT II'},inplace = True)

    df.rename(columns = {'How many AP Test Scores were submitted with a score of >= 3?':'AP', 'How many IB Test Scores were submitted with a score of >= 5?':'IB', 'What gender identity do you most identify with?':'Gender','What was your residency status when you applied to the University of Michigan?':'Residency Status', 'Were you considered a legacy (i.e. your parents or siblings went to the University of Michigan)?':'Legacy', 'Were you considered a first-generation college student (i.e. you were the first in your family to go to college)?':'First-Gen', 'Did you ask for Financial Aid?':'Financial Aid'}, inplace = True)

    df.rename(columns = {'Were you a part of Student government at your school?':'Student Gov','Did you have any notable leadership positions in high school (i.e. President/Vice-President of a club)?':'Leadership', 'Please indicate your ethnicity?':'Ethnicity','Were you a member of a Sports team in high school (Dedicated 100+ hours)?':'Sports','Did you volunteer in high school (Dedicated 100+ hours)?':'Volunteer','Did you participate in the performing arts (dance, drama and other forms of artistic expressions) while in high school (100+ hours)?':'Performing Arts',"If you'd like to be considered for the Amazon gift card raffle, please enter an email id that we can send the gift card to (Optional)":'Email'}, inplace = True)
    df['ConvertedAct'] = df.SAT.apply(convert_score)

    df['ACT'] = df.ACT.apply(act_fix)
    df['Standardized Score'] = df.apply(choose_score, axis = 1)
    df.drop(['SAT','ACT','ConvertedAct'], axis = 1, inplace = True)
    df.drop('Email',axis = 1,inplace = True)
    
    categorical_features=[feature for feature in df.columns if df[feature].dtype=='O']

    for feature in categorical_features:
        df[feature] = pd.factorize(df[feature])[0]

    return df.head()

