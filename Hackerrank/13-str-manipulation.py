'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.
Sample Input
chris alan

Sample Output
Chris Alan
You can use str.title() but will not work in one test case - abc 12g for title o/p - Abc 12G but we want Abc 12g
'''
# Complete the solve function below.
def solve(s):
    for el in s.split():
        s = s.replace(el,el.capitalize()) 
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)