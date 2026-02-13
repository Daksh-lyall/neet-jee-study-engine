from setuptools import setup, find_packages

setup(
    name='neet-jee-study-engine',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            'neet-jee-study-engine=your_module:main',
        ],
    },
    author='Daksh Lyall',
    author_email='your_email@example.com',
    description='A study engine for NEET and JEE preparation',
    url='https://github.com/Daksh-lyall/neet-jee-study-engine',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)