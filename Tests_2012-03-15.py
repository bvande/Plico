# March 15th, 2012
import nose, core
from nose.plugins.attrib import attr

from common.operations import *
from common.homepage import *

@attr(_type="sta")
class TestStatic(core.PilcoTest):
    @attr(_area='login')
    def Test_Login(self):
        assert login(self.driver, self.urls.home, self.data.user, self.data.password)
        assert logout(self.driver, self.urls.home)

    @attr(_area='allinfo')
    def Test_AllInfoSigned(self):
        assert login(self.driver, self.urls.home, self.data.user, self.data.password)
        assert onHomePage(self.driver, 'Signed Document')

    
@attr(_type="bug")
class TestBugs(core.PilcoTest):
    pass

@attr(_type="enc")
class TestEnc(core.PilcoTest):
    pass

if __name__ == "__main__":
    nose.run(argv=['-v'])
