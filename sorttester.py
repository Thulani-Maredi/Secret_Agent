# Progarm to test the sortsearch module
# mrdthu003
# 01 October 2024


from sortsearch import selection_sort, merge_sort, generate_number_list
import time 
def main():
    size = int(input(("Enter the size of the list:\n")))
    random_nums = generate_number_list(size)
    
    print("Choose the sort method:")
    print("1. Selection Sort.")
    print("2. Merge Sort.")
    choice = int(input())
    if choice == 1:
        begin = time.perf_counter()
        sorted_nums = selection_sort(random_nums)
        end = time.perf_counter()
        print("Before:", random_nums)
        print("After:", sorted_nums)
        taken_time = end - begin
        print("Time:", taken_time)
    elif choice == 2:
        begin = time.perf_counter()
        sorted_nums = merge_sort(random_nums)
        end = time.perf_counter()
        print("Before: ", random_nums)
        print("Ater: ", sorted_nums)
        taken_time = end - begin
        print("Time:", taken_time)        
        
main()