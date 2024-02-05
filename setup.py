"""
End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution
"""
from io import open
from setuptools import setup

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()

def readme():
    with open('README.md', encoding="utf-8-sig") as f:
        README = f.read()
    return README

setup(
    # name='myocr_small',
    name='myocr_small',
    # packages=['myocr_small'],
    packages=['myocr_small'],
    include_package_data=True,
    # version='1.7.1',
    version='0.1',
    install_requires=requirements,
    # entry_points={"console_scripts": ["myocr_small= myocr_small.cli:main"]},
    entry_points={"console_scripts": ["myocr_small= myocr_small.cli:main"]},
    license='Apache License 2.0',
    description='End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution',
    long_description=readme(),
    long_description_content_type="text/markdown",
    # author='Rakpong Kittinaradorn',
    author='someone',
    # author_email='r.kittinaradorn@gmail.com',
    author_email='kreative358@hotmail.com',
    # url='https://github.com/jaidedai/myocr_small',
    url='https://github.com/kreative358/myocr_small.git',
    # download_url='https://github.com/jaidedai/myocr_small.git',
    download_url='https://github.com/kreative358/myocr_small.git',
    keywords=['ocr optical character recognition deep learning neural network'],
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],

)
