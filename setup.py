from setuptools import setup, find_packages

setup(
    name='ebiodata',
    version='1.0.0',
    description='Test database',
    author='Jonathan Dickinson',
    author_email='jon.dickinson17@gmail.com',
    license='MIT',
    url='https://github.com/jonathjd/ebio-db',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'db': ['ebiodata.db'],
    },
    install_requires=[
        'numpy==1.26.4',
        'pandas==2.2.2',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'six==1.16.0',
        'SQLAlchemy==2.0.30',
        'typing_extensions==4.12.1',
        'tzdata==2024.1',
        'openpyxl==3.0'
    ],
    python_requires='>=3.8',
)
