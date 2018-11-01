###
# Script to copy files and compress them and put them in a separate location
#
# Created for Python 3.
# By:   Brad Beckwith
#       October 25, 2018
#       Verify the Zip folder is not the same as the source folder or the Zip file will
#       continue to grow until the drive is full unless stopped manually.
# Version: 1.0.0
#
###

import os
import zipfile
import shutil

# copy files and folder and compress into a zip file
def doprocess(source_folder, target_zip):
    zipf = zipfile.ZipFile(target_zip, "w")
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print(os.path.join(subdir, file))
            zipf.write(os.path.join(subdir, file))
    print("Created: ", target_zip)


# copy files to a target folder
def docopy(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print(os.path.join(subdir, file))
            shutil.copy2(os.path.join(subdir, file), target_folder)
    print("Copied files to target directory: " + '"' + target_folder + '"')


def replace_single_slash(slash):
    return slash.replace("\\","\\\\")


if __name__ == '__main__':
    print('Starting execution...')

    # compress to zip
    '''
    source_folder = 'c:\\temp\\amt'
    target_zip = ('c:\\tmp\\amt\\amt_zipfile.zip').title()
    target_folder = (os.path.dirname(target_zip)).title()
    '''

    source_folder = input("Enter source folder to copy from: ")
    target_zip = input("Enter target zip name: ").title()
    target_folder = (os.path.dirname(target_zip)).title()
    
    #target_folder = input("Enter target folder to copy to: ")

    if "\\\\" not in source_folder:
        source_folder = replace_single_slash(source_folder)

    if "\\\\" not in target_folder:
        target_folder = replace_single_slash(target_folder)

    if (os.path.exists(source_folder)) and (os.path.exists(target_folder)):
        if not os.path.exists(target_zip):
            doprocess(source_folder, target_zip)
        else:
            print("Target zip file: " + target_zip + " exists...")
    else:
        print("Source folder " + source_folder + " does not exist...")
        os.mkdir(target_folder)
        if not os.path.exists(target_zip):
            doprocess(source_folder, target_zip)

    # copy to backup folder
    # Assumptions: Source and Target folders are the same as above.

    if os.path.exists(source_folder):
        if os.path.exists(target_zip):
            if os.path.exists(target_folder):
                docopy(source_folder, target_folder)
            else:
                print("Target folder " + target_folder + " does not exist...")
                # Create target_folder
        else:
            print("Zip file does not exist...")
    else:
        print ("Source folder " + source_folder + " does not exist...")

    print('Ending execution...')