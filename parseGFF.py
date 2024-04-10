#! /usr/bin/env python3
import argparse

def get_args():
    # create an argumentParser object
    parser = argparse.ArgumentParser(description = 'Enters in a path of a gff3 file to enter')

    # add positional arguments (these are the ones that are absolutely essential/required)
    parser.add_argument("gff3", help="Enter full path to your file", type = str)

    # add positional arguments (these are the ones that are absolutely essential/required)
    parser.add_argument("fasta", help="Enter full path to your file", type = str)

 
    #parse the actual arguments
    args = parser.parse_args()
    return args



def main():
# get the command line arguments
    args = get_args() 

# opening the covid.gff3 file      
    with open(args.gff3) as gene_features:
        for i in gene_features:
            i.strip()
            col = i.split("\t")
            print(f'The lenght of this feature is {int(col[4])-int(col[3])+1}')



# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()



