import os
import random

import networkx as nx
import matplotlib.pyplot as plt
from os import listdir

import sys
import re

current_file_name = sys.argv[0].split('/')[-1]  #return current file name

# ######## Historyjka 1. #########
def extract_filename(file): 
    return file.split(".")[0]  


def get_file_size(file_path): 
    file_path = file_path if file_path.endswith('.py') else './'+file_path+'.py'
    return os.path.getsize(file_path)
