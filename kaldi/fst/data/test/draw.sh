#!/bin/bash 

if [[ $# != 1 ]]; then
	echo "usage: $0 name"
	exit 1
fi

fstdraw --isymbols=ascii.syms --osymbols=wotw.syms -portrait $1.fst | dot -Tjpg >$1.jpg
#fstdraw --isymbols=ascii.syms --osymbols=wotw.syms -portrait $1.fst | dot -Tbmp >$1.bmp
