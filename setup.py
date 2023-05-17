from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python CICD package'
LONG_DESCRIPTION = 'Python CICD package'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="python-cicd", 
        version=VERSION,
        author="Swetha Bikkasani",
        author_email="sbikkasani@deloitte.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'cicd', 'ci-cd'],
        classifiers= [
            "Development Status :: Initial Phase",
            "Intended Audience :: Takeda APCDL Users",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: Ubuntu",
            "Operating System :: Microsoft :: Windows",
        ]
)
