# -*- coding: utf-8 -*-
"""
    . Script to Build logs sequences . Deal with  True resistivities get 
    on the survey or with others firms. Indeed the input  resistivities values
    into our model,could yield an accuracy underground map.
    The challenge to build a pseudolog is to know how the layers are disposal 
    in underground so to emphasize the large conductive zone  especially 
    in the case of groundwater exploration. 
    
    Program works in combinaison with geophysic data especially Occam 2D 
    inversion data,  with geological data. Actually the program deals only
    with  Occam 2D inversion files or  Bo Yang (x,y,z) files and outputs some 
    model files for other external softares such as Golder sofware('surfer'). 
    If user has a golder software installed on its computer,  he can use  the 
    output files generated to produce 2D map so to compare both maps: 
    the model map and detail-sequences map to see the difference  between
    the "calculated model" and "pseudosequences model" which could match
    better the underground. When `step_descent` parameter is small,
    the detail sequences trends to the model map. So more geological data
    are, better the accuracy of detail sequences logs should be. 
    
    Customize your sequences(layers) using the matplotlib hatches and patterns.

Created on Mon Feb 15 13:25:21 2021
@author:K.L ~ @Daniel03

"""
import os 
from pycsamt.viewer.plot import Plot2d 

# path to OCCAM 2D folder 
path = 'data/occam2d'
#path2 =os.path.join(os.environ ['pyCSAMT'], 'data', '_iter2dat_2')

#savefigure =None              # path to save fig
savepath =None
# scale the output data 
scale= None                # if None : default is "m" .can be [m|km]

#  Maximum depth investigation  for CSAMT ,
# if not provided , will set to 1km 
#  can be float like 1000 = 1km 
DOI = '1km'                


# provided station id or number
# can be the station id like "S22" or 23 means the site number 23
station_to_plot = -1      

# Main parameters : value must be less or eagl of DOI. 
#if step =DOi WILL return your Occam model files.
STEP_DESCENT = 200.         # float value. Step to cut out data and to  
                            # force resistivites calcualted 
                            # to match the reference data as input resistivities 
                            # if not provided the step will be 20% of D0I

# Truth resistivities values otained on the sites or from other companies
#COMPULSORY parameter  
#INPUT_RESISTIVITIES = [312, 525, 1235., 2202., 4000, 7000.]   
# list of resistivites values : order is insensitives 
INPUT_RESISTIVITIES = [66,70, 180, 1000, 3000, 10000, 20000] 

# Truth layer names if given must match the input resistivities 
# if nname of layers not provided, program will seek in dataBase to find
# the name of layer whom its resistivities is much closer to abose 
#INPUT_LAYERS = ['alluvium', 'amphibolite',
#                'altered rock','augen gneiss', 'granite'] 
INPUT_LAYERS = ['river zone', 'fracture zone' , 'granite ',
                'Most Weathered', 'Less Weathered'] #                                              

#-----Read Occam 2D output files  ---------
# path to occam Data file
path_to_occam_data='OccamDataFile.dat'

# path to occam Mesh file 
path_to_occam_mesh = 'Occam2DMesh'

# path to occam Model file 
path_to_occam_model = 'Occam2DModel'
# path to Occam Iteration file 
path_to_occam_iter='ITER17.iter'

# ---------------Read with Iter2DAT FILE ------------------

# see Occam_module Iter2Dat to see what file is it 

#x, y, z model file 
iter2dat_fn = 'iter17.2412.dat'
# station location file 

bln_file = 'iter17.2412.bln'

# Matplotlib properties to customize plots 

station_label_rotation = None 
show_grid =True 
font_size = 8. 
lc = 'r'
fig_size =[5,5]
markeredgecolor ='k'
markerfacecolor ='k'

average_curve_color = (0.5, 0.8, 0.)
sequence_curve_color = 'blue'
font_dict_site = {'size': 8, 
                  'color':'saddlebrown', 
                  'weight': 'bold', 
                  'style': 'italic'}

#plot style 
plotStyle ="pcolormesh"            # if None Default is 'pcolormesh', can be 
                                    #["imshow"]
unknow_layer_color=  'white'
unknow_layer_pattern= '//.'
# can use other matplotlib to customize your plot 

#----------------define plot 2D object ----------------------
plot2d_obj = Plot2d(station_label_rotation=station_label_rotation , 
                    show_grid= show_grid , 
                    font_size =font_size , 
                    lc=lc , 
                    fig_size= fig_size, 
                    markerfacecolor=markerfacecolor , 
                    markeredgecolor=markeredgecolor )

plot2d_obj.plot_Pseudolog( station_id= station_to_plot, 
                            input_resistivities=INPUT_RESISTIVITIES, 
                            input_layers =INPUT_LAYERS ,
                            step_descent =STEP_DESCENT,
                            doi =DOI, 
                            mesh_fn = os.path.join(path , path_to_occam_mesh),
                            iter_fn = os.path.join(path , path_to_occam_iter), 
                            model_fn =os.path.join(path, path_to_occam_model) , 
                            data_fn =os.path.join(path, path_to_occam_data ),

                            plot_style= plotStyle ,
                            scale =scale, 
                            lc_AD_curves= (average_curve_color, sequence_curve_color),
                            # iter2dat_fn = os.path.join(path2 , iter2dat_fn),
                            # bln_fn = os.path.join(path2 , bln_file),
                            font_dict_site=font_dict_site, 
                            )

    



