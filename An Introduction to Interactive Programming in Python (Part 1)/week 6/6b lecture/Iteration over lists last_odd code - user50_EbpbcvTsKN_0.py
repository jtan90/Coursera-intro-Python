def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in range(len(numbers)):
        if num % 2 == 1:
            has_odd = True
            last_odd = num + 1
    
    if has_odd:
        numbers.pop(last_odd)

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers

run()


"""The for loop should have iterated over range(len(numbers)) 
and set last_odd to the position of the last odd number. 
Using numbers.pop(last_odd) in line 55 would then delete the last odd number. """
