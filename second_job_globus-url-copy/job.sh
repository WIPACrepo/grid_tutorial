#!/bin/bash

INPUT_DIR=$1
FILE_NAME=$2
OUTPUT_DIR=$3

eval `/cvmfs/icecube.opensciencegrid.org/py2-v2/setup.sh`

globus-url-copy gsiftp://gridftp.icecube.wisc.edu/${INPUT_DIR}/${FILE_NAME} ./

##############################
######## Do Work Here ########
/usr/bin/md5sum ${FILE_NAME} > ${FILE_NAME}.md5
##############################

globus-url-copy ./${FILE_NAME}.md5 gsiftp://gridftp.icecube.wisc.edu/${OUTPUT_DIR}/${FILE_NAME}.md5

rm -f ${FILE_NAME}
rm -f ${FILE_NAME}.md5
