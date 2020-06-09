## Print Function

Read an integer *N*.

Without using any string methods, try to print the following: 
*123...N*

Note that "..." represents the values in between.

### Input Format
The first line contains an integer *N*.

### Output Format
Output the answer as explained in the task.

### Sample Input 0
3

### Sample Output 0
123

### Submitted Code
```python
n = int(input())
    b = ''
    for i in range(1, (n+1)):
        b = b + str(i)

    print(b)
```


## Write a function
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:
- The year can be evenly divided by 4, is a leap year, unless: 
  - The year can be evenly divided by 100, it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
[Source](http://www.timeanddate.com/date/leapyear.html)

### Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

### Input Format
Read y, the year that needs to be checked. 

### Constraints
1900 <= y <= 100000

### Output Format
Output is taken care of by the template. Your function must return a boolean value (True/False)

### Sample Input 0
1990

### Sample Output 0
False

### Explanation 0
1990 is not a multiple of 4 hence it's not a leap year.

### Submitted Code
```python
def is_divisible_four_and_hundred(year):
    year = str(year)
    dois_ultimos = year[(len(year) - 2):len(year)]

    if int(dois_ultimos) == 00:
        return False
    if int(dois_ultimos) % 4 == 0:
        return True
    
    return False

def is_leap(year):
    leap = False
    
    # Write your logic here
    leap = is_divisible_four_and_hundred(year)
    
    if year % 400 == 0:
        leap = True

    return leap
```

## Loops
### Task

Read an integer *N*. For all non-negative integers *i* < *N*, print *i<sup>2</sup>*. See the sample for details.

### Input Format
The first and only line contains the integer, *N*.

### Constraints
1 <= N <= 20

### Output Format
Print N lines, one corresponding to each *i*.

### Sample Input 0
5

### Sample Output 0
```python
0
1
4
9
16
```

### Submitted Code
```python
n = int(input())
    i = 0

if n > 0 and n <= 20:
    while i < n:
        print(i ** 2)
        i = i + 1
```