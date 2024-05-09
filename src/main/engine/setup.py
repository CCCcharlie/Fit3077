from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'engine'
LONG_DESCRIPTION = 'Simple component-entity based game engine in pygame'

# Setting up
setup(
        name="engine", 
        version=VERSION,
        author="Xavier Younan",
        author_email="xyou0003@student.monash.edu",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pygame"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python'],
        classifiers= [
        ]
)