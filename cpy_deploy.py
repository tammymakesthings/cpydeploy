############################################################################
# cpy_deploy.py: Deploy a CircuitPython program and its dependencies
# Version 0.01, 05/30/2019, Tammy Cravit, tammymakesthings@gmail.com
############################################################################

"""CircuitPython Deployment Helper

This script assists in deploying a script and its associated libraries
(and, eventually, other resources) to a Circuit Python device. By maintaining
an up-to-date unzipped copy of the Circuit Python library bundle on your
computer, you can easily downlaod the script and the latest versions of
all required libraries in one step.

The name of the script to be deployed is specified as the first command
line argument. For each script you deploy, you need to create a .yaml
file of the same name containing the dependency information.

The YAML file should contain the following elements:

- deploy_as (string): THe name for the script in the target directory
                      (for example, 'main.py')

- libraries (string array): A list of libraries to include in the
  deployment. These can correspond to either a subdirectory of the
  CircuitPython library bundle, or to a single .mpy in the lib/ directory.

The source folder containing the CircuitPython library bundle is defined
by the helpers.config['libdir'] constant, or can be overridden by the --libdir command
line option..

The name of your CircuitPython's drive defaults to CIRCUITPY, but you
can override this with the --cpydrive command line option.
"""

import yaml
import os
import sys
import argparse
import shutil

import cpy_deploy

##### The current version number
VERSION    = "0.02"

##### The date of this version
VERDATE    = "05/30/2019"

###########################################################################

# cpy_deploy library objects

helpers    = cpy_deploy.Helpers()
boards     = cpy_deploy.Boards()
deployment = cpy_deploy.Deployment(helpers, boards)

############################################################################
# The main script starts here
############################################################################

arg_defaults = {}
arg_defaults["libdir"]    = 'D:/Electronics/circuitpython_code/adafruit-circuitpython-bundle-4.x-mpy'
arg_defaults["boardname"] = 'CIRCUITPY'
args = helpers.read_cmdline_helpers()

helpers.app_banner(VERSION, VERDATE)

global_config  = helpers.load_yaml_helpers(os.path.join(os.path.dirname(os.path.realpath(__file__))),'cpy_deploy.yaml')
script_config  = helpers.load_yaml_helpers(args.script[0].replace('.py', '.yaml'))
helpers.config = global_config.update(script_config)

deploy_path = helpers.find_cpy_path(helpers.config.cpydrive)

print('* Deploying script', args.script[0], 'to', deploy_path)

print('  - Script files:')
deployment.deploy_script_file(args.script[0], deploy_path, helpers.config['deploy_as'])

print('  - Library files:')
for lib in helpers.config['libraries']:
    lib_src_dir = os.path.join(helpers.config['libdir'], 'lib', lib)
    if (os.path.exists(lib_src_dir)):
        deployment.deploy_library_dir(lib, lib_src_dir, os.path.join(deploy_path, 'lib', lib))
    elif(os.path.exists(os.path.join(helpers.config['libdir'], 'lib', f"{lib}.mpy"))):
        deployment.deploy_library_file(lib, os.path.join(helpers.config['libdir'], 'lib', f"{lib}.mpy"), os.path.join(deploy_path, 'lib', f'{lib}.mpy'))
    else:
        print('    - ', lib, ': skipped (not found)')
