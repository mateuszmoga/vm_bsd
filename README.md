**Description:**<br/>
Script is used for setting up VM machines on FreeBSD and RED HAT.<br/>
tool should be invoked only from command line and.<br/>
only on machine when we want to set up VF.<br/>
<br/>
**Usage:**<br/>
`python3.6 main.py -h`<br/>
we should get output with all arguments:<br/>
`usage: main.py [-h] [-H] [-i] [-p] [-c] [-m]` <br/>
<br/>
`Values needed to create VM's` <br/>
<br/>
`optional arguments:`<br/>
  `-h, --help         show this help message and exit`<br/>
  `-H , --Host        type host name in uXXXX format` <br/>
  `-i , --interface   interface name where we put our VM's machine`<br/>
  `-p , --ppt         decimal number to help identify ppt bus and slot. If it`<br/>
                        `is your first VM on this machine please provide 0, second `<br/>
                     `provide 1 etc. If not given default is 0`<br/>
  `-c , --cpu         How many cpu's u need in your VM. If not given default is`
  `                   16`<br/>
  `-m , --memory      How much memory u need in your VM. If not given default`
  `                   is 16`<br/>
<br/>
You need only two arguments to start a script:<br/>
`[-H] [-i]`<br/>
example:<br/>
`python3.6 main.py -H u1961 -i eth1`<br/>
<br/>
script with all arguments:<br/>
`python3.6 main.py -H u1961 -i eth1 -p 0 -c 8 -m 8`<br/>

