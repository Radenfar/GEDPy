from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'An intuitive GEDCOM parsing library'
LONG_DESCRIPTION = 'An efficient and intuitive GEDCOM parser. It is designed to be easy to use and understand, while still being powerful enough to handle any GEDCOM file.'

setup(
    name='GEDPy',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Adam Comer',
    license='MIT',
    keywords=['GEDCOM', 'GEDCOM parser', 'GEDCOM library', 'GEDCOM python', 'GEDCOM parser python', 'GEDCOM library python', 'Family Tree'],
    url='https://github.com/Radenfar/GEDPy',
    packages=find_packages(),
    python_requires='>=3.11',
    install_requires=[
        # Add any dependencies here
    ],
    entry_points = {
        'console_scripts': [
            'gedpy = GEDPy.__main__:main'
        ]
    },
)
