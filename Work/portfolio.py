import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                stock_cost = float(row[2])
                shares = int(row[1])
                total_cost = total_cost + stock_cost * shares
            except ValueError:
                print("error parsing line", row)
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)