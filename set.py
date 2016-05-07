# Given 22 sets of integers, MM and NN, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either MM or NN but do not exist in both.
# Enter your code here. Read input from STDIN. Print output to STDOUTinput()
input()
a=set(map(int,raw_input().split()))
input()
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print n