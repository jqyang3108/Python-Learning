#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $08-26-2018$
#---------------------------------------

# Do not modify above this line.

echo -n "Enter a command: "
read Command

while [[ ! $Command == quit ]]                             #exit 
do
    
    if [[ $Command == hello ]]                               #hello
        then
            echo "Hello $(whoami)"
    
    elif [[ $Command == compile ]]                          #compile
        then
            for file in *.c
            do
                gcc -Wall -Werror $file -o "${file%.c}.o"
                if (( $? == 0 ))
                then
                    echo "Compilation succeeded for: $file"
                else
                    echo "Compilatiom failed for: $file"
                fi
            done

    elif [[ $Command == run ]]                              #run
        then
            echo -n "Enter filename: "
            read file
            echo -n "Enter arguments: "
            read arguments
            #echo "You entered: $arguments"
            
            if [[ ! -e $file ]]
            then
                echo "Invalid filename"
            
            else
                ./$file $arguments
            fi
            
    else
            echo "Error: unrecognized input"   
    fi

    echo
    echo -n "Enter a command: "                                 #Input again
    read Command
done

echo "Goodbye"
exit 0
