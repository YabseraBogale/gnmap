from pymetasploit3.msfrpc import MsfRpcClient
import os
try:
    username=os.getenv("username")
    password=os.getenv("password")
    client= MsfRpcClient(username=username,password=password,port=55553,ssl=True)
    module_type = 'auxiliary'
    module_name = 'scanner/smb/smb_version'
    exploit=client.modules.use(module_type,module_name)
    exploit["RHOSTS"]='192.168.1.1'
    res=exploit.execute()
    job=client.jobs.list
    print(res)
    print(job)

except Exception as e:
    print(e)
