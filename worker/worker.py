import logging
import os
from win32api import ShellExecute

import admin
logging.basicConfig()
logger = logging.getLogger(__name__)

STARCRAFT_DIR = r"C:/Program Files (x86)/StarCraft"
SCLE_DIR = "C:/Libraries/StarCraftLearningEnv"



class Worker(object):
    """
    Tiny python script responsible for starting up an injected StarCraft.exe and closing it upon
    request or failure.
    """

    def _executable_command(self):

        command = "{SCLE_DIR}/bin/injectory.x86.exe \
--launch '{STARCRAFT_DIR}/StarCraft.exe' \
--inject '{STARCRAFT_DIR}/bwapi-data/BWAPI.dll' \
--inject '{SCLE_DIR}/injectables/wmode.dll'"

        return command.format(STARCRAFT_DIR=STARCRAFT_DIR, SCLE_DIR=SCLE_DIR).\
            replace('/', '\\')  # Windows likes backslashes

    def start(self):
        command = self._executable_command()
        logger.info("Starting worker with the following command: \n{}".format(command))
        pid = ShellExecute(command)

        print pid
        with os.open("worker.pids", 'rw') as pid_file:
            pid_file.write("10000")

    def close(self):
        logger.info("Closing worker")
        with os.open("worker.pids", 'rw') as pid_file:
            pids = pid_file.read()

if __name__ == '__main__':
    logger.setLevel(logging.INFO)

    if not admin.isUserAdmin():
        logger.info("User is not an admin, escalating")
        admin.runAsAdmin()

    logger.info("User is Administrator")

    worker = Worker()
    worker.start()
    #
    # atexit.register(lambda: worker.close())