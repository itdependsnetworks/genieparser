expected_output = {
    "Port-channel12": {
        "operational_mode": "trunk",
        "switchport_mode": "trunk",
        "access_vlan_name": "default",
        "private_vlan": {},
        "switchport_enable": True,
        "native_vlan_tagging": True,
        "negotiation_of_trunk": False,
        "encapsulation": {
            "native_vlan": "1",
            "native_vlan_name": "default",
            "operational_encapsulation": "dot1q",
            "administrative_encapsulation": "dot1q",
        },
        "port_channel": {
            "port_channel_member_intfs": ["TenGigabitEthernet1/1/2"],
            "port_channel_member": True,
        },
        "pruning_vlans": "2-1001",
        "access_vlan": "1",
        "unknown_multicast_blocked": False,
        "trunk_vlans": "1,111,130,131,400,405,410,420,430,439-442,450,451,460,",
        "unknown_unicast_blocked": False,
    },
    "TenGigabitEthernet1/1/2": {
        "access_vlan": "1",
        "operational_mode": "trunk",
        "switchport_mode": "trunk",
        "access_vlan_name": "default",
        "switchport_enable": True,
        "private_vlan": {},
        "capture_mode": False,
        "trunk_vlans": "1,111,130,131,400,405,410,420,430,439-442,450,451,460,",
        "capture_vlans": "all",
        "negotiation_of_trunk": False,
        "unknown_multicast_blocked": False,
        "port_channel": {
            "port_channel_int": "Port-channel12",
            "port_channel_member": True,
        },
        "native_vlan_tagging": True,
        "encapsulation": {
            "native_vlan": "1",
            "native_vlan_name": "default",
            "operational_encapsulation": "dot1q",
            "administrative_encapsulation": "dot1q",
        },
        "unknown_unicast_blocked": False,
        "pruning_vlans": "2-1001",
    },
}