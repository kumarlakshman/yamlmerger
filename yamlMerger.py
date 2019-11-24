#-----------------------------------------------
# 
# Program for merging yaml files
# it takes absolute file-path as an arguments, 
# travesal through to its parent directories,
# 
#-----------------------------------------------

import os
import yaml
from glob import glob
from optparse import OptionParser

# defination for getting files from all 
# parent directories.

def get_all_files(dirPath,fileName):
    FilesToMerge = []  
    loop = 1
    os.chdir(dirPath)   # Changing to given path
    os.chdir('..')      # switching to the parent directory

    while loop:
        currentDir = os.getcwd()
        filePath = currentDir+'/'+fileName
        yamlFileName = glob(filePath)
        if len(yamlFileName):
            FilesToMerge.append(yamlFileName[0])
        else:
            loop = 0 # loop will be stoped as parent dir, does not contain file.
        os.chdir('..')
    return FilesToMerge
 
# defination for merging the parent and child yaml file.
# child sets override, when same data present in parent.

def yaml_merger(childObject,parentObject):

    for item in childObject:
        if item in parentObject:
            # if same item present in child and parent and if its of type str/int/float just delete the paraent value. 
            if isinstance(childObject[item],str) or isinstance(childObject[item],int) or isinstance(childObject[item],float):
                del parentObject[item]
           
            # if same item present in child and parent and it its of type list, join both the lists.
            elif isinstance(childObject[item],list):
                childObject[item].extend(parentObject[item])
                del parentObject[item]

            # if the same item present in child and parent and its of type dict, first delete the same elements from parent.
            # copy over all the remaning elements from parent to the child and delete the it.
            elif isinstance(childObject[item],dict):
                for dict_item in childObject[item]:
                    if dict_item in parentObject[item]:
                        del parentObject[item][dict_item]
                for dict_item in parentObject[item]:
                    childObject[item][dict_item] = parentObject[item][dict_item]
                del parentObject[item]

    #copy over the all remaing elements from the parent to the child                
    for item in parentObject:
        childObject[item] = parentObject[item]

    return childObject
    
if __name__ == '__main__':
    # adding parset options for passing the filename
    # exit the script if file name is not passed with -f or --file
    parser = OptionParser()
    parser.add_option("-f","--file", dest="childFileName",help="Yaml File Path")
    options, args = parser.parse_args()
    if options.childFileName:
        childFileName = options.childFileName
    else:
        parser.error("Please pass the file path,with --file or -f")

    # spliting the filename and the path
    dirPath = os.path.split(os.path.abspath(childFileName))
    # making call to get all the parent path where file is present
    FilesToMerge = get_all_files(dirPath[0],dirPath[1])

    # opening the child yaml
    with open(childFileName) as fil:
        childObject = yaml.safe_load(fil)

    print "Before Merging Yaml File::\n",yaml.dump(childObject)
    print "Files for Mergning",FilesToMerge

    # Pass file by file from parent direcotries for mergning.
    for files in FilesToMerge:
        with open(files) as fil:
            parentObject = yaml.safe_load(fil)
        childObject = yaml_merger(childObject,parentObject)

    print "After updating the object::\n",yaml.dump(childObject)
