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
    
    numbers = [1,10,20,100];
    squares = {10:1,1:10,2:20,3:100,4:110,50:120};

    student_file = open("/Users/sdg/student_file.txt", "a");

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
        student_file.write(student.__repr__(stu));

    student_file.close();

    print(len(student_record));
    print(locals());

    map_adults = map(lambda s:student.__validate_age__(s), student_record);
    print(list(map_adults));
    print(min(numbers));
    print(max(numbers));

    min_square = min(squares, key = lambda sq: squares[sq]);
    max_square = max(squares, key = lambda sq: squares[sq]);

    print(min_square);
    print(max_square);

    iter_squares = iter(student_record);
    print(next(iter_squares));

main();        