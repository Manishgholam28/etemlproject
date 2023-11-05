#it is automatically find the packages in the entire machine learning directory we are actually created
from setuptools import find_packages, setup
from typing import List

#This function returns a list 
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        
    
setup(
name= 'mlproject',
version= '0.0.1',
author='Manish',   
author_email="gholammanish28@gmail.com",
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)