#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max_profit = prices[1] - prices[0]
    cheapest = prices[0]
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - cheapest)
        cheapest = min(cheapest, prices[i])
        
    return max_profit
   



if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))