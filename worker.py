from subprocess import check_output

import os

from windows import set_reg_values
CHAOS_LAUNCHER_DIR = r"C:\Libraries\bwapi-src\Release_Binary\Chaoslauncher"

class Worker(object):

    def configure(self):
        set_reg_values(r'Software\Chaoslauncher\Launcher',
                       [
                           ('GameVersion', 'Starcraft 1.16.1'),
                           ('StartMinimized', '0'),
                           ('MinimizeOnRun', '1'),
                           ('RunScOnStartup', '1'),
                           ('AutoUpdate', '0'),
                           ('WarnNoAdmin', '0'),
                           ('TESTING', '0')
                       ])

        set_reg_values(r'Software\Chaoslauncher\PluginsEnabled',
                       [
                           ("BWAPI Injector (1.16.1) RELEASE", '1'),
                           ("W-MODE 1.02", "1"),
                           ("Chaosplugin for 1.16.1", '1')
                       ])

    def start(self):
        pid = check_output(CHAOS_LAUNCHER_DIR + "/chaoslauncher.exe")
        print pid
        with os.open("worker.pids", 'rw') as pid_file:
            pid_file.write("10000")

    def close(self):
        with os.open("worker.pids", 'rw') as pid_file:
            pids = 


worker = Worker()
worker.start()
