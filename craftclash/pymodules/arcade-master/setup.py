#!/usr/bin/env python

BUILD = 51
VERSION = "0.9.9"
RELEASE = VERSION + "r" + str(BUILD)

from os import path
import sys
from setuptools import setup

if __name__ == "__main__":

    if "--format=msi" in sys.argv or "bdist_msi" in sys.argv:
        # hack the version name to a format msi doesn't have trouble with
        VERSION = VERSION.replace("-alpha", "a")
        VERSION = VERSION.replace("-beta", "b")
        VERSION = VERSION.replace("-rc", "r")

    fname = path.join(path.dirname(path.abspath(__file__)), "README.rst")
    with open(fname, "r") as f:
        long_desc = f.read()

    setup(
          name="arcade",
          version=RELEASE,
          description="Arcade Game Development Library",
          long_description=long_desc,
          author="Paul Vincent Craven",
          author_email="paul.craven@simpson.edu",
          license="MIT",
          url="http://arcade.academy",
          download_url="http://arcade.academy",
          install_requires=[
          'pyglet',
          'pillow',
          'numpy'
          ],
          packages=["arcade",
                    "arcade.key",
                    "arcade.color"
                    ],
          classifiers=[
              "Development Status :: 3 - Alpha",
              "Intended Audience :: Developers",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
              "Programming Language :: Python",
              "Programming Language :: Python :: 3.5",
              "Programming Language :: Python :: Implementation :: CPython",
              "Topic :: Software Development :: Libraries :: Python Modules",
              ],
          test_suite="tests",
          data_files=[("Lib/site-packages/arcade/Win32", ["Win32/avbin.dll"]),
                      ("Lib/site-packages/arcade/Win64", ["Win64/avbin.dll"]),
                      ('lib/site-packages/arcade/lib',   ['lib/libavbin.10.dylib'])]
         )
