w = input("Enter Word: ")

w_len = len(w)
print(w + " is " + str(w_len) + " letters long.")

if (w_len % 2) == 0:
    w_mid=int((w_len / 2))
    print("The middle letters are: " + w[w_mid-1] + w[w_mid])
else:
    w_mid=int((w_len / 2))
    print("The middle letter is: " + w[w_mid])
