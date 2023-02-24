#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
# Github profile https://github.com/fred874

# Question A

# length, 𝐿
# load intensity, w
L = 12
w = 10

# x1 represents when x = 0
x1 = 0

# x2 represents when x = l
x = L

# bm1 is bending moment when x = 0
bm1 = w * (-6 * x1 ** 2 + 6 * L * x1 + (- L) ** 2) / 12

# bm2 is bending moment when x = L
bm2 = w * (-6 * x ** 2 + 6 * L * x + (- L) ** 2) / 12

# V1 represents shear force at x = 0
V1 = w * ((L / 2) - x)

# V2 represents shear force at x = L
V2 = w * ((L / 2) - x1)

print(
    f'bending moment at x = 0 is {bm1}\n bending moment at x = L is {bm2}\n'
    f'shear force at x = 0 is {V1}\nbending moment at x = L is {V2}')


# Question B
"""When M = 0 we get the expression -1/2*wx**2 + 1/2wLx - 1/12*wL**2 = 0"""

a = -1 / 2 * w
b = 1 / 2 * w * L
c = w * L ** 2

# using the almighty formulae the two roots are
discriminant = b ** 2 - 4 * a * c

# first root
root1 = (-b + np.sqrt(discriminant)) / 2 * a

# second root
root2 = (-b - np.sqrt(discriminant)) / 2 * a
print(f'the points of contra-flexure are {root1, root2}')


# Question C
""""when shear force v = 0"""
sf0 = L / 2

print(f"Shear force V = 0 when x = {sf0}")


# Question D and E
steps = 0.01

# array for bending moment at each step
new_list_bm = []

# array for shear force at each step
new_list_sf = []

for i in range(0, L-1):
    steps = steps + 0.01
    # bending moment at each step
    bms = w * (-6 * steps ** 2 + 6 * L * steps + (- L) ** 2) / 12

    # shear for at each step
    sfs = w * ((L / 2) - steps)

    values1 = new_list_bm.append(bms)
    values2 = new_list_sf.append(sfs)

    # bending moment array
    bma = np.array(bms)

    # shear force array
    sfa = np.array(sfs)

print(new_list_bm)
print(new_list_sf)


# Question F
"""finding point along L at which the absolute value in the array in d is minimum"""
min_bm = min(new_list_bm)
print(f"The point along L where the bendding moment is minimum is {min_bm}")


# Question G
"""the relative errors between the points of contra-flexure in b and f """
bf_error1 = root1 - min_bm
bf_error2 = root2 - min_bm

print(f'the relative errors between the point of contra-flexure in b and f is {bf_error2} and {bf_error1}')


# Question H
"""finding the point at which max and min bending moments occur"""
max_bm = max(new_list_bm)
print(f'the maximum bending moment occurs at {max_bm}\nthe minimum bending moment occurs at {min_bm}')