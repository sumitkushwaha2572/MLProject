# what is need of setup.py
# Through setup.py we can treated our ML application as a package and which we can install it and deploy in pypi
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sumit',
author_email='sumitkushwaha2572@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)




# whenever this findpackage runs its see in how many folder there is init.py file and consider that folder as a paackage itself and build it we can than import it 