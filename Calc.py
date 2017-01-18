#!/usr/bin/python3
# Imports all the necessary modules
from __future__ import print_function
import os
import sys
import argparse
import time
# Defines basic mathmatics for the program to run
def add(x, y):
	"""This adds two numbers together"""
	return x + y

def subtract(x, y):
	"""This subtracts two different numbers"""
	return x - y

def divide(x, y):
	"""This divides two different numbers"""
	return x / y

def multiply(x, y):
	"""This multiplies two different numbers"""
	return x * y

def square(x):
	"""This squares a number"""
	return x*x
# actually starts the program. wow
print("How many hours did you work this week?")
# define number of hours
num1 = float(raw_input())
# do math with that number homie
print('Your income will be',(subtract((subtract(multiply(num1, 9), (multiply(multiply(num1, 9), 0.076492819)))), 95)),'in checking and 95 in savings.')
time.sleep(2)
print("Have a good day!")
exec("raise SystemExit")
