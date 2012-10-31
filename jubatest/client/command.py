import ssh
import subprocess
import traceback

class Client:

  def execute(self, host, command):
    return self.__local(command)

  def __remote(self, host, command):
    client = ssh.SSHClient()
    if not env.disable_known_hosts:
      client.load_system_host_keys()
    client.connect(host)
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout.read().split('\n'):
      print line
    client.close()

  def __local(self, command):
    command_args = str(command).split()
    stdout_stream = subprocess.PIPE
    stderr_stream = subprocess.PIPE

    proc = subprocess.Popen(
      command_args,
      shell = True,
      stdout = stdout_stream,
      stderr = stderr_stream
    )
    (stdout, stderr) = proc.communicate()

    result = _Result()
    result.ret = proc.returncode
    result.stdout = stdout.strip() if stdout else ""
    result.stderr = stderr.strip() if stderr else ""
    result.failed = True if result.ret else False

    return result

class _Result(str):
    pass
