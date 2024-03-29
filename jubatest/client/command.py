import ssh
import subprocess

from jubatest.result import Result

class CommandClient:

  def execute(self, data):
    if data.has_key('host') and len(data['host']) != 0:
      return self.__remote(data)
    else:
      return self.__local(data)

  def __remote(self, data):
    # TODO: multiple hosts
    host = data['host']
    command_args = data['command']
    client = ssh.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(ssh.AutoAddPolicy())

    connected = False
    # TODO: cache password
    password = None
    tried = 0
    while not connected:
      try:
        tried += 1
        client.connect(host, password=password)
        connected = True
      except (ssh.PasswordRequiredException, ssh.AuthenticationException):
        if tried <= 3:
          import getpass
          prompt = 'password for %s: ' % (host)
          password = getpass.getpass(prompt)
          continue
        else:
          raise
      except:
        raise

    (stdin, stdout, stderr) = client.exec_command(command_args)

    result = Result()
    result.stdout = stdout.read().strip().split('\n') if stdout else None
    result.stderr = stderr.read().strip().split('\n') if stderr else None
    # TODO: check return code
    result.succeeded = True if len(result.stderr) != 0 else False

    client.close()

    return result

  def __local(self, data):
    command_args = data['command'].split()
    stdout_stream = subprocess.PIPE
    stderr_stream = subprocess.PIPE

    proc = subprocess.Popen(
      command_args,
      shell = True,
      stdout = stdout_stream,
      stderr = stderr_stream
    )
    (stdout, stderr) = proc.communicate()

    result = Result()
    result.stdout = stdout.strip().split('\n') if stdout else None
    result.stderr = stderr.strip().split('\n') if stderr else None
    result.succeeded = False if proc.returncode else True

    return result
