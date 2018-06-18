import csv

def import_data(csv_file):
    """Import a *.csv-file as a python list, where each line is a list of its own.
    
    Keyword arguments:
    csv_file -> the location of the *.csv-file
    """

    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            table = [[e for e in r] for r in reader]
        return table
    except FileNotFoundError:
        print("ERROR: The program called a file that did not exist: {} does not appear to exist.".format(csv_file))
        return []

# Writes a table to a given file, effectively overwriting its previous contents.
# Returns true if successful, false if unsuccessful.
def save(table,csv_file):
    """Save a table in a *.csv-file. Overwrites the file if the file already exists.
    
    Keyword arguments:
    table -> the list to be saved
    csv_file -> the file to write the list to
    """

    # write it
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(r) for r in table]
    return True
