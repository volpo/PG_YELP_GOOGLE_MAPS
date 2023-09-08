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

# PROTOCOL
from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# LOADERS METHODS
@data_loader
def get_trends():
    
    # Create Request
    API_Key = yelp_api_key
    yelp_api = YelpAPI(API_Key)
    current_date = date.today()
    states = ['NV','TX','CA','FL','NY']
    counter_trends = 0

    for state in states:
        
        # ------------------------
        # Get Trendy Stores from API
        # ------------------------
        response = yelp_api.search_query(   term='restaurant,cafe',
                                            location=state,
                                            attributes = 'hot_and_new',
                                            sort_by='rating',
                                            )
    
        trendy_stores = response['businesses']
        # ------------------------
        # Tabularize Data
        # ------------------------
    
              
        # Create dict
        dictionary_new = {  'business_id' : [],
                            'name': [],
                            'state': [],
                            'city': [],
                            'latitude':[],
                            'longitude':[],
                            'stars':[],
                            'review_count': [],
                            'attributes':[],
                            'categories':[],
                            'hours':[],
                            'is_open':[],
                            'postal_code':[],
                            'address':[]
                            }
        
        dictionary_trend = {    'business_id' : [],
                                'date': []
                            }

        # Iterate the responses and create dfs
        for store in trendy_stores:
            value_to_check = store['id']
            column_name = 'business_id'

            # Get information related to the Stores/Business
            dictionary_new['business_id'].append(store['id'])
            dictionary_new['name'].append(store['name'])
            dictionary_new['state'].append(store['location']['state'])
            dictionary_new['city'].append(store['location']['city'])
            dictionary_new['latitude'].append(store['coordinates']['latitude'])
            dictionary_new['longitude'].append(store['coordinates']['longitude'])
            dictionary_new['stars'].append(store['rating'])
            dictionary_new['review_count'].append(store['review_count'])
            dictionary_new['attributes'].append('')

            category_list = ''
            for category in store['categories']:
                if category_list == '':
                    category_list += str(category['title'])
                else:
                    category_list += ', ' + str(category['title'])


            dictionary_new['categories'].append(category_list)
            dictionary_new['hours'].append('')
            address_complete =  store['location']['address1'] + ', ' + store['location']['city'] + ', ' + store['location']['state'] + ' ' + store['location']['zip_code']
            dictionary_new['address'].append(address_complete)
            dictionary_new['is_open'].append(int(not store['is_closed']))
            dictionary_new['postal_code'].append(store['location']['zip_code'])
            

            # Get information related to history in trends
            dictionary_trend['business_id'].append(store['id'])
            dictionary_trend['date'].append(current_date)



        # Load data into the dfs
        df_new_store = pd.DataFrame(dictionary_new)
        df_trend_history = pd.DataFrame(dictionary_trend)
        
        # ------------------------
        # Load  dfs into CASSANDRA
        # ------------------------


        # LOAD df_new_store into CASSANDRA Business Table

        # Check that the business was not already stored  
        # Iterate over each row in the DataFrame
        counter_states = 0
        for index, row in df_new_store.iterrows():
            # Extract the values from the current row
            business_id = row['business_id']

            # Construct the query with the replaced parameters
            query = f"""
                        SELECT * 
                        FROM business
                        WHERE business_id = '{business_id}'
                        LIMIT 1
                    """

            # Execute the query
            answer = session.execute(query)

            # Prepare Insert
            statement = "INSERT INTO business(business_id, state, address, attributes, categories, city, hours, is_open, latitude, longitude, name, postal_code, review_count, stars) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            insert = session.prepare(statement)

            # Check if the result has returned zero rows
            if len(answer.current_rows) == 0:
                #The query result is empty, i.e. the business didn't exist in the Table
                #print("The query result is empty.")

                # Insert the new store
                session.execute(insert, (row['business_id'], row['state'], row['address'],row['attributes'], row['categories'], row['city'],row['hours'], int(row['is_open']), row['latitude'], row['longitude'], row['name'], row['postal_code'], row['review_count'], row['stars']))
                counter_states += 1

        print(f'{counter_states} new stores inserted in the state of {state}.')
        # LOAD df_trend_history into CASSANDRA stores_in_trend Table 
        
        for index, row in df_trend_history.iterrows():
            # Prepare Insert
            statement = "INSERT INTO stores_in_trend(business_id, date_in_trend) VALUES (?,?)"
            insert = session.prepare(statement)
            # Insert the new store
            session.execute(insert, (row['business_id'], str(row['date'])))

            counter_trends +=1

        # end for states
        print(f'{counter_trends} new rows inserted in stores_in_trends.')

    return counter_trends


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Checking the Insert
    counter = 0
    for row in session.execute("SELECT * FROM stores_in_trend",):
        counter +=1
        print(row)

    print(counter, ' rows in total.' )
    assert output is not None, 'The output is undefined'