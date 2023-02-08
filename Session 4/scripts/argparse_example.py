#!/usr/bin/python3

# import the argparse module
import argparse

# creating the parser
parser = argparse.ArgumentParser(description='Argparse example')

# add a command-line argument
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='integers to sum up')

# adds a command-line argument which triggers the summations of the previous integers
parser.add_argument('--sum', dest='sum', action='store_const',
                   const=sum, default=max,
                   help='sums the integers')

# invoke parsing (processing) of the arguments
args = parser.parse_args()

# the processed arguments are stored as attributes in the argparse object !
# attributes of object are accessed using the dot-operator.
print("Content of args.integers:")
print(args.integers)
print("Result of argument processing:")
print(args.sum(args.integers))
