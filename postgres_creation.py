from psycopg2.extras import execute_values


# def create_table(pg_cursor):
#     pg_cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark
#                        ( id int,
#                         col1 text,
#                         col2 text,
#                         col3 text,
#                         col4 text,
#                         col5 text
#                       )''')

# Data types need to be edited
def create_table(pg_cursor):
    pg_cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark
                       (  Year int,
                          Quarter int,
                          Month int,
                          DayofMonth int,
                          DayOfWeek int,
                          FlightDate Date,
                          UniqueCarrier text,
                          AirlineID int,
                          Carrier text,
                          TailNum text,
                          FlightNum text,
                          OriginAirportID int,
                          OriginAirportSeqID int,
                          OriginCityMarketID int,
                          Origin text,
                          OriginCityName text,
                          OriginState text,
                          OriginStateFips text,
                          OriginStateName text,
                          OriginWac int,
                          DestAirportID int,
                          DestAirportSeqID int,
                          DestCityMarketID int,
                          Dest text,
                          DestCityName text,
                          DestState text,
                          DestStateFips text,
                          DestStateName text,
                          DestWac int,
                          CRSDepTime int,
                          DepTime int,
                          DepDelay int,
                          DepDelayMinutes int,
                          DepDel15 int,
                          DepartureDelayGroups text,
                          DepTimeBlk text,
                          TaxiOut int,
                          WheelsOff int,
                          WheelsOn int,
                          TaxiIn int,
                          CRSArrTime int,
                          ArrTime int,
                          ArrDelay int,
                          ArrDelayMinutes int,
                          ArrDel15 int,
                          ArrivalDelayGroups int,
                          ArrTimeBlk text,
                          Cancelled int,
                          CancellationCode text,
                          Diverted int,
                          CRSElapsedTime int,
                          ActualElapsedTime int,
                          AirTime int,
                          Flights int,
                          Distance int,
                          DistanceGroup int,
                          CarrierDelay int,
                          WeatherDelay int,
                          NASDelay int,
                          SecurityDelay int,
                          LateAircraftDelay int,
                          FirstDepTime text,
                          TotalAddGTime text,
                          LongestAddGTime text,
                          DivAirportLandings text,
                          DivReachedDest text,
                          DivActualElapsedTime text,
                          DivArrDelay text,
                          DivDistance text,
                          Div1Airport text,
                          Div1AirportID int,
                          Div1AirportSeqID int,
                          Div1WheelsOn text,
                          Div1TotalGTime text,
                          Div1LongestGTime text,
                          Div1WheelsOff text,
                          Div1TailNum text,
                          Div2Airport text,
                          Div2AirportID int,
                          Div2AirportSeqID int,
                          Div2WheelsOn text,
                          Div2TotalGTime text,
                          Div2LongestGTime text,
                          Div2WheelsOff text,
                          Div2TailNum text,
                          Div3Airport text,
                          Div3AirportID int,
                          Div3AirportSeqID int,
                          Div3WheelsOn text,
                          Div3TotalGTime text,
                          Div3LongestGTime text,
                          Div3WheelsOff text,
                          Div3TailNum text,
                          Div4Airport text,
                          Div4AirportID int,
                          Div4AirportSeqID int,
                          Div4WheelsOn text,
                          Div4TotalGTime text,
                          Div4LongestGTime text,
                          Div4WheelsOff text,
                          Div4TailNum text,
                          Div5Airport text,
                          Div5AirportID int,
                          Div5AirportSeqID int,
                          Div5WheelsOn text,
                          Div5TotalGTime text,
                          Div5LongestGTime text,
                          Div5WheelsOff text,
                          Div5TailNum text
                       )''')


def insert_data(pg_cursor, tuple_lst):
    for i in range(1, 11):
        print(i * 10000)
        # execute_values(pg_cursor, "INSERT INTO benchmark (id, col1, col2, col3, col4, col5) VALUES %s",
        #              tuple_lst[(i - 1) * 10000:i * 10000])
        pg_cursor.execute("INSERT INTO benchmark VALUES", tuple_lst[(i - 1) * 10000:i * 10000])


def post(pg_cursor, tuple_lst):
    create_table(pg_cursor)
    insert_data(pg_cursor, tuple_lst)

    # pg_cursor.execute('''SELECT t.id, Count(*)
    # FROM (SELECT id FROM benchmark) as t
    # GROUP BY t.id
    # HAVING Count(*) = 1''')
    #
    # pg_cursor.execute('''SELECT Count(*) FROM benchmark''')
    # pg_cursor.fetchall()
