#! /bin/bash

#---------------------------------------
# $Jiaqi Yang$
# $Date: 2018-09-04 13:16:05 -0400 (Tue, 04 Sep 2018) $
#---------------------------------------

# Do not modify above this line.

if [[ $# == 0 ]]
then
  echo "Usage: ./UsageStats.bash <filename>"
  exit 1
elif [[ ! -e $1 ]]
then
  echo "Error: $1 does not exist"
  exit 2
else
  time=$(cat $1 | head -n1 | cut -d ' ' -f3)
  echo "Parsing file \"$1\". Timestamp: $time "
  echo "Your choices are: "
  echo "1) Active used IDs"
  echo "2) Highest CPU usage"
  echo "3) Top 3 longest running processes"
  echo "4) All processes by a specific user"
  echo "5) Exit"
  echo -n "Please enter your choice: "
  read choice

  while [[ ! $choice == 5 ]]
  do
    if (( $choice == 1 ))
    then
    usersNum=$(cat $1 | head -n1 | cut -d ' ' -f8)
      echo "Total number of active user IDs = $usersNum"

    elif(( $choice == 2 ))
	then
      ut=$(tail -n +8 $1 | head -n 1 | cut -d ' ' -f9)
      user=$(tail -n +8 $1 | head -n 1  | cut -d ' ' -f2)
      echo "User $user is utilizing the highest CPU resources at $ut"

    elif(( $choice == 3))
    then
      tail -n +8 $1 | sort -n -k11 -r | head -n 3

    elif(( $choice == 4 ))
    then	
      echo -n "Please a valid username: "
      read username
      echo -n "Please enter a filename to save user's processes: "
      read filename
      while read line
      do
	if [[ $( cut -d ' ' -f2 <<< $line ) == $username ]]
	then
	  #echo $line | tee -a $filename
	  echo $line >> $filename
	
	fi

      done <$1
      if [[ -s $filename ]]
      then
      echo "Output written to file $filename"
      else
	echo "No match found"
      fi
    else
      echo "Unrecognized input"
    fi

    echo
    echo -n "Please enter your choice: "
    read choice
  done

  fi
exit 0