#!/usr/bin/env python3
# 
import psycopg2

# define database name
DBNAME = "news"

# define sql queries variables
query_one = '''
    SELECT articles.title, count(*) as num
    FROM articles, log 
    WHERE log.path like concat('/article/',articles.slug)
    GROUP BY articles.title
    ORDER BY num desc LIMIT 3;
'''
query_two = '''
    SELECT authors.name,count(*)
    FROM log,articles, authors 
    WHERE log.path = concat('/article/',articles.slug)
    AND articles.author = authors.id
    AND log.status like '%200%'
    GROUP BY authors.name
    ORDER BY count(*) DESC;
'''
query_three = '''
    SELECT * From (
     SELECT error_day,
     ROUND( 100.0 * e.error_count / (o.ok_count + e.error_count), 2) as e_rate
     FROM (
      SELECT time::date as error_day, count(*) as error_count
      FROM log 
      WHERE status like '%404%'
      GROUP BY error_day
      ORDER BY error_count DESC
      ) as e,
      (
       SELECT time::date as ok_day, count(*) as ok_count
       FROM log 
       WHERE status like '%200%'
       GROUP BY ok_day 
       ORDER BY ok_count DESC
       )as o
       WHERE e.error_day = o.ok_day) as p
      WHERE e_rate > 1.0;
'''


# define queries functions
def query_one_exceute():
    """Q1: What are the most popular three articles of all time?"""
    articles_view = query_execute(query_one)
    print("Question 1: The Three most popular articles are: ")
    for row in articles_view:
        print("\"%s\" - %s views." % (row[0], str(row[1])))
    print()


def query_two_exceute():
    """Q2: Who are the most popular article authors of all time?"""
    authors_view = query_execute(query_two)
    print("Question 2: The most popular article authors are: ")
    for row in authors_view:
        print("\"%s\" - %s views." % (row[0], str(row[1])))
    print()


def query_three_exceute():
    """Q3: On which days did more than 1% of requests lead to errors?"""
    percentage_errors = query_execute(query_three)
    print("Question 3: The day that has more than 1% error requests is: ")
    for dt, er in percentage_errors:
        # dt = row[0]
        # er = row[1]
        print('{dt:%B %d, %Y} - {er:.2f}% errors.'.format(dt=dt, er=er))
    print()


def query_execute(query):
    """
    This function is taking a sql query as a parameter
    then execute it and return the result

    args:
        query : sql query as (string)

    returns:
        list of tuples containing query results 
    """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


# running queries functions
def run_queries():
    query_one_exceute()
    query_two_exceute()
    query_three_exceute()


# main funtion
if __name__ == "__main__":
    run_queries()
