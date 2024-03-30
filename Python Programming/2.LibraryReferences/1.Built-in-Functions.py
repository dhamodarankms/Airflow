from operator import attrgetter
import builtins
import math

class student:
    def __init__(self, name, age, grade):                               #setter
        self.name = name
        self.age = age
        self.grade = grade
    def __repr__(self):                                                 #getter
        return repr((self.name, self.age, self.grade));
    def __multisort__(self, specs):                                     #multisort
        for key, reverse in reversed(specs):
            self.sort(key=attrgetter(key), reverse=reverse)
        return self;
    def __validate_age__(self):
        if self.age > 40:
            return True
        else:
            return False;        
def main():
    student_record = [  student("Dhamo", 40, "L5"),
                        student('Sonia', 46, 'L4'),
                        student('Paul', 50, 'L3')  ]
    
    for index, stu in enumerate(student_record):
        print(["New Age : " + str(eval('a+b',{'a':stu.age,'b':index})), student.__repr__(stu)])
        exec('print(a+i)',{'a':stu.age, 'i':index});
        print(getattr(stu,"age"));
            
    adults = filter(lambda s:student.__validate_age__(s),student_record);
    adu = [float(st.age) for st in student_record if st.age > 20];
    print(adu);
    print(list(adults));
    print(isinstance(adu, list));
    print(isinstance(student_record, int));

    for stu in iter(student_record):
        print(stu);

    print(len(student_record));
    print(locals());

main();        