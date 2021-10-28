#coding: utf-8
import urllib


class TestCase (object):
	def __init__(self,name):
		self.name=name
	def setUp(self):
		pass
	def run(self):
		#TestCase wo tukuttara name ga arutokoroni idou
		#self.testMethod()
		self.setUp()
		method=getattr(self,self.name)
		method()
		
class WasRun (TestCase):
	def setUp(self):
		self.wasRun=False
		self.wasSetUp=True
	def testMethod(self):
		self.wasRun=True
								
class TestCaseTest(TestCase):
	def setUp(self):
		self.test=WasRun('testMethod')
	def testRunning(self):
		self.test.run()
		assert(self.test.wasRun)
		print('testRunning is pass')
	def testSetUp(self):
		self.test.run()
		assert(self.test.wasSetUp)
		print('testSetUp is pass')




#test method wo yobidasu - TestCase no run wo yobu
#setUp wo jikkousuru - TestCase no setUp wo yobu


class myTestCase (object):
	def __init__(self):
		self.flag_setUpRun=False
		self.flag_RunRun=False
	def setUp(self):
		self.flag_setUpRun=True
	def run(self):
		self.flag_RunRun=True


class myTestCase_Test (object):
	def __init__(self):
		self.test=myTestCase()
		
	def testRunning(self):
		self.test.run()
		assert(self.test.flag_RunRun)
		print('testRunning is pass')
	def testSetUp(self):
		self.test.setUp()
		assert(self.test.flag_setUpRun)
		print('testSetUp is pass')







if __name__ == '__main__':
	print('main test')
	
	
	TestCaseTest('testRunning').run()
	TestCaseTest('testSetUp').run()
	print('end')
	

	myTestCase_Test().testRunning()
	myTestCase_Test().testSetUp()	
	
	
	
	
	
	
	
	
	
	
