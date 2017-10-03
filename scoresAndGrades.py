import random

def grades():
    for i in range(0,10):
        randomNum = random.randint(60,100)
        if randomNum >= 90:
            print "Score: {}; Your grade is A".format(randomNum)
        elif randomNum >= 80:
            print "Score: {}; Your grade is B".format(randomNum)
        elif randomNum >= 70:
            print "Score: {}; Your grade is C".format(randomNum)
        else:
            print "Score: {}; Your grade is D".format(randomNum)

grades()