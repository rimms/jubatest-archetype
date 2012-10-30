import yaml

from jubatest.client.command import LocalClient

class Runner:

  def __init__(self, configfile):
    self.configfile = configfile
    self.results = {}

  def execute(self):
    with open(self.configfile, 'r') as config:
      for index, data in enumerate(yaml.load_all(config)):
        getattr(self, data['type'])(index, data)

  def command(self, index, data):
    client = LocalClient()
    client.execute(data['command'])
    self.results[index] = True

  def test(self, index, data):
    self.results[index] = True

  def print_details(self):
    print 'file:', self.configfile
    print 'result:'
    for index in sorted(self.results.keys()):
      print ' ', index + 1, ':', self.results[index]
