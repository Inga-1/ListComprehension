# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:36:50 2024

@author: Inga
"""

#Given a list of numbers, remove all odd numbers from the list:
def removeOdds(numbers):
    return [x for x in numbers if x %2 == 0]
numbers = [3,5,45,97,32,22,10,19,39,43]

#Given a list of numbers, remove floats (numbers with decimals)
def removeFloats(numbers):
    return [onlyInt for onlyInt in numbers if type(onlyInt) == int]


#Find all of the numbers from 1-1000 that are divisible by 7

def divby7():
    return [x for x in range(1,1001) if x % 7 == 0]

#Produce a list of tuples consisting of only the matching numbers in 2 lists 
def generateTuples(listA, listB):
    return [(a,a) for a in listA if a in listB]

#Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)
def divisionTest():
    return [x for x in range(1, 1001) if 0 in [x%i for i in range(2,10)]]

#Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
def randomList():
    return [x for x in range(1200, 2001, 130)]


#Flatten List: Given a list of lists, flatten it into a single list using list comprehension.
def flatten(nest):
    return [item for nestItem in nest for item in nestItem ]
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

#Doubled Values: Given a list of numbers, create a new list where each number is doubled using list comprehension.
def doubleVals(lista):
    return [item*2 for item in lista]

#Double Elements: Given a list of elements, create a new list where each element is present twice using list comprehension 
def doubleElems(lista):
    return [item for item in lista for n in range(2)]

#Creating a list of Tuples from two separate Lists (creating tuples with every single possible pairing)
def createTuples(lista1, lista2):
    return [(x, y) for x in lista1 for y in lista2]

#Creating a list of Tuples from two separate Lists (matching each element to the one in the same position in the other one)
def createTuples(lista1, lista2):
    return [(x, y) for x, y in zip(lista1, lista2)]

#return a list containing the numbers of the given list cubed 
def cube(lista):
    return [x**3 for x in lista]

#-------------------MATRICES------------------------------------
#Find the transpose of a matrix 
def transposeOfMatrix(matrix):
    return [[i[j] for i in matrix] for j in range(len(matrix[0]))]

#Rotate to the matrix opposite to clockwise direction
def reverseMatrix(matrix):
    return [[i[j] for i in matrix] for j in range(len(matrix[0])-1, -1, -1)]


matrix = [[10, 20, 30], 
              [40, 50, 60], 
              [70, 80, 90]]
print((reverseMatrix(matrix)))

