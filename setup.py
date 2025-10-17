'''setup.py is a essential component of packages and distributing project
it is used by setup tools to define cinfig of project 
such as meta data,dependencies etc'''

from setuptools import setup,find_packages
from typing import List

def get_requirement():
    requiremet_lst:list[str]=[]
    """"this func will return list of requirements"""
    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()
            for line in lines:
                requiremet=line.strip()
                if requiremet and requiremet!="-e .":
                    #use to direct to setup.py and run it also it get ignored by setup during installing pachages 
                    requiremet_lst.append(requiremet)
    except FileNotFoundError:
        print("no requirement.txt file")

    return requiremet_lst
setup(
    name='network security',
    author="Deepanshu",
    version='0.0.0.1',
    packages=find_packages(),
    install_requires=get_requirement()
)
