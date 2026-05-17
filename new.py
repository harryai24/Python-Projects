# Check e-mail validation in python using Regex
''' Condition 
1. a-z (small letter only and first character must  be alphabet)
2. 0-9 (include numbers)
3. . & _ (only once before @)
4. @ (Only one time)
5. . (Must be in 2nd to 3rd position from last)
'''

import re 
email_condition = r"^[a-z][a-z0-9]*[._]?[a-z0-9]+@[a-z0-9]+(\.[a-z0-9]+){1,2}\.[a-z]{2,3}$"
# ? is used for 0 or 1 occurance of characters otherwise it gives you false and ^ this sign denotes the first charcters in string must be this
user_email = input("Enter your Email: ")


if re.search(email_condition,user_email):
    print("Your Email is Valid..!!\u2705")
else:
    print("The email you entered is not correct, please check your email and try agian..!!\U0001F60A")

# Always executed action
print("Thank You..!!\U0001F64F")