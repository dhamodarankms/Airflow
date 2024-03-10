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