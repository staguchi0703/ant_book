#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2
2 3
3 4
3 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 2
1 3
2 4
4 5
4 6
3 7
7 8
8 9
8 10"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """31
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
8 16
8 17
9 18
9 19
10 20
10 21
11 22
11 23
12 24
12 25
13 26
13 27
14 28
14 29
15 30
15 31"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
