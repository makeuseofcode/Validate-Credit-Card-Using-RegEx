import re

def checkAmericanExpressCardNo(cardNo):
    regex = "^3[47][0-9]{13}$"
    r = re.compile(regex)

    if(re.search(r, cardNo)):
        print("Valid")
    else:
        print("Not Valid")

card1 = "372831730491196"
checkAmericanExpressCardNo(card1)

card2 = "84732593847743042"
checkAmericanExpressCardNo(card2)