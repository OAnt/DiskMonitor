import os
import DirectorySizeOrdering as DSO
import GeneralFunctions as GF
from Data import *
from DiskMonitor import disk_monitor
from sys import argv, exit

####################################################################
#### Input collection and analysis so as to have a functioning    #### 
#### procedure even if given inputs are correctly formated        ####
####################################################################



Analysis = "directorysizeordering"
Discrimination = "pareto"
Size = None
RootPath = []
Unit = 'mb'

InputVerification = [
                    [AnalysisDict, Analysis], 
                    [DiscFuncDict, Discrimination], 
                    [UnitDict, Unit]
                    ]

def word_analysis(Input):
    """
    compare an input with possible ones to ensure its existance
    or propose other possibilities if not recognized
    """
    LetterList = list(Input)
    TempNum = LetterList[0]
    Num = False
    while True:
        try:
            #print "TempNum", TempNum
            Num = int(TempNum)
            #print Num
            TempNum = "".join([str(Num), LetterList[1]])
        except ValueError:
            #print "Broken", Num
            break
        LetterList.pop(0)
        
    AUnit = "".join(LetterList)
    #print AUnit
    if AUnit in UnitDict.keys():
        global Size
        Size = Num
        global Unit
        InputVerification[2][1] = AUnit
    else:
        print "Not Considered:", Input
    

def input_analysis(Item):
    """
    Analyses an input word to determine what it is and what to do
    with it
    """
    Input = Item.lower()
    ToAnalyse = True
    try:
        global Size
        Size = int(Input)
    except ValueError:
        for Item in InputVerification:
            if Input in Item[0].keys():
                Item[1] = Input
                ToAnalyse = False
        if ToAnalyse:
            word_analysis(Input)

Scrypt = argv.pop(0)


for Item in argv:
    if os.path.isdir(Item) or Item == "-help":
        RootPath.append(Item)
    else:
        input_analysis(Item)

Analysis = InputVerification[0][1]
Discrimination = InputVerification[1][1]
Unit = InputVerification[2][1]

if "-help" in RootPath:
    for Item in HelpContext:
        print Item
    exit()
elif not(RootPath):
    Input = raw_input("Specify a valid path\n>")
    if os.path.isdir(Input):
        RootPath.append(Input)
    else:
        exit("No Path")

############################################################
#### Here begins the actual analysis using the inputs    ####
############################################################



for Item in RootPath:

    FinalQuantity, FileQuantity, EndSize, TotalSize, EndList, Ending, Files, Skipt = disk_monitor(Item, Analysis, Discrimination, Size, Unit)
    
    print FinalQuantity, "Folders out of", FileQuantity, "Folders"
    print GF.conversion_soft(EndSize), "Out of", GF.conversion_soft(TotalSize)
    for Item in EndList:
        print Item[0], GF.conversion_soft(Item[1])
    print "Calculaton time:", Ending, "s"
    print "Total files: ", Files
    print Skipt, "Folder skipt"