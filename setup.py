from setuptools import setup

setup(
    name='coastguard',
    version='0.1',
    packages=['coastguard', 'coastguard.lib'],
    url='https://github.com/wjimenez5271/coastguard',
    license='Apache 2.0',
    author='William Jimenez, Daniel Imfeld',
    author_email='wjimenez5271@gmail.com',
    description='Enforce good behavior in DigitalOcean',
    zip_safe=False,
    entry_points={
        'console_scripts': ['coastguard=coastguard.main:main']},
    install_requires = ['argparse', 'dateutil'],
)