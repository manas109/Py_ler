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
def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):


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
from collections import defaultdict

def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1 # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]

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
def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself
# a unival subtree.
def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False

"""
Given a list of integers, write a function that returns the largest sum 
of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""
def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last= max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)


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

### other code

from time import sleep
import threading

class Scheduler:
    def __init__(self):
        self.fns = [] # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))
        

self.poll()
self.delay()
"""
Implement an autocomplete system. That is, given a query string s and a set 
of all possible query strings, return all strings in the set that have s 
as a prefix.

For example, given the query string de and the set of strings 
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient 
data structure to speed up queries.
""" 
ENDS_HERE = '__ENDS_HERE'

class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

trie = Trie()
for word in words:
    trie.insert(word)

def autocomplete(s):
    suffixes = trie.elements(s)
    return [s + w for w in suffixes]


""" 13
Given an integer k and a string s, find the length of the longest 
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with 
k distinct characters is "bcb". 
"""
def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0

    # Keep a running window
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0] # lower bound remains the same
        else:
            # otherwise, pop last occurring char
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length
 """
14
The area of a circle is defined as πr^2. Estimate π to 3 
decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2. 
 """
 from random import uniform
from math import pow

def generate():
    return (uniform(-1, 1), uniform(-1, 1))

def is_in_circle(coords):
    return coords[0] * coords[0] + coords[1] * coords[1] < 1

def estimate():
    iterations = 10000000
    in_circle = 0
    for _ in range(iterations):
        if is_in_circle(generate()):
            in_circle += 1
    pi_over_four = in_circle / iterations
    return pi_over_four * 4
"""
Given a stream of elements too large to store in memory, pick 
a random element from the stream with uniform probability.
"""
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

"""16
You run an e-commerce website and want to record the last N order 
ids in a log. Implement a data structure to accomplish this, with the 
following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed 
to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
 class Log(object):
    def __init__(self, n):
        self.n = n
        self._log = []
        self._cur = 0

    def record(self, order_id):
        if len(self._log) == self.n:
            self._log[self._cur] = order_id
        else:
            self._log.append(order_id)
        self._cur = (self._cur + 1) % self.n

    def get_last(self, i):
        return self._log[self._cur - i]
    
"""
17 skip
"""
"""
18
Given an array of integers and a number k, where 1 <= k <= 
length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should 
get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
"""
from collections import deque

def max_of_subarrays(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their corresponding values are in descending order.
    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])

"""
19
A builder is looking to build a row of N houses that can be of K different 
colors. He has a goal of minimizing cost while ensuring that no two neighboring
 houses are of the same color.

Given an N by K matrix where the nth row and kth column represents 
the cost to build the nth house with kth color, return the minimum 
cost which achieves this goal.
"""
from math import inf

def build_houses(matrix):
    lowest_cost, lowest_cost_index = 0, -1
    second_lowest_cost = 0

    for r, row in enumerate(matrix):
        new_lowest_cost, new_lowest_cost_index = inf, -1
        new_second_lowest_cost = inf
        for c, val in enumerate(row):
            prev_lowest_cost = second_lowest_cost if c == lowest_cost_index else lowest_cost
            cost = prev_lowest_cost + val
            if cost < new_lowest_cost:
                new_second_lowest_cost = new_lowest_cost
                new_lowest_cost, new_lowest_cost_index = cost, c
            elif cost < new_second_lowest_cost:
                new_second_lowest_cost = cost
        lowest_cost = new_lowest_cost
        lowest_cost_index = new_lowest_cost_index
        second_lowest_cost = new_second_lowest_cost

    return lowest_cost
build_houses(2,2)

#20
"""
Given two singly linked lists that intersect at some point, find the intersecting node.
 The lists are non-cyclical.For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 
 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

def intersection(a, b):
    m, n = length(a), length(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in range(m - n):
            cur_a = cur_a.next
    else:
        for _ in range(n - m):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a

length(12)
intersection(2, 4)

#21
"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
def solution(n):
     time_counter = [0 for i in range(1441)]
     for i in n:
         time_counter[i[0]] += 1
         time_counter[i[1]] += -1
     rooms, tmp = 0, 0
     for i in time_counter:
         tmp += i
         if(tmp > rooms):
             rooms = tmp
     return rooms
 print solution([[30, 75], [0, 50], [60, 150]])
 print solution([[30, 75], [0, 50], [60, 150], [30, 75]])
 print solution([])
 print solution([[0, 60]])
#22
"""
Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
['bedbath', 'and', 'beyond'].
"""
#23
"""
You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you
 can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum
 number of steps required to reach the end coordinate from the start. If there 
 is no possible path, then return null. You can move up, left, down, and right. 
 You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum 
number of steps required to reach the end is 7, since we would need to go 
through (1, 2) because there is a wall everywhere else on the second row.
"""
#26
"""
Given a singly linked list and an integer k, remove the kth last element from 
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    slow, fast = head, head
    for i in range(k):
        fast = fast.next

    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
remove_kth_from_linked_list(head, 3)
print(head)

#27
"""
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
def balance(s):
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            # Check character is not unmatched
            if not stack:
                return False

            # Char is a closing bracket, check top of stack if it matches
            if (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()

    return len(stack) == 0
balance(34)

#29
"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single 
count and character. For example, the string "AAAABBBCCDAA" would be encoded as 
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be 
encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""
s='AAAABBBCCDAA'
def decode(s):
    count = 0
    result = ''
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            # char is alphabetic
            result += char * count
            count = 0
    return result
#30
"""
You are given an array of non-negative integers that represents a two-dimensional 
elevation map where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in 
the second, and 3 in the fourth index (we cannot hold 5 since it would run off to 
                                       the left), so we can trap 8 units of water.
"""

def capacity(arr):
    if not arr:
        return 0

    total = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for num in arr[1:max_i]:
        total += left_max - num
        left_max = max(left_max, num)

    right_max = arr[-1]
    for num in arr[-2:max_i:-1]:
        total += right_max - num
        right_max = max(right_max, num)

    return total