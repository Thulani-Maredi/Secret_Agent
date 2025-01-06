def main():
    import time
    total_taken = 0
    correct = 0
    for n in range(3):
        start_time = time.time()
        letters = input("Enter letters ‘abcdefghij’: ")
        end_time = time.time()
        total_taken += end_time - start_time
        if letters == "abcdefghij":
            correct += 1
    average_time = total_taken / 3
    print("Average time taken is {}".format(str(average_time)))
    print("Correct entries is {} out of 3".format(correct))
main()
