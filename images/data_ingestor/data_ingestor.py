#!/usr/bin/env python
from sqlalchemy import create_engine
from pandas import read_csv
from os import environ

# connect to the database
database_endpoint = "mysql://{}:{}@{}:{}/{}".format(environ.get("MYSQL_USER"), 
                                                    environ.get("MYSQL_PASSWORD"), 
                                                    environ.get("HOST"),
                                                    environ.get("PORT"),
                                                    environ.get("MYSQL_DATABASE"))
engine = create_engine(database_endpoint, future=True)

# load people table
peopleDf = read_csv('/data/people.csv')
peopleDf.to_sql('people', con=engine, index=False, if_exists='append', chunksize = 1000)

# load places table
placesDf = read_csv('/data/places.csv')
placesDf.to_sql('places', con=engine, index=False, if_exists='append', chunksize = 100)