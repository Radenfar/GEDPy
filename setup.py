from setuptools import setup

setup(
    name='GEDPy',
    version='0.1.0',
    description='An intuitive GEDCOM parsing library',
    author='Adam Comer',
    license='MIT',
    url='https://github.com/Radenfar/GEDPy',
    packages=['GEDPy'],
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
