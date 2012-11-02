from jubatest.client.command import CommandClient
from jubatest.result import Result

class Tester:

  def run(self, data):
    client = CommandClient()
    command_result = client.execute(data)

    result = Result()
    result.expected = data['expected']
    result.actual= command_result.stdout
    # TODO: assertion type
    result.succeeded = True if result.expected == result.actual else False

    return result
