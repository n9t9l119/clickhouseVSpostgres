import math, psycopg2
from psycopg2.extras import execute_values


class Postges:
    tableName = 'benchmark'

    def __init__(self, host, user, password=None):
        self.connection = psycopg2.connect(user=user, host=host, password=password)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName}
                        (Year smallint,
                            Quarter smallint,
                            Month smallint,
                            DayofMonth smallint,
                            DayOfWeek smallint,
                            FlightDate date,
                            UniqueCarrier varchar(7),
                            AirlineID integer,
                            Carrier varchar(2),
                            TailNum text,
                            FlightNum text,
                            OriginAirportID integer,
                            OriginAirportSeqID integer,
                            OriginCityMarketID integer,
                            Origin varchar(5),
                            OriginCityName text,
                            OriginState varchar(2),
                            OriginStateFips text,
                            OriginStateName text,
                            OriginWac integer,
                            DestAirportID integer,
                            DestAirportSeqID integer,
                            DestCityMarketID integer,
                            Dest varchar(5),
                            DestCityName text,
                            DestState varchar(2),
                            DestStateFips text,
                            DestStateName text,
                            DestWac integer,
                            CRSDepTime integer,
                            DepTime integer,
                            DepDelay real,
                            DepDelayMinutes real,
                            DepDel15 real,
                            DepartureDelayGroups text,
                            DepTimeBlk text,
                            TaxiOut real,
                            WheelsOff integer,
                            WheelsOn integer,
                            TaxiIn real,
                            CRSArrTime integer,
                            ArrTime integer,
                            ArrDelay real,
                            ArrDelayMinutes real,
                            ArrDel15 real,
                            ArrivalDelayGroups integer,
                            ArrTimeBlk text,
                            Cancelled real,
                            CancellationCode varchar(1),
                            Diverted real,
                            CRSElapsedTime real,
                            ActualElapsedTime real,
                            AirTime real,
                            Flights real,
                            Distance real,
                            DistanceGroup real,
                            CarrierDelay real,
                            WeatherDelay real,
                            NASDelay real,
                            SecurityDelay real,
                            LateAircraftDelay real,
                            FirstDepTime text,
                            TotalAddGTime text,
                            LongestAddGTime text,
                            DivAirportLandings text,
                            DivReachedDest text,
                            DivActualElapsedTime text,
                            DivArrDelay text,
                            DivDistance text,
                            Div1Airport text,
                            Div1AirportID integer,
                            Div1AirportSeqID integer,
                            Div1WheelsOn text,
                            Div1TotalGTime text,
                            Div1LongestGTime text,
                            Div1WheelsOff text,
                            Div1TailNum text,
                            Div2Airport text,
                            Div2AirportID integer,
                            Div2AirportSeqID integer,
                            Div2WheelsOn text,
                            Div2TotalGTime text,
                            Div2LongestGTime text,
                            Div2WheelsOff text,
                            Div2TailNum text,
                            Div3Airport text,
                            Div3AirportID integer,
                            Div3AirportSeqID integer,
                            Div3WheelsOn text,
                            Div3TotalGTime text,
                            Div3LongestGTime text,
                            Div3WheelsOff text,
                            Div3TailNum text,
                            Div4Airport text,
                            Div4AirportID integer,
                            Div4AirportSeqID integer,
                            Div4WheelsOn text,
                            Div4TotalGTime text,
                            Div4LongestGTime text,
                            Div4WheelsOff text,
                            Div4TailNum text,
                            Div5Airport text,
                            Div5AirportID integer,
                            Div5AirportSeqID integer,
                            Div5WheelsOn text,
                            Div5TotalGTime text,
                            Div5LongestGTime text,
                            Div5WheelsOff text,
                            Div5TailNum text
                        )''')
        self.cursor.execute(f"TRUNCATE TABLE {self.tableName}")

    # v1
    def insert_data(self, dataset):
        query = f"INSERT INTO {self.tableName} VALUES %s"
        execute_values(self.cursor, query, dataset)

    # v2 - для проверки есть ли разница в скорости добавлять весь датасет или лучше разбить на части
    def insert_data2(self, dataset):
        query = f"INSERT INTO {self.tableName} VALUES %s"

        for i in range(1, math.ceil(len(dataset) / 10000) + 1):
            print("pg insert {} of {}".format(str(i * 10000), len(dataset)))
            execute_values(self.cursor, query, dataset[(i - 1) * 10000:i * 10000])

    def create_and_insert(self, dataset):
        self.create_table()
        self.insert_data(dataset)

    def create_and_insert2(self, dataset):
        self.create_table()
        self.insert_data2(dataset)

    def close_connect(self):
        self.cursor.close()
        self.connection.close()
