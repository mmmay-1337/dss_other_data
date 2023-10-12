# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# import the netcdf4 module
import netCDF4 as nc
import io
import shutil
from pathlib import Path

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
folder = dataiku.Folder("q60yhFTA")
folder_info = folder.get_info()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
file_to_download = folder.list_paths_in_partition()[0]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# Firstly download the dataset, as the dataset was in the s3 folder

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#Create temporary directory in /tmp - unsure how to work with nc files yet

with tempfile.TemporaryDirectory() as tmpdirname:
    #Loop through every file of the TF model and copy it localy to the tmp directory
    for file_name in folder.list_paths_in_partition():
        local_file_path = tmpdirname + file_name
        #Create file localy
        if not os.path.exists(os.path.dirname(local_file_path)):
            os.makedirs(os.path.dirname(local_file_path))
        #Copy file from remote to local
        with folder.get_download_stream(file_name) as f_remote, open(local_file_path,'wb') as f_local:
            shutil.copyfileobj(f_remote,f_local)
            data = nc.Dataset(local_file_path)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# do stuff with the dataset
print(data.variables.keys())

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
print(data.variables['PM25_avg'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
data_processed = dataiku.Folder("ALNoAyyb")
data_processed_info = data_processed.get_info()