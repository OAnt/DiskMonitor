"""This module aims at returning a list of files with their
associated size

aims at locating directories with high density of voluminous files
"""

import os
import GeneralFunctions as GF
import time
import stat
from Clistdir import *

class Algo(object):
    pass
    
class DirectorySizeOrdering(Algo):
    """ This class takes the initial path to give associated
    directories
    
    This object contains methods used in the Algorithm
    """
    def __init__(self, InitPath):
        # Advanced User Input?
        Item = InitPath.decode('latin-1')
        self.ListPath = [Item]
        self.Size = 0
        self.EndSize = 0
        self.Files = 0
        self.Skipt = 0
        self.ListCell = {"Path" : 0,
                        "Size" : 1,
                        "Date" : 2,
                        }
        self.DictFile = {}
    
    def childrens(self,Path):
        """ returns same same outputs as os.listdir skipping
        windows error 5 for NTFS junction
        
        Moreover if a folder accessed is denied you'll never be able to
        clean it which is the ultimate goal of using DiskMonitor, so I
        skip windows error 5 access denied (BTW its number is 13 in
        python)
        """
        
        TempSize = 0
        
        Beg = time.time()
        TPath = "".join([Path,"/*"])
        Elements = Wlistdir(TPath)
        
        for Item in Elements:

            
            if Item[2]:
                ItemPath = "/".join([Path,Item[0]])
                self.ListPath.append([ItemPath,None,Item[3]])
                self.DictFile[ItemPath] = []
            else:
                self.Files = 1 + self.Files
                TempSize = TempSize + Item[1]
                self.DictFile[Path].append([Item[0], Item[1], Item[3])
        
        return TempSize
    
    
    def initialization_list(self):
        Path = self.ListPath[0]
        self.ListPath = [[Path, None]]
    
    def calculate_ListPath(self):
        """ This method unfold the original path to return a list
        containing all sub directories woth their sizes
        """
        Begin = time.time()
        for FatherItem in self.ListPath:
            
            FatherPath = FatherItem[0]
            FatherItem[1] = self.childrens(FatherPath)
            self.Size = self.Size + FatherItem[1]
        print time.time() - Begin
        return self.ListPath

    def filter_ListPath(self):
        FilteredListPath = [ x for x in self.ListPath if not(x[1] == 0)]
        self.ListPath = FilteredListPath
        return self.ListPath
        
    def discriminate_ListPath(self, AFunction, AFactor, DKey):
        SListPath = sorted(self.ListPath, key = lambda Item: Item[DKey], reverse = True)
        NewList = []
        NewFactor = AFactor
        for Item in SListPath:
            Discrimination, NewFactor = AFunction(Item[DKey], NewFactor)
            if Discrimination:
                self.EndSize = self.EndSize + Item[DKey]
                Smth = [Item[0].encode('utf8'), Item[DKey]]
                NewList.append(Smth)
            else:
                break
        return NewList
    
    def initialization_operations(self):
        self.initialization_list()
        self.calculate_ListPath()
        return self.ListPath
        
    def main_operations(self, Function, Factor, Type):
        #self.filter_ListPath()
        DKey = self.ListCell[Type]
        return self.discriminate_ListPath(Function, Factor, DKey)