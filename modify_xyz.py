import sys
import numpy as np
import xyz_n


def op_origin(xyz, idx):
    r = []
    origin = xyz[idx][1]
    for el, coord in xyz:
        r.append((el, coord - origin))
    return tuple(r)


def op_rotate(xyz, matrix):
    r = []
    for el, coord in xyz:
        r.append((el, np.dot(matrix, coord)))
    return tuple(r)


def rotx(angle_rad):
    th = angle_rad
    return np.array((
        (1.0, 0.0, 0.0),
        (0.0, np.cos(th), -np.sin(th)),
        (0.0, np.sin(th), np.cos(th))))


def modify(xyz, args):
    while len(args):
        operation = args.pop(0)
        if operation.lower() == 'origin':
            atom_idx = int(args.pop(0))
            xyz_out = op_origin(xyz, atom_idx)
        elif operation.lower() == 'rotx':
            angle = float(args.pop(0)) * np.pi / 180.0
            xyz_out = op_rotate(xyz, rotx(angle))
        xyz = xyz_out
    return xyz


def main(xyz_file, *args):
    xyz_in = xyz_n.read_xyz(xyz_file)
    xyz_out = modify(xyz_in, list(args))
    xyz_n.write_xyz(xyz_out, sys.stdout)


if __name__ == '__main__':
    main(*sys.argv[1:])
