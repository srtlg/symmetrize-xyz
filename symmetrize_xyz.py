""" employ symmol to symmetrize molecule given as XYZ ensuring point group 

usage
=====

symmetrize_xyz  <xyz-file>  [<tolerance> [<target point-group>]]

"""
import os
import re
import sys
from subprocess import Popen, PIPE
_match_point_group = re.compile('Schoenflies symbol = *([^ ]+)')

from xyz_n import read_xyz


def main(infile, tolerance=0.7, target_point_group='C2h', xyzin=None):
    if xyzin is None:
        xyzin = read_xyz(infile)

    path = os.path.dirname(os.path.abspath(__file__))
    symmol = Popen('%s/symmol' % path, stdin=PIPE, stdout=PIPE)

    symmol.stdin.write(('%d\n%f\n'%(len(xyzin), tolerance)).encode('ascii'))
    for el, coord in xyzin:
        symmol.stdin.write(('%d %f %f %f\n'%((el,)+tuple(coord))).encode('ascii'))
    symmol.stdin.close()

    out = symmol.stdout.read().decode('utf-8')
    print(out, file=sys.stderr)
    symmol.stdout.close()
    m = _match_point_group.search(out)
    if m is None:
        raise RuntimeError('something went wrong')
    if m.group(1) != target_point_group:
        raise AssertionError(infile+' got point group '+m.group(1))
    symmol.wait()


if __name__ == '__main__':
    infile = sys.argv[1]
    tolerance = 0.7 if len(sys.argv) <= 2 else float(sys.argv[2])
    target_point_group = "C2h" if len(sys.argv) <= 3 else sys.argv[3]
    main(infile, tolerance, target_point_group)
    if not os.path.isdir('symmetrized'):
        os.mkdir('symmetrized')
    os.rename('fort.20', 'symmetrized/%s'%sys.argv[1])

