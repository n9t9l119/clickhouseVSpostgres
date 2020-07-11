import csv
import glob

from datetime import datetime


def to_int(str_):
    if str_ == '' or str_ is None:
        return 0
    return int(str_)


def to_float(str_):
    if str_ == '' or str_ is None:
        return 0
    return float(str_)


def to_date(str_):
    return datetime.strptime(str_, "%Y-%m-%d").date()


converters = {
    'Year': to_int,
    'Quarter': to_int,
    'Month': to_int,
    'DayofMonth': to_int,
    'DayOfWeek': to_int,
    'FlightDate': to_date,
    'DOT_ID_Reporting_Airline': to_int,
    'OriginAirportID': to_int,
    'OriginAirportSeqID': to_int,
    'OriginCityMarketID': to_int,
    'OriginWac': to_int,
    'DestAirportID': to_int,
    'DestAirportSeqID': to_int,
    'DestCityMarketID': to_int,
    'DestWac': to_int,
    'CRSDepTime': to_int,
    'DepTime': to_int,
    'DepDelay': to_float,
    'DepDelayMinutes': to_float,
    'DepDel15': to_float,
    'TaxiOut': to_float,
    'WheelsOff': to_int,
    'WheelsOn': to_int,
    'TaxiIn': to_float,
    'CRSArrTime': to_int,
    'ArrTime': to_int,
    'ArrDelay': to_float,
    'ArrDelayMinutes': to_float,
    'ArrDel15': to_float,
    'ArrivalDelayGroups': to_int,
    'Cancelled': to_float,
    'Diverted': to_float,
    'CRSElapsedTime': to_float,
    'ActualElapsedTime': to_float,
    'AirTime': to_float,
    'Flights': to_float,
    'Distance': to_float,
    'DistanceGroup': to_float,
    'CarrierDelay': to_float,
    'WeatherDelay': to_float,
    'NASDelay': to_float,
    'SecurityDelay': to_float,
    'LateAircraftDelay': to_float,
    'Div1AirportID': to_int,
    'Div1AirportSeqID': to_int,
    'Div2AirportID': to_int,
    'Div2AirportSeqID': to_int,
    'Div3AirportID': to_int,
    'Div3AirportSeqID': to_int,
    'Div4AirportID': to_int,
    'Div4AirportSeqID': to_int,
    'Div5AirportID': to_int,
    'Div5AirportSeqID': to_int}


def get_csv_files():
    for file in glob.glob("csv\\On_Time_Reporting_Carrier_On_Time_Performance_*.csv"):
        yield file


def read_dataset(file):
    data_rows = []
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            row_lst = []

            for k, v in row.items():
                if k in converters:
                    row_lst.append(converters[k](v))
                elif k != '':
                    row_lst.append(v)

            data_rows.append(row_lst)
    return data_rows
