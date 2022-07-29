from setuptools import setup, find_packages

setup(
  name="fsapi",
  version="0.1.3",
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
    'Development Status :: 1 - Planning',
    'Intended Audience :: Science/Research',
    'License :: MIT License',  
    'Operating System :: Windows :: Linux',        
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5'
  ]
)

