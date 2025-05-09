from setuptools import find_packages,setup
from typing import List
E = "-e ."
def get_requirements(file_path:str) -> List[str]:
  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","")for req in requirements]
    if E in requirements:
      requirements.remove(E)
  return requirements

setup(
  name = 'mlprojects',
  version = '0.0.1',
  author='kunj',
  packages=find_packages(),
  install_requires = get_requirements('requirements.txt')
)