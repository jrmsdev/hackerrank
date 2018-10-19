#!/bin/sh

NAME=${1:?'name?'}

test -d ./${NAME} && {
    echo "ERROR: ${NAME} already created"
    exit 1
}
mkdir -p ./${NAME}

testname=${NAME}/$(basename ${NAME})
script_filename=${testname}.py

echo '#!/usr/bin/env python3' >${script_filename}
chmod 0750 ${script_filename}
echo ${script_filename}

touch ${testname}.t0.in
echo ${testname}.t0.in

touch ${testname}.t0.out
echo ${testname}.t0.out
