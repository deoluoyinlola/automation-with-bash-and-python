#!/bin/bash/
#Adding the desired username 
echo "Enter the name of the new user:"
read username
  
#checking if the user exists
if  
 getent passwd "$username" >/dev/null 
  then
   echo "Username already exists"

#if the user name does not exist it will be added 
else
 sudo useradd -m $username
  echo "$username has been created" 
fi
#Showing User ID Group Id and Group 
echo "Here is additional information for $username"       
 id $username