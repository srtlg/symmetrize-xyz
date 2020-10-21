""" employ symmol to symmetrize molecule given as XYZ ensuring point group 

usage
=====

symmetrize_xyz  <xyz-file>  [<tolerance>]

"""
import sys
import numpy as np

from xyz_n import read_xyz, write_xyz
from symmol import symmol


def main(infile, tolerance=0.7, xyzin=None):
    if xyzin is None:
        xyzin = read_xyz(infile)
    
    atomic_numbers = np.array([el for el, coord in xyzin], dtype='i')
    coordinates = np.array([coord for el, coord in xyzin])
    point_group = symmol(tolerance, coordinates.T, atomic_numbers)
    determined_point_group = point_group.decode('ascii')
    if infile is not None:
        outfile = infile.replace('.xyz', '-%s.xyz' % determined_point_group)
        if outfile == infile: outfile += '-' + determined_point_group
        with open(outfile, 'w') as fout:
            write_xyz(list(zip(atomic_numbers, coordinates)), fout)
    else:
        return determined_point_group


if __name__ == '__main__':
    infile = sys.argv[1]
    tolerance = 0.7 if len(sys.argv) <= 2 else float(sys.argv[2])
    main(infile, tolerance)

