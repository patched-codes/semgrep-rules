# License: MIT (c) GitLab Inc.

from pysnmp.hlapi import *


# SNMPv3 User details
username = 'myUsername'  
auth_key = 'myAuthKey'
priv_key = 'myPrivKey'


# auth MD5, privacy DES
# ok: python_snmp_rule-snmp-weak-cryptography
user_data1 = UsmUserData(username, auth_key, priv_key)
print(f"auth MD5, privacy DES : \n {user_data1}")


# auth SHA, privacy AES128
# ok: python_snmp_rule-snmp-weak-cryptography
user_data2 = UsmUserData(username, auth_key, priv_key,
                        authProtocol=usmHMACSHAAuthProtocol,
                        privProtocol=usmAesCfb128Protocol)
print("\nauth SHA, privacy AES128 : \n", user_data2)

# auth MD5, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data3 = UsmUserData(username, auth_key)
print("\nauth MD5, no privacy : \n",user_data3)

# auth MD5, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data4 = UsmUserData(username, auth_key, privKey=None)
print("\nauth MD5, no privacy : \n",user_data4)

# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data5 = UsmUserData(username, authKey=None, privKey=None)
print("\nno auth, no privacy : \n",user_data5)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data6 = UsmUserData(username)
print("\nno auth, no privacy : \n",user_data6)

# MD5 auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data7 = UsmUserData(username, authKey=auth_key, privKey=priv_key, privProtocol = usmNoPrivProtocol)
print("\nauth MD5, no privacy : \n",user_data7)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data8 = UsmUserData(username, authKey=None, authProtocol=usmNoAuthProtocol, privKey=None, privProtocol=usmNoPrivProtocol)
print("\nno auth, no privacy : \n",user_data8)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data9 = UsmUserData(username, authKey=auth_key, authProtocol=usmNoAuthProtocol)
print("\nno auth, no privacy : \n",user_data9)

# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data10 = UsmUserData(username, privKey=None, privProtocol=usmNoPrivProtocol)
print("\nno auth, no privacy : \n",user_data10)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data11 = UsmUserData(username, authKey=auth_key, privKey=None, authProtocol=(1,3,6,1,6,3,10,1,1,1), privProtocol=(1,3,6,1,6,3,10,1,2,1))
print("\nno auth, no privacy : \n",user_data11)

# MD5 auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data12 = UsmUserData(username, authKey=auth_key, privKey=priv_key, privProtocol=(1,3,6,1,6,3,10,1,2,1))
print("\nauth MD5, no privacy : \n",user_data12)


# SHA auth, AES privacy
# ok: python_snmp_rule-snmp-weak-cryptography
user_data13 = UsmUserData(username, authKey=auth_key, authProtocol=(1,3,6,1,6,3,10,1,1,3), privKey=priv_key, privProtocol=(1,3,6,1,6,3,10,1,2,4))
print("\nSHA auth, AES privacy : \n",user_data13)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data14 = UsmUserData(username, authKey=auth_key, authProtocol=(1,3,6,1,6,3,10,1,1,1))
print("\nno auth, no privacy : \n",user_data14)


# auth MD5, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data15 = UsmUserData(username, auth_key, None)
print("\nauth MD5, no privacy : \n",user_data15)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data16 = UsmUserData(username, None, None)
print("\nno auth, no privacy : \n",user_data16)


# auth SHA, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data17 = UsmUserData(username, auth_key, authProtocol=usmHMACSHAAuthProtocol, securityEngineId=None, securityName=None)
print("\nauth SHA, no privacy : \n",user_data17)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data18 = UsmUserData(username, securityEngineId=None, securityName=None)
print("\nno auth, no privacy : \n",user_data18)


# MD5 auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data19 = UsmUserData(username, authKey=auth_key, authProtocol=(1,3,6,1,6,3,10,1,1,2))
print("\nMD5 auth, no privacy : \n",user_data19)


# no auth, no privacy
# ruleid: python_snmp_rule-snmp-weak-cryptography
user_data20 = UsmUserData(username, None, securityEngineId=None, securityName=None)
print("\nauth MD5, no privacy : \n",user_data15)