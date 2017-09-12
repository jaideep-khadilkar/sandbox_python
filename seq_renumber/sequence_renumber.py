#!/usr/bin/python

import os
import re
import sys
import argparse

def SequenceRenumber(sourceDir='',padZero=0,recursive=False,rootDir=''):
    # Validate Inputs
    if not os.path.isdir(sourceDir):
        print 'Error : {0} directory does not exist !'.format(sourceDir)
        return
    if(padZero<0):
        print 'Error : Zero padding value can not be negative'
        return
    if(rootDir==''):
        rootDir = sourceDir

    items = os.listdir(sourceDir)
    # Sort input items to avoid clashing while renaming
    items.sort()
    # sequenceMap to track number of files in a sequence with a particular name and extension.
    sequenceMap = {}

    for item in items:
        fullPath = os.path.join(sourceDir,item)
        if os.path.isfile(fullPath):
            # Uses reg-ex to extract name, number and extension from a filename.
            pattern = r"(?P<name>[a-zA-Z0-9_]+[a-zA-Z_]+)(?P<number>[0-9]+)\.(?P<extension>[a-zA-Z0-9]+)"
            match = re.match(pattern,item)
            if(not match):
                print 'Warning : Skipping {0}. It does not fit into the renaming rules.'.format(os.path.relpath(fullPath,rootDir))
                continue
            name = match.group('name')
            extension = match.group('extension')
            # If sequence exists in the map, increase the count.Else initialize it to 1.
            if(name,extension) in sequenceMap:
                sequenceMap[(name,extension)] = sequenceMap[(name,extension)] + 1
            else:
                sequenceMap[(name,extension)] = 1
            # Rename the file.
            itemRename = '{0}{1}.{2}'.format(name,str(sequenceMap[(name,extension)]).zfill(padZero),extension)
            fullPathRename = os.path.join(sourceDir,itemRename)
            print 'Renamed : {0} --> {1}'.format(os.path.relpath(fullPath,rootDir),os.path.relpath(fullPathRename,rootDir))
            os.rename(fullPath,fullPathRename)
        else:
            if os.path.isdir(fullPath):
                if recursive:
                    # Run renumbering on children directories.
                    SequenceRenumber(fullPath, padZero, recursive,rootDir=sourceDir)
                else:
                    print 'Warning : Skipping directory {0}'.format(item)
                    continue
    return

"""
This is the entry point for CLI runs. Please use `--help` for help.
"""
if __name__ == '__main__':
    
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("sourceDir",default=None,metavar='SOURCE_DIRECTORY',
                        help="Absolute or relative path to the source directory on which the renumber is to be executed")
    parser.add_argument("-z","--Zero_Padding",dest='padZero',default=None,required=False,metavar='N',
                        help="Number of zeros to pad to the resultant sequence")
    parser.add_argument('-r', "--Recursive",dest='recursive',action='store_true',default=None,required=False,
                        help="Recursively apply operation to the children directories.")
    
    # Validate Inputs
    opts = parser.parse_args()
    if not opts.sourceDir:
        print "Error : Please specify the source directory"
        sys.exit(1)
     
    padZero = 0
    if opts.padZero:
        padZero = int(opts.padZero)

    sourceDirAbsPath = os.path.abspath(opts.sourceDir)
    SequenceRenumber(sourceDir=sourceDirAbsPath, padZero=padZero, recursive=opts.recursive)
    