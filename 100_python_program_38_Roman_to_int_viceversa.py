__author__ = 'c_disenc'
def int_to_roman (integer):

    returnstring=''
    table=[['X',10],['IX',9],['V',5],['IV',4],['I',1]]

    for pair in table:

        while integer-pair[1]>=0:

            integer-=pair[1]
            returnstring+=pair[0]

    return returnstring

def rom_to_int(string):

    table=[['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:
        continueyes=True
        while continueyes:
            if len(string)>=len(pair[0]):

                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False

    return returnint

print(rom_to_int("IXVII"))
print(int_to_roman(25))
