import os
import csv


def open_csv():
    while True:
        file1 = os.path.abspath(input(
            "Enter filename of original CSV (name is CaSe SeNsItIve): "))
        if os.path.exists(file1):
            with open(file1, 'r') as csv_file:
                read_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                f1 = list(read_file)
            break
        else:
            print("I'm sorry, that file does not exist. Try again.")
    while True:
        file2 = os.path.abspath(input(
            "Enter filename of CSV to compare against original (name is CaSe SeNsItIve): "))
        if os.path.exists(file2):
            with open(file2, 'r') as csv_file:
                read_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                f2 = list(read_file)
            break
        else:
            print("I'm sorry, that file does not exist. Try again.")
    return f1, f2


def compare_csv(f1, f2):
    print('..... comparing .....')
    changed = {'NEW ROWS'}
    deleted = {'MISSING ROWS'}
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(changed)
        for row in f2:
            if row not in f1:
                writer.writerow(row)
        writer.writerow(deleted)
        for row in f1:
            if row not in f2:
                writer.writerow(row)
    print('..... differences written to output.csv .....')


def print_header():
    print('\n')
    print('-' * 30)
    print('       CSV COMPARE TOOL')
    print('-' * 30, '\n')


def main():
    print_header()
    f1, f2 = open_csv()
    compare_csv(f1, f2)


if __name__ == '__main__':
    main()
