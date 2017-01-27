""" dealing with xyz files """
import logging
from numpy import array
import re
from elements import element_to_atomic_number

_xyz_parser = re.compile(' *([A-Za-z0-9]+) +([^ ]+) +([^ ]+) +([^ ]+)')
_log = logging.getLogger('xyz')
def read_xyz(fname):
    """ return a sequence for the molecule specified in `fname`.
    Conventional XYZ with two-line header as well as coordinate only XYZ are supported.
    Element labels are converted to atomic numbers when necessary. """
    with open(fname, 'r') as f:
        return read_xyz_fobj(f)


def read_xyz_fobj(fobj):
    first_line = f.readline().strip()
    if first_line.isdigit(): 
        _log.info('Reading conventional XYZ %s (%s)', f.readline().strip(), fname)
    else:
        _log.info('Reading XYZ-only (%s)', fname)
        f.seek(0)
    r=[]
    for ln in f.readlines():
        m = _xyz_parser.match(ln)
        if m.group(1).isdigit():
            r.append([int(m.group(1)), array((float(m.group(2)),
                float(m.group(3)),float(m.group(4))))])
        else:
            r.append([element_to_atomic_number(m.group(1)), array((float(m.group(2)),
                float(m.group(3)),float(m.group(4))))])
    return tuple(r)


def write_xyz_coord(element, coord, outf):
    outf.write('%2d %f %f %f\n'%((element,)+tuple(coord)))


def write_xyz_line(xyz, i, outf):
    write_xyz_coord(xyz[i][0], xyz[i][1], outf)


def write_xyz(xyz, outf, header=True):
    if header:
        outf.write("%d\n\n"%len(xyz))
    for i in range(len(xyz)):
        write_xyz_line(xyz, i, outf)
    
