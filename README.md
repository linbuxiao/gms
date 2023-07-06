# ms

[![PyPI - Version](https://img.shields.io/pypi/v/ms.svg)](https://pypi.org/project/ms)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ms.svg)](https://pypi.org/project/ms)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)
- [Usage](#usage)

Although mongo is a structureless database, there are times when we need to get a full definition of the structure. For example when defining fields for a data warehouse.

## Installation

```console
pip install ms
```

In addition to the traditional installation method, I personally recommend [pipx](https://pypa.github.io/pipx/) installation. pipx will help you to avoid global environment pollution.

```console
pipx install ms
```

## License

`ms` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Usage

1. Init ms config file
```console
ms init --config_path ./.env
```
2. Fill config file

3. Get mongo schema
```console
ms run --config_path ./.env
```
4. If u need json format
```console
ms run --config_path ./.env --output_format json
```
