import yaml
import os
import sys
import argparse

class Helpers:
    def __init__(self):
        self.description = "CPY_Deploy Helpers"
        self.config = {}

    def load_yaml_config(filename):
        """Read a YAML configuration file into a dictionary.
        
        Arguments:
            filename {string} -- The location of the YAML configuration file.]

        Returns:
            Dictionary -- The contents of the configuration file. An empty
            dictionary is returned on error.
        """
        with open(filename) as the_stream:
            try:
                return yaml.safe_load(the_stream)
            except yaml.YAMLError as exc:
                print(exc)
                return {}

    def find_cpy_path(cpydrive, mock_target=True):
        """Locate the Circuit Python device's drive location.

        Arguments:
            cpydrive {string} -- The name of the Circuit Python device's drive.
            mock_target (bool) -- Create a mock target directory in c:/temp if the target isn't found

        Returns:
            String -- The location of the CPY drive.
        """
        deploy_path = ''
        if sys.platform == 'win32':
            deploy_path = 'e:\\'
        elif sys.platform.startswith('linux'):
            deploy_path = os.path.join(os.sep, 'media', cpydrive, os.sep),
        else:
            deploy_path = os.path.join(os.sep, cpydrive, os.sep)
        if (os.path.exists(deploy_path) == False) and (mock_target == True):
            deploy_path = "c:/temp/CIRCUITPY"
            if os.path.exists(deploy_path) == False:
                os.mkdir(deploy_path)
        return deploy_path
    
    def app_banner(version_num, version_date):
        print('****************************************************************************')
        print('* cpy_deploy.py: Deploy a script and libraries to a CircuitPython device.  *')
        print('****************************************************************************')
        print(f'Tammy Cravit, tammymakesthings@gmail.com, v{version_num}, {version_date}')
        print('')        
    
    def read_cmdline_args(defaults):
        parser = argparse.ArgumentParser(description='Deploy a CircuitPython program and its dependencies')
        parser.add_argument('script',   nargs=1)
        parser.add_argument('libdir',   nargs='?', default=defaults["libdir"])
        parser.add_argument('cpydrive', nargs='?', default=defaults["boardname"])
        args = parser.parse_args()
        return args
