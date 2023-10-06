import pytest
import random
import math

from programs import factorial

def num_Test():
    for i in range(5):
       num = random.randint()
       assert factorial.fact(num) == math.factorial(num)

def input_Test(self):
    with self.assertRaises(ValueError):
        factorial.fact("hello")

def input_Test_Dos(self):
    with self.assertRaises(ValueError):
        factorial.fact(True)


