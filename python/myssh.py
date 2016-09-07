#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-01 15:55:56
# @Link    : http://example.org
# @Version : $Id$


import paramiko
import time
import sys
import json
import chardet

def sshclient_execmd(hostname, port, username, password, passroot, execmd):
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname,port=port,username=username,password=password)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - root')
        ssh.send('\n')
        time.sleep(0.1)
        buff = ''
        time.sleep(0.1)
        while not buff.endswith('Password: '):
            resp = ssh.recv(9999)
            fencode=chardet.detect(resp)['encoding']
            buff += resp.decode(fencode)
        ssh.send(passroot)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            fencode=chardet.detect(resp)['encoding']
            buff += resp.decode(fencode)

        ssh.send(execmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(999999)
            fencode=chardet.detect(resp)['encoding']
            buff += resp.decode(fencode)
        result=buff
    else:
        stdin, stdout, stderr = s.exec_command(execmd)
        # Generally speaking, the first connection, need a simple interaction.
        stdin.write("Y")
        result=stdout.read()
    s.close()
    return result


def main():
    try:
        file=open(sys.argv[1],'r')
        confs=json.loads(file.read())
        file.close()
        hostname = confs['hostname']
        port = int(confs['port'])
        username = confs['username']
        password = confs['password']
        passroot = confs['passroot']
        execmd = sys.argv[2]
        result=sshclient_execmd(hostname, port, username, password, passroot,execmd)
    except Exception as err:
        result="命令执行失败:"+str(err)
    finally:
        return result
if __name__ == "__main__":
    print(main())
