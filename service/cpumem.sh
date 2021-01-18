#!/bin/bash

sname=$(uname)
shostname=$(uname -n)
skernel=$(uname -r)
snetinfo=$(ip a)
sstorage=$(df -BG /)
myip="$(dig +short myip.opendns.com @resolver1.opendns.com)"
scpu=$(cat /proc/stat | awk '/cpu/{printf("%.2f%\n"), ($2+$4)*100/($2+$4+$5)}' |  awk '{print $0}' | head -1)
smem=$(free | awk '/Mem/{printf("%.2f%"), $3/$2*100}')
sswap=$(free | awk '/Swap/{printf("%.2f%"), $3/$2*100}')
echo "My WAN/Public IP address: ${myip}"
echo "--------------------------------------------------------------------------------------"
echo "$sstorage"
echo "--------------------------------------------------------------------------------------"
echo "$scpu   $smem   $sswap  $skernel  $shostname   $sname"

echo "--------------------------------------------------------------------------------------"

echo "$snetinfo"

echo "--------------------------------------------------------------------------------------"


#pgrep nginx
#pgrep httpd
#pgrep -x mysqld


# pidof program
# pidof httpd
# pidof mysqld
# pidof nginx