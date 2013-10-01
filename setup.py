from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['gevent', 'Flask>=0.7.2', 'MarkupSafe', 'Flask-SQLAlchemy', 'MySQL-Python'],
     )
