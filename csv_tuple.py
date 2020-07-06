import csv
from datetime import datetime

converters = {
    'Year': int,
    'Quarter': int,
    'Month': int,
    'DayofMonth': int,
    'DayOfWeek': int,
    'FlightDate': str,
    'UniqueCarrier': str,
    'AirlineID': int,
    'Carrier': str,
    'TailNum': str,
    'FlightNum': str,
    'OriginAirportID': int,
    'OriginAirportSeqID': int,
    'OriginCityMarketID': int,
    'Origin': str,
    'OriginCityName': str,
    'OriginState': str,
    'OriginStateFips': str,
    'OriginStateName': str,
    'OriginWac': int,
    'DestAirportID': int,
    'DestAirportSeqID': int,
    'DestCityMarketID': int,
    'Dest': str,
    'DestCityName': str,
    'DestState': str,
    'DestStateFips': str,
    'DestStateName': str,
    'DestWac': int,
    'CRSDepTime': int,
    'DepTime': int,
    'DepDelay': int,
    'DepDelayMinutes': int,
    'DepDel15': int,
    'DepartureDelayGroups': str,
    'DepTimeBlk': str,
    'TaxiOut': int,
    'WheelsOff': int,
    'WheelsOn': int,
    'TaxiIn': int,
    'CRSArrTime': int,
    'ArrTime': int,
    'ArrDelay': int,
    'ArrDelayMinutes': int,
    'ArrDel15': int,
    'ArrivalDelayGroups': int,
    'ArrTimeBlk': str,
    'Cancelled': int,
    'CancellationCode': str,
    'Diverted': int,
    'CRSElapsedTime': int,
    'ActualElapsedTime': int,
    'AirTime': int,
    'Flights': int,
    'Distance': int,
    'DistanceGroup': int,
    'CarrierDelay': int,
    'WeatherDelay': int,
    'NASDelay': int,
    'SecurityDelay': int,
    'LateAircraftDelay': int,
    'FirstDepTime': str,
    'TotalAddGTime': str,
    'LongestAddGTime': str,
    'DivAirportLandings': str,
    'DivReachedDest': str,
    'DivActualElapsedTime': str,
    'DivArrDelay': str,
    'DivDistance': str,
    'Div1Airport': str,
    'Div1AirportID': int,
    'Div1AirportSeqID': int,
    'Div1WheelsOn': str,
    'Div1TotalGTime': str,
    'Div1LongestGTime': str,
    'Div1WheelsOff': str,
    'Div1TailNum': str,
    'Div2Airport': str,
    'Div2AirportID': int,
    'Div2AirportSeqID': int,
    'Div2WheelsOn': str,
    'Div2TotalGTime': str,
    'Div2LongestGTime': str,
    'Div2WheelsOff': str,
    'Div2TailNum': str,
    'Div3Airport': str,
    'Div3AirportID': int,
    'Div3AirportSeqID': int,
    'Div3WheelsOn': str,
    'Div3TotalGTime': str,
    'Div3LongestGTime': str,
    'Div3WheelsOff': str,
    'Div3TailNum': str,
    'Div4Airport': str,
    'Div4AirportID': int,
    'Div4AirportSeqID': int,
    'Div4WheelsOn': str,
    'Div4TotalGTime': str,
    'Div4LongestGTime': str,
    'Div4WheelsOff': str,
    'Div4TailNum': str,
    'Div5Airport': str,
    'Div5AirportID': int,
    'Div5AirportSeqID': int,
    'Div5WheelsOn': str,
    'Div5TotalGTime': str,
    'Div5LongestGTime': str,
    'Div5WheelsOff': str,
    'Div5TailNum': str,
    'What': str}


def create_csv_tuple():
    with open('On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2017_6.csv') as csv_file:
        csv_table = csv.reader(csv_file)
        csv_tuple = list(csv_table)
        for line in csv_tuple:
            line = line[0].split(',')
            print(line)
            for i, type in enumerate(converters):
                if line[i] != "":
                    line[i] = converters[type](line[i])
                print(line[i])
        return csv_tuple


def test_data_types():
    with open('On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2017_6.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            for i in row:
                print(type(i))


create_csv_tuple()

