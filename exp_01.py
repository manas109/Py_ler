# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:46:59 2021

@author: Manaswini Raghavan
"""


"""There exists a staircase with N steps, and you can climb up either 1 or
   2 steps at a time.

Given N, write a function that returns the number of unique
 ways you can climb the staircase.The order of the steps matters."""
import time 

 
 
def fibonacci(n):
    if n <= 1:
        return 1 
    return fibonacci(n - 1) + fibonacci(n - 2)
st = time.time()
print(fibonacci(40))
et=time.time()
print(f"{et-st} time taken")


c = dict()
def fibonacci(n):
    if n <= 1:
        return 1 
    if n in c.keys():
        return c[n]
    c[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return c[n]
st = time.time()
print(fibonacci(40))
et=time.time()
print(f"{et-st} time taken")


def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)
staircase(4,[1,3,5])


def fibonacci(n):
     a, b = 1, 2
     for _ in range(n - 1):
         a, b = b, a + b
     return a
fibonacci(3)

"""
 Python automatically stores the value of the last 
 expression in the interpreter to a particular variable 
 called "_." You can also assign these value to another variable if you want.
 """
 """
 Given a list of numbers and a number k, return whether any two numbers from 
 the list add up to k.

 For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""

 def two_sum(lst, k):
     for i in range(len(lst)):
         for j in range(len(lst)):
             if i != j and lst[i] + lst[j] == k:
                 return True
     return False
 two_sum([10,15,3,7],20)

"""Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in 
the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
 would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
 the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? """


"""
Given the root to a binary tree, implement serialize(root),
 which serializes the tree into a string, and deserialize(s), 
 which deserializes the string back into the tree.
"""
def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

"""
Given an array of integers, find the first missing positive integer 
in linear time and constant space. In other words, find the lowest 
positive integer that does not exist in the array. The array can 
contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
should give 3.
"""
def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i
first_missing_positive([1, 2, 0])

"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns 
the first and last element of that pair. For example, car(cons(3, 4)) 
returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
cons(1,2)
def car(pair):
    return pair(lambda a, b: a)
car()
def cdr(pair):
    return pair(lambda a, b: b)
cdr()

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be 
decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001'
is not allowed.
"""

"""
A unival tree (which stands for "universal value") is a tree where all 
nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
"""
Given a list of integers, write a function that returns the largest sum 
of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""
"""
implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
"""
import threading
from time import sleep

class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            sleep(n / 1000)
            f()
        t = threading.Thread(target=sleep_then_call)
        t.start()
"""
Implement an autocomplete system. That is, given a query string s and a set 
of all possible query strings, return all strings in the set that have s 
as a prefix.

For example, given the query string de and the set of strings 
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient 
data structure to speed up queries.
""" 
""" 
Given an integer k and a string s, find the length of the longest 
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with 
k distinct characters is "bcb". 
"""
 
 
 
 