from distutils.core import setup # Need this to handle modules
import py2exe 
import pandas as pd 
import numpy as np 
import TimeLog
import os 
import time
from datetime import datetime


setup(console=['JobSearchIndexMain.py'])