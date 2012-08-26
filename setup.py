from distutils.core import setup

setup(
    name='weibo',
    author='Liao Xuefeng',
    author_email='askxuefeng@gmail.com',
    version='1.04',
    url='https://github.com/michaelliao/sinaweibopy',
    package_dir={'': 'src'},
    py_modules=[
        'weibo',
        ],
    long_description=open('README').read(),
    install_requires=[
        'simplejson',
        ],
)
