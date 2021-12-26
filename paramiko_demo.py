import paramiko
import sys

class Paramiko_Cmd:
    def __init__(self):
        ip='xxx.xxx.xx.x'
        port=22
        username='bob'
        password='mypasswd'

        cmd='nvidia-smi' 

        self.ssh=paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip,port,username,password)
        

    def cmd(self, cmd):
        print('\n\ncmd:',cmd)
        stdin,stdout,stderr=self.ssh.exec_command(cmd)
        outlines=stdout.readlines()
        #print(outlines,'\n'*2)

        resp=''.join(outlines)
        print(resp)

        stdinl=stderr.readlines()
        print('stdin:',stdinl)

        stderrl=stderr.readlines()
        print('stderr:',stderrl)
        
    def copy(self, src='server_test.py',dst='/tmp/server_test.py'):
        sftp = self.ssh.open_sftp()
        sftp.put(src, dst)
        sftp.close()
    
    def __del__(self):
        self.ssh.close()

if __name__=='__main__':
    param  = Paramiko_Cmd()
    ## Tensorflow check
    param.cmd('pwd')
    param.cmd('virtualenv venv3 --python=python3')
    param.cmd('source venv3/bin/activate')
    param.cmd('pip3 install tensorflow==2.4.0')
    param.cmd('pip3 list')
    param.cmd('source /cuda-env/cuda11.0-env')
    param.cmd('nvidia-smi')
    
    param.copy('server_test.py', 'server_test.py')
    param.cmd('ls')
    # Run the transmitted script remotely without args and show its output.
    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
    param.cmd('venv3/bin/python server_test.py')

    sys.exit(0)
