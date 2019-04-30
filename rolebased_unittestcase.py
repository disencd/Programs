import unittest

class CommonTests(object):
    def test_1_Common(self):
        print('Calling BaseTest:testCommon 1 - {}'.format(self.role))

    def test_2_Common(self):
        print('Calling BaseTest:testCommon 2 - {}'.format(self.role))

    def test_3_Common(self):
        print('Calling BaseTest:testCommon 3 - {}'.format(self.role))

class OrgAdminTest(unittest.TestCase, CommonTests):

    @classmethod
    def setUpClass(cls):
        print("OrgAdmin setUpClass \n")
        cls.role = "OrgAdmin"

class OrguserTest(unittest.TestCase, CommonTests):

    @classmethod
    def setUpClass(cls):
        print("Orguser setUpClass \n")
        cls.role = "Orguser"


class SysAdminTest(unittest.TestCase, CommonTests):
    @classmethod
    def setUpClass(cls):
        cls.role = "SysAdmin"
        print("SysAdmin setUpClass \n")


if __name__ == '__main__':
    unittest.main()
