# Tech Support
# Stephan Jamieson
# 5/1/2015
responses={
    'bluetooth':'Have you tried mouthwash?',
    'windows':'Ah, I think I see your problem. What version?',
    'apple':'You do mean the computer kind?',
    'blue':'Ah, the blue screen of death. And then what happened?',
    'spam':'You should see if your mail client can filter messages.',
    'connection':'Contact Telkom.',
    'crashed':'Are the drivers up to date?',
    'hacked':'You should consider installing anti-virus software.'}


def default_response():
    return 'Curious, tell me more.'
    
def get_response(words):
    for word in words: 
        if word in responses: # check if there is a key that matches the person's input
            return responses[word] # retrieve the value of the corrosponding key in responses
    return default_response()
    

def print_welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')


def get_input():
    # convert the whole string into lowercase
    query = input().lower().split(' ') 
    return query

def main():
    print_welcome()
    while True: # make it to repeatedly ask for input
        query = get_input()
        if query == ['quit']: # if statement to break if user enters quit
            break
        else: 
            response = get_response(query)
            print(response)
            
# Call on the main function to start the program
if __name__=='__main__': 
    main()