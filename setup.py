from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='automationLibs',
    version='0.0.1',
    author='Yas Barrientos',
    author_email='yasmin.barrientos@globe.com.ph',
    description='Automation Team reusable codes - Logger Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/yasmin.barrientos/automationLibs_logger',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    test_suite='tests'
)
