from nose.tools import*
import DiskMonitor.GeneralFunctions as GF

def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"
	
def test_basic():
	print "I RAN!"

def test_pareto_discrimination():
	AFactor = 100
	Value = 10
	Stop = AFactor/Value
	for i in range(1,15):
		TestVar, AFactor = GF.pareto_discrimination(Value, AFactor)
		if i <= Stop + 1:
			assert_true(TestVar)
		else:
			assert_false(TestVar)
			
def test_size_discrimination():
	AFactor = 100
	Value = 75
	for i in range(1,2):
		TestVar, AFactor = GF.size_discrimination(Value, AFactor)
		Value = Value + Value
		if i == 1:
			assert_false(TestVar)
		else:
			assert_true(TestVar)