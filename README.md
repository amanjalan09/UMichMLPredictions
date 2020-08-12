## ChanceMe@UMich
With increasingly competitive applications, current college admissions criteria are hard to define. ChanceMe@UMich aims to predict a student's chances into the University of Michigan using Machine Learning based on various factors such as academics, extracurricular activities, and demographics. Through an interactive web applciation, prospective students will be able to gauge where they stand in comparison to previously accepted applicants. Based on the 1000+ entries collected, the web application will also provide tips and tricks to improve chances of admission!

## Process

* Collecting the Dataset

Since no publicly dataset was available, we had to collect data first-hand (this was the most time-consuming part of the project). We created a survey on Google Forms and surveyed 1000+ students who previously applied to the University of Michigan from 40+ universities across the United States. We reached out to students mainly through University Facebook groups and also through some personal connections. We asked objective questions such as Acceptance Status into University of Michigan, SAT/ACT Score, Class Rank, Gender, Ethnicity, Student Government involvement, etc. (The survey link is posted below! Feel free to take it if you previously applied to the University of Michigan!)

https://forms.gle/LZXtainRFroLHHmC8

Fig 1 shows the number of responses we recieved as of August 13th, whereas Fig 2,3,4 show some graphs of the dataset.

| Fig 1: No. of Responses to Survey  | Fig 2: Survey Data (Acceptance to UMich) |
| ------------- | ------------- |
| <img src="/ChanceMeScreenshots/ChanceMeFig1.png" width=500>  | <img src="/ChanceMeScreenshots/ChanceMeFig2.png" width=500>   |

| Fig 3: Survey Data (EA/RA)  | Fig 4: Survey Data (ACT Scores) |
| ------------- | ------------- |
| <img src="/ChanceMeScreenshots/ChanceMeFig3.png" width=500>  | <img src="/ChanceMeScreenshots/ChanceMeFig4.png" width=500>   |

* Preprocessing the Data

Preprocessing the data involved making data more readable by changing column names, converting ACT/SAT scores to one metric, normalizing data, filtering data to remove invalid entries (Ex. people who didn't submit SAT or ACT scores, or people who submitted SAT scores not ending with 0, which is impossible), etc. Fig 5 demonstrates one such invalid entry, where the student claimed that he got a 5 on the SAT and ACT.


| Fig 5: Example of an invalid entry  | 
| ------------- |
| <img src="/ChanceMeScreenshots/ChanceMeFig5.png" width=500>  |


* Performing Exploratory Data Analysis

Data was also visualized using Matplotlib and Seaborn to make sense of data trends. This also helped with performing Feature Engineering (converting categorical data to numeric) & Feature Selection (reducing redundant variables). Fig 6 demonstrates a countplot used to analyze the trend between applicants who applied through Early Action vs Regular Action and their acceptance chances. 

| Fig 6: Countplot displaying Early Action vs Regular Decision in terms of acceptance rate | 
| ------------- |
| <img src="/ChanceMeScreenshots/ChanceMeFig6.png" width=500>  |


* Creating an ML Model

Lastly, using Scikit-Learn, various Machine Learning models were applied (Logistic Regression, Support Vector Machines, Random Forest, etc.). Fig 7 displays a classification report where an accuracy of 65% was achieved (This was only with a partial dataset of 825 responses).

| Fig 7: Classification Report of SVM model | 
| ------------- |
| <img src="/ChanceMeScreenshots/ChanceMeFig7.png" width=500>  |



* Deploying the ML Model onto a web application

Under Construction. 


## Languages/Frameworks used
* Python (NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn)
* Django


## How to use?
The interactive web application is currently construction! We're hoping to roll it out by the end of August!

## Credits
* Machine Learning by Andrew Ng (Online Course available on Coursera)
* Python for Data Science and Machine Learning Bootcamp by Jose Portilla (Online Course available on Udemy)
* https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig - Very helpful Machine Learning YouTube channel!
