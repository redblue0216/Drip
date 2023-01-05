from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'drip',
        version = '0.1',
        author = 'shihua',
        author_email = "15021408795@163.com",
        python_requires = ">=3.9.12",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = 'Drip is a lightweight production level algorithm platform, covering the whole life cycle from algorithm experiment, algorithm pre run management, algorithm runtime management to algorithm post run management.',
        # install_requires = ['flask-appbuilder'],

        ### 包接入点，命令行索引
        entry_points = {
            'console_scripts': [
                'dripctl = drip.cli:drip'
            ]
        }      
)