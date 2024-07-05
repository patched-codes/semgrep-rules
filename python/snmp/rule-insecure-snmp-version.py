# License: MIT (c) GitLab Inc.
# source: https://bandit.readthedocs.io/en/latest/_modules/bandit/plugins/snmp_security_check.html#snmp_insecure_version_check

from pysnmp.hlapi import CommunityData

# SHOULD FAIL
# ruleid: python_snmp_rule-insecure-snmp-version
a = CommunityData('public', mpModel=0)
# ruleid: python_snmp_rule-insecure-snmp-version
b = CommunityData('public', mpModel=1)
