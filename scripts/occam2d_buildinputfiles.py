# -*- coding: utf-8 -*-
"""
    .Script to generate occam2d building inputfiles from 'MTpy' module. 
    MTpy is a magnetotelluric toolbox from authors 
    Alison Louise Kirkby1,Fei Zhang1, Jared Peacock2, 
    Rakib Hassan1, and Jingming Duan is already available. 
    Get the documentation here :.
        - DOI : 10.21105/joss.01358 
        - https://mtpy2.readthedocs.io/en/develop/core.html
        
Created on Wed Apr 15 09:51:02 2015
sets up input files for running 2d occam inversions using 
the occam2d_rewrite module    
    
    if you are already MTpy installed on your computer you may use this script to 
    build occam 2D input files.  if 'MTpy' is not intalled 'pyCSAMT' will try tp 
    install mtpy with its dependancies. To avoid some packages conflits , better 
    approch is to create a virtual environnement to use 'pyCSAMT' . If automatic
    downloading failed ,  you can download MTpy  following steps in MTpy wiki page : 
        https://github.com/MTgeophysics/mtpy/wiki : see intallation
        guide and dependancies.
    
-------------------------------------------------------------------------------
... note:: Note that pycsamt uses `MTpy` for building model inputfiles. 
    So when you build your occam2d  building files on WINDOW, you will meet a 
    little bug into the `MTpy module` such ``FileNotFoundError::
        
        [Errno 2] No such file or directory: '/tmp/profile_angle0.png` 
        relate to `line 1392: plt.savefig('/tmp/profile_angle0.png')`

    Please comment this line of code in the MTpy module and run it again or 
    create a temp directory to hold the profile angle image...
    ... 
-------------------------------------------------------------------------------

Edited  on Mon Feb 15 16:27:49 2021
@author: @Daniel03

"""
import os
from  pycsamt.modeling.occam2d import occam2d_write


#path where edi files are located
edipath =r'C:\Users\Daniel\Desktop\Data\AMT\E1\maskeditest'#'maskedis' #'data/edi' # specify the path where edi is located 
#edipath = r'C:\Users\Daniel\Desktop\Data\AMT\E1\attemps\edi_test'#ediout_batch1'#
 # specify the path to save the Occam 2D inputfiles
savepath = r'C:\Users\Daniel\Desktop\Data\AMT\E1\oci_res100e20'#None# r'C:\Users\Daniel\Desktop\Data\AMT\E1\oci'#'data/occam2dBuildInputfiles'

# occam_output_dataname 
OccamDataFile= 'OccamDataFile.dat'
StartupFile_name= 'Startup'

# if interpolate frequency is set to true , bring limit of interpolatation il logspace frequency 

interpolate_frequency =True 
number_of_frequency = 27#54 # 17            # number of frequency for interpolated 

frequency_interpolate_range = (2,4, number_of_frequency ) # 1.99,4.76(-1, 4, 17) in logspace log10. last item is number of frequency 

# ---> create model 
# number of layers
number_of_model_layers = 31.#31.
# investigation depth 

expected_investigation_depth_or_z_target =550.#1100. #1100. 
# exaggeration depth , must be enough as possible. Around 5* time  the investigation depth 

exaggerate_vertical_z_bottom = 2500.#5000.      # exagerate bottom 

model_first_layer_thickness_z1 = 2.5     # first layer value 

# starting resistivity model value in log 10 res 

starting_res_model_value = 2. 

#number_of_iteration to run 
number_of_iteration_to_run = 500.

# bring geoelectrik strike if provided 
geoelectric_strike = 0.#45. #34.                     # if not given set to 0.
# error floors 
    #----TM mode 
occam_mode ='4'         # must be string 
TM_phase_error= 20.#20.      # in percentage 
TM_res_error =20.#10.        # in percentage 

    #TE mode 
#occam_mode = '5'
TE_phase_error=20.#20.      # in percentage 
TE_res_error =20.#10.        # in percentage 
 
# Configuration mesh features 

model_cell_width = 5. # cell width to aim for, note 
                      # this is the mesh size (2 mesh # blocks per model block)
horizontal_node_x_pad_multiplier = .8#1.7 # controls size of padding
brick_trigger = .5 #1.12            # controls aspect ratio of blocks


occam2d_write.buildingInputfiles(edi_fn =edipath,
                           geoelectric_strike= geoelectric_strike,
                           interpolate_freq= interpolate_frequency, 
                           intp_freq_logspace =frequency_interpolate_range, 
                            iteration_to_run= number_of_iteration_to_run, 
                            resistivity_start = starting_res_model_value, 
                            startup_basename=StartupFile_name,
                            res_tm_err= TM_res_error, 
                            phase_tm_err= TM_phase_error , 
                            occam_mode= occam_mode, 
                            n_layers = number_of_model_layers , 
                            cell_width = model_cell_width , 
                            x_pad_multiplier = horizontal_node_x_pad_multiplier, 
                            trigger =brick_trigger, 
                            z_bottom =exaggerate_vertical_z_bottom , 
                            z1_layer =model_first_layer_thickness_z1, 
                            z_target = expected_investigation_depth_or_z_target, 
                            occamDataFile = OccamDataFile, 
                            savepath = savepath, 
                        )

    

