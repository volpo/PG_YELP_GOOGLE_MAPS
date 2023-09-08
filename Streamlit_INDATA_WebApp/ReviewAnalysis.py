#======================================================
#               IMPORTS GLOBAL
#======================================================
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaMulticore
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


from time import sleep
from stqdm import stqdm # for getting animation after submit event 
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import transformers

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer




# Define a function to preprocess the text
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    # Return the preprocessed tokens as a string
    return lemmatized_tokens

def get_topics(review_text=''):

    # Extract the tokens based on specified conditions
    tokens = preprocess_text(review_text)

    # Load and Check the model
    lda_model_loaded = LdaMulticore.load('./LDA_model/lda_model_10topics')
    dictionary = Dictionary.load('./GensimDictionary/dictionary.dict')


    # Predict
    new_doc_bow = dictionary.doc2bow(tokens)
    topics_probabilities = lda_model_loaded.get_document_topics(new_doc_bow)

    return topics_probabilities


def ReviewAnalysisPage():
    st.header('Topic Recognition and Sentiment Analysis for Restaurants')
   
   # Labels associated with each index
    labels = [
        "Family friendly",
        "Family owned business - Small and Cozy",
        "Desserts Quality",
        "Menu variety",
        "Waiting time (take order, answer questions and bring food)",
        "Food Quality (International food)",
        "Food Quality (Tasteful and generous)",
        "Traditional Location",
        "Fun night Atmosphere",
        "Customer Support, enjoyable atmosphere and Affordable"
    ]

    # Preload pipeline Transformers
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'

    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    sentiment_analysis = pipeline("sentiment-analysis",
                                model = model,
                                tokenizer = tokenizer)

    # Define a box for text input
    review_text = st.text_input("Enter your review text:", "Review text")
    ok = st.button('Get Topics')

    if ok :
        # Sentiment triggering
        result = sentiment_analysis(review_text)[0]
        sentiment = result['label']
        # Topic triggering
        predictions = get_topics(review_text=review_text)

        # Extract probabilities and labels from the data list
        probabilities = [t[1] for t in predictions]
        labels = [labels[t[0]] for t in predictions]

        # Waiting
        for _ in stqdm(range(50), desc="Please wait a bit. The model is fetching the results !!"):
            sleep(0.1)


        # ---------------------------------------------------------------------
        st.subheader("Sentiment Analysis")

        
        if sentiment =="POSITIVE":
            st.write("""### This text has a Positive Sentiment.  🤗""")
        elif sentiment =="NEGATIVE":
            st.write("""### This text has a Negative Sentiment. 😤""")
        elif sentiment =="NEUTRAL":
            st.write("""### This text seems Neutral ... 😐""")

        # ---------------------------------------------------------------------
        st.subheader("Topic Modelling")
        # Enable dark mode
        plt.style.use('dark_background')
        # BAR PLOT
        # Create a pink color for the bars
        bar_color = '#FF69B4'

        # Horizontal Bar Plot
        fig, ax = plt.subplots(figsize=(20, 12))
        y_pos = np.arange(len(labels))
        ax.barh(y_pos, probabilities, color=bar_color)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels, fontsize=40)  # Specify the desired font size
        ax.invert_yaxis()
        ax.set_xlabel('Probability', fontsize=40)  # Specify the desired font size

        # Display the horizontal bar plot using Streamlit
        st.pyplot(fig)

        # Pie Plot
        fig, ax = plt.subplots(figsize=(10, 6))
        cmap = cm.get_cmap('RdPu')
        colors = cmap(np.linspace(0, 1, len(labels)))
        ax.pie(probabilities, labels=labels, autopct='%1.1f%%', colors=colors)
        ax.axis('equal')
        ax.tick_params(labelsize=30)  # Specify the desired font size for tick labels

        # Display the pie plot using Streamlit
        st.pyplot(fig)

        