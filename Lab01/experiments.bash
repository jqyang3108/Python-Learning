#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $08-28-2018$
#---------------------------------------

# Do not modify above this line.
inputNum=$#
cursor=$#
sum=0
avg=0
if (( $# == 0 ))
then
    echo "Usage: experiments.bash <input1> [input2] .. [input N]"
    exit 1
else
    for arg in $@
    do
	if [[ ! -r $arg ]]
	then
	    echo "$arg:"
	    echo "Filename \"$arg\" is not readable."
	    echo
	else
	    echo "$arg:"
	    while read arg
	    do
		((sum=$( cut -d " " -f2 <<< $arg)+$( cut -d " " -f3 <<< $arg)+$( cut -d " " -f4 <<< $arg)))
		((avg=$sum/3))
		echo "$( cut -d " " -f1 <<< $arg) $sum $avg"
	    done < $arg
	    echo
		  
	fi
	
    done
    

fi
exit 0


