from setuptools import setup

setup(name='ConverterBot',
      version='0.1',
      description='A Unit conversion bot in python ',
      url='https://github.com/Chase22/ConverterBot',
      author='Chase',
      author_email='Chase@mailbox.org',
      license='GNU-GPL3',
      packages=['bot'],
      install_requires=[
          'python-telegram-bot',
          'pint',
      ],
      zip_safe=False)