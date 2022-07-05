import re
import subprocess
from time import sleep

import cmd
from cmd import RhelCmd
from host_dict import host_dict
from logger import logger

xml_replaced_values = []
xml_values_to_replace = ['%HOST%',
                         '%MEM%',
                         '%CUR_MEM%',
                         '%CPUNUM%',
                         '%BUS%',
                         '%SLOT%',
                         '%FUNCTION%',
                         '%PORT%',
                         '%MAC%']



def rhel(host: str,
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
    sleep(3)
    drv_loaded = subprocess.Popen(RhelCmd.vf_driver, stdout=subprocess.PIPE, shell=True)
    # this is needed to corectly read exit code:
    drv_loaded.communicate()[0]
    print(drv_loaded.returncode)
    if drv_loaded.returncode == 0:
        logger.info(RhelCmd.vf_driver_loaded)
        drv_unloaded = subprocess.check_output(RhelCmd.vf_driver, shell=True, encoding='UTF-8')
        for elem in RhelCmd.vm_list:
            if elem in drv_unloaded:
                print(elem)
                subprocess.Popen(RhelCmd.vf_driver_unloading.format(elem), stdout=subprocess.PIPE, shell=True)
                logger.info(RhelCmd.vf_diver_unload_success.format(elem))
    if drv_loaded.returncode == 1:
        logger.info(RhelCmd.vf_driver_unloaded)
    subprocess.call(RhelCmd.vm_number_path_cmd.format(RhelCmd.vm_number, interface), shell=True)
    logger.info("activating interface ({})".format(interface))
    subprocess.call(RhelCmd.vm_number_path_cmd.format(RhelCmd.if_up, interface), shell=True)
    logger.info(RhelCmd.vm_number_path_cmd.format(RhelCmd.vm_number, interface))
    logger.info("Added VM quantity you'v provided to sriov_numvfs path ")

    logger.info("Finding proper function ({}) from bus:slot:function ...".format(ppt))
    process = subprocess.Popen(RhelCmd.list_vf_driver, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.read().decode('utf-8')
    rhel_regex = '([a-zA-Z0-9]{1,2}:[a-zA-Z0-9]{1,2}.'+ppt+')(.*Virtual\sFunction)'
    regex = re.search(rhel_regex, output)
    if regex is None:
        logger.error("Regex probably not found - pls be sure that VM instance was created.")
        subprocess.call(cmd.RhelCmd.list_vf_driver, shell=True)
        logger.info("PLease be sure that proper driver is installed")
        exit(1)
    function = regex.group(1)
    function = function.replace(":", ".")

    xml_replaced_values.append(host)
    xml_replaced_values.append(memory)
    xml_replaced_values.append(memory)
    xml_replaced_values.append(cpu)
    for item in function.split("."):
        xml_replaced_values.append(item)
    xml_replaced_values.append(ppt)
    xml_replaced_values.append(host_dict[host])
    logger.info("Copying temp XML file to desirable path")
    host_xml_cmd = "cp {} {}{}.xml".format(cmd.RhelCmd.xml_temp, cmd.RhelCmd.path_host_conf, host)
    subprocess.call(host_xml_cmd, shell=True)
    logger.info("Replacing strings in xml file to create instance of VM  with variables you gave me")
    logger.debug(xml_replaced_values)
    file = cmd.RhelCmd.path_host_conf + host + ".xml"  # TODO maybe some try except if file not exist
    for i in range(0, len(xml_replaced_values)):  # TODO refactor this to not open file every line
        with open(file, "r") as r:
            mem_swap = r.read().replace(xml_values_to_replace[i], xml_replaced_values[i])

        with open(file, "w") as w:
            w.write(mem_swap)
    logger.info("XML is set. Now restarting libvirtd service...")
    subprocess.call(cmd.RhelCmd.libvirtd_restart, shell=True)  # shell=True
    logger.info("libvirtd service restarted")
    logger.info("Everything seems to work fine. Now starting VM: ({})".format(host))
    subprocess.call(cmd.RhelCmd.virsh_start.format(host), shell=True)  # shell=True
    logger.info("VM started. Now you should be able to see it running:")
    subprocess.call(cmd.RhelCmd.virsh_list, shell=True)
    sleep(5)
    subprocess.call(cmd.RhelCmd.virsh_list, shell=True)
    logger.info("Configuration ended successfully. "
                "Please search {} into diskless to set OS of you desire".format(host))
    logger.info("Script has ended. SEE YA")
    exit(0)
