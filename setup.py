from setuptools import setup, find_packages

setup(
  name="fsapi",
  version="0.2.3",
  description="Frontier Silicon (former Frontier Smart) API",
  url="https://github.com/MatrixEditor/frontier-smart-api",
  author="MatrixEditor",
  author_email="not@supported.com",
  license="MIT License",

  packages=find_packages(
    where='.',
    include=['fsapi*']
  ),

  requires=['urllib3', 'xml'],

  classifiers= [
    'Development Status :: 2 - Implementing',
    'Intended Audience :: Science/Research',
    'License :: MIT License',  
    'Operating System :: Windows :: Linux',        
    'Programming Language :: Python :: 3.8.5'
  ]
)

