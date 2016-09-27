'''
VEP VCF to Cassandra-ready CSV converter
Brian S. Cole, Dichen Li, and Zhengxuan Wu
University of Pennsylvania
'''

import argparse, sys, os
from populate_vcf_to_csv import csv_populator
#from populate_csv_to_DB import db_populator

def getargs():
    '''Collect input and output files.'''
    parser = argparse.ArgumentParser(description="Convert a VEP VCF file to a Cassandra-ready CSV file.")
    parser.add_argument('-i', '--input_file', required=True, help="Input VEP VCF file to convert to CSV.")
    parser.add_argument('-o', '--output_file', required=True, help="Output CSV file to generate.")
    args = parser.parse_args()
    return args

def main ():
    '''Collect input VEP VCF file name and output CSV file name, then generate output.'''
    args = getargs()
    converter = csv_populator(args.input_file, args.output_file)
    converter.vcf_to_csv()
    print "Completed"

if __name__ == '__main__':
    main()
