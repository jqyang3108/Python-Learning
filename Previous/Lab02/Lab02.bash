#! /bin/bash

#----------------------------------
# $Jiaqi Yang$
# $01/23/2018$
#----------------------------------

function part_1 
{              
    # Fill out your answer here

    sort -t ',' -k4,4 -k6,6 -k1,1 -k2,2 people.csv | tail -n9
    return                      
}                               

function part_2
{              
    # Fill out your answer here
    Arr=(a.txt b.txt c.txt d.txt e.txt)
    r=$(( $RANDOM%5 ))


    line=($( cat ${Arr[$r]} | wc -l ))
    let deter=$line%2

    if (( $deter == 0 ))
    then
        let middle=$line/2+1
        cat ${Arr[$r]} | head -n$middle | tail -n2
    else
        let middle=$line/2+1       
        cat ${Arr[$r]} | head -n$middle | tail -n1

    fi  
    return                     
}                              

function part_3
{
    # Fill out your answer here

    A=($(ls ./src/*.c))

    let size=${#A[@]}-1
    i=0

    while (( $i <= $size ))
    do
        gcc ${A[$i]} 2> TEMP.TXT
        if (( $? == 0 ))
        then
               echo "<${A[$i]}>: success"
        else
               echo "<${A[$i]}>: failure"
    fi
        
        let i=$i+1
    done
    return
}

# To test your function, you can call it below like this:
#
part_2
