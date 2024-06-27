from setuptools import setup

setup(
    name='libml_URLPhishing',
    version='4.1.2',
    long_description='Library to download and process data for the URL phishing project',
    description='Library to download and process data for the URL phishing project',
    author='Shantnav Agarwal',
    project_urls={
        'Documentation': 'https://remla24-team-15.github.io/libml/',
        'Source Code': 'https://github.com/REMLA24-TEAM-15/libml'
    },
    install_requires=[
        'tensorflow>=2.16.1',
        'numpy>=1.26.4',
        'scikit-learn>=1.5.0'
    ]
)
