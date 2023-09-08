import streamlit as st
import pickle
import ast
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

from time import sleep
from stqdm import stqdm # for getting animation after submit event 


def SWAnalysisPage():
    
    st.header('Strengths and Weaknesses Analysis for Restaurants')
    
    st.write("Let's choose a store first!")
    menuState = ["--Select--",
                 "California",
                 "Florida",
                 "Nevada",
                 "New York",
                 "Texas"
                 ]
    
    choiceState = st.sidebar.selectbox("Choose your State", menuState)
    
    if choiceState != "--Select--":
        
        #folder_path = 'Streamlit2/TopicModellingStreamlit-main'
        
        if choiceState == "California":
            file_path = './dfStrengthAnalysis/CA_categories.pkl'
            file_df = './dfStrengthAnalysis/df_california.csv'
        elif choiceState == "Florida":
            file_path = './dfStrengthAnalysis/FL_categories.pkl'
            file_df = './dfStrengthAnalysis/df_florida.csv'
        elif choiceState == "Nevada":
            file_path = './dfStrengthAnalysis/NV_categories.pkl'
            file_df = './dfStrengthAnalysis/df_nevada.csv'
        elif choiceState == "New York":
            file_path = './dfStrengthAnalysis/NY_categories.pkl'
            file_df = './dfStrengthAnalysis/df_ny.csv'
        elif choiceState == "Texas":
            file_path = './dfStrengthAnalysis/TX_categories.pkl'
            file_df = './dfStrengthAnalysis/df_texas.csv'

        # Load the filtered set from the file
        with open(file_path, 'rb') as file:
            loaded_filtered_set = pickle.load(file)

        categories = list(loaded_filtered_set)
        sorted_categories = sorted(categories)

        # Load the df from the file
        df = pd.read_csv(file_df)
        df['categories'] = df['categories'].apply(ast.literal_eval)
        # st.write(df.head()) #debugging
        # Waiting
        for _ in stqdm(range(10), desc=f"Searching Restaurant Categories in {choiceState}"):
            sleep(0.1)

        # Second Menu - Category Filter

        menuCategory = ["--Select--"]
        menuCategory.extend(sorted_categories)
    
        choiceCategory = st.sidebar.selectbox("Choose your Category", menuCategory)
    
        if choiceCategory != "--Select--":
            # Filter the stores based on the requested category
            # st.write(choiceCategory) #debugging
            stores = df[df['categories'].apply(lambda x: choiceCategory.lower() in [c.lower() for c in x])]
            # st.write(stores) #debugging
            stores_names = stores['name'].unique()
            stores_names = sorted(stores_names)

            menuStore = ["--Select--"]
            menuStore.extend(stores_names)


            choiceStore = st.sidebar.selectbox("Choose your Restaurant", menuStore)

            if choiceStore != "--Select--":
                # Load information
                df_avg = pd.read_csv('./dfStrengthAnalysis/avg_stores.csv')
                df_avg['business_id'] = df_avg['business_id'].astype(str)
                #st.write(df_avg.head())

                business_id = df[df['name'] == choiceStore]['business_id']
                business_id = business_id.values
                #st.write(business_id[0])


                store = df_avg[df_avg['business_id'] == business_id[0]]
                #st.write(store)
                # Waiting
                for _ in stqdm(range(10), desc=f"Searching Restaurants"):
                    sleep(0.1)

                # SHOW INFO

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
                # STRENGTHs and WEAKNESSES

                # Exclude the 'business_id' column
                store = store.drop(columns=['business_id'])
                #st.write(store) # debugging



                # Get the two columns with the highest scores
                highest_columns = store.mean().nlargest(2)
                st.subheader("Strengths:")
                for topic in highest_columns.index:
                    st.write(f'+ {labels[int(topic)]}')

                # Get the two columns with the lowest scores
                lowest_columns = store.mean().nsmallest(2)
                st.subheader("Weaknesses:")
                if lowest_columns.values[1] <= 4.5:
                    for topic in lowest_columns.index:
                        st.write(f'+ {labels[int(topic)]}')
                else:
                    st.write("The costumers haven't mentioned complains yet")


                # RADAR CHART

                # Set data
                #store = store.fillna(0)   
                store.dropna(axis=1, inplace=True)




                # Number of variables
                categories = list(store)[0:]
                N = len(categories)

                # We are going to plot the first line of the data frame.
                # But we need to repeat the first value to close the circular graph:
                values = store.values[0]
                values = list(values)
                values += values[:1]

                # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
                angles = [n / float(N) * 2 * pi for n in range(N)]
                angles += angles[:1]

                # Initialize the spider plot
                fig = plt.figure(facecolor='#212636')
                ax = fig.add_subplot(111, polar=True)

                # Draw one axe per variable + add labels
                plt.xticks(angles[:-1], categories, color='white', size=12)

                # Draw ylabels
                ax.set_rlabel_position(0)
                plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="white", size=10)
                plt.ylim(0, 5)

                # Plot data
                ax.plot(angles, values, linewidth=1.5, linestyle='solid', color='pink')

                # Fill area
                ax.fill(angles, values, 'pink', alpha=0.3)

                # Set background color and grid color for dark mode
                ax.spines['polar'].set_color('white')
                ax.spines['polar'].set_linewidth(0.5)
                ax.yaxis.grid(color='white', alpha=0.5)

                # Set the background color of the figure
                fig.set_facecolor('#212636')

                # Show the graph
                st.pyplot(fig)

                # Specify Labels
                st.write("Topics:")
                for column in store.columns:
                    st.write(f'{int(column)}. {labels[int(column)]}')