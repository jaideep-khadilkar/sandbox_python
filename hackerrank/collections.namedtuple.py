
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
N = int(raw_input())
attribs = raw_input().split()
Student = namedtuple('Student', attribs)
totalMarks = 0
for _ in range(N):
    attrib_vals = raw_input().split()
    student = Student._make(attrib_vals)
    totalMarks += int(student.MARKS)
print float(totalMarks)/N

