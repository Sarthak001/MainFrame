import paramiko
import time
import _thread

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

global channel
channel = None
def connect(ip,port,user,passwd):
     global channel
     ssh.connect(ip,port=port,username=user,password=passwd)
     channel = ssh.invoke_shell()



def output_send():
     global channel
     if(channel and channel.recv_ready()):
          data = channel.recv(9999)
          output = data.decode()
          return output


def recv(command):
     global channel
     channel.send(command)
