
bsd = "FreeBSD"
rhel = "RED HAT"
system_id_info = "VM will be created on system you are currently on: {}"
ppt_def_value = "0"
memory_def_value = "16"
cpu_def_value = "16"
system_val_rhel = "linux"
system_val_bsd = "bsd"
ddp_pkg = "If you are creating VM on 100G project please be sure that correct DDP package was added."
class BsdCmd:
    string_to_replace = "  device : \"{}\";"
    iov_temp = "iovctl.txt"
    iovctl_conf = "iovctl.conf"
    iovctl_cmd = "iovctl -C -f {}".format(iovctl_conf)
    vm_create = "vm create {}"
    path_host_conf = "/opt/vms/{}/"
    mem_string_to_replace = "memory=4G"
    cpu_string_to_replace = "cpu=4"
    replaced_mem_string = "memory={}G"
    replaced_cpu_string = "cpu={}"
    vm_passthru_find = "vm passthru | grep ' Yes '"  # Find VF passthrough address
    vm_start = "vm start {}"
    vm_list = "vm list"


class RhelCmd:
    drv_info = "To ensure that VM will be created properly,\n \
    please install proper NIC driver from /opt/common/drivers/"
    vm_number = "1"
    vf_driver = "lsmod | grep vf"
    vf_driver_loaded = "VF Driver is loaded. Trying to unload...'"
    vf_diver_unload_success = "VF Driver ({}) unload successfully. Proceeding..."
    vf_driver_unloaded = "VF Driver is NOT loaded. Proceeding..."
    vf_driver_unloading = "rmmod {}"
    vm_number_path_cmd = "echo {} > /sys/class/net/{}/device/sriov_numvfs"
    list_vf_driver = "lspci -vv | grep Eth"
    path_host_conf = "/etc/libvirt/qemu/"
    xml_temp = "uXXYY_temp.xml"
    libvirtd_restart = "service libvirtd restart"
    virsh_start = "virsh start {}"
    virsh_list = "virsh list"
    if_up = "ifconfig {} up"
    vm_list = ["iavf", "ixlvf", "ixv", "i40evf", "igbvf", "ixgbevf"]


