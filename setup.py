from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT =  '-e .'
def get_requirements(file_path:str)->List[str]:
  '''
  this function will return the list of requirements
  '''
  requirements=[]
  with open(file_path, 'r') as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    if HYPHEN_E_DOT in requirements:
      requirements.remove(HYPHEN_E_DOT)
      print("Final requirements:", requirements) 
      
    return requirements

setup(
name='wineproject',
version='0.0.1',
author='Ruby',
author_email='write2ruby@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)