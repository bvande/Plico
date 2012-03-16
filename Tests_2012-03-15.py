# March 15th, 2012
import nose, core
from nose.plugins.attrib import attr
from nose.tools import assert_in

from common import *

@attr(_type="sta")
class TestStatic(core.PilcoTest):
    
    @attr(_area='login')
    def Test_Login(self):
        common.login(self.driver, 'bvandemerwea', 'snoopy')
    
@attr(_type="bug")
class TestBugs(core.PilcoTest):
    pass

@attr(_type="enc")
class TestEnc(core.PilcoTest):
    pass

if __name__ == "__main__":
    nose.run(argv=['-v'])
