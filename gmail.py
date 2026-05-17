email = input("Enter your Email : ") # g@g.in, hiku@gmailc.com
k,j,d = 0,0,0
if len(email)>=6:
   if email[0].isalpha():
      if ("@" in email) and (email.count("@")==1):
         if (email[-4]==".") ^ (email[-3]=="."):
            for i in email:
               if i==i.isspace():
                  k=1
               elif i.isalpha():
                  if i==i.upper():
                     j=1
               elif i.isdigit():
                  continue
               elif i=="_" or i=="." or i=="@":
                  continue
               else:
                  d=1
            if k==1 or j==1 or d==1:
               print("Wrong Email, There is space or upper case in your email..!!")
               print("You cannot use special characters in email, other than @..!!")
            else:
               print("Your Email is valid..!!\u2705")
         else:
            print("Dot must be in right place")
      else:
        print("You can use @ once in an email..!!")
   else:
      print("Wrong Email, First letter must be alphabet..!!")
else:
   print("Email you provided is wrong..!!")
   print("Characters must be atleast 6..!!") 

