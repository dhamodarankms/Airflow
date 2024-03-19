#list
numbers = [1, 10, 2, 0];

#object

#while
i = 0;
while i < (numbers.__len__()):
    numbers[i] = numbers[i]*3;
    i = i+1;
print(numbers);

#for loop
i=0;
for j in numbers: 
    numbers[i] = j*3;
    i=i+1;
print(numbers);

#for loop with range
for i in range(numbers.__len__()):
    if numbers[i]*3 in range(0,10):
        print(numbers[i], "Not required to talk anymore");
        break; #reverse validation is continue
    else:
        numbers[i] = numbers[i]*3;
print(numbers);

#for loop in a list comprehension
output = [(i,j) for i in (1,2,3) for j in (1,4,3) if i == j];
print(output);
vec = [[1,2,3],[4,5,6],[7,8,9]];
output = [num for elem in vec for num in elem];
print(output);

#transpose rows to columns
matrix = [  [1,2,3],    
            [4,5,6],
            [7,8,9,10] ];

output = [[row[i] for row in matrix] for i in range(3)];
print(output);

