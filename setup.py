try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()


setup(
    name='langua',
    version='1.0.4',
    description='Faster port of Language detection built by Shuyo in Python',
    long_description=readme,
    author='Krishna Sangeeth KS',
    author_email='kskrishnasangeeth@gmail.com',
    url='https://github.com/whiletruelearn/langua',
    keywords='language detection library',
    packages=['langua', 'langua.utils', 'langua.tests'],
    include_package_data=True,
    install_requires=['six','numpy'],
    license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)