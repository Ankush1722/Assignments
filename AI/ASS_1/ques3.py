# Input the password
string = input("Enter your password:")

# Get the length of the password
plen = len(string)

# Convert the password to a list of characters
pswd = list(string)

# Check if the password length is between 6 and 16 characters
if plen <= 16 and plen >= 6:
    # Check for at least one uppercase letter
    for big in pswd:
        if ord(big) <= 90 and ord(big) >= 65:
            # Check for at least one lowercase letter
            for small in pswd:
                if ord(small) <= 122 and ord(small) >= 97:
                    # Check for at least one special character
                    for spe in pswd:
                        if ord(spe) <= 64 and ord(spe) >= 32:
                            print("Password verified")
                            break
                    break
            break
else:
    print("Password incorrect")

# Print the password as a list of characters
print (pswd)

