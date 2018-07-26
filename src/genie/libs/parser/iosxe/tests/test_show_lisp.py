
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.iosxe.show_lisp import ShowLispSession,\
                                              ShowLispPlatform,\
                                              ShowLispExtranet,\
                                              ShowLispDynamicEidDetail,\
                                              ShowLispService,\
                                              ShowLispServiceMapCache



# =================================
# Unit test for 'show lisp session'
# =================================
class test_show_lisp_session(unittest.TestCase):

    '''Unit test for "show lisp session"'''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default': 
                {'sessions':
                    {'established': 3,
                    'peers':
                        {'2.2.2.2':
                            {'state': 'up',
                            'time': '00:51:38',
                            'total_in': 8,
                            'total_out': 13,
                            'users': 3},
                        '6.6.6.6':
                            {'state': 'up',
                            'time': '00:51:53',
                            'total_in': 3,
                            'total_out': 10,
                            'users': 1},
                        '8.8.8.8':
                            {'state': 'up',
                            'time': '00:52:15',
                            'total_in': 8,
                            'total_out': 13,
                            'users': 3}},
                    'total': 3},
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp session
        Sessions for VRF default, total: 3, established: 3
        Peer                           State      Up/Down        In/Out    Users
        2.2.2.2                        Up         00:51:38        8/13     3
        6.6.6.6                        Up         00:51:53        3/10     1
        8.8.8.8                        Up         00:52:15        8/13     3
        '''}

    def test_show_lisp_session_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_session_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================
# Unit test for 'show lisp platform'
# ==================================
class test_show_lisp_platform(unittest.TestCase):

    '''Unit test for "show lisp platform"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'current_config_style': 'service and instance',
        'latest_supported_config_style': 'service and instance',
        'parallel_lisp_instance_limit': 2000,
        'rloc_forwarding_support':
            {'local':
                {'ipv4': 'ok',
                'ipv6': 'ok',
                'mac': 'unsupported'},
            'remote':
                {'ipv4': 'ok',
                'ipv6': 'ok',
                'mac':'unsupported'}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp platform
        Parallel LISP instance limit:      2000
        RLOC forwarding support:
        IPv4 RLOC, local:                 OK
        IPv6 RLOC, local:                 OK
        MAC RLOC, local:                  Unsupported
        IPv4 RLOC, remote:                OK
        IPv6 RLOC, remote:                OK
        MAC RLOC, remote:                 Unsupported
        Latest supported config style:     Service and instance
        Current config style:              Service and instance
        '''}

    def test_show_lisp_platform_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispPlatform(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_platform_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispPlatform(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===========================================================================
# Unit test for 'show lisp all extranet <extranet> instance-id <instance_id>'
# ===========================================================================
class test_show_lisp_extranet(unittest.TestCase):

    '''Unit test for "show lisp all extranet <extranet> instance-id <instance_id>"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances':
            {0:
                {'service':
                    {'ipv4':
                        {'map_server':
                            {'virtual_network_ids':
                                {'101':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'subscriber':
                                                {'192.168.0.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '192.168.0.0/24'},
                                                '192.168.9.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '192.168.9.0/24'}}}},
                                    'vni': '101'},
                                '102':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'subscriber':
                                                {'172.168.1.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '172.168.1.0/24'}}}},
                                    'vni': '102'},
                                '103':
                                    {'extranets':
                                        {'ext1':
                                            {'extranet': 'ext1',
                                            'home_instance_id': 103,
                                            'provider':
                                                {'100.100.100.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '100.100.100.0/24'},
                                                '200.200.200.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '200.200.200.0/24'},
                                                '88.88.88.0/24':
                                                    {'bidirectional': True,
                                                    'eid_record': '88.88.88.0/24'}}}},
                                    'vni': '103'},
                            'total_extranet_entries': 6}}}}}}}

    golden_output1 = {'execute.return_value': '''
        204-MSMR#show lisp all extranet ext1 instance-id 103
        Output for router lisp 0

        -----------------------------------------------------
        LISP Extranet table
        Home Instance ID: 103
        Total entries: 6
        Provider/Subscriber  Inst ID    EID prefix
        Provider             103        88.88.88.0/24
        Provider             103        100.100.100.0/24
        Provider             103        200.200.200.0/24
        Subscriber           102        172.168.1.0/24
        Subscriber           101        192.168.0.0/24
        Subscriber           101        192.168.9.0/24
        '''}

    def test_show_lisp_extranet_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispExtranet(device=self.device)
        parsed_output = obj.parse(extranet='ext1', instance_id='103')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_extranet_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispExtranet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(extranet='ext1', instance_id='103')


# ==========================================================================
# Unit test for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# ==========================================================================
class test_show_lisp_dynamic_eid_detail(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> dynamic-eid detail"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances':
            {0:
                {'service':
                    {'ipv4':
                        {'etr':
                            {'local_eids':
                                {101:
                                    {'dynamic_eids':
                                        {'192.168.0.0/24':
                                            {'dynamic_eid_name': '192',
                                            'discovered_by': 'Packet Reception',
                                            'eid_address':
                                                {'virtual_network_id': 'red'},
                                            'global_map_server': True,
                                            'id': '192.168.0.0/24',
                                            'interface': 'GigabitEthernet5',
                                            'last_activity': '00:00:23',
                                            'last_dynamic_eid': '192.168.0.1',
                                            'last_dynamic_eid_discovery_time': '01:17:25',
                                            'registering_more_specific': True,
                                            'map_server': False,
                                            'rlocs': 'RLOC',
                                            'roaming_dynamic_eid': 1,
                                            'uptime': '01:17:25',
                                            'site_based_multicast_map_nofity_group': 'none configured'}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 dynamic-eid detail
        Output for router lisp 0

        -----------------------------------------------------
        LISP Dynamic EID Information for VRF "red"

        Dynamic-EID name: 192
          Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
          Registering more-specific dynamic-EIDs
          Map-Server(s): none configured, use global Map-Server
          Site-based multicast Map-Notify group: none configured
          Number of roaming dynamic-EIDs discovered: 1
          Last dynamic-EID discovered: 192.168.0.1, 01:17:25 ago
            192.168.0.1, GigabitEthernet5, uptime: 01:17:25
              last activity: 00:00:23, discovered by: Packet Reception
        '''}

    def test_show_lisp_dynamic_eid_detail_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispDynamicEidDetail(device=self.device)
        parsed_output = obj.parse(instance_id=101)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_dynamic_eid_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispDynamicEidDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id=101)


# =================================================================
# Unit test for 'show lisp all instance-id <instance_id> <service>'
# =================================================================
class test_show_lisp_instance_id_service(unittest.TestCase):

    '''Unit test for "show lisp all instance-id <instance_id> <service>"'''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ipv4': 
                        {'database': 
                            {'dynamic_database_limit': 65535,
                            'dynamic_database_size': 0,
                            'inactive_deconfig_away_size': 0,
                            'route_import_database_limit': 1000,
                            'route_import_database_size': 0,
                            'static_database_limit': 65535,
                            'static_database_size': 1,
                            'total_database_mapping_size': 1},
                        'delegated_database_tree': False,
                        'eid_table': 'vrf red',
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'lisp',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'13.13.13.13 (00:00:35)': 
                                    {'ms_address': '13.13.13.13 (00:00:35)'},
                                '4.4.4.4 (17:49:58)': 
                                    {'ms_address': '4.4.4.4 (17:49:58)'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '2.2.2.2',
                            'map_resolvers': 
                                {'13.13.13.13': 
                                    {'map_resolver': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'map_resolver': '4.4.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process',
                            'use_proxy_etr_rloc': '10.10.10.10'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'imported_route_count': 0,
                            'imported_route_limit': 1000,
                            'map_cache_activity_check_period': '60 secs',
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 1000,
                            'map_cache_size': 2,
                            'persistent_map_cache': False,
                            'static_mappings_configured': 0},
                        'map_request_source': 'derived from EID destination',
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False,
                            'virtual_network_ids': 
                                {'101': 
                                    {'vni': '101'}}},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv4',
                        'site_registration_limit': 0}}}}}

    golden_output1 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4

        =================================================
        Output for router lisp 0
        =================================================
          Instance ID:                         101
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           vrf red
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4 (17:49:58), 13.13.13.13 (00:00:35)
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        2.2.2.2
          ITR use proxy ETR RLOC(s):           10.10.10.10
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Static mappings configured:        0
            Map-cache size/limit:              2/1000
            Imported route count/limit:        0/1000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Database:                            
            Total database mapping size:       1
            static database size/limit:        1/65535
            dynamic database size/limit:       0/65535
            route-import database size/limit:  0/1000
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  lisp
        '''}

    golden_parsed_output2 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ipv6': 
                        {'database': 
                            {'dynamic_database_limit': 65535,
                            'dynamic_database_size': 0,
                            'inactive_deconfig_away_size': 0,
                            'route_import_database_limit': 1000,
                            'route_import_database_size': 0,
                            'static_database_limit': 65535,
                            'static_database_size': 1,
                            'total_database_mapping_size': 1},
                        'delegated_database_tree': False,
                        'eid_table': 'vrf red',
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'lisp',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'13.13.13.13 (00:00:35)': 
                                    {'ms_address': '13.13.13.13 (00:00:35)'},
                                '4.4.4.4 (17:49:58)': 
                                    {'ms_address': '4.4.4.4 (17:49:58)'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '2.2.2.2',
                            'map_resolvers': 
                                {'13.13.13.13': 
                                    {'map_resolver': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'map_resolver': '4.4.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process',
                            'use_proxy_etr_rloc': '10.10.10.10'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'imported_route_count': 0,
                            'imported_route_limit': 1000,
                            'map_cache_activity_check_period': '60 secs',
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 1000,
                            'map_cache_size': 2,
                            'persistent_map_cache': False,
                            'static_mappings_configured': 0},
                        'map_request_source': 'derived from EID destination',
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False,
                            'virtual_network_ids': 
                                {'101': 
                                    {'vni': '101'}}},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ipv6',
                        'site_registration_limit': 0}}}}}

    golden_output2 = {'execute.return_value': '''
        202-XTR#show lisp all instance-id 101 ipv4

        =================================================
        Output for router lisp 0
        =================================================
          Instance ID:                         101
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           vrf red
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4 (17:49:58), 13.13.13.13 (00:00:35)
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        2.2.2.2
          ITR use proxy ETR RLOC(s):           10.10.10.10
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Static mappings configured:        0
            Map-cache size/limit:              2/1000
            Imported route count/limit:        0/1000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Database:                            
            Total database mapping size:       1
            static database size/limit:        1/65535
            dynamic database size/limit:       0/65535
            route-import database size/limit:  0/1000
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  lisp
        '''}

    golden_parsed_output3 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_limit': 65535,
                            'dynamic_database_size': 2,
                            'import_site_db_limit': 65535,
                            'import_site_db_size': 0,
                            'inactive_deconfig_away_size': 0,
                            'proxy_db_size': 0,
                            'route_import_database_limit': 5000,
                            'route_import_database_size': 0,
                            'static_database_limit': 65535,
                            'static_database_size': 0,
                            'total_database_mapping_size': 2},
                        'delegated_database_tree': False,
                        'eid_table': 'Vlan 102',
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'encapsulation': 'vxlan',
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'44.44.44.44 (00:00:45)': 
                                    {'ms_address': '44.44.44.44 (00:00:45)'},
                                '44.44.44.44 (00:00:50)': 
                                    {'ms_address': '44.44.44.44 (00:00:50)'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '11.11.11.1',
                            'map_resolvers': 
                                {'44.44.44.44': 
                                    {'map_resolver': '44.44.44.44'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'imported_route_count': 0,
                            'imported_route_limit': 5000,
                            'map_cache_activity_check_period': '60 secs',
                            'map_cache_fib_updates': 'established',
                            'map_cache_limit': 5120,
                            'map_cache_size': 0,
                            'persistent_map_cache': False,
                            'static_mappings_configured': 0},
                        'map_request_source': 'derived from EID destination',
                        'map_resolver': 
                            {'enabled': False},
                            'map_server': 
                                {'enabled': False,
                                'virtual_network_ids': 
                                    {'0': {'vni': '0'},
                                    '1': {'vni': '1'},
                                    '102': {'vni': '102'},
                                    '131': {'vni': '131'},
                                    '132': {'vni': '132'},
                                    '133': {'vni': '133'},
                                    '134': {'vni': '134'},
                                    '135': {'vni': '135'},
                                    '136': {'vni': '136'},
                                    '137': {'vni': '137'},
                                    '138': {'vni': '138'},
                                    '139': {'vni': '139'},
                                    '140': {'vni': '140'},
                                    '141': {'vni': '141'},
                                    '142': {'vni': '142'},
                                    '143': {'vni': '143'},
                                    '144': {'vni': '144'},
                                    '145': {'vni': '145'},
                                    '146': {'vni': '146'},
                                    '147': {'vni': '147'},
                                    '148': {'vni': '148'},
                                    '149': {'vni': '149'},
                                    '150': {'vni': '150'},
                                    '151': {'vni': '151'},
                                    '152': {'vni': '152'},
                                    '153': {'vni': '153'},
                                    '154': {'vni': '154'},
                                    '155': {'vni': '155'},
                                    '156': {'vni': '156'},
                                    '157': {'vni': '157'},
                                    '158': {'vni': '158'},
                                    '159': {'vni': '159'},
                                    '160': {'vni': '160'},
                                    '161': {'vni': '161'},
                                    '162': {'vni': '162'},
                                    '163': {'vni': '163'},
                                    '164': {'vni': '164'},
                                    '165': {'vni': '165'},
                                    '166': {'vni': '166'},
                                    '167': {'vni': '167'},
                                    '168': {'vni': '168'},
                                    '169': {'vni': '169'},
                                    '170': {'vni': '170'},
                                    '171': {'vni': '171'},
                                    '172': {'vni': '172'},
                                    '173': {'vni': '173'},
                                    '174': {'vni': '174'},
                                    '175': {'vni': '175'},
                                    '176': {'vni': '176'},
                                    '177': {'vni': '177'},
                                    '178': {'vni': '178'},
                                    '179': {'vni': '179'},
                                    '180': {'vni': '180'},
                                    '181': {'vni': '181'},
                                    '182': {'vni': '182'},
                                    '183': {'vni': '183'},
                                    '184': {'vni': '184'},
                                    '185': {'vni': '185'},
                                    '186': {'vni': '186'},
                                    '187': {'vni': '187'},
                                    '188': {'vni': '188'},
                                    '189': {'vni': '189'},
                                    '190': {'vni': '190'},
                                    '191': {'vni': '191'},
                                    '192': {'vni': '192'},
                                    '193': {'vni': '193'},
                                    '194': {'vni': '194'},
                                    '195': {'vni': '195'},
                                    '2': {'vni': '2'}}},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ethernet',
                        'site_registration_limit': 0,
                        'source_locator_configuration': 
                            {'vlans': 
                                {'vlan100': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'},
                                'vlan101': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all instance-id * ethernet

        =================================================
        Output for router lisp 0 instance-id 0
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 1
        =================================================
          Instance ID:                         1
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           Vlan 101
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Mr-use-petr:                         disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 44.44.44.44
                                               66.66.66.66 *** not reachable ***
          ETR Map-Server(s):                   44.44.44.44 (00:00:45)
                                               66.66.66.66 (never)
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        11.11.11.1
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:
            Static mappings configured:        0
            Map-cache size/limit:              4/5120
            Imported route count/limit:        0/5000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Source locator configuration:
            Vlan100: 11.11.11.1 (Loopback0)
            Vlan101: 11.11.11.1 (Loopback0)
          Database:
            Total database mapping size:       2
            static database size/limit:        0/65535
            dynamic database size/limit:       2/65535
            route-import database size/limit:  0/5000
            import-site-reg database size/limit0/65535
            proxy database size:               0
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  vxlan

        =================================================
        Output for router lisp 0 instance-id 2
        =================================================
          Instance ID:                         2
          Router-lisp ID:                      0
          Locator table:                       default
          EID table:                           Vlan 102
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Mr-use-petr:                         disabled
          Delegated Database Tree (DDT):       disabled
          Site Registration Limit:             0
          Map-Request source:                  derived from EID destination
          ITR Map-Resolver(s):                 44.44.44.44
                                               66.66.66.66 *** not reachable ***
          ETR Map-Server(s):                   44.44.44.44 (00:00:50)
                                               66.66.66.66 (never)
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        11.11.11.1
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:
            Static mappings configured:        0
            Map-cache size/limit:              0/5120
            Imported route count/limit:        0/5000
            Map-cache activity check period:   60 secs
            Map-cache FIB updates:             established
            Persistent map-cache:              disabled
          Source locator configuration:
            Vlan100: 11.11.11.1 (Loopback0)
            Vlan101: 11.11.11.1 (Loopback0)
          Database:
            Total database mapping size:       2
            static database size/limit:        0/65535
            dynamic database size/limit:       2/65535
            route-import database size/limit:  0/5000
            import-site-reg database size/limit0/65535
            proxy database size:               0
            Inactive (deconfig/away) size:     0
          Encapsulation type:                  vxlan

        =================================================
        Output for router lisp 0 instance-id 102
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 131
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 132
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 133
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 134
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 135
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 136
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 137
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 138
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 139
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 140
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 141
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 142
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 143
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 144
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 145
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 146
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 147
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 148
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 149
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 150
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 151
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 152
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 153
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 154
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 155
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 156
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 157
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 158
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 159
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 160
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 161
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 162
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 163
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 164
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 165
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 166
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 167
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 168
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 169
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 170
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 171
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 172
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 173
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 174
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 175
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 176
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 177
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 178
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 179
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 180
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 181
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 182
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 183
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 184
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 185
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 186
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 187
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 188
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 189
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 190
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 191
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 192
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 193
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 194
        =================================================
        % EID table not enabled for MAC.

        =================================================
        Output for router lisp 0 instance-id 195
        =================================================
        % EID table not enabled for MAC.
        '''}

    golden_parsed_output4 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_mapping_limit': 1000},
                            'delegated_database_tree': False,
                            'etr': 
                                {'accept_mapping_data': 'disabled, verify disabled',
                                'enabled': True,
                                'map_cache_ttl': '1d00h',
                                'mapping_servers': 
                                    {'13.13.13.13': 
                                        {'ms_address': '13.13.13.13'},
                                    '4.4.4.4': 
                                        {'ms_address': '4.4.4.4'}},
                                'proxy_etr_router': False},
                            'itr': 
                                {'enabled': True,
                                'local_rloc_last_resort': '*** NOT FOUND ***',
                                'map_resolvers': 
                                    {'13.13.13.13': 
                                        {'map_resolver': '13.13.13.13'},
                                    '4.4.4.4': 
                                        {'map_resolver': '4.4.4.4'}},
                                'max_smr_per_map_cache_entry': '8 more specifics',
                                'multiple_smr_suppression_time': '20 secs',
                                'proxy_itr_router': False,
                                'solicit_map_request': 'accept and process'},
                            'locator_status_algorithms': 
                                {'ipv4_rloc_min_mask_len': 0,
                                'ipv6_rloc_min_mask_len': 0,
                                'lsb_reports': 'process',
                                'rloc_probe_algorithm': False,
                                'rloc_probe_on_member_change': False,
                                'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                            'locator_table': 'default',
                            'map_cache': 
                                {'map_cache_activity_check_period': '60 secs',
                                'map_cache_limit': 1000,
                                'persistent_map_cache': False},
                            'map_resolver': 
                                {'enabled': False},
                            'map_server': 
                                {'enabled': False},
                            'mobility_first_hop_router': False,
                            'nat_traversal_router': False,
                            'service': 'ethernet'}}}}}

    golden_output4 =  {'execute.return_value': '''
        202-XTR#show lisp all service ipv4
        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4, 13.13.13.13
          xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
          site-ID:                             unspecified
          ITR local RLOC (last resort):        *** NOT FOUND ***
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Map-cache limit:                   1000
            Map-cache activity check period:   60 secs
            Persistent map-cache:              disabled
          Database:                            
            Dynamic database mapping limit:    1000
        '''}

    golden_parsed_output5 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_mapping_limit': 1000},
                            'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'13.13.13.13': 
                                    {'ms_address': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'ms_address': '4.4.4.4'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '*** NOT FOUND ***',
                            'map_resolvers': 
                                {'13.13.13.13': 
                                    {'map_resolver': '13.13.13.13'},
                                '4.4.4.4': 
                                    {'map_resolver': '4.4.4.4'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process'},
                        'locator_status_algorithms': 
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'map_cache_activity_check_period': '60 secs',
                            'map_cache_limit': 1000,
                            'persistent_map_cache': False},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ethernet'}}}}}

    golden_output5 = {'execute.return_value': '''
        202-XTR#show lisp all service ipv6
        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
          ETR Map-Server(s):                   4.4.4.4, 13.13.13.13
          xTR-ID:                              0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5
          site-ID:                             unspecified
          ITR local RLOC (last resort):        *** NOT FOUND ***
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:                           
            Map-cache limit:                   1000
            Map-cache activity check period:   60 secs
            Persistent map-cache:              disabled
          Database:                            
            Dynamic database mapping limit:    1000
        '''}

    golden_parsed_output6 = {
        'lisp_router_instances': 
            {0: 
                {'lisp_router_id': 
                    {'site_id': 'unspecified',
                    'xtr_id': '0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC'},
                'lisp_router_instance_id': 0,
                'service': 
                    {'ethernet': 
                        {'database': 
                            {'dynamic_database_mapping_limit': 5120},
                            'delegated_database_tree': False,
                        'etr': 
                            {'accept_mapping_data': 'disabled, verify disabled',
                            'enabled': True,
                            'map_cache_ttl': '1d00h',
                            'mapping_servers': 
                                {'44.44.44.44': 
                                    {'ms_address': '44.44.44.44'}},
                            'proxy_etr_router': False},
                        'itr': 
                            {'enabled': True,
                            'local_rloc_last_resort': '*** NOT FOUND ***',
                            'map_resolvers': 
                                {'44.44.44.44': 
                                    {'map_resolver': '44.44.44.44'}},
                            'max_smr_per_map_cache_entry': '8 more specifics',
                            'multiple_smr_suppression_time': '20 secs',
                            'proxy_itr_router': False,
                            'solicit_map_request': 'accept and process'},
                        'locator_status_algorithms':
                            {'ipv4_rloc_min_mask_len': 0,
                            'ipv6_rloc_min_mask_len': 0,
                            'lsb_reports': 'process',
                            'rloc_probe_algorithm': False,
                            'rloc_probe_on_member_change': False,
                            'rloc_probe_on_route_change': 'N/A (periodic probing disabled)'},
                        'locator_table': 'default',
                        'map_cache': 
                            {'map_cache_activity_check_period': '60 secs',
                            'map_cache_limit': 5120,
                            'persistent_map_cache': False},
                        'map_resolver': 
                            {'enabled': False},
                        'map_server': 
                            {'enabled': False},
                        'mobility_first_hop_router': False,
                        'nat_traversal_router': False,
                        'service': 'ethernet',
                        'source_locator_configuration': 
                            {'vlans': 
                                {'vlan100': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'},
                                'vlan101': 
                                    {'address': '11.11.11.1',
                                    'interface': 'Loopback0'}}}}}}}}

    golden_output6 = {'execute.return_value': '''
        OTT-LISP-C3K-3-xTR1#show lisp all service ethernet

        =================================================
        Output for router lisp 0
        =================================================
          Router-lisp ID:                      0
          Locator table:                       default
          Ingress Tunnel Router (ITR):         enabled
          Egress Tunnel Router (ETR):          enabled
          Proxy-ITR Router (PITR):             disabled
          Proxy-ETR Router (PETR):             disabled
          NAT-traversal Router (NAT-RTR):      disabled
          Mobility First-Hop Router:           disabled
          Map Server (MS):                     disabled
          Map Resolver (MR):                   disabled
          Mr-use-petr:                         disabled
          Delegated Database Tree (DDT):       disabled
          ITR Map-Resolver(s):                 44.44.44.44
                                               66.66.66.66
          ETR Map-Server(s):                   44.44.44.44
                                               66.66.66.66
          xTR-ID:                              0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC
          site-ID:                             unspecified
          ITR local RLOC (last resort):        *** NOT FOUND ***
          ITR Solicit Map Request (SMR):       accept and process
            Max SMRs per map-cache entry:      8 more specifics
            Multiple SMR suppression time:     20 secs
          ETR accept mapping data:             disabled, verify disabled
          ETR map-cache TTL:                   1d00h
          Locator Status Algorithms:
            RLOC-probe algorithm:              disabled
            RLOC-probe on route change:        N/A (periodic probing disabled)
            RLOC-probe on member change:       disabled
            LSB reports:                       process
            IPv4 RLOC minimum mask length:     /0
            IPv6 RLOC minimum mask length:     /0
          Map-cache:
            Map-cache limit:                   5120
            Map-cache activity check period:   60 secs
            Persistent map-cache:              disabled
          Source locator configuration:
            Vlan100: 11.11.11.1 (Loopback0)
            Vlan101: 11.11.11.1 (Loopback0)
          Database:
            Dynamic database mapping limit:    5120
        '''}

    def test_show_lisp_instance_id_service_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_lisp_instance_id_service_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id=101, service='ipv6')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_lisp_instance_id_service_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_lisp_instance_id_service_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_lisp_instance_id_service_full5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_lisp_instance_id_service_full6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowLispService(device=self.device)
        parsed_output = obj.parse(instance_id='*', service='ethernet')
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_show_lisp_instance_id_service_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLispService(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(instance_id='*', service='ipv4')





if __name__ == '__main__':
    unittest.main()
