import sys

print(sys.argv) # get command line args

sys.modules  # modules which are imported. the format is <k,v>= module name, object

import pprint # formatting the output
pprint.pprint(sys.modules)

pprint.pprint(sys.path) # the path when we are search the sys lib

pprint.pprint(sys.platform)

#sys.exit() #exit the application. codes after this will be not executed

import os

pprint.pprint(os.environ['path']) #get the environ variables

os.system('dir') # execute os command