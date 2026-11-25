# Add two number
'''
add = lambda a,b: a+b
print("Sum=",add(89,77))
'''
# AVERAGE THE TWO NUMBER
'''
average = lambda a,b: (a+b)/2
print("average=",average(89,97))
'''
# CACLULATE THE CUBE OF EACH NUMBER IN A LIST.
'''
dataset = [12,24,36,48,60]
cube = list(map(lambda x: x**3,dataset))
print(cube)
'''
# FIND THE DIFFERENCE BETWEEN THE MAXIMUM AND MINIMUM VALUE IN A DATASET.
'''
dataset = [12,24,36,48,60]
range_diff = lambda x: max(x) - min(x)
print("Range=",range_diff(dataset))
'''
# FILTER ALL EVEN NUMBERS FORM A DATASET.
'''
dataset = [1,2,3,4,5,6,7]
evens = list(filter(lambda x: x%2 ==0,dataset))
print(evens)
'''
# SELECT ALL OBSERVATION GREATER THEN 50
'''
observation = [12,23,24,46,68,45,68,88,58]
greater_than_50 = list(filter(lambda x: x>50,observation))
print(greater_than_50)
'''
# SORT A LIST OF NUMBERS IN DESCENDING ORDER.
'''
NUMBER = [12222,23,45,34,56,231,1234,451,212,456566]
sorted_desc = sorted(NUMBER , reverse=True)
print(sorted_desc)
'''
# sort recording according to marks.
'''
student = [
    ("Riya",78),
    ("Jiya",88),
    ("Kiya",87)
    ]
result = sorted(student,key=lambda x: x[1])
print(result)
'''
# CALCULATE  THE SQUARE OF DEVIATIONS FROM A GIVEN MEAN.
'''
data = [12,222,24,46,68,88]
mean = lambda x: sum(x)/len(x)
print("Mean=",mean(data))
'''
# filter marks student whose score 40.
''
score = [13,34,67,86,64,34]
passed_marks = filter(lambda x: x>=40,score)
print(list(passed_marks))
