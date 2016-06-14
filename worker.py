from subprocess import check_output

import os

from windows import set_reg_values
STARCRAFT_DIR = r"C:/Program Files (x86)/StarCraft"
SCLE_DIR = "C:/Libraries/StarCraftLearningEnv"

EXECUTABLE_COMMAND = " \
{SCLE_DIR}/injectory.x86.exe \
    --launch '{STARCRAFT_DIR}/StarCraft.exe' \
    --inject '{STARCRAFT_DIR}/bwapi-data/BWAPI.dll' \
    --inject '{SCLE_DIR}/injectables/wmode.dll' \
".format(STARCRAFT_DIR=STARCRAFT_DIR, SCLE_DIR=SCLE_DIR)

print(EXECUTABLE_COMMAND)

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
        pid = check_output(EXECUTABLE_COMMAND)

        print pid
        with os.open("worker.pids", 'rw') as pid_file:
            pid_file.write("10000")

    def close(self):
        with os.open("worker.pids", 'rw') as pid_file:
            pids = pid_file.read()


worker = Worker()
worker.configure()
worker.start()