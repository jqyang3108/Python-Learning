#! /bin/bash

#----------------------------------
# $Author: ee364b01 $
# $Date: 2018-02-14 17:20:47 -0500 (Wed, 14 Feb 2018) $
#----------------------------------

function part_a 
{               
    # Fill out your answer here. Do not include exit 0 in your code.
    
    return 
}                               

function part_b
{              
    # Fill out your answer here. Do not include exit 0 in your code.
    num1=0
    num2=0
    for FILE in myDir1/*
    do
        ((num1=$num1+1))
    
    done
    for FILE in myDir2/*
    do
        ((num2=$num2+1))
    done


    if (($num1 == $num2))
    then
        echo "Similar"
    else
        echo "Different"
    fi
    return                     
}                              

function part_c
{
    # Fill out your answer here. Do not include exit 0 in your code.

    return
}

function part_d
{
    # Fill out your answer here. Do not include exit 0 in your code.

    while read temp.txt
    do
        echo "read"
    done < $1

    return
}

function part_e
{
    # Fill out your answer here. Do not include exit 0 in your code.
    return
}

function part_f
{
    # Fill out your answer here. Do not include exit 0 in your code.
    sort -t ',' -k4,4 -k6,6, -k1,1 -k2,2 people.csv | head -n10
    return
}

function part_g
{
    # Fill out your answer here. Do not include exit 0 in your code.
    cnum=0
    cj=0
    for FILE in myDir/*.c
    do  
        ((cnum=$cnum+1))
    done
        echo $cnum
    for FILE in myDir/*.java
    do
        ((cj=$cj+1))
    done
        echo $cj
    return
}


function part_h
{
    # Fill out your answer here. Do not include exit 0 in your code.
    return
}

function part_i
{
    # Fill out your answer here. Do not include exit 0 in your code.
    return
}


# To test your function, you can call it below like this:
#
 part_d
