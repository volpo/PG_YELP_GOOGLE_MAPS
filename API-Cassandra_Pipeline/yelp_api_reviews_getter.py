# IMPORTS
from yelpapi import YelpAPI
from credentials import YELPAPIKEY
import pandas as pd
import numpy as np

from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, dict_factory

from datetime import date

# CLUSTER SESSION
cluster = Cluster(['186.87.6.161'], port='9042', protocol_version = 5) #IP del servidor y el puerto estandar de cassandra 9042
session = cluster.connect('henry')
session.row_factory = dict_factory

# API Auth
yelp_api_key = YELPAPIKEY

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def get_new_reviews(API_Key = yelp_api_key, id_to_query = '', current_date = '',*args, **kwargs):
    '''
    Steps to follow:
        1.  Get the business name to update
        2.  Create YELP API Request
        3.  Create DF to insert
        4. LOAD df_yelp_api into CASSANDRA
            4.1 Check that the review was not already stored
            4.2 Insert the new review
        5. UPDATE row in stores_updates   
    '''
    # 1. Get the business name to update
    query = f""" 
                SELECT name 
                FROM business
                WHERE business_id = '{id_to_query}'
                LIMIT 1
                """

    statement = SimpleStatement(query, fetch_size = 5000)
    answer = session.execute(statement, timeout=None)

    for row in answer:
        business_name = row['name']
        #print(business_name)

    # 2. Create Request
    # Get the Store ID 
    business_id = id_to_query

    # Create Request
    yelp_api = YelpAPI(API_Key)
    response = yelp_api.reviews_query(id=business_id, limit = 50)

    # 3. Create DF
    # Parse Response
    reviews = response['reviews']

    # Create dict
    dictionary = {'review_id' : [],
                'user_id': [],
                'name': [],
                'business_id':[],
                'Platform':[],
                'rating':[],
                'date': [],
                'text':[],
                'comment':[],
    }

    for review in reviews:
        dictionary['review_id'].append(review['id'])
        dictionary['user_id'].append(review['user']['id'])
        dictionary['name'].append(business_name)
        dictionary['business_id'].append(business_id)
        dictionary['date'].append(review['time_created'])
        dictionary['Platform'].append('Yelp')
        dictionary['rating'].append(review['rating'])
        dictionary['text'].append(review['text'])
        dictionary['comment'].append('')


    # Create Df to load
    df_yelp_api = pd.DataFrame(dictionary) 
    df_yelp_api['date'] = pd.to_datetime(df_yelp_api['date']).dt.strftime('%Y-%m-%d')

    # 4. LOAD df_yelp_api into CASSANDRA

    # 4.1 Check that the review was not already stored  
    # Iterate over each row in the DataFrame
    counter = 0
    for index, row in df_yelp_api.iterrows():
        # Extract the values from the current row
        user_id = row['user_id']
        business_id = row['business_id']
        review_date = row['date']

        # Construct the query with the replaced parameters
        query = f"""
                    SELECT * 
                    FROM reviews_yelp
                    WHERE user_id = '{user_id}'
                        AND business_id = '{business_id}'
                        AND review_date = '{review_date}'
                    LIMIT 1
                """

        # Execute the query
        answer = session.execute(query)

        # Prepare Insert
        statement = "INSERT INTO reviews_yelp(user_id,business_id,review_date,cool,funny,useful,review_text,stars) VALUES (?,?,?,?,?,?,?,?)"
        insert = session.prepare(statement)

        # Check if the result has returned zero rows
        if len(answer.current_rows) == 0:
            #The query result is empty, i.e. the review didn't exist in the Table
            #print("The query result is empty.")

            # 4.2 Insert the new review
            session.execute(insert, (user_id, business_id, review_date, int(0), int(0), int(0), row['text'], int(row['rating'])))
            counter += 1
        '''
        else:
            # The review already existed
            for row in answer:
                print(row)
        '''

    print(f'{counter} new reviews inserted for store "{business_name}".')
    # 5. UPDATE row in stores_updates
    statement = "INSERT INTO stores_updates(business_id, date_update, updated) VALUES (?,?,?)"
    insert = session.prepare(statement)
    session.execute(insert, (id_to_query, current_date, True))

    return counter

@data_loader
def load_data(*args, **kwargs):
    """
    Now I have to query to get Business_ID that:
    1. Are not inserted in stores_updates
    2. Are Inserted but have a False condition on 'Updated'
    """
    # Initialize id_list
    id_list = []

    # Query the Table business
    states = ['NV','TX','CA','FL','NY']

    # Construct the query with the updated id_list
    query = f""" 
            SELECT business_id,state 
            FROM business
            """

    statement = SimpleStatement(query, fetch_size = 5000)
    business_table_ids = session.execute(statement, timeout=None)

    # Get information from stores_updates

    dictionary = {'business_id' : [], 'updated':[] }
    query = f""" 
            SELECT business_id,updated 
            FROM stores_updates
            """

    statement = SimpleStatement(query, fetch_size = 5000)
    updates_table = session.execute(statement, timeout=None)

    for row in updates_table:
        dictionary['business_id'].append(row['business_id'])
        dictionary['updated'].append(row['updated'])

    df_updates = pd.DataFrame(dictionary)


    for row in business_table_ids:
        if row['state'] in states:
            # Check in stores_updates
            if row['business_id'] not in list(df_updates['business_id']):
                id_list.append(row['business_id'])
            else:
                # Check if the store is updated
                cond = df_updates[df_updates['business_id'] == str(row['business_id'])]['updated']
                try:
                    if (list(cond)[0]) == False:
                            id_list.append(row['business_id'])
                except:
                    print((list(cond)[0]))

            
        if len(id_list) >= 10:
            break

    API_Key = yelp_api_key
    YELPcredits = 17  
    credits = YELPcredits
    current_date = date.today()
    current_date = str(current_date)
    
    global_counter = 0
    for i in range(credits):
        #print(id_list[i])
        counter = get_new_reviews(API_Key,id_list[i],current_date)
        global_counter += int(counter)

    print(f'{global_counter} new reviews inserted in Reviews_yelp".')
    return global_counter


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Checking the Insert
    for row in session.execute("SELECT * FROM stores_updates"):
        print(row)
    assert output is not None, 'The output is undefined'