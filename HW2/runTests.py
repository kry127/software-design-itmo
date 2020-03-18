import unittest as unittest
import io
import os
from contextlib import redirect_stdout
from src.parser import Parser


class CdLsTest(unittest.TestCase):
    '''Данный класс тестирует в совокупности cd и ls'''
    def __init__(self, *args):
        super().__init__(*args)
        self.parser = Parser()
        self.init_root_dir = os.getcwd()
        self.init_root_dir += '\\test\\'
        self.run_cmd(f"cd {self.init_root_dir}")

    def setUp(self):
        self.run_cmd(f'cd "{self.init_root_dir}"')

#    def test_cd_parent(self):
#        self.assertNotEqual("Incorrect arguments: ['..']", self.run_cmd("cd ..").strip())

    def test_cd_inexistent(self):
        self.assertEqual("Incorrect arguments: ['kek']", self.run_cmd("cd kek").strip())

    def test_ls1(self):
        result = self.run_cmd("ls")
        result = set(result.split('\n'))
        result.remove('')
        self.assertEqual({'subDir1', 'subDir2', 'testDir', 'file1.txt', 'file2.txt', 'file3.txt'}, result)

    def test_ls2(self):
        result = self.run_cmd("ls subDir1")
        result = set(result.split('\n'))
        result.remove('')
        self.assertEqual({'ghhffg.txt'}, result)

    def test_ls3(self):
        result = self.run_cmd("ls subDir2")
        result = set(result.split('\n'))
        result.remove('')
        self.assertEqual({'report.txt', 'unknown.exe'}, result)

    def test_ls_error(self):
        self.assertEqual("Incorrect arguments: ['subDir3']", self.run_cmd("ls subDir3").strip())
        self.assertEqual("Incorrect arguments: ['subDir1', 'subDir2']", self.run_cmd("ls subDir1 subDir2").strip())

    def run_cmd(self, cmd):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.parser.parse(cmd)
            return buf.getvalue()