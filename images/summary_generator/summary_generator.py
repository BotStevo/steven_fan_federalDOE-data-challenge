#!/usr/bin/env python
from collections import defaultdict
from json import dump
from sqlalchemy import create_engine, schema, sql
from calendar import month_abbr
from os import environ

database_endpoint = "mysql://{}:{}@{}:{}/{}".format(environ.get("MYSQL_USER"), 
                                                    environ.get("MYSQL_PASSWORD"), 
                                                    environ.get("HOST"),
                                                    environ.get("PORT"),
                                                    environ.get("MYSQL_DATABASE"))
engine = create_engine(database_endpoint, future=True)

with engine.connect() as connection:
  metadata = schema.MetaData(engine)
  people = schema.Table('people', metadata, autoload=True, autoload_with=engine)
  places = schema.Table('places', metadata, autoload=True, autoload_with=engine)

  summary = defaultdict(int)
  bonus_summary = {}

  # mapping of cities to a dict of dobs in the city mapped to number of dob occurence
  countyToDobCounts = defaultdict(lambda: defaultdict(int)) 

  # parse inner join of people and places
  rows = connection.execute(sql.select(places.c.county, people.c.date_of_birth, places.c.country)
  .select_from(people.join(places, people.c.place_of_birth == places.c.city))).fetchall()
  connection.commit() 
  for row in rows:
    
    # count number of people born in each country
    summary[row[-1]] += 1
    
    # count birth month for each county of Northern Ireland
    if (row[-1] == "Northern Ireland"):
      countyToDobCounts[row[0]][row[1].month] += 1

  # find most common birth month for each county
  for county, dobCounts in countyToDobCounts.items():
    bonus_summary[county] = month_abbr[int(max(dobCounts, key=dobCounts.get))]

  # save summaries to output
  with open('/data/summary_output.json', 'w') as json_file:
    dump(summary, json_file, separators=(',', ':'))

  with open('/data/bonus_summary_output.json', 'w') as json_file:
    dump(bonus_summary, json_file, separators=(',', ':'), indent=4)
