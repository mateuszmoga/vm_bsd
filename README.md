# vm_bsd
Script is used to automatically set Virtual machine o FreeBSD or RED HAT hosts

usage: main.py [-h] [-H] [-i] [-p] [-c] [-m]

Values needed to create VM's

optional arguments:<br />
  -h, --help         show this help message and exit<br />
  -H , --Host        type host name in uXXXX format<br />
  -i , --interface   interface name where we put our VM's machine<br />
  -p , --ppt         decimal number to help identify ppt bus and slot. If it is your first VM on this machine please provide 0, second provide<br />
                     1 etc. If not given default is 0<br />
  -c , --cpu         How many cpu's u need in your VM. If not given default is 16<br />
  -m , --memory      How much memory u need in your VM. If not given default is 16<br />