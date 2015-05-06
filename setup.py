from setuptools import setup, find_packages


setup(
    name="Pong",
    author="Cal Paterson",
    author_email="cal@calpaterson.com",
    packages=find_packages(),
    scripts=[
        "run-pong"
    ],
    install_requires=[
        "pyglet==1.2.2"
    ]
)
