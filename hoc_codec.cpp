"""để xem digit(0-9) xuất hiện ở kí tự thứ mấyyy(PYTHON NHA)"""

strings = input("enter the sentence: ")
found = False
position = 0
while not found and position < len(strings):
    if strings[position].isdigit() :
        found=True
    else:
        position=position + 1

if found:
    print("first ouccurs at position", position)
else:
    print("the string does not contant a digit.")


    """trên kia là first còn đây là last nha"""
string = input("enter the sentence: ")
found = False
position = len(string) - 1
while not found and position >= 0:
    if string[position].isdigit() :
        found = True
    else :
        position = position-1
