#! /bin/bash

#----------------------------------
# $Author: ee364b15 $
# $Date: 2018-09-04 13:16:05 -0400 (Tue, 04 Sep 2018) $
#----------------------------------

function part_1 
{               
    # Fill out your answer here
    sort -t ',' -k4,4 -k6,6 -k1,1 -k2,2 people.csv | tail -n5

    return                      
}                               

function part_2
{              
    # Fill out your answer here
    return                     
}                              


# To test your function, you can call it below like this:
#
 part_1
