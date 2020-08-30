from time import time

from problem_two.generate_csv import create_csv_file

if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))

    start = time()

    elapsed = time() - start
    print('got totals time: {}'.format(elapsed))
