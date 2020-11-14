#!/usr/bin/python3

import argparse
import yaml
import base_benchmark
import time
import subprocess
import sys

class timed_command(base_benchmark.base_benchmark):
    def __init__(self):
        base_benchmark.base_benchmark.__init__(self)
        self.name = __class__.__name__

    def run_benchmark(self):
        print("running " + self.get_name())
        print(self.settings)
        command = self.settings['command']
        start = time.time()
        with subprocess.Popen(command, stdout=sys.stderr, stderr=subprocess.PIPE, universal_newlines=True, shell=True) as process:
                _, stderr = process.communicate()
                if process.returncode != 0:
                    print(stderr.splitlines()[:-1], file=sys.stderr)
                    raise ExecutionError(command, process.returncode)
        end = time.time() - start
        print(end)
        return end
