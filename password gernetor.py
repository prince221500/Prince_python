import random
import string

length = int(input("Enter the desired length of the password: "))

characters = string.ascii_letters + string.digits

password = ""                       # typical way

for i in range(length):
    password += random.choice(characters)

print("Generated password:", password)

# *************** another way **********************

ot=" "
st=0
for i in range(length):                  # easy way 
    st=random.randint(48,122)
    ot=ot+chr(st)
print(f"{ot} is the geernated password ",)