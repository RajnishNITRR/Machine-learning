from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will give list of requirement
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[  req.replace("/n"," ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='machine learning project',
    version='0.0.0.1',
    author='Rajnish',
    author_email='rajnish1800084@gmail.com',
    packages=find_packages(),
    install_requirement=get_requirement('requirements.txt')

)