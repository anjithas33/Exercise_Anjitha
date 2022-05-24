import re
  
def isValid(s):
      
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)

phone=input("Phone number: ")
if isValid(phone):
    print("Valid")
else:
    print("invalid")