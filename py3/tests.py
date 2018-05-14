"""
PyBC/ python -m py3.tests
"""

# %% Imports

import unittest
import coverage

from pyx.utils import hash_SHA256, hash_SHA256_twice
from py3.Chain import Dat
from py3.Block import TxOut


# %% Tests for functions

class TestHashes(unittest.TestCase):
    """
    Test hash function in pyx.utils in python 3 environment
    """
    def setUp(self):
        pass

    def test_hash_SHA256_s1(self):
        """
        A test test to test testing
        """
        inp = b'\xf3\x17\x9d\x8c\xd7\xbd\x03'

        exp = b"\xd8\xc6\xaa\x92\x04\x94\xc0kK\xf8\xf8\xf9\xdd"\
            b"\x96fhW\xa0,[\x84\xd0\xc3\x80Uu\xf8\xdb\xb2\xde`\xd5"

        self.assertEqual(hash_SHA256(inp), exp)

    def test_hash_SHA256_twice_s1(self):
        """
        """
        inp = b'\xf3\x17\x9d\x8c\xd7\xbd\x03'

        exp = b"\xb8xn\xdc\x07\xa2\x19\x1e\xd8\xa5\x18\xa3"\
            b"\x8cc\xdf\xda\xf7\xde\xb3n\x91\x00\xfc)\x90P<\xbdzE\xff\xf6"

        self.assertEqual(hash_SHA256_twice(inp), exp)

    def tearDown(self):
        pass


# %% Tests for specific blocks (genesis etc.)

class GenesisTest(unittest.TestCase):
    """
    Test parsing of genesis block
    """

    def setUp(self):
        """
        Load genesis block from Blocks/blk0000.dat
        """
        f = 'Blocks/blk00000.dat'
        dat = Dat(f,
                  verb=1)

        dat.read_next_block()
        self.dat = dat

    def test__hash(self):
        h = b"o\xe2\x8c\n\xb6\xf1\xb3r\xc1\xa6\xa2F\xaec\xf7O\x93\x1e\x83e"\
            b"\xe1Z\x08\x9ch\xd6\x19\x00\x00\x00\x00\x00"
        self.assertEqual(h, self.dat.blocks[0]._hash)

    def test_hash(self):
        h = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
        self.assertEqual(h, self.dat.blocks[0].hash)

    def test__merkleRootHash(self):
        h = b";\xa3\xed\xfdz{\x12\xb2z\xc7,>gv\x8fa\x7f\xc8"\
            b"\x1b\xc3\x88\x8aQ2:\x9f\xb8\xaaK\x1e^J"
        self.assertEqual(h, self.dat.blocks[0]._merkleRootHash)

    def test_merkleRootHash(self):
        h = '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
        self.assertEqual(h, self.dat.blocks[0].merkleRootHash)

    def tearDown(self):
        """
        Close opened file
        """
        self.dat.mmap.close()


# %% Tests for classes

class TestTrans(unittest.TestCase):
    """
    Test py3.Block.Trans class methods
    """
    def setUp(self):
        """
        Prepare dummy object
        """
        pass

    def tearDown(self):
        pass


class TestTxOut(unittest.TestCase):
    """
    Test py3.Block.TxOut class methods
    """
    def setUp(self):
        pass

    def test_PK2Addr(self):
        """
        Test static method to extract adress from public key
        """
        pk = "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0e"\
            "a1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4"\
            "c702b6bf11d5f"
        exp = b'1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'

        self.assertEqual(exp, TxOut.PK2Addr(pk))

    def tearDown(self):
        pass


# %% Run

if __name__ == '__main__':

    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()
    cov.html_report(directory='covhtml')
