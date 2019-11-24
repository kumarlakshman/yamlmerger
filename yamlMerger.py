import os
import yaml
from glob import glob
from optparse import OptionParser

def get_all_files(dir_path,file_name):
    files_to_merge = []
    loop = 1
    os.chdir(dir_path)
    os.chdir('..')
    while loop:
        current_dir = os.getcwd()
        file_path = current_dir+'/'+file_name
        yaml_file_name = glob(file_path)
        if len(yaml_file_name):
            files_to_merge.append(yaml_file_name[0])
        else:
            loop = 0
        os.chdir('..')
    return files_to_merge
 
def yaml_merger(child_object,parent_object):
    for item in child_object:
        if item in parent_object:

            if isinstance(child_object[item],str) or isinstance(child_object[item],int):
                del parent_object[item]

            elif isinstance(child_object[item],list):
                child_object[item].extend(parent_object[item])
                del parent_object[item]

            elif isinstance(child_object[item],dict):
                for dict_item in child_object[item]:
                    if dict_item in parent_object[item]:
                        del parent_object[item][dict_item]
                for dict_item in parent_object[item]:
                    child_object[item][dict_item] = parent_object[item][dict_item]
                del parent_object[item]
                    
    for item in parent_object:
        child_object[item] = parent_object[item]
    return child_object
    
if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-f","--file", dest="child_file_name",help="Yaml File Path")
    options, args = parser.parse_args()
    if options.child_file_name:
        child_file_name = options.child_file_name
    else:
        parser.error("Please pass the file path,with --file or -f")

    dir_path = os.path.split(os.path.abspath(child_file_name))
    files_to_merge = get_all_files(dir_path[0],dir_path[1])

    with open(child_file_name) as fil:
        child_object = yaml.safe_load(fil)

    print "Before Merging Yaml File::\n",yaml.dump(child_object)
    print files_to_merge
    for files in files_to_merge:
        with open(files) as fil:
            parent_object = yaml.safe_load(fil)
        child_object = yaml_merger(child_object,parent_object)

    print "After updating the object::\n",yaml.dump(child_object)
