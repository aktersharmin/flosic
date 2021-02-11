import os, sys
from glob import glob

dirs = sorted(glob('*/'))
subdirs = ['x', 'x-', 'y', 'y-', 'z', 'z-']
for dir in dirs:
  vals = []
  for subdir in subdirs:
    dipole_file = dir + subdir + '/DIPOLE'
    if not os.path.isfile(dipole_file):
      print(dipole_file + " is not available")
      # print(dir[:-1] + ','*6)
      continue
    with open(dipole_file) as f:
      content = f.read().splitlines()[0].replace('D', 'E').split(' ')
    content = [c for c in content if c != '']
    val = None
    if subdir[0] == 'x':
      val = content[0]
    elif subdir[0] == 'y':
      val = content[1]
    else:
      val = content[2]

    vals.append(val)

  print(dir[:-1] + ': ' + ','.join(vals))
