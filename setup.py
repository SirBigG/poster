from setuptools import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='poster',
    description='',
    license='',
    author='Andrii Gots',
    author_email='gotsandriy@gmail.com',
    url='https://github.com/SirBigG/poster',
    install_requires=required,
    zip_safe=False,
    include_package_data=True,
)
