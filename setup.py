from setuptools import setup,find_namespace_packages
import os

REQUIREMENT_FILE_NAME="requirements.txt"
Project_Name="modelLab"
Version="0.0.1"
AUTHOR="Abhishek Kaddipudi"
DESCRIPTION="A lib for automating model training process of choosing best model that works for you data"
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.11',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

pkg_path=os.path.join('./modelLab')
subpkg1_path=os.path.join(pkg_path,'Classification')
subpkg2_path=os.path.join(pkg_path,'Regression')
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(

    name=Project_Name,
    version=Version,
    author=AUTHOR,
    description=DESCRIPTION,
    license="MIT",
    packages=['modelLab','modelLab.Classification','modelLab.Regression'],
    package_dir = {
        'modelLab':pkg_path,
        'modelLab.Classification':subpkg1_path,
        'modelLab.Regression':subpkg2_path,
                   },
    install_requires=['scikit-learn',
                      'xgboost',
                      'catboost',
                      'lightgbm'
                      ],
    long_description=read("README.md"),
    author_email = "abhishekkaddipudi007@gmail.com",
    classifiers=CLASSIFIERS,

)
