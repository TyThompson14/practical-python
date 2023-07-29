# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
                portfolio.append(holding)
            except ValueError:
                print("error parsing line", row)

    return portfolio
    

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("error parsing line", row)
    return prices

def get_report():
    report = []
    prices = read_prices('Data/prices.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    for row in portfolio:
        init_price = float(row['price'])
        cur_price = float(prices[row['name']])
        shares = int(row['shares'])
        total_init_val = round(init_price * shares, 4)
        total_cur_val = round(cur_price * shares,4)

        stock = {
            'name': row['name'],
            'init_price': init_price,
            'cur_price': cur_price,
            'shares': shares,
            'total_init_val': total_init_val,
            'total_cur_val': total_cur_val,
            'gain/loss': total_cur_val - total_init_val,
        }
        report.append(stock)
    return report

def make_report():
    report = []
    prices = read_prices('Data/prices.csv')
    portfolio = read_portfolio('Data/portfolio.csv')

    for row in portfolio:
        init_price = float(row['price'])
        cur_price = float(prices[row['name']])
        shares = int(row['shares'])

        stock = (
            row['name'],
            shares,
            cur_price,
            cur_price - init_price
        )
        report.append(stock)
    return report


report = make_report()

for name,shares,price,change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
