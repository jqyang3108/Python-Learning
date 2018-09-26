#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $01/16/2018$
#---------------------------------------

# Do not modify above this line.

input=$1
num=$((10#$input))
count=1
echo "$num"

if (( ! $# == 1 ))
    then
        echo "Usage: karprekar.bash <non-negetive integer>"
        exit 1
    
else
while (( $num >= $count ))
do
    (( square=$count*$count ))
   
    digitsq=1
    digit=1
    find=$square
    find1=$count
   
    #-------------------------------------------------1

    while (( $find1 >= 10 ))  # # of digits of current number
    do
        (( find1=$find1/10))
        ((digit=$digit+1))
    done
    #--------------------------------------------------------2
    while (( $find >= 10 ))              # # of digits of squared number
     do
        (( find=$find/10 ))
        (( digitsq=$digitsq+1 ))
      done
    (( cursor=$digitsq-$digit ))
    #-----------------------------------------------3
    if (( $cursor <= 0 ))
    then
        cursor=1
        fi
    (( cursor1=$cursor+1 ))
   # echo "cursor$cursor  cursor1$cursor1  sqdigit$digitsq digit$digit"------------------------------------4
   
   if (( $digitsq == 1 ))
   then
        left=0
        right=$( echo $square | cut -c 1 )
    else
        left=$( echo $square | cut -c 1-$cursor )
        right=$( echo $square | cut -c $cursor1-$digitsq )    
    fi
    
    (( sum=$left+$((10#$right)) ))

    if (( $sum == $count ))

    then   echo "$count, square=$square, $right+$left=$sum"
    fi    
    (( count=$count+1 ))
done 

exit 0
fi
