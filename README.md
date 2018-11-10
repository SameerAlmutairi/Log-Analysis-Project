# FSND Project (1) - Log Analysis

By 

### Project overview
> In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data. 

## How to Run the program
### 1. Software Installation
* Vagrant: https://www.vagrantup.com/downloads.html
* Virtual Machine: https://www.virtualbox.org/wiki/Downloads
* Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm 
* Unix-style terminal program:
  * OSX & Linux users : use installed <b>terminal</b>
  * Windows users: download Git Bash: https://git-scm.com/download/win

Once you get the above software installed, follow the following instructions :

* Extract the FSND file (downloaded inside Downloads Folder):
```console
YourMachineName:~ $ cd Downloads
YourMachineName:Downloads$ unzip -a fullstack-nanodegree-vm-master.zip
```
* Then run the following instructions to lunch vagrant:
```console
YourMachineName:Downloads$ cd fullstack-nanodegree-vm-master
YourMachineName:fullstack-nanodegree-vm-master$ cd vagrant
YourMachineName:vagrant$ vagrant up
YourMachineName:vagrant$ vagrant ssh
```
### 2. Downloading and Loading Data
  * Inside the vagrant create <b>“log-analysis-project“</b> folder:
  ```console
  vagrant@vagrant:~$ cd /vagrant
  vagrant@vagrant:/vagrant$ mkdir log-analysis-project
  vagrant@vagrant:/vagrant$ cd log-analysis-project
  vagrant@vagrant:/vagrant/log-analysis-project$ 
  ```
  * Download “newsdata.sql” using the link: [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 
  
  * Unzip <b>“newsdata”</b> file and copy it to <b>“log-analysis-project“</b> folder that is inside shared folder (/vagrant)
  * Inside the vagrant vm, load the data using the next command:
  ```console
  vagrant@vagrant:/vagrant/log-analysis-project$ psql -d news -f newsdata.sql
  ```
  * Connect to news database using :
  ```console
  vagrant@vagrant:/vagrant/log-analysis-project$ psql -d news
  ```
  * To show <b>“news”</b> databse schema use:
  ```sql
  news=> \dt
          List of relations
 Schema |   Name   | Type  |  Owner  
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
(3 rows)
```
 * To show databse schema for particular table use:
 ```sql
  news=> \d articles
                                  Table "public.articles"
 Column |           Type           |                       Modifiers                       
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     | 
 body   | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
```
* To exit the psql use this command:
```sql
  news=> \q
```
### 3. Downloading and Running Python Code

  * Prerequisites
    - Python3
    - psycopg2 use:
      `pip3 install psycopg2`
  * Download or clone this project inside <b>“log-analysis-project“</b> folder using:
    ```console
    vagrant@vagrant:/vagrant/log-analysis-project$ git clone https://github.com/SameerAlmutairi/Log-Analysis-Project.git
    ```
     > _need to install git in your machine to run the previous command_
    
  * Run python script inside vagrant vm using next command:
    ```console
    vagrant@vagrant:/vagrant/log-analysis-project$ python3 log-analysis.py
    ```
     > _You might get a message that you need to install `psycopg2-binary`, if you did just run the next command:_
    
    ```console
    vagrant@vagrant:/vagrant/log-analysis-project$ pip3 install psycopg2-binary
    ```