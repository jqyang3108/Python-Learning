#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $01-011-2018$
#---------------------------------------

# Do not modify above this line.

file=$1
sport=$2
Num_Of_Argu=$#
Num_Of_Ath=0
Num_Of_Med=0
Largerst_Med=0
Champ=No_One
Current_Med=0

if (( $Num_Of_Argu != 2 ))
then
    echo "Usage: ./collect_stats.bash <file> <sport>"
    exit 1



elif [ ! -e $file ]
    then
    echo "Error: $file does not exist"
    exit 2


#read $file
else 
    while read file
        do
        if [[ $( cut -d ',' -f2 <<< $file )  == $sport ]]    #Find the athelete who played
            then
                ((Num_Of_Ath=$Num_Of_Ath+1))
                ((Num_Of_Med=$Num_Of_Med+$( cut -d ',' -f3 <<< $file )))

                Current_Med=$( cut -d ',' -f3 <<< $file )
        
                 if (( Current_Med > Largest_Med ))    #Find the athelete who won the most medals
                    then
                        Largest_Med=$( cut -d ',' -f3 <<< $file ) 
                        Champ=$( cut -d ',' -f1 <<< $file )    
                    fi
            fi

        done < $1
    fi

echo "Total contestants: $Num_Of_Ath"
echo "Total medals won: $Num_Of_Med"
echo "$Champ won the most medals: $Largest_Med"

exit 0

