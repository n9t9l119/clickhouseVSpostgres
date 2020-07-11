# PostgreSQL VS Clickhouse

Utility to compare the speed performance of ClickHouse and PostgreSQL in OLAP situations.

This utility contains two sub utilities:
  - utility, that reads a dataset and fills it in two databases
  - utility, that sends SQL-queries 100 times and shows statistics *(min time, max time, mean time)*

This utility was made by Lonkina N. and Savchenko A. as summer practical work.

### Requierements:
  - **Python 3.7 +**
  - **Installed Clickhouse**
  - **Installed PostgreSQL**
  - **Installed dataset** *[(Read more)](#about-the-dataset)*
  - **Clickhouse-driver** *[(GitHub rep)](https://github.com/mymarilyn/clickhouse-driver)*
  - **Psycopg2** *[(GitHub rep)](https://github.com/psycopg/psycopg2)*
  - *more about Python requirements check* **requirements.txt**
##

### Installing Python requirements via pip
Open terminal/command prompt in the project folder and install requirements.
> pip install -r requirements.txt
##

### Installing Clickhouse via Docker
Download Clickhouse image and run container with port forwarding 9000 to use database outside docker container.
> docker pull yandex/clickhouse-server  
> docker run -p 9000:9000 -d --ulimit nofile=262144:262144 yandex/clickhouse-server
###### Read more **[here](https://hub.docker.com/r/yandex/clickhouse-server/)**
##

### Installing PostgreSQL via Docker
Download Postgres image and run container with port forwarding 5432 to use database outside docker container and without password **(don't recommend, but this's only for testing)**.
> docker pull postgres  
> docker run -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust -d postgres
###### Read more **[here](https://hub.docker.com/_/postgres)**
##

### About the dataset
We are using **[this dataset](https://transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)** for benchmarking. This is a flight dataset, that contains many metrics. You need check **Prezipped file** and download **.zip** archives how much do you need and for any periods, and place **.csv** files in **\csv** folder.  More data files you place, the more load will be on databases, and the more accurate comparison will be.
##

### First sub utility
First utility **run_creation.py** connects to databases via *clickhouse-driver* and *psycopg2*, creates and declares tables **benchmark** and fills them with **[dataset files](#about-the-dataset)** from **\csv** folder.
##

### Second sub utility
Second utility **run_benchamark.py** connects to databases and sends 100 times every query from **\sql** folder. After that, the utility displays min, max, and mean execution time for every query. This utility takes into account also the exection time of Python libraries, not only the queries execution time. For the demonstration, it has 10 different queries, but you can write your own and also use other datasets. There are no requirements for the file, the main thing is that file must have **.sql** extension and must be placed in **\sql** folder.