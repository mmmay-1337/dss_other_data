# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
main_folder = dataiku.Folder("q60yhFTA")
main_folder_info = main_folder.get_info()




# Write recipe outputs
data_processed = dataiku.Folder("ALNoAyyb")
data_processed_info = data_processed.get_info()
