# Program to identify the winner of a long jump competition
# mrdthu003
# Thuani Mredi
# 23/07/2024

def main():
 # collect competior names and put in list
 print("***** Long Jump Information System *****")
 print("Please enter the names of competitors. (Press return when done.)")
 n = 1
 names = []
 while True:
    name = input("Competitor no. " + str(n) + ":\n")
    n += 1
    if name == "":
        break # use break to stop collecting competitor when user click enter
    names.append(name)
    
 longest = []
 print("Please enter the distances for each competitor.")
 for competitor in names:
    print("Competitor", competitor + ":")
    score = []
    # Collect3 Attempts for each competitor
    for attempts in range(1,4):
        attempt = input("Attempt "+str(attempts)+":\n")
        if not attempt.isalpha():
            attempt = f"{float(attempt):.2f}"
            score.append(attempt)
    # Append highest score for each and if there is none append no jump
    if score:
        longest.append(max(score))
    else:
        longest.append("No jump")
 
 # print all high score for each competitor
 print("\nCompetitor               Longest Distance")
 for i in range(len(names)):
    print("{:25}{:<16}".format(names[i], longest[i]))
 
 # Replace the no jump in longest to compared their highest scores and find the winner
 for i in range(len(longest)):
  if longest[i] == 'No jump':
   longest[i] = 0
  else:
   longest[i] = float(longest[i]) 
 highest = max(longest) # find the highest score (winner)
 winner_index = longest.index(highest) # find the index of the score of the winner by finding their results and leading to their name
 
 print()
 print(f"The winner is {names[winner_index]} with a jump of {highest:.2f}.")



if __name__ == "__main__":
 main()