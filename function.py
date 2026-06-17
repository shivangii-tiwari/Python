#global varible we can acess and modifi in main space if you have to modifie the global varible in method area u have to use the keywrord global
# a = 10
# print(a)
# def sam():
#     global a # the keyword
#     a = 20
#     print(a)
# sam()
# print(a)
# local varible deal with the method area or inside function
def shivangi():
    a = 90
    print(a)
    def aloo():
        a = 30
        print(a)
    aloo()
    print(a)
shivangi()
#to modifie inside one nested function we will be using one keyword "non local"
def shivangi():
    a = 90
    print(a)
    def aloo():
        nonlocal a # keyword
        a = 30
        print(a)
    aloo()
    print(a)
shivangi()
#scope of globalvarible is inside and outside of the function
#scope of localvarible is inside the function
def extract_vowel():
    a = kiki
    s = 'aeiouAEIOU'
    pip = " "
    for a in s:
        print(pip)
extract_vowel()