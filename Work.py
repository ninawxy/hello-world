#  File: Work.py

#  Description: solution using binary search

#  Student Name:  Xiaoying Wei

#  Student UT EID:  xw4483

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: July 23

#  Date Last Modified: July 23

def read_file ():
    workfile = open('work.txt').read().splitlines()
    data = []
    for lines in workfile:
        lines = lines.split()
        data.append(lines)
    for element in data:
        for i in range(len(element)):
            element[i] = int(element[i])
    del data[0]
    return data

def does_work(v, k, n):
    result = 0
    p = 0
    while v//(k ** p) != 0:
        result += v//(k ** p)
        p += 1

    if result >= n:
        return True
    else:
        return False

def binary_search(numbers, k, n):
    low = 0
    high = len(numbers) - 1

    while high != low :
        mid = (high + low) // 2
        if does_work(numbers[mid], k, n):
            high = mid
        else:
            low = mid + 1
    return numbers[high]

def main():
    data = read_file()
    for pair in data:
        n = pair[0]
        k = pair[1]
        vList = list(range(1, n + 1))
        print(binary_search(vList, k, n))


main()