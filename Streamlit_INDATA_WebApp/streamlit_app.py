#======================================================
#               IMPORTS GLOBAL
#======================================================
#import pandas as pd
#import spacy
#import en_core_web_sm
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaMulticore
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


from time import sleep
from stqdm import stqdm # for getting animation after submit event 
#import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
#import json
#import spacy
#import spacy_streamlit
import transformers

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#======================================================
#               IMPORTS GLOBAL
#======================================================

from ReviewAnalysis import ReviewAnalysisPage
from SWAnalysis import SWAnalysisPage



#======================================================
#               NLTK libraries
#======================================================
# Download the required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')



#======================================================
#               Sidebar
#======================================================
def draw_all(
    key,
    plot=False,
):
    st.write(
        """
        # INDATA - USA Gastronomics Web App
        
        This Natural Language Processing Based Web App provides two main functionalities: 
        
        ```python
        # Key Features of this App.
        1. Review Analysis
        2. Stores Strengths and Weaknesses       
        ```

        
        This App is built using transformers and LDA Unsupervised models to recognize the topics present in the users reviews and classifier whether the review has a positive, negative or neutral cognotation.
        
        """
    )
    
with st.sidebar:
    draw_all("sidebar")


    def main():
        st.title("INDATA - USA Gastronomics - NLP Web App")
        menu = ["--Select--","Review Analysis","Stores Strengths and Weaknesses"]
        choice = st.sidebar.selectbox("Choose your Analysis", menu)


        if choice=="--Select--":
            #folder_path = 'Streamlit2/TopicModellingStreamlit-main'
            folder_path = '.'
            st.image(folder_path + '/figures/indatalogo.jpg')

            st.write("""
                    
                    This Natural Language Processing Based Web App was trained with Google and Yelp datasets
                    which provide reviews from different stores all over USA.
            """)
            
            st.write("""
                    
                    This NLP Web App is based on two main models. 
                    1. A BERT model for sentiment analysis allowing to identify
                     whether a review has a positive, negative or neutral cognotation.
                    2. A LDA Unsupervised model for topic modelling allowing to recognize 
                     the presence or not of 10 topics in a review.
            """)

        elif choice=="Review Analysis":
            ReviewAnalysisPage()

        elif choice=="Stores Strengths and Weaknesses":
            SWAnalysisPage()
            
            
            
            
            





if __name__ == '__main__':
    main()
