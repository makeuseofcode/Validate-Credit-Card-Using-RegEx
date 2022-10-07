import re

def checkVisaCardNo(cardNo):
    regex = "^4[0-9]{12}(?:[0-9]{3})?$"
    r = re.compile(regex)

    if(re.search(r, cardNo)):
        print("Valid")
    else:
        print("Not Valid")

card1 = "4539890694174109"
checkVisaCardNo(card1)

card2 = "49237429498"
checkVisaCardNo(card2)