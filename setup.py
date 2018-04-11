from setuptools import setup, find_packages

try:
    with open('README.rst') as file:
        long_description = file.read()
except Exception as error:
    print("Could not find README.rst for long description. Error: {}".format(
        error))
    print("Leaving long_description as None")
    long_description = None

setup(
    name='tomaty',
    author='elias julian marko garcia',
    author_email='elias.jm.garcia@gmail.com',
    description=(
        'tomaty is a pomodoro program featuring a GUI and tracking system'),
    url='https://github.com/ejmg/tomaty',
    version='1.0.33',
    packages=find_packages(),
    entry_points={
        "console_scripts": ['tomaty = tomaty.tomaty:run'],
    },
    install_requires=[
        'pygobject',
        'simpleaudio',
        'datetime',
        'pathlib',
    ],
    include_package_data=True,
    license='MIT',
    long_description=long_description)
