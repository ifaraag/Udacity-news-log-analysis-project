#!/usr/bin/env python3
""" Udacity Full Stack Nanodegree Project 1 :Log Analysis Project """

# improt database PostgreSQl lib
import psycopg2

# Database queries: SQL Queries to get or extract the required information from the newsdata.sql database 
#-------------------------------------------------------------------------------------------------------

# Query 1:What are the three most popular articles of all time? 
query_popular_articles = """ title,count (*) as count 
							from articles join log on '/article/' || articles.slug like log.path 
							where status like '%200%' 
							group by title,slug,path 
							order by count desc 
							limit 3;"""
# Database query 2: Who are the most popular article authors of all time?





# Database query 3: On which day did more than 1% of requests lead to errors?

#-------------------------------------------------------------------------------------------------------