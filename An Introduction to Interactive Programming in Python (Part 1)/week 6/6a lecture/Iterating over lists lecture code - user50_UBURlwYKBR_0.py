# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    odd = False
    for num in numbers:
        if num % 2 == 1:
            odd = True
    return odd

# or

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)
            
def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
    
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
    
    for num in remove:
        numbers.remove(num)   

def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    
    return newnums         

def remove_last_odd(numbers):
    range = len(numbers)
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
    
    if has_odd:
        numbers.remove(last_odd)

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    print count_odd(numbers)
    print check_odd(numbers)
    print check_odd(numbers)
    remove_last_odd(numbers)
    print numbers

run()


"""The for loop should have iterated over range(len(numbers)) 
and set last_odd to the position of the last odd number. 
Using numbers.pop(last_odd) in line 55 would then delete the last odd number. """

 
def remove_last_odd1(numbers):
    range = len(numbers)
    if numbers[range-1] % 2 == 1:
        numbers.pop()

numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
        
remove_last_odd1(numbers)
print numbers




