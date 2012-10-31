import yaml
import inspect

from jubatest.client import command

class Operator:

  def __init__(self, configfile):
    self.configfile = configfile
    self.results = {}

  def run(self):
    with open(self.configfile, 'r') as config:
      for index, data in enumerate(yaml.load_all(config)):
        getattr(self, data['action'])(index, data)

  def command(self, index, data):
    client = command.Client()
    result = client.execute(data['host'], data['command'])
    self.results[index] = not result.failed

  def test(self, index, data):
    self.results[index] = True

  def print_details(self):
    print 'file:', self.configfile
    print 'result:'
    for index in sorted(self.results.keys()):
      print ' ', index + 1, ':', self.results[index]
