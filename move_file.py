#! python3

import os, shutil, fnmatch

def add_folder_prefix(foldername, original_filename):
    """This function will add a prefix to the result names based on the name of the subfolder they are stored in"""
    dirname, basename = os.path.split(foldername)   #split foldername to find parent folder for prefix
    return "{}_{}".format(basename, original_filename)  #return new filename

def make_dir_bins(dir_list, gen3_subdir_list):
    """Creates directory bins for the sorted eyes to be copied to. Receives list of folder names to create"""
    if not os.path.exists(os.path.join(os.getcwd(), "Comparison")):
        os.makedirs(os.path.join(os.getcwd(), "Comparison"))

    cwd = os.path.join(os.getcwd(),"Comparison")    #This creates a subfolder for all of these comparison directories

    # This will check to see if directories in list exist, and create them if they do not
    for directory in dir_list:
        if not os.path.exists(os.path.join(cwd, directory)):
            os.makedirs(os.path.join(cwd, directory))
        if(directory == "Gen3"):
            for subdir in gen3_subdir_list:
                if not os.path.exists(os.path.join(cwd,"Gen3",subdir)):
                    os.makedirs(os.path.join(cwd,"Gen3",subdir))

def sort_eyes(foldername, filenames, filter_list, gen3_subfilter_list, dir_list, gen3_subdir_list):
    """Sorts *.png results based on generation and preset"""
    copy_dst = os.getcwd() + "\\Comparison\\"

    for file in filenames:  # Walk through filenames in the current folder
        for filter in range(len(filter_list)): #Check against each part of filter list to find generation/preset
            if fnmatch.fnmatch(file, "*" + filter_list[filter] + "*.png"):  #Search for match with current list item (eg. "Gen1", "Gen2p1")
                newfile = add_folder_prefix(foldername, file)   # adds prefix when copying, does not change original filename
                if filter_list[filter] == "Gen3":   # Gen3 is special case with 11 presets
                    gen3_dir = os.path.join(copy_dst, "Gen3")
                    for subfilter in range(len(gen3_subfilter_list)):   # Iterate through list of preset names
                        if fnmatch.fnmatch(file, "*" + gen3_subfilter_list[subfilter] + "*"):   #If matching preset name then...
                            try:
                                shutil.copy(os.path.join(foldername, file), os.path.join(gen3_dir, gen3_subdir_list[subfilter], newfile))    # copy to correct Gen3 preset subdirectory
                            except (shutil.Error, FileNotFoundError) as e:
                                print("Failed to copy file due to error {}".format(e))
                else:   #all other cases go directly to folder
                    try:
                        shutil.copy(os.path.join(foldername, file), os.path.join(copy_dst,dir_list[filter], newfile)) #copy files over
                    except (shutil.Error, FileNotFoundError) as e:
                        #print("Failed to copy file {}".format(os.path.join(foldername, file)))
                        print("Failed to copy file due to error {}".format(e))

def main():
    exclude= set(["Comparison"]) #exclude comparison folder and subfolders from os.walk

    # make sure dir_list and filter_list are static
    dir_list = ["Gen1", "Gen2P0", "Gen2P1", "Gen3"]  # List of top level directories
    gen3_subdir_list = ["P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]  # List of subdirectories under Gen3

    filter_list = ["Gen1", "Gen2_p0", "Gen2_p1", "Gen3"]
    gen3_subfilter_list = ["p00", "p01", "p02", "p03", "p04", "p05", "p06", "p07", "p08", "p09", "p10"]

    make_dir_bins(dir_list, gen3_subdir_list)   #Create "Comparison" folder and subfolders

    # making topdown=True means that any directories excluded from walk will have their subdirectories ignored as well
    for foldername, subfolders, filenames in os.walk(os.getcwd(), topdown=True):
        # This filters out any dirs listed in exclude and all of their subdirs
        # subfolders[:] allows the list to be modified in place
        subfolders[:] = [d for d in subfolders if d not in exclude]
        sort_eyes(foldername, filenames, filter_list, gen3_subfilter_list, dir_list, gen3_subdir_list)

if __name__ == '__main__':
    main()
