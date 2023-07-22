from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]


setup(
    name='StopWord',
    version = '0.0.2',
    description = 'Swahili Stop-words ',
    url = '',
  
    classifiers=classifiers,
    keywords='Swahili Stop-words,NLP',
    packages=find_packages(),
    install_requires = []
)
