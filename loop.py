m = eval(input("Enter for multples from 5 t0 20:\n"))
for k in range (5,21):
    print(k,"x", m, "=", k*m)
if 5 <= m < 21:
    print("Here are your multiples.")
else:
    print("Number entered not required.")