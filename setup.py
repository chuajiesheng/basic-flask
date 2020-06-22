from setuptools import find_packages, setup

setup(
    name='basic-flask',
    version='0.0.1',
    url='https://www.jschua.com',
    maintainer='Chua Jie Sheng',
    maintainer_email='hello@jschua.com',
    description='Basic Flask App',
    packages=find_packages(),
    zip_safe=False,
    python_requires='>=3.7',
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   ],
    install_requires=[
        'gunicorn',
        'wheel',
        'Flask',
    ],
)
