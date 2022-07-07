from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
    name='pypimc',
    version='1.0',
    description='Minecraft Information Library',
    url='',  
    author='Beete',
    author_email='beete@protonmail.com',
    license='MIT', 
    classifiers=classifiers,
    keywords='Minecraft', 
    packages=find_packages(),
    install_requires=['requests'] 
)
