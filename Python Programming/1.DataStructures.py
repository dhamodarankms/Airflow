from operator import itemgetter, attrgetter
from functools import cmp_to_key
#Variables
tax_slap = 38.8;
price = 140000;
tax = round((price/tax_slap) * 100, 2);
print(tax);

#Substrings
name = 'Dhamodaran';
firsttwo = name[:2];                                                    #Substring - first two
aftertwo = name[2:];                                                    #Substring - after second character
exactPosition = name[1:2];                                              #Substring - Exact Position
fromlast = name[-2:];
print(firsttwo, aftertwo, exactPosition, fromlast);

#List
strings = [firsttwo, aftertwo, exactPosition, fromlast];
print(strings);
findElement = strings.count(firsttwo);                                  #Find the given Element in the list
print(findElement);
def findlength(str):                                                    #Sorted list - Element number based sort [asc, desc[reverse], key based]
    return len(str);
strings.sort;                                               
strings.sort(reverse=True);                          
strings.sort(reverse=True, key=findlength);            
print(strings);
strings = sorted(strings, key=str.casefold, reverse=False);             #Sorted list - Element value based sort
print(strings);
strings.append('Sonia');                                                
strings.insert(3,'Dhamo');
strings.extend(strings); 
strings.reverse;
print(strings);

class student:
    def __init__(self, name, age, grade):                               #setter
        self.name = name
        self.age = age
        self.grade = grade
    def __repr__(self):                                                 #getter
        return repr((self.name, self.age, self.grade));
    #def __itemsort__(self,key):
    def __multisort__(self, specs):                                     #multisort
        for key, reverse in reversed(specs):
            self.sort(key=attrgetter(key), reverse=reverse)
        return self;

student_record = [  student('Dhamo', 75, 'L5'),
                    student('Sonia', 46, 'L4'),
                    student('Paul', 50, 'L3')  ];

student_record = sorted(student_record, key=lambda student: student.age);                   #sort based on attribute            
print(student_record);                    
student_record = sorted(student_record, key=attrgetter('name','age'), reverse=False);       #sort based on multiple attribute
print(student_record);
student_record = student.__multisort__(student_record,(('age',False),('name',True)));       #sort based on multisort
print(student_record);
