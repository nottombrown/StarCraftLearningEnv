from subprocess import check_output

from windows import set_reg


class Worker(object):

    def configure(self):
        chaos_launcher_reg_edit_config = [
        	('GameVersion', 'Starcraft 1.16.1'),
        	('StartMinimized','0'),
        	('MinimizeOnRun', '1'),
        	('RunScOnStartup', '1'),
        	('AutoUpdate', '0'),
        	('WarnNoAdmin', '0'),
        	('TESTING', '0')
        ]

        reg_path = r'Software\Chaoslauncher\Launcher'
        for name, value in chaos_launcher_reg_edit_config:
            set_reg(reg_path, name, value)

Worker().configure()
