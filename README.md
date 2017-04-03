# saltstack-vulcan

Vulcan is a formula build tool for SaltStack. The idea is to assemble formulas from remote Git repositories to create an atomic 'build' for deployment.

SaltStack has a native [package manager](https://docs.saltstack.com/en/latest/topics/spm/) which is a system package manager (SPM). It assembles formulas from remote locations but is geared towards assembling on the Salt master itself and requires extra metadata.

Salt is also capable of loading formulas from Git using a [fileserver_backend](https://docs.saltstack.com/en/latest/ref/configuration/master.html#std:conf_master-fileserver_backend) however this too is geared towards assembly on the host itself.

The goal of this project is to make it easy to assemble formulas from Git repositories during a build stage running on something like Jenkins. After assembly, all files can be delivered to Salt master(s) in an atomic way. This makes it easier to keep multiple masters sync'd and Docker based Salt master deployments easier.

## Installation

```bash
sudo pip install saltstack-vulcan -U
```

## Configuration

Configuration is handled by a local YAML file. By default, $PWD/vulcan.yaml is used. An alternative path can be set with the --config flag.

Formula configuration is stored as a list of dictionaries. Each formula has the following attributes. Only 'name' and 'url' are required however it is best practice to set the branch and revision as well.


- **name**: A name for the formula for example 'apache' or 'mysql'. This is required.
- **url**: Git URL for the project. This is required.
- **branch**: Name of branch for checkout. Defaults to 'master'.
- **revision**: Git revision to use. If this does not exists, an exception will be thrown. Defaults to 'HEAD'.
- origin_name**: If renaming a formula, the origin_name of the formula must be used to determine the change. Defaults to value of 'name' if not set.
- **install_directory**: Directory to install formula into. Defaults to ./formulas.

### Example vulcan.yaml

```yaml
formulas:
  - name: bind
    url: https://github.com/saltstack-formulas/bind-formula
    branch: master
    revision: 29662c0f0452a48e1004038b6a3190b46fc4ed0b

  - name: docker
    url: https://github.com/saltstack-formulas/docker-formula
    branch: master
    revision: 0bff590b7bdd9568140c9693ca6e8b6fb4731408

  - name: vpn
    origin_name: openvpn
    url: https://github.com/saltstack-formulas/openvpn-formula
    branch: master
    revision: b51cd17524cac79274c883bc381f0ba07edff3c7
    install_directory: formulas

  - name: jenkins
    url: https://github.com/saltstack-formulas/jenkins-formula
    branch: jenkins_plugins
    revision: 407118135d59aa6577085b0570034341fe5f038a
```

## Usage

```bash
Usage: vulcan [OPTIONS] COMMAND [ARGS]...

  Formula build tool for SaltStack.

  See https://github.com/iamseth/saltstack-vulcan for documentation.

Options:
  --debug        Enables debug mode.
  --config PATH  Configuration file path. Defaults to ./vulcan.yaml.
  --version      Show the version and exit.
  --help         Show this message and exit.

Commands:
  install  Install all non-installed formulas.
  update   Update or install formulas.
```
