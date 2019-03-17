import math
import _random
import random

code = raw_input("Code:")
#-----------------------------------------------------------------------------------------------------------------#
codelistinit = map(int, str(code))          #Making our input code a list that all numbers are independent element so we can shuffle it.

TFL = []                                    #We need 10 independent random entries.
TFLoutput = []
TFLkey = []

Stage1shuffle = []                          #We have new, independent burner list for each step.
Stage2shuffle = []
Stage3shuffle = []
Stage4shuffle = []
Stage5shuffle = []
Stage6shuffle = []
Stage7shuffle = []
Stage8shuffle = []
Stage9shuffle = []
Stage10shuffle = []

def RNG_LOOP ():
    y = 0
    while y < 10:
        rdm = random.uniform(0.0, 100.0)
        if rdm >= 40.0:
            TFL.append("T")
        else:
            TFL.append("F")
        y = y + 1
def RNG_NORMAL():                                  #True, False list
    rand1 = random.uniform(0.0, 100.0)      #finding random between 0.0 to 100.0
    if rand1 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand2 = random.uniform(0.0, 100.0)
    if rand2 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand3 = random.uniform(0.0, 100.0)
    if rand3 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand4 = random.uniform(0.0, 100.0)
    if rand4 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand5 = random.uniform(0.0, 100.0)
    if rand5 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand6 = random.uniform(0.0, 100.0)
    if rand6 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand7 = random.uniform(0.0, 100.0)
    if rand7 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand8 = random.uniform(0.0, 100.0)
    if rand8 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand9 = random.uniform(0.0, 100.0)
    if rand9 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    rand10 = random.uniform(0.0, 100.0)
    if rand10 >= 40.0:
        TFL.append("T")
    else:
        TFL.append("F")
    return TFL

def one_step():         #change location of first half and second half like 1234 to 3412
    firsthalf = []
    secondhalf = []
    if TFL[0] == "T":
        lenght = len(codelistinit)
        if lenght % 2 == 0:
            a = lenght / 2
            firsthalf = codelistinit[0:a]
            secondhalf = codelistinit[a:lenght]
            while len(secondhalf) >= 1:
                Stage1shuffle.append(secondhalf[0])
                del secondhalf[0]
            while len(firsthalf) >= 1:
                Stage1shuffle.append(firsthalf[0])
                del firsthalf[0]
        else:
            codelistinit.append("a")
            lenght = len(codelistinit)
            a = lenght / 2
            firsthalf = codelistinit[0:a]
            secondhalf = codelistinit[a:lenght]
            secondhalf.remove("a")
            while len(secondhalf) >= 1:
                Stage1shuffle.append(secondhalf[0])
                del secondhalf[0]
            while len(firsthalf) >= 1:
                Stage1shuffle.append(firsthalf[0])
                del firsthalf[0]
    else:
        while len(codelistinit) >= 1:
            Stage1shuffle.append(codelistinit[0])
            del codelistinit[0]
        return
def two_step():         #change location of quarters like 1234 to 3142
    firstquarter = []
    secondquarter = []
    thirdquarter = []
    fourthquarter = []
    if TFL[1] == "T":
        length = len(Stage1shuffle)
        if length % 4 == 1:
            Stage1shuffle.append("a")
            Stage1shuffle.append("b")
            Stage1shuffle.append("c")
            length = len(Stage1shuffle)
            a = length / 4
            firstquarter = Stage1shuffle[0:a]
            secondquarter = Stage1shuffle[a:2 * a]
            thirdquarter = Stage1shuffle[2 * a:3 * a]
            fourthquarter = Stage1shuffle[3 * a:length]
            while len(thirdquarter) >= 1:
                Stage2shuffle.append(thirdquarter[0])
                del thirdquarter[0]
            while len(firstquarter) >= 1:
                Stage2shuffle.append(firstquarter[0])
                del firstquarter[0]
            while len(fourthquarter) >= 1:
                Stage2shuffle.append(fourthquarter[0])
                del fourthquarter[0]
            while len(secondquarter) >= 1:
                Stage2shuffle.append(secondquarter[0])
                del secondquarter[0]
            Stage2shuffle.remove("a")
            Stage2shuffle.remove("b")
            Stage2shuffle.remove("c")
        elif length % 4 == 2:
            Stage1shuffle.append("a")
            Stage1shuffle.append("b")
            length = len(Stage1shuffle)
            a = length / 4
            firstquarter = Stage1shuffle[0:a]
            secondquarter = Stage1shuffle[a:2 * a]
            thirdquarter = Stage1shuffle[2 * a:3 * a]
            fourthquarter = Stage1shuffle[3 * a:length]
            while len(thirdquarter) >= 1:
                Stage2shuffle.append(thirdquarter[0])
                del thirdquarter[0]
            while len(firstquarter) >= 1:
                Stage2shuffle.append(firstquarter[0])
                del firstquarter[0]
            while len(fourthquarter) >= 1:
                Stage2shuffle.append(fourthquarter[0])
                del fourthquarter[0]
            while len(secondquarter) >= 1:
                Stage2shuffle.append(secondquarter[0])
                del secondquarter[0]
            Stage2shuffle.remove("a")
            Stage2shuffle.remove("b")
        elif length % 4 == 3:
            Stage1shuffle.append("a")
            length = len(Stage1shuffle)
            a = length / 4
            firstquarter = Stage1shuffle[0:a]
            secondquarter = Stage1shuffle[a:2 * a]
            thirdquarter = Stage1shuffle[2 * a:3 * a]
            fourthquarter = Stage1shuffle[3 * a:length]
            while len(thirdquarter) >= 1:
                Stage2shuffle.append(thirdquarter[0])
                del thirdquarter[0]
            while len(firstquarter) >= 1:
                Stage2shuffle.append(firstquarter[0])
                del firstquarter[0]
            while len(fourthquarter) >= 1:
                Stage2shuffle.append(fourthquarter[0])
                del fourthquarter[0]
            while len(secondquarter) >= 1:
                Stage2shuffle.append(secondquarter[0])
                del secondquarter[0]
            Stage2shuffle.remove("a")
        else:
            length = len(Stage1shuffle)
            a = length / 4
            firstquarter = Stage1shuffle[0:a]
            secondquarter = Stage1shuffle[a:2 * a]
            thirdquarter = Stage1shuffle[2 * a:3 * a]
            fourthquarter = Stage1shuffle[3 * a:length]
            while len(thirdquarter) >= 1:
                Stage2shuffle.append(thirdquarter[0])
                del thirdquarter[0]
            while len(firstquarter) >= 1:
                Stage2shuffle.append(firstquarter[0])
                del firstquarter[0]
            while len(fourthquarter) >= 1:
                Stage2shuffle.append(fourthquarter[0])
                del fourthquarter[0]
            while len(secondquarter) >= 1:
                Stage2shuffle.append(secondquarter[0])
                del secondquarter[0]
    else:
        while len(Stage1shuffle) >= 1:
            Stage2shuffle.append(Stage1shuffle[0])
            del Stage1shuffle[0]
        return
def three_step():       #make the numbers reverse like 1234 to 4321
    tre = len(Stage2shuffle)
    if TFL[2] == "T":
        while tre > 0:
            Stage3shuffle.append(Stage2shuffle[tre-1])
            del Stage2shuffle [tre-1]
            tre = tre - 1
    else:
        while len(Stage2shuffle) >= 1:
            Stage3shuffle.append(Stage2shuffle[0])
            del Stage2shuffle[0]
        return
def four_step():        #the hindu shuffle like 12-34-56 to 34-12-56 after that 34-56-12
    firstpack = []
    secondpack = []
    thirdpack = []
    stage1 = []
    firstpack2 = []
    secondpack2 = []
    thirdpack2 = []
    if TFL[3] == "T":
        length = len(Stage3shuffle)
        if length % 3 == 2:
            Stage3shuffle.append("a")
            Stage3shuffle.append("b")
            length = len(Stage3shuffle)
            a = length / 3
            firstpack = Stage3shuffle[0:a]
            secondpack = Stage3shuffle[a:2 * a]
            thirdpack = Stage3shuffle[2 * a:length]
            while len(secondpack) >= 1:
                stage1.append(secondpack[0])
                del secondpack[0]
            while len(firstpack) >= 1:
                stage1.append(firstpack[0])
                del firstpack[0]
            while len(thirdpack) >= 1:
                stage1.append(thirdpack[0])
                del thirdpack[0]
            length = len(stage1)
            a = length / 3
            firstpack2 = stage1[0:a]
            secondpack2 = stage1[a:2 * a]
            thirdpack2 = stage1[2 * a:length]
            while len(firstpack2) >= 1:
                Stage4shuffle.append(firstpack2[0])
                del firstpack2[0]
            while len(thirdpack2) >= 1:
                Stage4shuffle.append(thirdpack2[0])
                del thirdpack2[0]
            while len(secondpack2) >= 1:
                Stage4shuffle.append(secondpack2[0])
                del secondpack2[0]
            Stage4shuffle.remove("a")
            Stage4shuffle.remove("b")

        elif length % 3 == 1:
            Stage3shuffle.append("a")
            length = len(Stage3shuffle)
            a = length / 3
            firstpack = Stage3shuffle[0:a]
            secondpack = Stage3shuffle[a:2 * a]
            thirdpack = Stage3shuffle[2 * a:length]
            while len(secondpack) >= 1:
                stage1.append(secondpack[0])
                del secondpack[0]
            while len(firstpack) >= 1:
                stage1.append(firstpack[0])
                del firstpack[0]
            while len(thirdpack) >= 1:
                stage1.append(thirdpack[0])
                del thirdpack[0]
            length = len(stage1)
            a = length / 3
            firstpack2 = stage1[0:a]
            secondpack2 = stage1[a:2 * a]
            thirdpack2 = stage1[2 * a:length]
            while len(firstpack2) >= 1:
                Stage4shuffle.append(firstpack2[0])
                del firstpack2[0]
            while len(thirdpack2) >= 1:
                Stage4shuffle.append(thirdpack2[0])
                del thirdpack2[0]
            while len(secondpack2) >= 1:
                Stage4shuffle.append(secondpack2[0])
                del secondpack2[0]
            Stage4shuffle.remove("a")
        else:
            length = len(Stage3shuffle)
            a = length / 3
            firstpack = Stage3shuffle[0:a]
            secondpack = Stage3shuffle[a:2 * a]
            thirdpack = Stage3shuffle[2 * a:length]
            while len(secondpack) >= 1:
                stage1.append(secondpack[0])
                del secondpack[0]
            while len(firstpack) >= 1:
                stage1.append(firstpack[0])
                del firstpack[0]
            while len(thirdpack) >= 1:
                stage1.append(thirdpack[0])
                del thirdpack[0]
            length = len(stage1)
            a = length / 3
            firstpack2 = stage1[0:a]
            secondpack2 = stage1[a:2 * a]
            thirdpack2 = stage1[2 * a:length]
            while len(firstpack2) >= 1:
                Stage4shuffle.append(firstpack2[0])
                del firstpack2[0]
            while len(thirdpack2) >= 1:
                Stage4shuffle.append(thirdpack2[0])
                del thirdpack2[0]
            while len(secondpack2) >= 1:
                Stage4shuffle.append(secondpack2[0])
                del secondpack2[0]
            return
    else:
        while len(Stage3shuffle) >= 1:
            Stage4shuffle.append(Stage3shuffle[0])
            del Stage3shuffle[0]
        return
def five_step():        #the riffle shuffle like 12345678 to 1234-5678 then 51627384
    firsthalf = []
    secondhalf = []
    z = 0
    if TFL[4] == "T":
        lenght = len(Stage4shuffle)
        if lenght % 2 == 0:
            a = lenght / 2
            firsthalf = Stage4shuffle[0:a]
            secondhalf = Stage4shuffle[a:lenght]
            while z < a:
                Stage5shuffle.append(secondhalf[z])
                Stage5shuffle.append(firsthalf[z])
                z = z + 1
        else:
            Stage4shuffle.append("a")
            lenght = len(Stage4shuffle)
            a = lenght / 2
            firsthalf = Stage4shuffle[0:a]
            secondhalf = Stage4shuffle[a:lenght]
            while z < a:
                Stage5shuffle.append(secondhalf[z])
                Stage5shuffle.append(firsthalf[z])
                z = z + 1
            Stage5shuffle.remove("a")
    else:
        while len(Stage4shuffle) >= 1:
            Stage5shuffle.append(Stage4shuffle[0])
            del Stage4shuffle[0]
        return


    return
def six_step():         #change location of first half reversed and second half normal like 123456 to 321-456 then 456321
    firsthalf = []
    secondhalf = []
    q = len(Stage5shuffle)
    if TFL[5] == "T":
        if q % 2 == 0:
            a = q / 2
            firsthalf = Stage5shuffle[0:a]
            secondhalf = Stage5shuffle[a:q]
            w = len(firsthalf)
            while w > 0:
                Stage6shuffle.append(firsthalf[w - 1])
                del firsthalf[w - 1]
                w = w - 1
            while len(secondhalf) >= 1:
                Stage6shuffle.append(secondhalf[0])
                del secondhalf[0]
        else:
            Stage5shuffle.append("a")
            q = len(Stage5shuffle)
            e = len(Stage5shuffle) / 2
            firsthalf = Stage5shuffle[0:e]
            secondhalf = Stage5shuffle[e:q]
            w = len(firsthalf)
            while w > 0:
                Stage6shuffle.append(firsthalf[w - 1])
                del firsthalf[w - 1]
                w = w - 1
            while len(secondhalf) >= 1:
                Stage6shuffle.append(secondhalf[0])
                del secondhalf[0]
            Stage6shuffle.remove("a")
    else:
        while len(Stage5shuffle) >= 1:
            Stage6shuffle.append(Stage5shuffle[0])
            del Stage5shuffle[0]
        return
    return
def seven_step():       #reverse 1 first half and riffle
    firsthalf = []
    secondhalf = []
    firsthalfrev = []
    z = 0
    q = len(Stage6shuffle)
    if TFL[6] == "T":
        if q % 2 == 0:
            a = q / 2
            firsthalf = Stage6shuffle[0:a]
            secondhalf = Stage6shuffle[a:q]
            w = len(firsthalf)
            while w > 0:
                firsthalfrev.append(firsthalf[w - 1])
                del firsthalf[w - 1]
                w = w - 1
            z1 = len(firsthalfrev)
            while z < z1:
                Stage7shuffle.append(secondhalf[z])
                Stage7shuffle.append(firsthalfrev[z])
                z = z + 1
        else:
            Stage6shuffle.append("a")
            q = len(Stage6shuffle)
            e = len(Stage6shuffle) / 2
            firsthalf = Stage6shuffle[0:e]
            secondhalf = Stage6shuffle[e:q]
            w = len(firsthalf)
            while w > 0:
                firsthalfrev.append(firsthalf[w - 1])
                del firsthalf[w - 1]
                w = w - 1
            z1 = len(firsthalfrev)
            while z < z1:
                Stage7shuffle.append(secondhalf[z])
                Stage7shuffle.append(firsthalfrev[z])
                z = z + 1
            Stage7shuffle.remove("a")
    else:
        while len(Stage6shuffle) >= 1:
            Stage7shuffle.append(Stage6shuffle[0])
            del Stage6shuffle[0]
        return
    return
def eight_step():       #reverse 2 second half and riffle
    firsthalf = []
    secondhalf = []
    secondhalfrev = []
    z = 0
    q = len(Stage7shuffle)
    if TFL[7] == "T":
        if q % 2 == 0:
            a = q / 2
            firsthalf = Stage7shuffle[0:a]
            secondhalf = Stage7shuffle[a:q]
            w = len(secondhalf)
            while w > 0:
                secondhalfrev.append(secondhalf[w - 1])
                del secondhalf[w - 1]
                w = w - 1
            z1 = len(secondhalfrev)
            while z < z1:
                Stage8shuffle.append(secondhalfrev[z])
                Stage8shuffle.append(firsthalf[z])
                z = z + 1
        else:
            Stage7shuffle.append("a")
            q = len(Stage7shuffle)
            e = len(Stage7shuffle) / 2
            firsthalf = Stage7shuffle[0:e]
            secondhalf = Stage7shuffle[e:q]
            w = len(secondhalf)
            while w > 0:
                secondhalfrev.append(secondhalf[w - 1])
                del secondhalf[w - 1]
                w = w - 1
            z1 = len(secondhalfrev)
            while z < z1:
                Stage8shuffle.append(secondhalfrev[z])
                Stage8shuffle.append(firsthalf[z])
                z = z + 1
            Stage8shuffle.remove("a")
    else:
        while len(Stage7shuffle) >= 1:
            Stage8shuffle.append(Stage7shuffle[0])
            del Stage7shuffle[0]
        return
    return
def nine_step():        #reverse hindu -- reverse all series first then do hindu
    tre = len(Stage8shuffle)
    ninrev = []
    if TFL[8] == "T":
        while tre > 0:
            ninrev.append(Stage8shuffle[tre - 1])
            del Stage8shuffle[tre - 1]
            tre = tre - 1
        firstpack = []
        secondpack = []
        thirdpack = []
        stage1 = []
        firstpack2 = []
        secondpack2 = []
        thirdpack2 = []
        length = len(ninrev)
        if length % 3 == 2:
            ninrev.append("a")
            ninrev.append("b")
            length = len(ninrev)
            a = length / 3
            firstpack = ninrev[0:a]
            secondpack = ninrev[a:2 * a]
            thirdpack = ninrev[2 * a:length]
            while len(secondpack) >= 1:
                stage1.append(secondpack[0])
                del secondpack[0]
            while len(firstpack) >= 1:
                stage1.append(firstpack[0])
                del firstpack[0]
            while len(thirdpack) >= 1:
                stage1.append(thirdpack[0])
                del thirdpack[0]
            length = len(stage1)
            a = length / 3
            firstpack2 = stage1[0:a]
            secondpack2 = stage1[a:2 * a]
            thirdpack2 = stage1[2 * a:length]
            while len(firstpack2) >= 1:
                Stage9shuffle.append(firstpack2[0])
                del firstpack2[0]
            while len(thirdpack2) >= 1:
                Stage9shuffle.append(thirdpack2[0])
                del thirdpack2[0]
            while len(secondpack2) >= 1:
                Stage9shuffle.append(secondpack2[0])
                del secondpack2[0]
            Stage9shuffle.remove("a")
            Stage9shuffle.remove("b")
        elif length % 3 == 1:
            ninrev.append("a")
            length = len(ninrev)
            a = length / 3
            firstpack = ninrev[0:a]
            secondpack = ninrev[a:2 * a]
            thirdpack = ninrev[2 * a:length]
            while len(secondpack) >= 1:
                stage1.append(secondpack[0])
                del secondpack[0]
            while len(firstpack) >= 1:
                stage1.append(firstpack[0])
                del firstpack[0]
            while len(thirdpack) >= 1:
                stage1.append(thirdpack[0])
                del thirdpack[0]
            length = len(stage1)
            a = length / 3
            firstpack2 = stage1[0:a]
            secondpack2 = stage1[a:2 * a]
            thirdpack2 = stage1[2 * a:length]
            while len(firstpack2) >= 1:
                Stage9shuffle.append(firstpack2[0])
                del firstpack2[0]
            while len(thirdpack2) >= 1:
                Stage9shuffle.append(thirdpack2[0])
                del thirdpack2[0]
            while len(secondpack2) >= 1:
                Stage9shuffle.append(secondpack2[0])
                del secondpack2[0]
            Stage9shuffle.remove("a")
        else:
            length = len(ninrev)
            a = length / 3
            firstpack = ninrev[0:a]
            secondpack = ninrev[a:2 * a]
            thirdpack = ninrev[2 * a:length]
            while len(secondpack) >= 1:
                stage1.append(secondpack[0])
                del secondpack[0]
            while len(firstpack) >= 1:
                stage1.append(firstpack[0])
                del firstpack[0]
            while len(thirdpack) >= 1:
                stage1.append(thirdpack[0])
                del thirdpack[0]
            length = len(stage1)
            a = length / 3
            firstpack2 = stage1[0:a]
            secondpack2 = stage1[a:2 * a]
            thirdpack2 = stage1[2 * a:length]
            while len(firstpack2) >= 1:
                Stage9shuffle.append(firstpack2[0])
                del firstpack2[0]
            while len(thirdpack2) >= 1:
                Stage9shuffle.append(thirdpack2[0])
                del thirdpack2[0]
            while len(secondpack2) >= 1:
                Stage9shuffle.append(secondpack2[0])
                del secondpack2[0]
            return
    else:
        while len(Stage8shuffle) >= 1:
            Stage9shuffle.append(Stage8shuffle[0])
            del Stage8shuffle[0]
        return
    return
def ten_step():         #reverse both half and do riffle
    tre = len(Stage9shuffle)
    tenone = []
    firsthalf = []
    secondhalf = []
    z = 0
    if TFL[9] == "T":
        while tre > 0:
            tenone.append(Stage9shuffle[tre - 1])
            del Stage9shuffle[tre - 1]
            tre = tre - 1
        lenght = len(tenone)
        if lenght % 2 == 0:
            a = lenght / 2
            firsthalf = tenone[0:a]
            secondhalf = tenone[a:lenght]
            while z < a:
                Stage10shuffle.append(secondhalf[z])
                Stage10shuffle.append(firsthalf[z])
                z = z + 1
        else:
            tenone.append("a")
            lenght = len(tenone)
            a = lenght / 2
            firsthalf = tenone[0:a]
            secondhalf = tenone[a:lenght]
            while z < a:
                Stage10shuffle.append(secondhalf[z])
                Stage10shuffle.append(firsthalf[z])
                z = z + 1
            Stage10shuffle.remove("a")
    else:
        while len(Stage9shuffle) >= 1:
            Stage10shuffle.append(Stage9shuffle[0])
            del Stage9shuffle[0]
        return
    return

def codeworks():
    RNG_NORMAL()
    if TFL.count("T") >= 6:
        print "Input code is:",codelistinit
        one_step()
        two_step()
        three_step()
        four_step()
        five_step()
        six_step()
        seven_step()
        eight_step()
        nine_step()
        ten_step()

        key = len(TFL)
        while key > 0:
            TFLkey.append(TFL[key - 1])
            del TFL[key - 1]
            key = key - 1

        print "Output code is:", Stage10shuffle
        print "Key for decoding is:",TFLkey
        print "Output files are created succesfully"
        keyoutstr = "".join(TFLkey)
        keyoutint = int(''.join(map(str,Stage10shuffle)))
        K = open("Key_Code.txt", "w")
        with open('Output_Code.txt', 'w') as f:
            f.write('%d' % keyoutint)
        K.write(keyoutstr)
        return
    else:
        cle = len(TFL)
        while cle > 0:
            del TFL[cle - 1]
            cle = cle - 1
        codeworks()
        return

codeworks()



1 8 0 4 2 0 1 8