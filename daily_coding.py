# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:32:30 2021

@author: Manaswini Raghavan
"""
#17

Given a list, sort it using this method: reverse(lst, i, j), 
which reverses lst from i to j.

#16
Gray code is a binary code where each successive value differ 
in only one bit, as well as when wrapping around. Gray code is 
common in hardware so that we don't see temporary spurious values 
during transitions.

Given a number of bits n, generate a possible gray code for it.
For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""
Gray Code:The reflected binary code (RBC), also known just as 
           reflected binary (RB) or Gray code.
           
 For example, the representation of the decimal value "1" in binary 
 would normally be "001" and "2" would be "010". In Gray code, these 
 values are represented as "001" and "011". That way, incrementing a 
 value from 1 to 2 requires only one bit to change, instead of two.
"""

def gray_code(n):
    if n == 0:
        return []
    elif n == 1:
        return [0, 1]

    prev_gray_code = gray_code(n - 1)

    result = []
    for code in prev_gray_code:
        result.append(code)

    for code in reversed(prev_gray_code):
        result.append((1 << n - 1) + code)

    return result

#day15

There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb 
the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

[1, 1, 1, 1]
[2, 1, 1]
[1, 2, 1]
[1, 1, 2]
[2, 2]
"""
What if, instead of being able to climb 1 or 2 steps at a time, you could climb= 
any number from a set of positive integers X? For example, if X = {1, 3, 5}, 
you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X
"""
def staircase(n):
    n = input("enter a value for n:")
    print(n)
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return staircase(n-1)+staircase(n-2)
  
def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

#14 hackathon

#printing the name uisng place holders 

name=input ('enter the name\n')
print('hello {0}'.format(name))


#13
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

def two_num(lst,k):
    k=input()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!=j and lst[i]+lst[j]==k:
                return True
            else:
                return False

#12
Given an array of integers, return a new array such that each 
element at index i of the new array is the product of all the 
numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected
 output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
 the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?



#11
serialize and deserialize :Serialization is to store tree in a file so 
  that it can be later restored. The structure of tree must 
  be maintained. Deserialization is reading tree back from file.
  
#12
A unival tree (which stands for "universal value") is a 
tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right
            
        
#11
Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.

import threading
"""
threading :n python is used to run multiple threads (tasks, function calls) 
             at the same time
"""
from time import sleep
"""
sleep(): The sleep() function suspends (waits) execution of the
          current thread for a given number of seconds.
"""

class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            sleep(n / 1000)
            f()
        t = threading.Thread(target=sleep_then_call)
        t.start()

#10
Implement an autocomplete system. That is, given 
a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings 
[dog, deer, deal], return [deer, deal].

WORDS = ['foo', 'bar', ...]
def autocomplete(s):
    results = set()
    for word in WORDS:
        if word.startswith(s):
            results.add(word)
    return results

#11
Given an integer k and a string s, find the length of the longest 
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring 
with k distinct characters is "bcb".:

#10
Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.

import random
"""
random:functions in Python that provide the ability to 
        generate random numbers. All of these functions 
        are present in the random module which can be 
        imported using import random.
"""
def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
"""
Instead, let’s attempt to solve using loop invariants. On the ith 
iteration of our loop to pick a random element, let’s assume we
 already picked an element uniformly from [0, i - 1]. In order to 
 maintain the loop invariant, we would need to pick the ith element 
 as the new random element at 1 / (i + 1) chance. For the base case
 where i = 0, let’s say the random element is the first one. 
 Then we know it works because

For i >= 0, before the loop began, any element 
K in [0, i - 1] had 1 / i chance of being chosen as the random element. 
We want K to have 1 / (i + 1) chance of being chosen after the iteration. 
This is the case since the chance of having being chosen already but not 
getting swapped with the ith element is 1 / i (1 - (1 / (i + 1))) 
which is 1 / i i / (i + 1) or 1 / (i + 1)
"""     
#09
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 
       1111 0000 1111 0000 1111 0000 1111 0000, 
return 0000 1111 0000 1111 0000 1111 0000 1111.

NUM_BITS = 32

def reverse_bits(n):
    reversed_num = 0
    for i in range(NUM_BITS):
        j = n >> i & 1
        reversed_num += j << (NUM_BITS - i - 1)
    return reversed_num\
        
#08
Given a string, return the first recurring character in it, 
or null if there is no recurring character.

For example, given the string "acbbac", return "b". 
Given the string "abcdef", return null.

def first_recurring(str):
    checker = 0
    for c in str:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return c
        checker |= (1 << val)
    return None

#07
Given a positive integer n, find the smallest number 
of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.

from math import inf

def num_squares_naive(n):
    if n == 0:
        return 0

    min_num_squares = inf

    i = 1
    while n - i*i >= 0:
        min_num_squares = min(min_num_squares, num_squares_naive(n - i*i) + 1)
        i += 1

    return min_num_squares

#06

Find an efficient algorithm to find the smallest distance 
(measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of 
"dog cat hello cat dog dog hello cat world", return 1 because there's 
only one word "cat" in between the two words.

def min_distance(text, word0, word1):
    text_words = [w.strip() for w in text.split(' ')]
    """
    strip(): method is used to return the copy of the string 
            in which all the characters have been stripped from the 
            beginning and the ending of the string.
            
    split(): method splits a string into a list.
 
    Enumerate(): method adds a counter to an iterable and returns 
                 it in a form of enumerating object. 
 
    """
    print text_words

    word0_indices = [i for i, w in enumerate(text_words) if w == word0]
    word1_indices = [i for i, w in enumerate(text_words) if w == word1]

    if not word0_indices or not word1_indices: # one of the words doesn't exist.
        return float('inf')

    i = j = 0

    min_distance = abs(word0_indices[i] - word1_indices[j])

    while i < len(word0_indices) and j < len(word1_indices):

        current_distance = abs(word0_indices[i] - word1_indices[j])
        min_distance = min(min_distance, current_distance)

        if word0_indices[i] < word1_indices[j]:
            i += 1
        else:
            j += 1
    return min_distance - 1 # Don't count the last step to get to word1

#05
Given a list of points, a central point, and an integer k, 
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], 
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].


mport math

def nearest_k_points(points, center, k):
    if len(points) <= k:
        return points

    pq = PriorityQueue()

    for point in points:
        if len(pq) < k:
            pq.push(point, distance(point, center))
        else:
            dist = distance(point, center)
            if dist < pq.peek()[1]:
                pq.pop()
                pq.push(point, dist)

    return [pq.pop()[0] for i in range(k)]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
