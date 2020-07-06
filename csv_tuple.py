import csv


def create_csv_tuple():
    with open('On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2017_6.csv') as csv_file:
        csv_table = csv.reader(csv_file)
        csv_tuple = list(csv_table)
        # for row in csv_tuple:
        #     print(row)
        return csv_tuple
