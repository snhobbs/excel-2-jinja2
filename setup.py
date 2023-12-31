#!/usr/bin/env python3
from setuptools import setup, find_packages

try:
    requirements = []
    with open("requirements.txt", 'r') as f:
        for line in f:
            requirements.append(line)
except FileNotFoundError:
    requirements = [
        "click",
        "pandas",
        "jinja2"
    ]


description = ""
try:
    with open("README.md", 'r') as f:
        description = f.read()
except FileNotFoundError:
    pass



setup(name='excel_2_jinja2',
      version='0.1.0',
      long_description=description,
      long_description_content_type="text/markdown",
      url='https://github.com/snhobbs/render-df.git',
      author='Simon Hobbs',
      author_email='simon.hobbs@electrooptical.net',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      install_requires=requirements,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
        "console_scripts": [
            "excel-2-jinja2=excel_2_jinja2:cli_main",
        ],
      },
      include_package_data=False,
      zip_safe=True)
