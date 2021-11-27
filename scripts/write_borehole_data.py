# -*- coding: utf-8 -*-
"""
    . Script to Build Drill data . Deal only with OasisMonj Drillhole modules 
    User can build manually it own drill files by enter layer names as well has 
    the depth . program will recohnize the top and the bottom of the stratigraphy 
    sequences. User can also provided a typical file  parser : User must folow 
    how file is arranged .Once  the script is called , it will recognize the file 
    to build all the Drill data.' An examples of `parser file` are located in 
    ::r'//pyCSAMT/geodrill/data/drill_example_files'::
    Later , an other simple parser file will propose . 

Note: If an error occurs like 
    ModuleNotFoundError: No module named 'openpyxl'
    Please install `openpyxl` nanually using: 
        <python -m pip install openpyxl>
    before running this script 
Created on Sun Feb 21 19:26:21 2021

"""

import os 
from pycsamt.geodrill.geocore import Drill 

path_to_parser_files ='data/drill_example_files'

#name of parserfile : eg: data collected from `location `nble`. 

parser_file ='nbleDH.csv'
#savepath : path to save outfile borehole files 
savepath = None 
# data2zrite : whick kind of data do you want to output ?
# borehole geology? borehole geochemistry sample ? or borehole survey elevation ? 
kind_of_data2output = '*'       # can be '5',"all",
                                # `Collar`,`Geology`,`Sample`,`Elevation`,`Azimuth`
                                #            or   `*`.
                                #`*` is a joker , mean output all data .

# if set to False , user will add step by step all data with the layer thicknesses 
build_borehole_auto=True

borehole_obj = Drill (well_filename= os.path.join(path_to_parser_files,
                                                  parser_file), 
                   auto= build_borehole_auto)
borehole_obj.writeDHData(data2write=kind_of_data2output, 
                         savepath  = savepath )

