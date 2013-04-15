import setuptools

setuptools.setup(
    name="fike",
    description="A Python class that provides you a fork and a pipe.",
    long_description=open("README.md").read(),
    version="0.1dev",
    packages=["fike"],
    url="https://github.com/nlw0/fike",
    maintainer="Nicolau Werneck",
    maintainer_email="nwerneck@gmail.com",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Topic :: System :: Distributed Computing',
        'License :: OSI Approved :: Apache Software License',
    ],
)
