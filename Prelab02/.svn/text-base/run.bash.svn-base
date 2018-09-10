#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $08-31-2018$
#---------------------------------------

# Do not modify above this line
path=c-files

for file in $path/*.c
do
	file=$( echo $file | cut -d '/' -f2 )
	filename=$( echo $file | cut -d '.' -f1 )
	#echo "$filename"
	#file=$( cut -d '/' f2 <<< $file )
	gcc -Wall -Werror -std=c99 $path/$file  2> /dev/null
       	if (( $? == 0 ))
     	then	
    	    echo "Compiling file $file... Compilation succeeded."
	(./a.out | tee $filename.out) > /dev/null
	else	
            echo "Compiling file $file... Error: Compilation failed."
        fi
  	
done
exit 0
