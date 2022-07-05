import argparse
import subprocess
from sys import platform

import cmd
from bsd import Bsd
from logger import logger
from rhel import rhel

"""
Script is used to automatically set Virtual machine o FreeBSD or RED HAT hosts
"""



def main():
    if args.memory is None:
        args.memory = cmd.memory_def_value
    if args.cpu is None:
        args.cpu = cmd.cpu_def_value
    if args.ppt is None:
        args.ppt = cmd.ppt_def_value
    logger.info("PLease be sure that proper driver for NIC is installed")
    logger.warning(cmd.ddp_pkg)
    # system_id = subprocess.Popen(cmd.error_code_check_cmd, stdout=subprocess.PIPE, shell=True)
    # exit_code = system_id.communicate()[0]
    if cmd.system_val_bsd in platform:
        logger.info(cmd.system_id_info.format(platform))
        Bsd(host=args.Host,
            interface=args.interface,
            ppt=args.ppt,
            memory=args.memory,
            cpu=args.cpu)
    if cmd.system_val_rhel in platform:
        logger.info(cmd.system_id_info.format(platform))
        rhel(host=args.Host,
             interface=args.interface,
             ppt=args.ppt,
             memory=args.memory,
             cpu=args.cpu)


if __name__ == "__main__":
    # TODO Add mandatory and positional args into arg funk and also main bsd, rhel func
    parser = argparse.ArgumentParser(description="Values needed to create VM's")
    parser.add_argument("-H", "--Host", type=str, metavar="", help="type host name in uXXXX format")
    parser.add_argument("-i", "--interface", type=str, metavar="", help="interface name where we put our VM's machine ")
    parser.add_argument("-p", "--ppt", type=str, metavar="",
                        help="decimal number to help identify ppt bus and "
                        "slot. If it is your first VM on this"
                        " machine please provide 0, second provide 1 etc.\n"
                        "If not given default is {}".format(cmd.ppt_def_value))
    parser.add_argument("-c", "--cpu", type=str, metavar="",
                        help="How many cpu's u need in your VM.\n"
                             "If not given default is {}".format(cmd.cpu_def_value))
    parser.add_argument("-m", "--memory", type=str, metavar="",
                        help="How much memory u need in your VM.\n"
                             "If not given default is {}".format(cmd.memory_def_value))

    args = parser.parse_args()
    main()
