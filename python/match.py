import re
text=input("Enter text: ")


#replace1=re.sub("/\s/g", "_",text)
#if s in text:
    
res_str = re.sub(r"\s", "_", text)
print(res_str)

#    res_str = re.sub(r"\s", "_", text)
