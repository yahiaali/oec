from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
]

with open('README.md') as f:
    long_description = f.read()

setup(
      name='oec',
      version='0.2.5',
      description='API Wrapper for The Observatory for Economic Complexity',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Yahia Ali',
      author_email='yahiaali@me.com',
      license='MIT',
      url='https://github.com/yahiaali/oec',
      classifiers=classifiers,
      install_requires=['requests'],
      python_requires='>=3',
      py_modules=['oec']
)
