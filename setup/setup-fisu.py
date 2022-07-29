from setuptools import setup, find_packages

setup(
  name="fsisu",
  version="0.1.2",
  description="Frontier Silicon (former Frontier Smart) ISU tools",
  url="https://github.com/MatrixEditor/frontier-smart-api",
  author="MatrixEditor",
  author_email="not@supported.com",
  license="MIT License",

  packages=find_packages(
    where='.',
    include=['fsisu*']
  ),

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

