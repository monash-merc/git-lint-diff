from distutils.core import setup

setup(name='flake8-diff',
      version='1.0',
      description='Run flake8 against only changed lines.',
      author='Simon Yu',
      author_email='xm.yuau@gmail.com',
      install_requires=['flake8'],
      scripts=['git-lint-diff'])
