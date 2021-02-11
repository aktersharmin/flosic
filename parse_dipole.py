# This script reads the DIPOLE file from all subdirectories in the current directory.
# Author: Sharmin Akter
# Last modified: 02/10/2021

import os, sys
from glob import glob


if __name__=="__main__":
  if len(sys.argv) != 2:
    print("Usage: python parse_dipole.py <dirname>")
    sys.exit(1)

  dir_name = sys.argv[1]
  dirs = sorted(glob(dir_name + '/*/'))
  subdirs = ['x', 'x-', 'y', 'y-', 'z', 'z-']
  output = []
  for dir in dirs:
    vals = []
    for subdir in subdirs:
      dipole_file = dir + subdir + '/DIPOLE'
      if not os.path.isfile(dipole_file):
        print(dipole_file + " is not available")
        continue
      with open(dipole_file) as f:
        content = f.read().splitlines()[0].replace('D', 'E').split(' ')
      content = [c for c in content if c != '']
      assert len(content) == 3
      val = None
      if subdir[0] == 'x':
        val = content[0]
      elif subdir[0] == 'y':
        val = content[1]
      else:
        val = content[2]

      vals.append(val)
    output.append([os.path.basename(os.path.dirname(dir)),] + vals)

  output = sorted(output, key=lambda s: s[0].lower())
  output = [','.join(s) for s in output]
  print('\n'.join(output))
  
