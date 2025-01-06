# Program that calls on the previous module i created
# mrdthu003
# 11 August 2024

# Retrive functtion from modules created called vectormaths
from vectormaths import vector_sum, vector_product, vector_norm

def main():
    # Collect 3 integer inputs from user and put in list A
    A = []
    ques1 = input('Enter vector A:\n')
    ques1 = ques1.split()
    for i in ques1:
        if i.lstrip('-').isdigit():
            a = int(i)
            A.append(a)
    # Collect 3 integer inputs from user and put in list B    
    B = []
    ques2 = input('Enter vector B:\n')
    ques2 = ques2.split()
    for i in ques2:
        if i.lstrip('-').isdigit():
            b = int(i)
            B.append(b)
   
    # Create if statements to get user to choose what do with their inputs and use the function to print answer
    ques3 = input("Select a calculation to perform. Enter '+', '.' or '|':\n")
    if ques3 == '+':
        answer = vector_sum(A,B)
        print('A+B =', answer)
    elif ques3 == '.':
        answer = vector_product(A,B)
        print('A.B =', answer)        
    elif ques3 == '|':
        answer1 = vector_norm(A)
        answer2 = vector_norm(B)
        print(f'|A| = {answer1:.2f}')
        print(f'|B| = {answer2:.2f}')
    else:
        print('Selection not recognised.')
        
if __name__=='__main__':
    main()
