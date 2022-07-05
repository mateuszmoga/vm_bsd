import re
import subprocess
from time import sleep

from cmd import BsdCmd
from host_dict import host_dict
from logger import logger


class Bsd:

    def __init__(self,
                host: str,
                interface: str,
                ppt: str = "0",
                cpu: str = "16",
                memory: str = "16"):
        """
    :param host: host name ex. u1961
    :param interface: if name ex. eth3
    :param ppt: ppt number - always start with 0 if its first VM
    :param cpu: How many cores u need in VM
    :param memory: How much memory u need in VM
    :return: VM started with given params
    """
        logger.info("You chose wisely as a system Host - FreeBSD")
        with open(BsdCmd.iov_temp, "r") as r:
            logger.info("Started to creating and configuring {} file".
                        format(BsdCmd.iovctl_conf))
            string_swap = r.read().replace(BsdCmd.string_to_replace,
                                           BsdCmd.string_to_replace.format(interface))

        with open(BsdCmd.iovctl_conf, "w") as w:
            w.write(string_swap)
            logger.info("Ended creating and configuring {} file".format(BsdCmd.iovctl_conf))
        logger.info("Creating and configuring {} file".format(BsdCmd.iovctl_conf))
        subprocess.call(BsdCmd.iovctl_cmd, shell=True)
        logger.info("Creating VM named: ({})".format(host))
        subprocess.call(BsdCmd.vm_create.format(host), shell=True)
        logger.info("VM created.")
        host_conf = BsdCmd.path_host_conf.format(host) + host + ".conf"
        # TODO refactor this with for loop and writelines
        with open(host_conf, "r") as r:
            logger.info("Started to configure memory size into: ({})".format(memory))
            mem_swap = r.read().replace(BsdCmd.mem_string_to_replace, BsdCmd.replaced_mem_string.format(memory))
        with open(host_conf, "w") as w:
            logger.info("Saving configurations memory size and pcu cores into: ({})".format(host_conf))
            w.write(mem_swap)
        with open(host_conf, "r") as r:
            logger.info("Started to configure memory size and pcu cores into: ({})".format(cpu))
            cpu_swap = r.read().replace(BsdCmd.cpu_string_to_replace, BsdCmd.replaced_cpu_string.format(cpu))
        with open(host_conf, "w") as w:
            logger.info("mem set to: ({}) cpu set to ({})".format(memory, cpu))
            w.write(cpu_swap)
        logger.info("conf saved.")
        logger.info("Adding VM's MAC into VM's conf file ({})".format(host_dict[host]))
        subprocess.call("echo \'network0_mac=\"{}\"\' >> {}".format(host_dict[host], host_conf), shell=True)
        logger.info("Finding proper Passthru ppt{} bus:slot:function ...".format(ppt))
        process = subprocess.Popen(BsdCmd.vm_passthru_find, shell=True, stdout=subprocess.PIPE)
        output = process.communicate()

        regex = re.search('(ppt'+ppt+'\s\s\s\s\s\s\s)(\d{1,3}/\d{1}/\d{1,3})', str(output))
        logger.info("Passthru found. adding into conf file following value : ({})".format(regex.group(2)))
        subprocess.call("echo \'passthru0=\"{}\"\' >> {}".format(regex.group(2), host_conf), shell=True)
        # subprocess.call("echo \'memory={}G' >> {}".format("16", host_conf), shell=True)
        # subprocess.call("echo \'cpu={}' >> {}".format("12", host_conf), shell=True)
        logger.info("Starting your VM machine with your arguments you gave it to me")
        subprocess.call(BsdCmd.vm_start.format(host), shell=True)
        logger.info("Configuration ended successfully. "
                    "Please search {} into diskless to set OS of you desire".format(host))
        subprocess.call(BsdCmd.vm_list, shell=True)
        sleep(5)
        subprocess.call(BsdCmd.vm_list, shell=True)
        sleep(12)
        subprocess.call(BsdCmd.vm_list, shell=True)
        logger.info("Configuration ended successfully. "
                    "Please search {} into diskless to set OS of you desire".format(host))
        logger.info("Script has ended. SEE YA")
        exit(0)
