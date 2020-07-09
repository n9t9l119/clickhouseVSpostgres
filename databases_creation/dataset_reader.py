import csv, glob
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


to_int_indexes = [0, 1, 2, 3, 4, 7, 11, 12, 13, 19, 20, 21, 22, 28, 29, 30, 37, 38, 40, 41, 45, 70, 71, 78, 79, 86, 87,
                  94, 95, 102, 103]
to_float_indexes = [31, 32, 33, 36, 39, 42, 43, 44, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
to_date_indexes = [5]

converters = {
    'Year': to_int,
    'Quarter': to_int,
    'Month': to_int,
    'DayofMonth': to_int,
    'DayOfWeek': to_int,
    'FlightDate': to_date,
    'Reporting_Airline': lambda x: x,
    'DOT_ID_Reporting_Airline': to_int,
    'IATA_CODE_Reporting_Airline': lambda x: x,
    'Tail_Number': lambda x: x,
    'Flight_Number_Reporting_Airline': lambda x: x,
    'OriginAirportID': to_int,
    'OriginAirportSeqID': to_int,
    'OriginCityMarketID': to_int,
    'Origin': lambda x: x,
    'OriginCityName': lambda x: x,
    'OriginState': lambda x: x,
    'OriginStateFips': lambda x: x,
    'OriginStateName': lambda x: x,
    'OriginWac': to_int,
    'DestAirportID': to_int,
    'DestAirportSeqID': to_int,
    'DestCityMarketID': to_int,
    'Dest': lambda x: x,
    'DestCityName': lambda x: x,
    'DestState': lambda x: x,
    'DestStateFips': lambda x: x,
    'DestStateName': lambda x: x,
    'DestWac': to_int,
    'CRSDepTime': to_int,
    'DepTime': to_int,
    'DepDelay': to_float,
    'DepDelayMinutes': to_float,
    'DepDel15': to_float,
    'DepartureDelayGroups': lambda x: x,
    'DepTimeBlk': lambda x: x,
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
    'ArrTimeBlk': lambda x: x,
    'Cancelled': to_float,
    'CancellationCode': lambda x: x,
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
    'FirstDepTime': lambda x: x,
    'TotalAddGTime': lambda x: x,
    'LongestAddGTime': lambda x: x,
    'DivAirportLandings': lambda x: x,
    'DivReachedDest': lambda x: x,
    'DivActualElapsedTime': lambda x: x,
    'DivArrDelay': lambda x: x,
    'DivDistance': lambda x: x,
    'Div1Airport': lambda x: x,
    'Div1AirportID': to_int,
    'Div1AirportSeqID': to_int,
    'Div1WheelsOn': lambda x: x,
    'Div1TotalGTime': lambda x: x,
    'Div1LongestGTime': lambda x: x,
    'Div1WheelsOff': lambda x: x,
    'Div1TailNum': lambda x: x,
    'Div2Airport': lambda x: x,
    'Div2AirportID': to_int,
    'Div2AirportSeqID': to_int,
    'Div2WheelsOn': lambda x: x,
    'Div2TotalGTime': lambda x: x,
    'Div2LongestGTime': lambda x: x,
    'Div2WheelsOff': lambda x: x,
    'Div2TailNum': lambda x: x,
    'Div3Airport': lambda x: x,
    'Div3AirportID': to_int,
    'Div3AirportSeqID': to_int,
    'Div3WheelsOn': lambda x: x,
    'Div3TotalGTime': lambda x: x,
    'Div3LongestGTime': lambda x: x,
    'Div3WheelsOff': lambda x: x,
    'Div3TailNum': lambda x: x,
    'Div4Airport': lambda x: x,
    'Div4AirportID': to_int,
    'Div4AirportSeqID': to_int,
    'Div4WheelsOn': lambda x: x,
    'Div4TotalGTime': lambda x: x,
    'Div4LongestGTime': lambda x: x,
    'Div4WheelsOff': lambda x: x,
    'Div4TailNum': lambda x: x,
    'Div5Airport': lambda x: x,
    'Div5AirportID': to_int,
    'Div5AirportSeqID': to_int,
    'Div5WheelsOn': lambda x: x,
    'Div5TotalGTime': lambda x: x,
    'Div5LongestGTime': lambda x: x,
    'Div5WheelsOff': lambda x: x,
    'Div5TailNum': lambda x: x}

converters2 = {
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
    for file in glob.glob("..\On_Time_Reporting_Carrier_On_Time_Performance_*.csv"):
        yield file


limit = 10000


# v1 - использовать списки индексов, которые нужно ковертировать в нужный тип
def read_dataset():
    data_rows = []
    for file in get_csv_files():
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Пропускать строку с заголовками
                if csv_reader.line_num == 1:
                    continue

                # Заплатка, чтобы ограничить датасет на Х строк
                if csv_reader.line_num == limit + 2:
                    break

                row_lst = []

                for i in range(0, len(row) - 1):
                    if i in to_int_indexes:
                        row_lst.append(to_int(row[i]))
                    elif i in to_float_indexes:
                        row_lst.append(to_float(row[i]))
                    elif i in to_date_indexes:
                        row_lst.append(to_date(row[i]))
                    else:
                        row_lst.append(row[i])

                data_rows.append(row_lst)

                if csv_reader.line_num % 10000 == 0:
                    print(csv_reader.line_num)

    return data_rows


# v2 словарь "имя столбца- функция конвертации"
def read_dataset2():
    data_rows = []
    for file in get_csv_files():
        with open(file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_rows = []
            for row in csv_reader:
                if csv_reader.line_num == limit + 2:
                    break

                row_lst = []

                for k, v in converters.items():
                    row_lst.append(v(row[k]))

                data_rows.append(row_lst)

                if csv_reader.line_num % 10000 == 0:
                    print(csv_reader.line_num)
    return data_rows


# v2 словарь "имя столбца- функция конвертации", но без стобцов, где должен быть str
def read_dataset3():
    data_rows = []
    for file in get_csv_files():
        with open(file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_rows = []
            for row in csv_reader:
                if csv_reader.line_num == limit + 2:
                    break

                row_lst = []

                for k, v in row.items():
                    if k in converters2:
                        row_lst.append(converters[k](v))
                    elif k != '':
                        row_lst.append(v)

                data_rows.append(row_lst)

                if csv_reader.line_num % 10000 == 0:
                    print(csv_reader.line_num)
    return data_rows


def test_data_types():
    with open('On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2017_6.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            for i in row:
                print(type(i))
