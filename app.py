import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()

def load_pickle_file(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

tfidfVectorizer=load_pickle_file("./pklFiles/tfidf_vectorizer.pkl")
VotingClassifier=load_pickle_file("./pklFiles/votingClf.pkl")

def text_preprocess(text):
    lower_text = text.lower()

    text = nltk.word_tokenize(lower_text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words("english"):
            y.append(i)

    text=y[:]
    y.clear()

    
    for i in text:
        y.append(ps.stem(i))


    return  " ".join(y)


st.header("Email/Message Spam Classifier")

s1=st.text_input("Text To Analyze")

btn=st.button("Predict")

if btn:
    ans=VotingClassifier.predict(tfidfVectorizer.transform([text_preprocess(s1)]))[0]

    
    

    if ans==0:
        st.subheader("Not Spam")
    else:
        st.subheader("Spam")

