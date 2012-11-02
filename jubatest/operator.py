import yaml
import inspect

from jubatest.client.command import CommandClient

class Operator:

  def __init__(self, configfile):
    self.configfile = configfile
    self.results = {}

  def run(self):
    with open(self.configfile, 'r') as config:
      for index, data in enumerate(yaml.load_all(config)):
        getattr(self, data['action'])(index, data)

  def command(self, index, data):
    client = CommandClient()
    self.results[index] = client.execute(data)

  def test(self, index, data):
    self.results[index] = True

  def dump(self, outfile):
    ret = []
    for index in sorted(self.results.keys()):
      data = {}
      data['index'] = index + 1
      data['result'] = self.results[index]
      ret.append(data)
    with open(outfile, 'w') as out:
      yaml.dump_all(ret, stream=out, allow_unicode = True, default_flow_style=False)
