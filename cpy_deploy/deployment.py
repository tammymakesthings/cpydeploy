import yaml
import os
import sys
import shutil

class Deployment:
    def __init__(self, helpers, boards):
        self.description = "CPY_Deploy Deployment Methods"
        self.helpers     = helpers
        self.boards      = boards
        
    def deploy_script_file(script_file, deploy_to, as_file):
        """Deploy a Python script file to the CPY drive.

        Arguments:
            script_file {string} -- The name of the script file to deploy
            deploy_to {string} -- The directory to which the script file will be copied
            as_file {string} -- The name of the script file on the target.
        """
        print('    - ', script_file, '=>', f"{deploy_to}{as_file}")
        shutil.copyfile(script_file, os.path.join(deploy_to, as_file))

    def deploy_library_dir(library_name, lib_src_dir, deploy_to):
        """Copy a library directory to the CPY drive.

        Arguments:
            library_name {string} -- The name of the library to copy
            lib_src_dir {string} -- The folder containing the CPY library bundle
            deploy_to {string} -- The target directory to deploy the library to]
        """
        print('    - ', library_name, ':', lib_src_dir.replace(f"{helpers.config['libdir']}{os.sep}", ''), '=>', deploy_to)
        if os.path.exists(deploy_to):
            shutil.rmtree(deploy_to, ignore_errors=True)
        shutil.copytree(lib_src_dir, deploy_to, ignore=shutil.ignore_patterns('.git'))

    def deploy_library_file(library_name, source_file, deploy_to):
        """Copy a single .mpy library file to the CPY drive.

        Arguments:
            library_name {string} -- The name of the library to deploy.
            source_file {string} -- The path to the source .mpy file.
            deploy_to {[type]} -- The target path on the CPU device.
        """
        print('    - ', library_name, ':', source_file.replace(f"{helpers.config['libdir']}{os.sep}", ''), '=>', deploy_to)
        shutil.copyfile(source_file, deploy_to)
