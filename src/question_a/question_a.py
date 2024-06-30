def get_sum_of_evens(num):
   
    sum_of_evens = 0
    for i in range(2, num + 1, 2): 
        sum_of_evens += i
    return sum_of_evens
