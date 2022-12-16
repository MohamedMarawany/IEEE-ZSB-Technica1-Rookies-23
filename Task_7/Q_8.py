n = input()
s = ""
lis = ["--","-.","."]
for i in lis:
    if i == "--" :
        s = n.replace(i,"2")
    elif i == "-." :
        s = n.replace(i,"1")
    elif i == "." :
        s = n.replace(".","0")
    n = s
print(s)
