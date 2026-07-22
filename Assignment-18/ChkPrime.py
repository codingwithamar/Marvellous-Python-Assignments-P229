def CheckPrime(DataValue):
    if DataValue <= 1:
        return False

    for i in range(2,DataValue):
        if DataValue%i==0:
            return False
    return True

def PrimeAddition(iData1,iData2):
    return iData1+iData2
