from nose.tools import*
import DiskMonitor.DirectorySizeOrdering as DSO
import DiskMonitor.GeneralFunctions as GF
import os.path


def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"
	
def test_basic():
	print "I RAN!"
	
	
def init_purpose():
	Path = "d:\\Pn\\projects\\PLM"
	zzz = DSO.DirectorySizeOrdering(Path)
	return zzz, [[Path, None]]
	
	
def test_initialization_list():
	Item, TestList = init_purpose()
	Item.initialization_list()
	assert_equal(Item.ListPath, TestList)
	assert_false(Item.ListPath == [])
	
def test_calculate_ListPath():
	Item, TestList = init_purpose()
	Item.initialization_operations()
	Item.filter_ListPath()
	assert_false(Item.ListPath == [])
	for Duet in Item.ListPath:
		assert_true(os.path.isdir(Duet[0]))
		#assert_is_instance(Duet[1], int)
	return Item.ListPath
	
def discrimination(ItemSize, Factor):
	return True, 0
	
def test_main_operations():
	Item, TestList = init_purpose()
	NewList = Item.main_operations(discrimination, 0)
	assert_equal(Item.ListPath, NewList)
	assert_false(Item.ListPath == [])