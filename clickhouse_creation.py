from clickhouse_driver import Client

class ClickHouse:
    tableName = 'benchmark3'

    def __init__(self):
        self.client = Client(host='localhost')


    def create_table(self):
        self.client.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName}
                            (Year Int16,
                            Quarter Int16,
                            Month Int16,
                            DayofMonth Int16,
                            DayOfWeek Int16,
                            FlightDate date,
                            UniqueCarrier FixedString(7),
                            AirlineID Int32,
                            Carrier FixedString(2),
                            TailNum String,
                            FlightNum String,
                            OriginAirportID Int32,
                            OriginAirportSeqID Int32,
                            OriginCityMarketID Int32,
                            Origin FixedString(5),
                            OriginCityName String,
                            OriginState FixedString(2),
                            OriginStateFips String,
                            OriginStateName String,
                            OriginWac Int32,
                            DestAirportID Int32,
                            DestAirportSeqID Int32,
                            DestCityMarketID Int32,
                            Dest FixedString(5),
                            DestCityName String,
                            DestState FixedString(2),
                            DestStateFips String,
                            DestStateName String,
                            DestWac Int32,
                            CRSDepTime Int32,
                            DepTime Int32,
                            DepDelay Float32,
                            DepDelayMinutes Float32,
                            DepDel15 Float32,
                            DepartureDelayGroups String,
                            DepTimeBlk String,
                            TaxiOut Float32,
                            WheelsOff Int32,
                            WheelsOn Int32,
                            TaxiIn Float32,
                            CRSArrTime Int32,
                            ArrTime Int32,
                            ArrDelay Float32,
                            ArrDelayMinutes Float32,
                            ArrDel15 Float32,
                            ArrivalDelayGroups Int32,
                            ArrTimeBlk String,
                            Cancelled Float32,
                            CancellationCode FixedString(1),
                            Diverted Float32,
                            CRSElapsedTime Float32,
                            ActualElapsedTime Float32,
                            AirTime Float32,
                            Flights Float32,
                            Distance Float32,
                            DistanceGroup Float32,
                            CarrierDelay Float32,
                            WeatherDelay Float32,
                            NASDelay Float32,
                            SecurityDelay Float32,
                            LateAircraftDelay Float32,
                            FirstDepTime String,
                            TotalAddGTime String,
                            LongestAddGTime String,
                            DivAirportLandings String,
                            DivReachedDest String,
                            DivActualElapsedTime String,
                            DivArrDelay String,
                            DivDistance String,
                            Div1Airport String,
                            Div1AirportID Int32,
                            Div1AirportSeqID Int32,
                            Div1WheelsOn String,
                            Div1TotalGTime String,
                            Div1LongestGTime String,
                            Div1WheelsOff String,
                            Div1TailNum String,
                            Div2Airport String,
                            Div2AirportID Int32,
                            Div2AirportSeqID Int32,
                            Div2WheelsOn String,
                            Div2TotalGTime String,
                            Div2LongestGTime String,
                            Div2WheelsOff String,
                            Div2TailNum String,
                            Div3Airport String,
                            Div3AirportID Int32,
                            Div3AirportSeqID Int32,
                            Div3WheelsOn String,
                            Div3TotalGTime String,
                            Div3LongestGTime String,
                            Div3WheelsOff String,
                            Div3TailNum String,
                            Div4Airport String,
                            Div4AirportID Int32,
                            Div4AirportSeqID Int32,
                            Div4WheelsOn String,
                            Div4TotalGTime String,
                            Div4LongestGTime String,
                            Div4WheelsOff String,
                            Div4TailNum String,
                            Div5Airport String,
                            Div5AirportID Int32,
                            Div5AirportSeqID Int32,
                            Div5WheelsOn String,
                            Div5TotalGTime String,
                            Div5LongestGTime String,
                            Div5WheelsOff String,
                            Div5TailNum String
                            )Engine=Log()''')
        self.client.execute(f"TRUNCATE TABLE {self.tableName}")


    def insert_data(self, dataset):
        self.client.execute(f"INSERT INTO {self.tableName} VALUES", dataset)


    def create_and_insert(self, dataset):
        self.create_table()
        self.insert_data(dataset)

    def close_connect(self):
        self.client.disconnect()
