from setuptools import setup, find_packages

setup(name='clean_folder',
      version='0.0.1',
      description='sorting files due to types',
      url='http://github.com/storborg/usefull',
      author='w00her',
      author_email='rodon@protonmail.ch',
      license='MIT',
      packages=['clean_folder'],
      entry_points={
          'console_scripts': ['clean-folder=clean_folder.clean:main']
      },
      include_package_data=True,
      zip_safe=False)
