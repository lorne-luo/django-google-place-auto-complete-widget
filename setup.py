import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()




setup(
    name='django-google-place-auto-complete-widget',
    version='0.1.0',
    packages=find_packages(),
    url='https://git.butterfly.com.au/django-packages/django-google-place-auto-complete-widget.git',
    download_url='https://git.butterfly.com.au/django-packages/django-google-place-auto-complete-widget.git',
    license='Apache 2.0',
    author='Min Dang',
    author_email='min.dang@butterfly.com.au',
    maintainer='Min',
    maintainer_email='min.dang@butterfly.com.au',
    include_package_data=True,
     zip_safe=False,
)
