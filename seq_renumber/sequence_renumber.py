#!/usr/bin/python

import os
import re
import sys
import argparse
import logging

def SequenceRenumber(sourceDir="",padZero=0,renameUnnumberedFiles=False,recursive=False):
    if not os.path.isdir(sourceDir):
        print 'Error : {0} directory does not exist !'.format(sourceDir)
        return
    items = os.listdir(sourceDir)
    items.sort()
    sequenceMap = {}
    
    for item in items:
        fullPath = os.path.join(sourceDir,item)
        if os.path.isfile(fullPath):
            if(renameUnnumberedFiles):
                pattern = r"(?P<name>[a-zA-Z0-9_]+[a-zA-Z_]+)(?P<number>[0-9]*)\.(?P<extension>[a-zA-Z0-9]+)"
            else:
                pattern = r"(?P<name>[a-zA-Z0-9_]+[a-zA-Z_]+)(?P<number>[0-9]+)\.(?P<extension>[a-zA-Z0-9]+)"
            match = re.match(pattern,item)
            if(not match):
                print 'Warning : Skipping item {0}. It does not fit into the rename rules'.format(item)
                continue
            name = match.group('name')
            number = match.group('number')
            extension = match.group('extension')
            if(name,extension) in sequenceMap:
                sequenceMap[(name,extension)] = sequenceMap[(name,extension)] + 1
            else:
                sequenceMap[(name,extension)] = 1
            itemRename = '{0}{1}.{2}'.format(name,str(sequenceMap[(name,extension)]).zfill(padZero),extension)
            fullPathRename = os.path.join(sourceDir,itemRename)
            print 'Renaming {0} to {1}'.format(fullPath,fullPathRename)
            os.rename(fullPath,fullPathRename)
        else:
            if os.path.isdir(fullPath):
                if recursive:
                    SequenceRenumber(fullPath, padZero, renameUnnumberedFiles, recursive)
                else:
                    print 'Warning : Skipping directory {0}'.format(item)
                    continue

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--Source_Directory_Path",dest='sourceDir',default=None,nargs='+',
                        help="The source directory on which the renumber is to be executed")
    parser.add_argument("-z","--Zero_Padding",dest='padZero',default=None,nargs='?',
                        help="Number of zeros to pad to the resultant sequence")
    
    opts = parser.parse_args()
    
    if not opts.sourceDir:
        print "Error : Please specify the source directory"
        sys.exit(1)
    sourceDir = opts.sourceDir[0]
    
    padZero = 0
    if opts.padZero:
        if(opts.padZero<0):
            print 'Error : Zero padding value shout not be negative'
        else:
            padZero = int(opts.padZero)
    
    sourceDirAbsPath = os.path.abspath(sourceDir)
    SequenceRenumber(sourceDir=sourceDirAbsPath, padZero=padZero, renameUnnumberedFiles=False, recursive=False)