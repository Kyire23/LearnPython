import sys, gzip
filename = sys.argv[0]         #python file name, i.e. gzipfile.py
filenamezip = filename + '.gz'   #file extension .gz
# gzip compression 
with gzip.open(filenamezip, 'wt') as f:  
    for s in open(filename, 'r'):
        f.write(s)
# gzip decompression/extraction 
for s in gzip.open(filenamezip, 'r'):
    print(s)
