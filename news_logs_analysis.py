#!/usr/bin/env python3
""" Udacity Full Stack Nanodegree Project 1 :Log Analysis Project """

# improt database PostgreSQl lib
import psycopg2

# Database queries: SQL Queries to get or extract the required information from the newsdata.sql database 
#-------------------------------------------------------------------------------------------------------

# Query 1:What are the three most popular articles of all time? 
query_popular_articles = """select articles.title,count (*) as count 
			from articles join log on '/article/' || articles.slug like log.path 
			where status like '%200%' 
			group by articles.title
			order by count desc 
			limit 3;"""
# Query 2: Which authors get the most page views? Each author Read counts ?
query_authors_popularity = """select authors.name,count (*) as count
			from articles, log ,authors where '/article/' || articles.slug like log.path
			and log.status like '%200%' and articles.author=authors.id
			group by authors.name
			order by count desc;"""
# Query 3: On which day did more than 1% of requests lead to errors?
query_bad_requests = """select *
			from ( select total_request.day, total_req, num_failed_req, (num_failed_req::float/total_req::float) * 100 as precent 
			from failed_request, total_request 
			where failed_request.day=total_request.day ) as error 
			where  precent  > 1;"""
#-------------------------------------------------------------------------------------------------------

# Open connection to database, Query data from the database, Return results and Close the connection
#-------------------------------------------------------------------------------------------------------
def query_database(sql_query_request):
	try:
		connection = psycopg2.connect(database="news")
		cursor = connection.cursor()
	except:
		print("Failed to connect to the PostgreSQL database.")
        return None
    else:
    	cursor.execute(sql_query_request)
    	results = cursor.fetchall()
    	connection.close()
    return results
#-------------------------------------------------------------------------------------------------------