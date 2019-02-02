# Logs Analysis Project
Logs Analysis Project, part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
### By Ibrahim Farrag

## Project Requirements
The project is a reporting tool that uses information from a database containing newspaper articles and the web server log for a website. The reporting tool should answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Rquired Libraries and Dependencies
The project code requires the following software:

* Python
* psycopg2
* PostgreSQL
* Linux-based virtual machine (VM) Vagrant

## Project contents

* `news_logs_analysis.py` - The Python program that connects to the PostgreSQL database, executes the SQL queries and displays the results.
* `README.md` - This read me file.
* `results.txt` - The text output of the [news_logs_analysis.py]

## System setup and how to view this project
This project makes use of [Udacity's Linux-based virtual machine (VM)] configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Download the [fsnd-virtual-machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) and extract to a directory or your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip** (not provided here though)) and **news_logs_analysis.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. Run the two ```CREATE VIEW ``` commands below.
6. ```news_logs_analysis.py``` to run the reporting tool.

## Views used

#### total_req
This view is used to only show the dates and the total number of requests to the website (good or bad) done on that day 

````sql
CREATE VIEW total_request AS SELECT time::date AS day, count(*) AS total_req
                FROM log
                GROUP BY time::date
                ORDER BY time::date desc;

````

#### failed_request
This view is used to only show the dates and the total number of bad or requests to the website done on that day 

````sql 

CREATE VIEW failed_request AS SELECT time::date AS day, count(*) AS num_failed_req
                FROM log WHERE status not LIKE '%200%'
                GROUP BY day
                ORDER BY day;

````


## Helpful Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
