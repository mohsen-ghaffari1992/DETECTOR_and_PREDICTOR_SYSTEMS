# ###############################################
#   PREDICTOR & DETECTOR SYSTEMS CODED IN PYTHON 3.7
#
#   Programmer:
#       Mohsen Ghaffari
#       &
#       Mansoor Davoodi
#
#
#   Jan, 2021
#
# ###############################################
#
#   TO RUN THE CODE:
#
#       if you are using more than one version of pyhton in your system:
#           python3 main.py data
#
#       otherwise:
#           python main.py data
#
# ###############################################

from initialValues import InitialValues
from learner import Learner
from tester import Tester
import sys

class Main:
    def __init__(self):
        #Initialization class
        self.initialvalue = InitialValues(sys.argv[1])
        #Detector system class
        self.learn = Learner(self.initialvalue)
        #Predictor system class
        self.test = Tester(self.learn)
        
    
Main()
