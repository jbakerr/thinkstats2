import setuptools

setuptools.setup(
        name='thinkstats2',
        version='0.1',
        packages=setuptools.find_packages(),
        install_requires=[
            'scipy',
            'pandas',
            'numpy',
            'thinkplot @ git+git://github.com/jbakerr/thinkplot'
            ]
        )
