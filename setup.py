from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='crypto-tools',
      version='1.0',
      description='Cryptography tools',
      author='Adiel Matuf',
      author_email='matufadiel@gmail.com',
      install_requires=required,
      )
