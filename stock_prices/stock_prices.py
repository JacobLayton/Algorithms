#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max_profit = -20
    index = 0
    for i in prices:
        index += 1
        for k in prices[index:]:
            profit = k - i
            if profit > max_profit:
                max_profit = profit
    return max_profit

# def find_max_profit(prices):
#     max_profit = 0
#     l = len(prices)
#     for i in prices:
#         for k in prices[i + 1:]:
#             profit = prices[i] - prices[k]
#             if profit > max_profit:
#                 max_profit = profit
#                 print(max_profit)
#     return max_profit


if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))