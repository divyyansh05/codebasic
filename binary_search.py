from utils import time_it

@time_it
def linear_search(numbers:list,number_to_find):
    count=0
    while count<len(numbers):
        if numbers[count]==number_to_find:
            return count
        count+=1

    else:
        return -1

@time_it
def binary_search(numbers_list,number_to_find):
    left_index=0
    right_index=len(numbers_list)-1
    middle_index=0

    while left_index<=right_index:
        middle_index=(left_index + right_index) // 2
        mid_number=numbers_list[middle_index]

        if mid_number==number_to_find:
            return middle_index
        
        if mid_number<number_to_find:
            left_index=middle_index+1
        else:
            right_index=middle_index-1
@time_it       
def binary_search_recursively(numbers_list,number_to_find,left_index,right_index):
    if left_index > right_index:
        return -1
    
    middle_index=(left_index + right_index) // 2
    if middle_index >= len(numbers_list):
        return -1
    mid_number=numbers_list[middle_index]
    if mid_number==number_to_find:
        return middle_index
        
    if mid_number<number_to_find:
        left_index=middle_index+1
    else:
        right_index=middle_index-1

    return binary_search_recursively(numbers_list,number_to_find,left_index,right_index)









if __name__=="__main__":
    numbers_list=[2,4,1,34,23,1,3,5]
    number_to_find=34

    index=linear_search(numbers_list,number_to_find)
    print("index of the number in linear search is {0}".format(index))

    numbers_list1=[1,3,4,7,9,11,34,45,67]

    index=binary_search(numbers_list1,number_to_find)
    print("index of the number in binary search is {0}".format(index))

    index=binary_search_recursively(numbers_list1,number_to_find,0,(len(numbers_list1)-1))
    print("index of the number in binary search recursive is {0}".format(index))
