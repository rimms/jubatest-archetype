Jubatest
========

A test tool for distributed enviropment.

How to Use
----------

::

  $ git clone https://github.com/rimms/jubatest.git
  $ cd jubatest
  $ python setup.py install
  $ jubatest -c sample/sample.yml
  $ view result-sample.yml

Functions
---------

* Run command
    * localhost
    * remote (via SSH)

* Assertion
    * stdout

TBD
---

* Remote process control and monitoring
    * start
    * stop
    * is_running
    * ...
* Calculate precision
    * number of train data
    * train time
    * ...
* Benchmark
    * latency
    * throughput
    * ...
* Jubatus monitoring
    * model
    * membership
    * ...
* Reporting
    * assert
    * graph
    * ...

