import unittest

from md5 import MD5


class TestMD5(unittest.TestCase):
    def test_md5(self):
        expectations = {
            "": "e24bcbbc2075cef9f121e0cf69d117d9",
            "a": "fefe4b05cb78f877d4304f37108ce7b4",
            "abhishek": "1331342478b9e112d0dd465e4d60a48d"

        }

        for string, md5_hash in expectations.items():
            with self.subTest(string=string, md5_hash=md5_hash):
                self.assertEqual(MD5.hash(string), md5_hash)
