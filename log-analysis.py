#!/bin/bash/python3
import psycopg2

# define database name
DBNAME = "news"

# define sql queries variables
query_one = '''
    SELECT articles.title, count(*) as num
    FROM articles, log WHERE
    log.path like concat('/article/',articles.slug)
    GROUP BY articles.title
    ORDER BY num desc LIMIT 3;
'''
query_two = '''
    SELECT authors.name,count(*)
    FROM log,articles, authors WHERE
    log.path = concat('/article/',articles.slug)
    AND articles.author = authors.id
    AND log.status like '%200%'
    GROUP BY authors.name
    ORDER BY count(*) DESC Limit 1;
'''
query_three = '''
    SELECT * From (
     SELECT error_day,
     ROUND( e.error_count * 100.0 /o.ok_count, 2) as e_rate
     FROM (
      SELECT time::date as error_day, count(*) as error_count
      FROM log WHERE status like '%404%'
      GROUP BY error_day
      ORDER BY error_count DESC
      ) as e,
      (
       SELECT time::date as ok_day, count(*) as ok_count
       FROM log WHERE status like '%200%'
       GROUP BY ok_day ORDER BY ok_count DESC
       )as o
       WHERE e.error_day = o.ok_day) as p
      WHERE e_rate > 1.0;
'''


# define queries functions
# Q1: What are the most popular three articles of all time?
def query_one_exceute():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_one)
    articles_view = c.fetchall()
    db.close()
    print("Question 1: The Three most popular articles are: ")
    for row in articles_view:
        print("\"%s\" - %s views." % (row[0], str(row[1])))
    print()


# Q2: Who are the most popular article authors of all time?
def query_two_exceute():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_two)
    authors_view = c.fetchall()
    db.close()
    print("Question 2: The most popular article author is: ")
    for row in authors_view:
        print("\"%s\" - %s views." % (row[0], str(row[1])))
    print()


# Q3: On which days did more than 1% of requests lead to errors?
def query_three_exceute():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_three)
    percentage_errors = c.fetchall()
    db.close()
    print("Question 3: The day that has more than 1% error requests is: ")
    for row in percentage_errors:
        dt = row[0]
        er = row[1]
        print('{dt:%a %d, %Y} - {er:.2f}% errors.'.format(dt=dt, er=er))
    print()


def queries_execute():
    query_one_exceute()
    query_two_exceute()
    query_three_exceute()


# main funtion
if __name__ == "__main__":
    queries_execute()
