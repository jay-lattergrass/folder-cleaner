import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


class TestDirectoryPerms(unittest.TestCase):
    def testRootDirAccess(self):
        '''
        Tests whether the provided root directory can be accessed.
        '''
        import settings

        result = os.access(settings.ROOT_DIR, os.F_OK)
        self.assertTrue(result)

    def testRootDirReadAccess(self):
        '''
        Tests whether the provided root directory can be written to.
        '''
        import settings

        result = os.access(settings.ROOT_DIR, os.R_OK)
        self.assertTrue(result)

    def testRootDirWriteAccess(self):
        '''
        Tests whether the provided root directory can be accessed.
        '''
        import settings

        result = os.access(settings.ROOT_DIR, os.W_OK)
        self.assertTrue(result)

    def testTargetDirAccess(self):
        '''
        Tests whether the provided target directory can be accessed.
        '''
        import settings

        result = os.access(settings.TARGET_DIR, os.F_OK)
        self.assertTrue(result)

    def testTargetDirReadAccess(self):
        '''
        Tests whether the provided target directory can be accessed.
        '''
        import settings

        result = os.access(settings.TARGET_DIR, os.R_OK)
        self.assertTrue(result)

    def testTargetDirWriteAccess(self):
        '''
        Tests whether the provided target directory can be written to.
        '''
        import settings

        result = os.access(settings.TARGET_DIR, os.W_OK)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
