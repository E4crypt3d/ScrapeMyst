from setuptools import setup, find_packages

setup(
    name='scrapemyst',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='E4crypt3d',
    author_email='gohramgkb@gmail.com',
    description='A class for sending web requests with customizable headers and user-agents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/E4crypt3d/ScrapeMyst',
    download_url='https://github.com/E4crypt3d/ScrapeMyst/archive/refs/tags/0.3.tar.gz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
