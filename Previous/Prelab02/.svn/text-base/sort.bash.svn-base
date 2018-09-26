#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $01/20/2018$
#---------------------------------------

# Do not modify above this line.

file=$1



if [ ! -e $file ]
then
    echo "Error: $file does not exist."
    exit 2

elif (( ! $# == 1 ))
then
    echo "Usage: ./sort.bash <filename>"

else
    
    #fastest ------------------------------
    echo "The 5 fastest CPUs: "
    sort -t ',' -n -k5 $file | tee sort.out | head -n5 
    
    #efficient ----------------------------
    echo
    echo "The 3 most efficient CPUs: "
    sort -t ',' -n -k4 $file | head -n3    
    
    #cache -------------------------------
    echo
    echo "The CPUs wich cache size 4: "
    sort -t ',' -n -k5 $file | while read line
    do
        if (( $( cut -d ',' -f2 <<< $line) == 4 ))
        then
            echo  "$line"
        fi
    done 
    
    #slowest -------------------------------
    echo
    echo -n "Enter a value for n: "
    read n 
    sort -t ',' -n -r -k5 $file | head -n$n
    
    #Print -----------------------------------
    echo
    sort -t ',' -k1,1 -k4,4 $file | cat  >&sorted_CPI.txt

    exit 0
fi


exit 0
