#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]
print('fibonacci(1, 6): ', fibonacci(1, 6))

def sort_to_max(origin_list):
    if len(origin_list) > 1:
        index = len(origin_list) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(origin_list):
            if i != index:
                if val < origin_list[index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        sort_to_max(smaller_items)
        sort_to_max(larger_items)
        origin_list[:] = smaller_items + [origin_list[index]] + larger_items

    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

def filter_func(function, iterable):
    return (item for item in iterable if function(item))

print(list(filter_func(lambda x: True if x % 2 == 0 else False,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
