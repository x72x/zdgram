from setuptools import setup, find_packages
import os
import re


with open("README.md", encoding="utf-8") as f:
    long_description = "\n" + f.read()

with open("shitgram/__init__.py", encoding="utf-8") as f:
    VERSION = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

DESCRIPTION = 'Coming soon'

# Setting up
setup(
    name="shitgram",
    version=VERSION,
    author="ZAID",
    author_email="y8838@hotmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['asyncio', 'aiohttp', 'aiofiles'],
    keywords=['bots', 'bot-api', 'telegram'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires="~=3.6",
)