from setuptools import setup, find_packages

setup(
    name='passwordgenerator',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    author='Nicolas Livenson & Sanon Jean Duckens',
    author_email='nicolaslivenson@gmail.com',
    description='Un générateur de mots de passe simple',
    long_description='Un package Python pour générer des mots de passe aléatoires.',
    url='https://github.com/votreutilisateur/passwordgenerator',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='password generator security',
)