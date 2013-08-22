"""This module aims at returning a list of files with their
associated size

aims at locating directories with high density of voluminous files
"""

import os
import GeneralFunctions as GF
import time
import stat

class Algo(object):
	pass
	
class DirectorySizeOrdering(Algo):
	""" This class takes the initial path to give associated
	directories
	
	This object contains methods used in the Algorithm
	"""
	def __init__(self, InitPath):
		# Advanced User Input?
		Item = InitPath.decode('utf_8')
		self.ListPath = [Item]
		self.Size = 0
		self.EndSize = 0
		self.Files = 0
		self.Skipt = 0
	
	def childrens(self,Path,i):
		""" returns same same outputs as os.listdir skipping
		windows error 5 for NTFS junction
		
		Moreover if a folder accessed is denied you'll never be able to
		clean it which is the ultimate goal of using DiskMonitor, so I
		skip windows error 5 access denied (BTW its number is 13 in
		python)
		"""
		#DirList = []
		#FileList = []
		TempSize = 0
		#Beg = time.time()
		i = i+1
		try:
		
			Elements = os.listdir(Path)
			#os.chdir(Path)
			#print Elements
			for Item in Elements:

				ItemPath = "\\".join([Path,Item])
				
				FSObject = os.stat(ItemPath)
				mode = FSObject.st_mode
				if stat.S_ISDIR(mode):
					self.ListPath.insert(i,[ItemPath,None])
					i=i+1
				else:
					#FileList.append(ItemPath)
					self.Files = 1 + self.Files
					TempSize = TempSize + FSObject.st_size

					
		except OSError, E:
			if E.errno == 13:
				print Path, "Skipt because this program is not able to handle NTFS junction or accessed denied"
				self.Skipt = self.Skipt + 1
				#print time.time() - Beg
			elif E.errno == 2:
				print Path, "decoding error"
			else:
				raise E
		
		return TempSize
	
	
	def initialization_list(self):
		Path = self.ListPath[0]
		self.ListPath = [[Path, None]]
	
	def calculate_ListPath(self):
		""" This method unfold the original path to return a list
		containing all sub directories woth their sizes
		"""
		Begin = time.time()
		i = 0
		for FatherItem in self.ListPath:
			
			FatherPath = FatherItem[0]
			FatherItem[1] = self.childrens(FatherPath,i)
			self.Size = self.Size + FatherItem[1]
			i = i + 1
			#FatherItem[1] = GF.calculate_local_size(FileList)
			#for Item in DirList:
			#	self.ListPath.append([Item, None])
		print time.time() - Begin
		return self.ListPath

	def filter_ListPath(self):
		FilteredListPath = [ x for x in self.ListPath if not(x[1] == 0)]
		self.ListPath = FilteredListPath
		return self.ListPath
		
	def discriminate_ListPath(self, AFunction, AFactor):
		SListPath = sorted(self.ListPath, key = lambda Item: Item[1], reverse = True)
		NewList = []
		NewFactor = AFactor
		for Item in SListPath:
			Discrimination, NewFactor = AFunction(Item[1], NewFactor)
			if Discrimination:
				self.EndSize = self.EndSize + Item[1]
				Smth = [Item[0].encode('utf_8'), Item[1]]
				NewList.append(Smth)
			else:
				break
		return NewList
	
	def initialization_operations(self):
		self.initialization_list()
		self.calculate_ListPath()
		return self.ListPath
		
	def main_operations(self, Function, Factor):
		#self.filter_ListPath()
		return self.discriminate_ListPath(Function, Factor)