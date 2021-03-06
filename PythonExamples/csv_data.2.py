import csv


def main():
    print('Inside of main...')
    try:
        process_data()
    except OSError as e:
        print('Could not process file because {}'.format(str(e)))

file = 'C:/users/litec/documents/sandbox/python/example.csv'

def read_file(csv_file):
    print('Reading file...')
    row_lists = []
    f = open(csv_file)
    csv_info = csv.reader(f)
    for row in csv_info:
        row_lists.append(row)
        #print(row)
    del row_lists[0]
    print('...read complete')
    f.close()
    return row_lists


def process_data():
    row_lists = read_file(file)
    print('Processing data...')
    user = ''
    info = []
    full_dict = {}
    counter = 0
    for item in row_lists:
        user = item[0]
        info = [item[1], item[2]]
        full_dict[counter] = {user: info}
        counter += 1
        #print(user)
        #print(info)
    #print(row_lists)
    print(full_dict)
    print('...processing complete')
    

def write_file(file):
    pass

if __name__ == '__main__':
    main()




