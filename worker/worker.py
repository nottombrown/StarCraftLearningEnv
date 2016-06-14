import atexit
import logging
import os
from time import sleep
from win32api import ShellExecute

import subprocess

# import admin
logging.basicConfig()
logger = logging.getLogger(__name__)

STARCRAFT_DIR = "C:/StarCraft"
SCLE_DIR = "C:/Libraries/StarCraftLearningEnv"


class Worker(object):
    """
    Tiny python script responsible for starting up an injected StarCraft.exe and closing it upon
    request or failure.
    """

    def __init__(self):
        self.proc = None

    @staticmethod
    def _executable_command():

        if " " in STARCRAFT_DIR or " " in SCLE_DIR:
            logger.error("Directories must not have a space in them for injectory.exe to work correctly.")

        # Command flags here: https://github.com/blole/injectory/tree/651700018750c4f2003f1f048b090c4d521717a6
        injectory_command = "{SCLE_DIR}/bin/injectory.x86.exe \
            --launch {STARCRAFT_DIR}/StarCraft.exe \
            --inject {STARCRAFT_DIR}/bwapi-data/BWAPI.dll \
            --inject {SCLE_DIR}/injectables/wmode.dll \
            --kill-on-exit --wait-for-exit --rethrow"

        return injectory_command.format(STARCRAFT_DIR=STARCRAFT_DIR, SCLE_DIR=SCLE_DIR)

    def start(self):
        command = self._executable_command()

        logger.info("Starting worker with the following command: \n{}".format(command))
        # pid = ShellExecute(command)
        self.proc = subprocess.Popen(command)
        print self.proc

    def close(self):
        logger.info("Closing worker")

        self.proc.kill()
        self.proc.wait()

if __name__ == '__main__':
    logger.setLevel(logging.INFO)

    worker = Worker()
    worker.start()

    # Close the worker on ending this process
    def handle_exit():
        worker.close()

    atexit.register(handle_exit)

    # Keep this running
    while(True):
        sleep(1)
