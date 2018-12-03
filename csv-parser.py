#!/usr/bin/python

"""
Supported Python Version: 3

This script reassembles nessus export csv  into a well structured csv
Usage: 
1) simply start this script via cmd  > python3 csv-parser.py /path/to/nessus-csv-file.csv
2) wait et violà you get a well structured csv in the same directory



* ----------------------------------------------------------------------------
* "THE BEER-WARE LICENSE" (Revision 42):
*  As long as you retain this notice you
*  can do whatever you want with this stuff. If we meet some day, and you think
*  this stuff is worth it, you can buy me a beer in return. 
*  2018, @plonxyz   github.com/plonxyz
* ----------------------------------------------------------------------------


"""

import csv
import sys
import os

def welcomebanner():
   print(" \n      _   __________________ __  _______    ___      ____________    __\n     / | / / ____/ ___/ ___// / / / ___/   |__ \    / ____/ ___/ |  / / \n    /  |/ / __/  \__  \\__ \/ / / /\__ \    __/ /   / /    \__ \| | / /   \n   / /|  / /___ ___/ /__/ / /_/ /___/ /   / __/   / /___ ___/ /| |/ /   \n  /_/ |_/_____//____/____/\____//____/   /____/   \____//____/ |___/    \n\n")


def checkfile(filepath):  #Input validation / remove " " from path
    filepath = filepath.replace('"',"")
    check=os.path.isfile(filepath)
    return check
           
def reassemble_file(filepath): # remove " " from path / open original csv / parsing each line and Remove newlines till EOF and write line into new %FILENAME%_converted.csv
    filepath = filepath.replace('"',"")
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            row9split=row[9].split('\n')
            output=(f'{row[0]};{row[1]};{row[2]};{row[3]};{row[4]};{row[5]};{row[6]};{row[7]};{row[8]};{row9split} \n')
            newfilename=os.path.splitext(filepath)[0]
            newfilepath=os.path.dirname(filepath)
            f= open(f"{newfilename}_converted.csv","a")
            f.writelines(output)
            line_count=line_count+1
        print(f'\n\nFile {filepath} with {line_count} lines converted:\n\n goodbye... \n')

def main(): #main
    welcomebanner()
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = input('please provide csv for converting > ')

    check=checkfile(filepath)
    if check == True :
        print('\n\nFile found \n ... converting ...')
        reassemble_file(filepath)
    else :
        print('File not found')

if __name__ == "__main__": 
  main()
