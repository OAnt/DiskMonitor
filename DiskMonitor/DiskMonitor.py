"""this part contains the algorithm"""

import os
import DirectorySizeOrdering as DSO
import GeneralFunctions as GF
from Data import *
import time

def disk_monitor(RootPath, Analysis, Discrimination, Size, Unit):
	
	Begin = time.time()
	FactorSize = 0
	
	print "Root path:", RootPath
	print "Analysis type:", Analysis
	print "Discrimination function:", Discrimination
	if Discrimination == "limitsize":
		try:
			I = UnitDict[Unit]
			FactorSize = Size * I
			print "Size:", Size, Unit.upper()
		except (KeyError, TypeError) as E:
			if Size == None:
				print "No Size or Unit defined please provide some inputs"
				exit()
			else:
				raise E

	A = AnalysisDict[Analysis](RootPath)
	List = A.initialization_operations()

	FileQuantity = len(List)
	TotalSize = A.Size
	#for Item in List:
		#print TotalSize, "+", Item[1], Item[0]
	#	TotalSize = TotalSize + Item[1]
		
	# Calculating discriminating factor 
	
	
	if Discrimination == "pareto":
		FactorSize = 8*TotalSize/10
		
	EndList = A.main_operations(DiscFuncDict[Discrimination],FactorSize)

	FinalQuantity = len(EndList)
	EndSize = A.EndSize
	Files = A.Files
	#for Item in EndList:
	#	EndSize = EndSize + Item[1]
	
	Skipt = A.Skipt
	
	Ending = time.time() - Begin
		
	return FinalQuantity, FileQuantity, EndSize, TotalSize, EndList, Ending, Files, Skipt

	#return EndSize, FinalQuantity, FileQuantity, EndSize, TotalSize
