# create algorithm that finds the lowest positive number from array A that is not repeated

def Solution(test_list):
    curr_num = None
    test_list = sorted(test_list)
    for num in test_list:
        if num > 0:
            if not curr_num:
                curr_num = num
            elif num == curr_num + 1:
                curr_num = num
            elif num > curr_num + 1:
                return curr_num + 1
    
    if curr_num and curr_num > 0:
        return curr_num + 1
    
    return 1

print(Solution([1, 2, 3]))
print(Solution([-1, -3]))


def SolutionB(s):
    if not s:
        return None

    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    largest_char_count = 1
    ret_char = s[0]

    for char, count in counts.items():
        if count >= largest_char_count and char <= ret_char:
            ret_char = char
            largest_char_count = count
    
    return(ret_char, largest_char_count)
    return ret_char

print(SolutionB("hello"))
print(SolutionB("hhello"))
