import csv

def import_data(csv_file):
    """Import a *.csv-file as a python list, where each line is a list of its own.
    
    Keyword arguments:
    csv_file -> the location of the *.csv-file
    """

    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            tab1, tab2 = []
            for r in reader:
                tab1.append(r[0])
                tab2.append(r[1])
        return tab1,tab2
    except FileNotFoundError:
        print("ERROR: The program called a file that did not exist: {} does not appear to exist.".format(csv_file))
        return []

def save(table,csv_file):
    """Save a table in a *.csv-file. Overwrites the file if the file already exists.
    Given the way your thermostat csv-files look, don't use this one. Ask for the function if needed.
    
    Keyword arguments:
    table -> the list to be saved
    csv_file -> the file to write the list to
    """

    # write it
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(r) for r in table]
    return True
