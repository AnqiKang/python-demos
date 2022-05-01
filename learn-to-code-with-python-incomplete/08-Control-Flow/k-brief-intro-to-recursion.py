# recursion: when a function calls itself! 

def count_down(number):
    start = number
    while start > 0:
        print(start)
        start -= 1

# recursion way
def count_down_from(number):
    if number == 0:
        return
    
    print(f"Current number is {number}")
    count_down_from(number - 1)


count_down(5)
count_down_from(5)


