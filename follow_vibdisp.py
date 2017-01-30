"""
Follow a displacement matrix from a frequency calculation

useful to get out of an saddle point

output is compatible with ORCA multistep xyz files
"""
from __future__ import print_function
import argparse
import sys
from cclib.io import ccopen
from cclib.parser.utils import PeriodicTable


def _parse_arg():
    p = argparse.ArgumentParser()
    p.add_argument('output_file')
    p.add_argument('-m', '--mode', type=int, default=0)
    p.add_argument('-n', '--number_steps', type=int, default=10)
    p.add_argument('-s', '--scale', type=float, default=0.1)
    p.add_argument('-c', '--central', action='store_true', default=False)
    return p.parse_args()


def main():
    args = _parse_arg()
    data = ccopen(args.output_file).parse()
    pt = PeriodicTable()
    natom = data.natom
    element_list = [pt.element[Z] for Z in data.atomnos]
    print('coordinates', data.atomcoords[0], file=sys.stderr)
    print('displacements', data.vibdisps[args.mode], file=sys.stderr)
    for i in range(args.number_steps):
        print(natom)
        if args.central:
            d = (i - args.number_steps / 2.0)
        else:
            d = i
        d *= args.scale
        print('step', i + 1, 'of', args.number_steps, 'with', d)
        for el, coord in zip(element_list, data.atomcoords[0] + d * data.vibdisps[args.mode]):
            print(el, '%15.10f %15.10f %15.10f' % tuple(coord))
        if i == args.number_steps - 1:
            print()
        else:
            print('>')


if __name__ == '__main__':
    main()

