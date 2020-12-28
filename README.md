<img alt="Icon" src="misc/app_icon.png?raw=true" align="left" hspace="1" vspace="1">

# cryptography-cli

[![License Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-0D47A1.svg?style=flat-square)](http://www.apache.org/licenses/LICENSE-2.0)
[![Python](https://img.shields.io/badge/python-%3E%3D3.5-brightgreen)](https://www.python.org/downloads/release/python-350/)
[![CI status](https://github.com/thiagoolsilva/cryptography-cli/workflows/CI/badge.svg)](https://github.com/thiagoolsilva/cryptography-cli/actions?queryworkflow%3ACI+event%3Apush+branch%3Amain)

</br>

## Description

The project aims to help users to create PEM keys using a specific cryptography algorithm.

Below is the overview of the available functions:

```
$ key-generator --help
Usage: key-generator [OPTIONS]

Options:
  --algorithm [rsa]               Algorithm type  [required]
  --key_size INTEGER              The output format keys. The default value is
                                  2048  [required]

  --format [open_ssl|decrypted_open_ssl]
                                  The output format to be used.  [required]
  --help                          Show this message and exit.

Enjoy the program!
```

## Architecture

The application uses the design pattern MVP with the concepts of [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). To do it I've used the package feature pattern and separated it as displayed below.

<img src="misc/cryptography-cli.png" width="600"/>


## Tech-stack

| Technology   	| Description   	|
|---	|---	|
| [cryptography](https://cryptography.io/en/latest/) 	| Perform cryptography operations   	|
| [click](https://click.palletsprojects.com/en/5.x/quickstart/) 	| Click is a Python package for creating beautiful command line interfaces   	|
| [pytest](https://docs.pytest.org/en/stable/) 	| The pytest framework makes it easy to write small tests   	|
| [pytest-cov](https://pypi.org/project/pytest-cov/) 	| This plugin produces coverage tests reports   	|
| [pytest-html](https://pypi.org/project/pytest-html/) 	| This plugin produces a html tests reports   	|
| [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) 	| It is a framework that helps developers to mock, stub and spy the code under test. |

## Characteristics

This project brings to table set of best practices, tools, and solutions:

* MVP + clean architecture
* 100% [python](https://www.python.org/)
* Package feature pattern
* Testing (coverage + unit testing)
* CI integration by github actions
* static code analyse - TBD

## Test coverage

### key-generator module

The module `key-generator` has 97% code coverage.

```
============================= test session starts ==============================
platform linux -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.12.0
plugins: metadata-1.11.0, cov-2.10.1, pylama-7.7.1, html-3.1.1
collected 15 items

tests/test_create_rsa_keys_use_case.py ...                               [ 20%]
tests/test_dependency_factory.py ....                                    [ 46%]
tests/test_key_generator_product.py .                                    [ 53%]
tests/test_main_presenter.py .                                           [ 60%]
tests/test_rsa_algorithm_impl.py .                                       [ 66%]
tests/test_rsa_creator.py .                                              [ 73%]
tests/test_rsa_repository.py ..                                          [ 86%]
tests/test_rsa_source.py ..                                              [100%]

----------- coverage: platform linux, python 3.9.1-final-0 -----------
Name                                                                            Stmts   Miss  Cover
---------------------------------------------------------------------------------------------------
source/algorithm/__init__.py                                                        0      0   100%
source/algorithm/asymmetric/__init__.py                                             0      0   100%
source/algorithm/asymmetric/asymmetric_algorithm_contract.py                        7      1    86%
source/algorithm/asymmetric/rsa_feature/__init__.py                                 1      0   100%
source/algorithm/asymmetric/rsa_feature/data/__init__.py                            2      0   100%
source/algorithm/asymmetric/rsa_feature/data/rsa_creator.py                         5      0   100%
source/algorithm/asymmetric/rsa_feature/data/rsa_key_generator_product.py           8      0   100%
source/algorithm/asymmetric/rsa_feature/data/rsa_repository.py                      9      0   100%
source/algorithm/asymmetric/rsa_feature/data/rsa_source.py                         20      0   100%
source/algorithm/asymmetric/rsa_feature/impl/__init__.py                            1      0   100%
source/algorithm/asymmetric/rsa_feature/impl/rsa_algorith_impl.py                  10      0   100%
source/algorithm/asymmetric/rsa_feature/rsa_data_source_contract.py                18      4    78%
source/algorithm/asymmetric/rsa_feature/user_case/__init__.py                       0      0   100%
source/algorithm/asymmetric/rsa_feature/user_case/create_rsa_keys_use_case.py      14      0   100%
source/algorithm/asymmetric/supported_asymmetric_algorithm.py                       4      0   100%
source/algorithm/cryptography_algorithm_creator.py                                  5      1    80%
source/algorithm/cryptography_product.py                                            5      1    80%
source/main/__init__.py                                                             2      0   100%
source/main/client_contract.py                                                     13      2    85%
source/main/factory_dependencies.py                                                18      0   100%
source/main/presenter/__init__.py                                                   1      0   100%
source/main/presenter/main_presenter.py                                            16      0   100%
source/shared/__init__.py                                                           0      0   100%
source/shared/keys_entity.py                                                        8      1    88%
tests/__init__.py                                                                   0      0   100%
tests/test_create_rsa_keys_use_case.py                                             32      0   100%
tests/test_dependency_factory.py                                                   21      0   100%
tests/test_key_generator_product.py                                                 5      0   100%
tests/test_main_presenter.py                                                       16      0   100%
tests/test_rsa_algorithm_impl.py                                                   16      0   100%
tests/test_rsa_creator.py                                                           6      0   100%
tests/test_rsa_repository.py                                                       16      0   100%
tests/test_rsa_source.py                                                           13      0   100%
---------------------------------------------------------------------------------------------------
TOTAL                                                                             292     10    97%

============================== 15 passed in 0.24s ==============================
```

# Pre-Installation Requirements:

To run and install the app you must have the following specifications:

```
click==7.1.2
cryptography~=3.3.1
```

# QuickStart

## Download and usage

First of all you need to download a stable releases of the standalone cryptography-cli binaries [here](https://github.com/thiagoolsilva/cryptography-cli/releases). After that you have two options to install:

### 1. Install the program using whl file:

To install it you must use the following command.

```
pip install key_generator_cli-X.X.X-py3-none-any.whl 
```

Check if no error happens in the terminal and move to the next section.

### 2. Install the program in developer mode:

To do it you must type the command `pip install --editable .` in folder that will install it on your env python dependencies in developer mode.

Ps: This approach will remove the key_generator_cli from the path after it is closed.

## Using the library

After install it you can type  `key-generator --help` to get all information about the program.

### Generating Open SSL rsa keys:

Type the command `key-generator --algorithm rsa --key_size 2048 --format open_ssl` to get the generated openSSL RSA keys.

```
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCxZ0k4Lc5t28Xo+TAHo6b5pXz/9GtQztSJQYdxH+deNWDrXej6
touK5t9eFLIyYvOsHeF2RovFPw7WV+jNs2nESWFnsp/MuouuRXH7j0dkZiUJkxGg
1uAyQGPslIy9Fs/wnvrCDdIcCVoXbCTW7Epi2JR/we6oD1nPcRJfx6nb6wIDAQAB
AoGBAI0yGLum8ZLMhdNsaYbbAO3Xggqxvaw+QjjQN/2Yl+yKbY5HW0QYgC3YnVVj
AYVK7ohB7A3YDiy6iJOeukLmFjn5edEZ+H3SxUk5WKYpe86I8dC5XSkVihcX8vq6
ItPbSBGOsjevTtBbLSpMrq6MCvSZe8viNxAf9fHU3Mly9vkxAkEA3TPJtzQort7a
u1Y7Qz07KadbFpKlr2+0wD3K0QSW5HCPsok4G6cjMaPSjHGn+EHMPLkDTlFcQ9Gi
+bwrJ4r/owJBAM1PpAAONeHLrWMuAYgtFeF+AJHbDj4GThwhgV5m95EC+Ut7F7Zj
LcJrRjbkuPHRUAbDiKwUcqzXtPmUPVpX1xkCQQDFWJ+9H/6vzMjuW8dxfJ5c0h9U
6y6AbzOeU0Kv6d1JHxdEnGF/YkTm05ZTkE7gEKvK/PDzHWkoZE53aaZCmCLrAkAP
cpWRV4BgW9XQ544/87x4ueVLFCNPMWRBI5g7RR4NcB7Xugw/sdiojy+6Q51SvH/7
8kxfPi6eqKA6QxgWqxNJAkBbHS3+h5U7thUh68N9EqRlduHzO/wYH1kdTSuHmfgZ
947+a+JYbuATCB26XDi5ibG7xVYbrkpNah9+SMH/b5AL
-----END RSA PRIVATE KEY-----

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCxZ0k4Lc5t28Xo+TAHo6b5pXz/9GtQztSJQYdxH+deNWDrXej6touK5t9eFLIyYvOsHeF2RovFPw7WV+jNs2nESWFnsp/MuouuRXH7j0dkZiUJkxGg1uAyQGPslIy9Fs/wnvrCDdIcCVoXbCTW7Epi2JR/we6oD1nPcRJfx6nb6w==
```


### Generating decrypted rsa keys:

Type the command `key-generator --algorithm rsa --key_size 1024 --format decrypted_open_ssl` to get the generated decrypted RSA keys

```
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC8itpxBNPqpxzQicLZt6C03UYBQ8MTSBF2XKt8s/7amJxQn+Pe
Fe+6oKxmVmkKrr0mcDQFzypymtb9KUsCXN2mtZFj4AmyqULY9j84HiqL/E0TPJ6e
dSJ8Ey3u/LPMUkgpLJfDutscYLQbranMzOGmeeZPgnDAGqsjaq5BK7UqJQIDAQAB
AoGARGFz0lO27D8Jw1SDd+USgyZRknnaEW8s7im0BHlfsDZzUwZ6ZXy9QomtnTwv
wrEXZw6Av66gLYqc+Jp2WvgFZyYoS4Hv9eknN/UghKRB/oIYrpXoG1FQtxoGIsj1
E+Jg25+yRRJ+3dbEXMcVBRRpvdqAVfpa1rq4pIxoe7e7t0ECQQDwTDd6ZhA4ZjMj
/6H3WX4UuFQ++tImoLpwXUfp84WV2TT7G8dN8vS0TjKERw+/3Tzpvlopn0Vj+Ica
7sb1lScRAkEAyNzbCRLtDnZ36ha59GIRjgYQaz32UTL3iJY0P+8hA3HqayveN5go
/cmNUXmc6FMbuSrfOl9d5aF7nLvjtxsZ1QJAM9w/HOtqFMH5x4skKX3m+BHQHMeF
E1Ec66M2IgesjOqTxJ36JZiJt2ApBuNPQtk8jDXIv7LgBvNcNTPTPK00AQJBAIM6
j7v46nm1episqmb4n2F7osR94eyg8MoC4DYZBCedCDtmmLMXrUhJoxNk8ddzXLx4
PwmC/vSksP7wXlDl2tUCQHzDAqDt/0GkXzYb2d/4ADnY4xIyPrK8g8bodpSk58Rf
Z1S8+GjKO1XuHFZL8kVGC/RldTHgPdR2dXHiG2BHgmc=
-----END RSA PRIVATE KEY-----

-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8itpxBNPqpxzQicLZt6C03UYB
Q8MTSBF2XKt8s/7amJxQn+PeFe+6oKxmVmkKrr0mcDQFzypymtb9KUsCXN2mtZFj
4AmyqULY9j84HiqL/E0TPJ6edSJ8Ey3u/LPMUkgpLJfDutscYLQbranMzOGmeeZP
gnDAGqsjaq5BK7UqJQIDAQAB
-----END PUBLIC KEY-----
```

# Features

This section is related to the features/bug fixes of project.

## Do you want to contribute?

I'd love if you contribute with the upcoming features or bug fixes. Go ahead and read the [CONTRIBUTING](CONTRIBUTING.md) file.

## Upcoming features

You can check it out for new features on [github](https://github.com/thiagoolsilva/cryptography-cli/issues?q=is%3Aopen+is%3Aissue+label%3Aupcoming).

# Author

<img src="misc/myAvatar.png" width="40"/>

Follow me

[![Follow me](https://img.shields.io/badge/Medium-thiagoolsilva-yellowgreen)](https://medium.com/@thiagolopessilva)
[![Linkedin](https://img.shields.io/badge/Linkedin-thiagoolsilva-blue)](https://www.linkedin.com/in/thiago-lopes-silva-2b943a25/)
[![Twitter](https://img.shields.io/twitter/follow/thiagoolsilva?style=social)](https://twitter.com/thiagoolsilva)   

## License
```
Copyright (c) 2020  Thiago Lopes da Silva

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
