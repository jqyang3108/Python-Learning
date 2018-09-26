#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $01/20/2018$
#---------------------------------------

# Do not modify above this line

file=$1
i=0
row=0
col=0
colVal=0
rowVal=0

if (( ! $# == 1 ))
then
    echo "Usage: ./treasure.bash <filename>"
    
else
    while read file
    do
        A[i]=$file
        (( i=$i+1 ))
    done < $1
        
    rowVal=($( cut -f1 <<< ${A[0]} | cut -c1));
    colVal=($( cut -f1 <<< ${A[0]} | cut -c2));

    while (( !( $row == $rowVal && $col == $colVal ) ))
    do  
        echo "($rowVal, $colVal)" 

        row=$rowVal
        col=$colVal

        (( a=$rowVal ))
        (( b=$colVal+1 ))

        rowVal=($( cut -d ' ' -f$b <<< ${A[$a]} | cut -c1))
        colVal=($( cut -d ' ' -f$b <<< ${A[$a]} | cut -c2))
    done
    
    echo "Treasure found at: ($rowVal, $colVal)"
    exit 0
fi

exit 0
