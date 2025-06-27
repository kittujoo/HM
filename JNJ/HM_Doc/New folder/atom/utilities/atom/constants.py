import os
from os.path import dirname as up

ATOM_ROOT_FOLDER = up(up(up(os.path.realpath(__file__))))
RESULTS_FOLDER = os.path.join(ATOM_ROOT_FOLDER, 'results')
