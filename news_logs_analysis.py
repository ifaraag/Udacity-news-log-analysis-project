#!/usr/bin/env python3
""" Udacity Full Stack Nanodegree Project 1 :Log Analysis Project """

# improt database PostgreSQl lib
import psycopg2


'''Database queries: SQL Queries to get or extract the required information
 from the newsdata.sql database'''
# -------------------------------------------------------------------------------------------------------

# Query 1:What are the three most popular articles of all time?
query_popular_articles = """select articles.title,count (*) as count
            from articles , log
            where'/article/' || articles.slug = log.path
            and status = '200 OK'
            group by articles.title
            order by count desc
            limit 3;"""
# Query 2: Which authors get the most page views? Each author Read counts ?
query_authors_popularity = """select authors.name,count (*) as count
            from articles, log ,authors
            where '/article/' || articles.slug = log.path
            and log.status = '200 OK'
            and articles.author=authors.id
            group by authors.name
            order by count desc;"""
# Query 3: On which day did more than 1% of requests lead to errors?
query_bad_requests = """select *
            from ( select total_request.day,
            (num_failed_req::float/total_req::float) * 100 as precent
            from failed_request, total_request
            where failed_request.day=total_request.day ) as error
            where  precent  > 1;"""
# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------


def query_database(sql_query_request):
    ''' Open connection to DB, Query data from the database, Return results
    and Close the connection
    '''
    try:
        connection = psycopg2.connect(database="news")
        cursor = connection.cursor()
    except psycopg2.Error:
        print("Failed to connect to the PostgreSQL database.")
        return None
    else:
        cursor.execute(sql_query_request)
        results = cursor.fetchall()
        connection.close()
        return results
# -------------------------------------------------------------------------------------------------------

# Report Output

# ------------------------------------------------------------------------------------------------------


def popular_articles():
    '''print the three top articles in the database'''
    popular_3_articles = query_database(query_popular_articles)
    print("\n\t\t The Three Most Popular Articles \n")
    for title, count in popular_3_articles:
        print(" \"{}\" -- {} views".format(title, count))
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------


def authors_popularity():
    '''Print the number of viwes per author'''
    authors_popularity = query_database(query_authors_popularity)
    print("\n\t\t Number of Viwes Per Author \n")
    for name, count in authors_popularity:
        print(" {} -- {} views".format(name, count))
# ------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------
def bad_requests():
    '''Print days with more than 1% bad requests'''
    bad_requests = query_database(query_bad_requests)
    print("\n\t\t Days with more than one percentage of bad requests \n")
    for day, precent in bad_requests:
        print("""{0:%B %d, %Y} -- {1:.2f} % errors""".format(day, precent))
# ------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    popular_articles()
    authors_popularity()
    bad_requests()
