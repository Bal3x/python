# solution_a 

# create algorithm that finds the lowest positive number from array A that is not repeated

def solution(A):

# test if list has values and set a max interger from the array to establish the range of the array
    if A: 
        max_int = max(A)
# convert the array A and n into a set 
# set() range of n then substract the sets in order to find difference between them
# elements of n that are not in A (n-A)
        A = set(A)
        n = set(range(1, max_int + 1))
        pos_int = (n - A)
        
# make sure that if negative values are given return lowest value
        if max_int < 1:
         return 1
# if len() is equal to 0 then use the max integer and add + 1
        if len(pos_int) == 0:
            return max_int + 1
# else return the minimun value from the remaining set 
        else:
            return min(pos_int)
    else:
        print("Missing integers, please add values to list.")

# given array
A = [-1, -4, 1]
print(solution(A))


            


    


   