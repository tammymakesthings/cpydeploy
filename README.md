# What is CPYDeploy?

This script assists in deploying a script and its associated libraries
(and, eventually, other resources) to a Circuit Python device. By maintaining
an up-to-date unzipped copy of the Circuit Python library bundle on your
computer, you can easily downlaod the script and the latest versions of
all required libraries in one step.

# What Does It Do?

At present, CPYDeploy will copy the specified script, and the libraries
it uses, to your Circuit Pythonh board/device. That's it. But I'm rapidly
developing this to make it a more fully featured deployment tool for 
CircuitPython projects.

# Using CPYDeploy

The process of using the CPYDeploy is as follows:

1. Create a YAML deployment spec for the script you're deploying.
2. Run the `cpy_deploy.py` tool.

These steps are described in more detail in the following sections.

## Global Configuration

Currently, you need to edit the definition of `CPY_LIBDIR` near the
top of the `cpy_deploy.py` file to define the location of the 
Circuit Python library bundle. This will shortly be moved to a config
file.

## Creating a YAML Deployment Spec

Each Circuit Python script to be deployed needs to have a deployment
specification file. This is named the same as the script, but with a
`.yaml` extension. This deployment spec needs to contain the following
elements:

- `deploy_as`: Specifies the name you'd like the script to have when
  it's deployed on the target board (for example, `main.py`).

- `libraries`: A list of the libraries used by the script. These should
  correspond with either a subdirectory in the Circuit Python library
  bundle, or the name (minus extension) of a single .mpy file in the
  library bundle for libraries not in a subdirectory.

Here's a sample YAML file showing the deployment of the script
`cp_neopixel_demo.py`. The YAML file needs to be named 
`cp_neopixel_demo.yaml` and be in the same directory as the script
to be deployed.

```yaml
"deploy_as": "main.py"
"libraries":
  - "neopixel"
  - "adafruit_fancyled"
  - "adafruit_itertools"
```

Note that the sample YAML file in this repo currently has some extra
stuff for future expansion. Unrecognized elements in the YAML file are
parsed when the file is read, but are ignored.

## Running the Script

The command-line usage for the script is:

`cpy_deploy.py [--libdir path_to_library_bundle] [--cpydrive drive_name] script_name.py`

The source folder containing the CircuitPython library bundle is defined
by the CPY_LIBDIR constant, or can be overridden by the --libdir command
line option..

The name of your CircuitPython's drive defaults to CIRCUITPY, but you
can override this with the --cpydrive command line option.

# Future Enhancements

The following tasks are on the roadmap for this script. If you feel like
contributing to this project, feel free to submit pull requests.

## Minimum Viable Script tasks
- [ ] Error handling

## Enhanced Functionality
- [ ] Deploying other assets (bitmaps, fonts, etc.)
- [ ] Configuring library sources in the YAML file
- [ ] Global YAML plus per-project
- [ ] Detection of CPY version installed and copying appropriate libraries
- [ ] Function to scan the script file and attempt to generate a YAML config
- [ ] Function to download/update CP Library Bundle zips

## Refactoring
- [ ] A more robust implementation of find_cpy_drive
- [ ] Modularize script methods into the library and incorporate that

# Contributing
Please be aware that by contributing to this
project you are agreeing to the 
[Code of Conduct](https://github.com/tammymakesthings/cpydeploy/blob/master/CODE_OF_CONDUCT.md).
Contributors who follow the 
[Code of Conduct](https://github.com/tammymakesthings/cpydeploy/blob/master/CODE_OF_CONDUCT.md)
are welcome to submit pull requests and they will be promptly reviewed by project admins.