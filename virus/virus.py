#!/usr/bin/env python3

import os
import shutil

# get working paths
startingPath = "/home/slyguy/Documents/pythonProjects"
fileName = "script.py"
curDir = os.getcwd()

def main():
    # check if file exists
    if(os.path.exists(curDir+"/"+fileName)):
        print(" File " + fileName + " already exists! ")
        print(" Deleting . . . ")
        os.remove(curDir + "/" + fileName)
        print(" File removed! ")

    # if not do all this good stuff
    else:
        print( "Building virus . . . ")
        # write info to a file
        fileText = "This could be virus code"
        f= open(fileName, "w+")
        f.write(fileText)
        f.close()

        # loop over directories
        baseDir = startingPath
        for folder in os.listdir(baseDir):
            fodPath = os.path.join(baseDir, folder)
            #check if directory
            if (os.path.isfile(fodPath) == False):
                #copy file to other locations
                shutil.copy(curDir + "/" + fileName, curDir + "/" +folder)


main()
