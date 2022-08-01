from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='automationLibs_logger',
    version='0.0.4',
    author='Yas Barrientos',
    author_email='yasmin.barrientos@globe.com.ph',
    description='Automation Team Library of reusable codes - Logger Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/yasmin.barrientos/automationLibs_logger',
    license='MIT',
    packages=find_packages(),
    install_requires=['python-dotenv'],
    keywords=['python', 'automationLibs', 'logger', 'automationLibs_logger'],
    download_url='https://gitlab.com/yasmin.barrientos/automationLibs_logger/-/archive/main/automationLibs_logger'
                 '-main.zip',
    test_suite='tests',
    classifiers=[                                   # https://pypi.org/classifiers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

)
