# Copyright 2018 The AdaNet Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Setup for pip package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import find_packages
from setuptools import setup

# Can't import the module during setup.py.
# Use execfile to find __version__.
with open('adanet/version.py') as in_file:
  exec(in_file.read())

REQUIRED_PACKAGES = [
    'numpy >= 1.12.0',
    'six >= 1.10.0',
    'protobuf >= 3.6.0',
]

setup(
    name='adanet',  # Automatic: adanet, etc. Case insensitive.
    version=__version__.replace('-', ''),
    description=(
        'adanet is a lightweight and scalable TensorFlow AutoML framework for '
        'training and deploying adaptive neural networks using the AdaNet '
        'algorithm [Cortes et al. ICML 2017](https://arxiv.org/abs/1607.01097).'
    ),
    long_description='',
    url='https://github.com/tensorflow/adanet',
    author='Google LLC',
    author_email='opensource@google.com',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='Apache 2.0',
    keywords=('tensorflow machine learning automl module subgraph framework '
              'ensemble neural network adaptive metalearning'),
)
