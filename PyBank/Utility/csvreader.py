import csv


def read_csv_to_list(file_path, csv_delimiter = ','):
    # reads csv file and returns a list of dictionaries with the key values set to header rows

    csv_list = list()

    with open(file_path) as file:
        csv_list.append([
            {key: value for key, value in row.items()} 
            for row in csv.DictReader(
                file, 
                delimiter = csv_delimiter, 
                skipinitialspace = True)
                ])

    return csv_list
