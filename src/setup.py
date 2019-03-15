from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('VERSION', 'r') as fh:
    version = fh.read()

setup(name='async-graphql',
      version=version,
      description='Async GraphQL client',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/remorses/async-graphql',
      author='Tommaso De Rossi',
      author_email='beats.by.morse@gmail.com',
      license='MIT',
      packages=['async_graphql'],
      install_requires=[
          'six',
          'asyncio'
      ],
      zip_safe=False)
