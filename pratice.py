s= input("enter the string: ")
if 'A' <= s <= 'Z' or 'a'<=s<='z':
    print("string found")
    if s in 'aeiouAEIOU':
        print("string is vowel")
    else:
        print("string is consonent")
