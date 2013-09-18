__author__ = "Jeremy Nelson"


import argparse
import os
import subprocess
import sys




class Platform(object):
    """Convenience Class for running the Redis Library Services Platform"

    NOTE: Platform class not meant for production RLSP, but only for
    local development and evaluation purposes
    """

    def __init__(self,
                 **kwargs):
        "Creates an Platform instance"
        self.django_process = None
        self.django_ip_addr = kwargs.get('ip_addr',
                                           '0.0.0.0')
        self.django_port = kwargs.get('port', 8000)
        self.redis_process = None
        self.working_dir = os.path.dirname(".")
        print(self.working_dir)
        if sys.platform.startswith('win'):
            self.redis_bin_location = "winbinaries"
        else:
            self.redis_bin_location = "."

    def start(self):
        "Starts up Redis and Django processes"
        self.redis_process = subprocess.Popen([
            os.path.join(self.working_dir,
                         self.redis_bin_location,
                         "redis-server"),
            os.path.join(self.working_dir,
                         "bibframe-datastore",
                         "rlsp-basic.conf")])
        self.django_process = subprocess.Popen([
            sys.executable,
            os.path.join(self.working_dir,
                         "aristotle-library-apps",
                         "manage.py"),
            "runserver",
            "{0}:{1}".format(
                self.django_ip_addr,
                self.django_port)])

    def stop(self):
        "Terminates Redis and Django processes"
        self.redis_process.terminate()
        self.django_process.terminate()
    
parser = argparse.ArgumentParser(
    description='Manage Redis Library Services Platform')
parser.add_argument('mode',
                    help='Start for Stop RLSP')
mode = parser.parse_args().mode
platform = Platform()
if mode.lower().startswith("start"):
    platform.start()
else:
    platform.stop()
