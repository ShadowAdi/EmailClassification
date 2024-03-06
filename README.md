# **Email Classification Project**
## [Dataset Link](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

## [Demo](https://emailclassification-zsvhdksef7gwhntu8tecxw.streamlit.app/)

### **Description**
> Introduction
This Is an email/message spa classification Web App.You Give Message to the Input Field And It will tell you where moel is spam or not..
> Goal
The Main Goal is to get the best `precision` score.

I Used `NLTK` For Text Preprocessing and `TfidfVectorizer` For Text Representation.
The Dataset Is Also Unbalanced.So I Also Use Class Weights For Giving extra weightage to my  Spam Messages.
So i Chose Voting Classifier Because It Give Me A `Precision Score` of `1.0` and an `accuracy score` of `0.98`.

>Deployment
I Deployed My App Using `Streamlit`
