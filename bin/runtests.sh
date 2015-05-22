#!/bin/bash

export set PYTHONPATH=$(readlink -f $(dirname $0))/../src/main:../src/test

find `dirname $0`/../src/test/zing -name '*py' -execdir python {} \;

