import yaml
import inspect

from jubatest.client.command import CommandClient

class Operator:

  def __init__(self, configfile):
    self.configfile = configfile
    self.results = {}
    self.stdouts = {}
    self.stderrs = {}

  def run(self):
    with open(self.configfile, 'r') as config:
      for index, data in enumerate(yaml.load_all(config)):
        getattr(self, data['action'])(index, data)

  def command(self, index, data):
    client = CommandClient()
    result = client.execute(data)
    self.results[index] = not result.failed
    self.stdouts[index] = result.stdout
    self.stderrs[index] = result.stderr

  def test(self, index, data):
    self.results[index] = True

  def dump(self, outfile):
    ret = []
    for index in sorted(self.results.keys()):
      data = {}
      data['result'] = self.results[index]
      data['stdout'] = self.stdouts[index] if self.stdouts.has_key(index) else ""
      data['stderr'] = self.stderrs[index] if self.stderrs.has_key(index) else ""
      ret.append(data)
    with open(outfile, 'w') as out:
      yaml.dump_all(ret, stream=out, default_flow_style=False)
