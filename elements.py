""" convert element labels to atomic numbers """

import re

_periodic_system = """
h                                                                                            he
li be                                                                         b  c  n  o  f  ne
na mg                                                                         al si p  s  cl ar
k  ca sc                                           ti v  cr mn fe co ni cu zn ga ge as se br kr
rb sr y                                            zr nb mo tc ru rh pd ag cd in sn sb te i  xe
cs ba la ce pr nd pm sm eu gd tb dy ho er tm yb lu hf ta w  re os ir pt au hg tl pb bi po at rn""".strip()

_atomic_numbers = re.split('[ \n] *', _periodic_system)

def element_to_atomic_number(element_label):
    lower = element_label.lower()
    if lower == 'x' or lower == 'xx' or lower == 'bq':
        return 0
    else:
        return _atomic_numbers.index(lower)+1

def atomic_number_to_element(atomic_number):
    return _atomic_numbers[atomic_number-1].title()
