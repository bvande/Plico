# March 15th, 2012

import nose, core
from nose.plugins.attrib import attr

class TestClass(core.PilcoTest):

    @attr(_type='bug', _priority='1', _area='navpane')
    def test_true(self):
        self.driver.get('http://google.com')
        assert True
    
    @attr(_type='enc', _priority="1", _area='navpane')
    def test_yahoo(self):
        self.driver.get('http://yahoo.com')
        assert True

if __name__ == "__main__":
    nose.run(argv=['-v'])
