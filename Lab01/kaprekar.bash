#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $08-28-2018$
#---------------------------------------
# Do not modify above this line.
input=$1
count=1

if (( ! $# == 1 ))
    then
        echo "Usage: karprekar.bash <non-negetive integer>"
        exit 1
else
while (( $input >= $count ))       #process every number in the range of input
do
    ((square=$count*$count ))
    #-------------------------------------------------1   # of digits of current number
    digit=1
    temp=$count
    while (($temp >= 10 )) 
    do
        ((temp=$temp/10))
        ((digit=$digit+1))
    done
    #--------------------------------------------------------2  # of digits of squared number
    digitsq=1
    tempsq=$square
    while (( $tempsq >= 10 ))        
     do
        ((tempsq=$tempsq/10))
        ((digitsq=$digitsq+1))
      done
    ((cursor=$digitsq-$digit))                     #find the which digit is to be cut
   # -----------------------------------------------3 output result
   if (( $digitsq == 1 ))   #------------------------------- 1, square=1, 1+0=1
   then

       left=0 
       right=$( echo $square | cut -c 1 )
   else
       (( cursorLeft=$cursor+1 ))                         #digit on the left of current digit
       left=$( echo $square | cut -c 1-$cursor )           #cut left and right at the cursor digit
       right=$( echo $square | cut -c $cursorLeft-$digitsq )    
   fi
                                                 
   if (( $((left+$((10#$right)))) == $count ))    #sum up the left and right digit and make right number if 0x to x, then check if the sum matches current count number
   then
       echo "$count, square=$square, $right+$left= $((left+$((10#$right))))"
   fi    
   ((count=$count+1))     #go to next number
done 
fi
exit 0

