"# SortSigtestEyes" 

This script will only run with Python 3

Copy move_file.py into the base directory of your sigtest eye diagram results.

Running move_file.py will create a new folder "Comparison" and populate it with eye diagrams for comparison. These eyes will be divided by Generation and then by Preset.

Before running move_file.py, check that each subfolder is appropriately named, because it will be used as a prefix when copying each *.png file.
For example, if you have two subfolders Lane0 and Lane1 and each has two files Gen3_Preset0.png and Gen3_Preset1.png, the result will be as follows:

Comparison\Gen3\P0:
	Lane0_Gen3_Preset0.png
	Lane1_Gen3_Preset0.png

Comparison\Gen3\P1:
	Lane0_Gen3_Preset1.png
	Lane1_Gen3_Preset1.png
