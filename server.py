import sys
import os

def main():
  if len(sys.argv) != 2:
    print "Please enter correct directory name."
    return
  work_dir = sys.argv[1]
  print os.path.isdir(work_dir)
main()