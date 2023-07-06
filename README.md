# gms

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)
- [Usage](#usage)

Although mongo is a structureless database, there are times when we need to get a full definition of the structure. For example when defining fields for a data warehouse.

## Installation

```console
pip install git+https://github.com/linbuxiao/gms.git
```

In addition to the traditional installation method, I personally recommend [pipx](https://pypa.github.io/pipx/) installation. pipx will help you to avoid global environment pollution.

```console
pipx install git+https://github.com/linbuxiao/gms.git
```

## License

`gms` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Usage

1. Init gms config file
```console
gms init --config_path ./.env
```
2. Fill config file

3. Get mongo schema
```console
gms run --config_path ./.env
```
4. If u need json format
```console
gms run --config_path ./.env --output_format json
```
