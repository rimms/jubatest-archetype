import ssh
import subprocess
import traceback

class CommandClient:

  """
  TODO: switch client
         remotehost -> RemoteClient
         localhost  -> LocalClient
  """

class RemoteClient:

  def execute(self, host, command):
    client = ssh.SSHClient()
    client.load_system_host_keys()
    client.connect(host)
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout.read().split('\n'):
      print line
    client.close()

class LocalClient:

  def execute(self, command):
    stdout = None
    try:
      stdout = subprocess.check_output(command.split(), shell=False, stderr=subprocess.STDOUT)
      print stdout
    except subprocess.CalledProcessError as e:
      traceback.format_exc()

