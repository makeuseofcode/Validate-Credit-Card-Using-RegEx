import re

def checkMasterCardNo(cardNo):
    regex = "^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$"
    r = re.compile(regex)

    if(re.search(r, cardNo)):
        print("Valid")
    else:
        print("Not Valid")

card1 = "5110762060017101"
checkMasterCardNo(card1)

card2 = "8632458236982734"
checkMasterCardNo(card2)