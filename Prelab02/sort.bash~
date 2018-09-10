#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $08-28-2018$
#---------------------------------------

# Do not modify above this line.

file=$1

if (( ! $# == 1 ))
then
    echo "Usage: ./sort.bash <filename>"
    exit 1
elif [[ ! -e $file ]]
then
    echo "$file does not exist."
    exit 2
else
    echo "The 5 fastest CPUs: "
    sort -t ',' -n -k5 $file | head -n5
    echo

    echo "The 3 most efficient CPUs: "
    sort -t ',' -n -k4 $file | head -n3
    echo


    echo "The CPUs with cache size 4: "
    sort -t ',' -n -k5 $file | while read line
    do
	# echo "current line: $line"
	if (( $( cut -d ',' -f2 <<< $line) == 4))
	then
	    echo "$line"
	fi
    done

    echo
    echo -n "Enter a value for n: "
    read n
    echo "The $n slowest CPUs: "
    sort -t ',' -n -r -k5 $file | head -n$n

    sort -t ',' -k1,1 -k4,4 $file | cat >&sorted_CPI.txt
    exit 0
fi

exit 0

    
