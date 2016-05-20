#input consists of N which means N studetns
#and more info about name and scores




marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())]) #read two lines into one cube in a list
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] # find the second hightest score in all students
print('\n'.join(a for a,b int sorted(marksheet) if b == second_highest))

#second version
n = int(raw_input())
marks = [[raw_input(), float(raw_input())] for i in  xrange(n)]
scores = sorted({s[1] for s in marks})
result = sorted(s[0] for s in marks if s[1] == scores[1])
print '\n'.join(result)

