import csv
import numpy
x1 = input('Enter your Age: ')
x2 = input('Enter your Workclass: ')
x3 = numpy.random.randint(77053,201490)
x4 = input('Enter your Qualification: ')
x5 = input('Enter your Qualification Number: ')
x6 = input('Enter your Marital status: ')
x7 = input('Enter your Occupation: ')
x8 = input('Enter your Relationship status: ')
x9 = input('Enter your Race: White/Black')
x10 = input('Enter your Gender: ')
x11 = input('Enter your Capital Gain: ')
x12 = input('Enter your Capital Loss: ')
x13 = input('Enter your Hour Per Week: ')
x14 = input('Enter your Native Country: ')
new_row = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,'1']
with open(r'adult1.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)
