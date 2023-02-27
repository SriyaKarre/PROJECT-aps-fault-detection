from setuptools import find_packages,setup

from typing import list 

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()

setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="sriya165karre@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)

