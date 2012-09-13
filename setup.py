import os
#from setuptools import setup
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-feedback-pv',
    version='0.5',
    description='A pluggable user feedback app',
    author='POPVOX.com',
    author_email='feedback@popvox.com',
    license='GNU Affero General Public License',
    url='https://github.com/tauberer/django-feedback-pv',
    keywords = ['django', 'feedback', 'ajax', 'user', 'customer', 'comment'],
    #package_data = {'feedback':['media/*.js','media/*.css','media/images/*','CREDITS']},
    packages=[
        'feedback',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
