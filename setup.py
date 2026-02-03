from setuptools import setup, find_packages

setup(
    name="scrapemyst",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="E4crypt3d",
    author_email="gohramgkb@gmail.com",
    description="A lean wrapper for requests with stealth features.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/E4crypt3d/ScrapeMyst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/E4crypt3d/ScrapeMyst",
        "Tracker": "https://github.com/E4crypt3d/ScrapeMyst/issues",
    },
    python_requires=">=3.6",
)
