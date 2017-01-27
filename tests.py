import unittest
import io
import symmetrize_xyz
import xyz_n


xyz_methylene = '''\
 C        0.0000000000   0.0000000000  -0.1584796219
 H       -0.8569426061   0.0000000000   0.5695694992
 H        0.8569426061  -0.0000000000   0.5695694992
'''

xyz_ammonia = '''\
N  0.0000000000   0.0000000000   0.0000000000
H -0.4882960784   0.8457536168   0.0000000000
H -0.4882960784  -0.8457536168   0.0000000000
H  0.9765921567   0.0000000000   0.0000000000
'''


class TestSymmetrize(unittest.TestCase):
    xyz_data = None
    pgrp = None
    def setUp(self):
        self.xyz = xyz_n.read_xyz_obj(io.StringIO(self.xyz_data))


class TestMethylene(TestSymmetrize):
    xyz_data = xyz_methylene
    pgrp = 'C2v'


class TestAmmonia(TestSymmetrize):
    xyz_data = xyz_ammonia
    pgrp = '?'


if __name__ == '__main__':
    unittest.main()
