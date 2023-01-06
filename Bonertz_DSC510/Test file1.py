# Assignment 1.2
print('Hello World :-)')


def costperfoot(feet):
    if feet > 500:
        return float(.50)
    elif feet > 250:
        return float(.70)
    elif feet > 100:
        return float(.80)
    else:
        return float(.87)

feetofcable = int(input("How many feet of cable"))

costperfoot()
