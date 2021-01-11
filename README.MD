# python

## use cases

    * web servers
        - Django(framework for web apps)
        - Flask(another web “microframework.”)
        - Crawl websites using scrapy or Beautiful Soup
    * data science
        Python is popular within the data science community,
        resulting in a growing ecosystem of Python tooling for data analytics:
        - Anaconda is open-source software used for data processing, scientific computing, and predictive analytics
        - Jupyter Notebook(iPython) is another tool in the data science world

## features

    * universal, glue-lang for C packages
    * GIL(Global Interpreter Lock, singlethread)
    * crossplatform
    * multi-paradigm
    * expressive
    * inbuild standart lib
    * 1/3 of the size of equivalent C++ and Java code
    * 2-10 times slower of equivalent C++ and Java code
    * can be both dynamically and strongly typed
    * py(interpretor)=>pyc(bytecode on compilation)
    * /usr/local/bin/python
    * Integrated Development Environment (IDLE) - shell
    * pip3 `pip3 install package_name`
    * youtube, instagram

## interpreters

    * CPython(prime)
    * Cython(84 times faster and static typing)
    * Jython (no GIL, Java multythread, JVM)
    * IronPython
    * MicroPython
    * PyPy(3 times faster CPython)

## local/server programming environment(ubuntu)

    - setup python

    ```sh
    $sudo apt install -y python3-pip # package manager
    $sudo apt install build-essential libssl-dev libffi-dev python 3-dev # addons
    ```

    - virtual environment for projects
    isolated space on your machine for Python projects. Each of your projects
    can have its own set of deps that won’t disrupt any of your other projects.
    You can set up as many Python programming environments as you want - each is
    basically a dir or folder that has a few scripts to make it act as an environment.
    There are a few ways to achieve a programming environment in Python, here the venv
    module, which is part of the standard library.
    Python Wheels(built-package format for Python that can speed up your software
    production by reducing the number of compilations) will be in the Ubuntu share dir.

    ```sh
    $sudo apt install -y python3-venv
    $sudo mkdir environments && $cd environments
    $python3 -m venv my_env  # create env 'my_env' inside dir
    $source my_env/bin/activate # activate
    # Your prompt will now be prefixed with the name of your environment
    (my_env) sammy@localhost:~/environments$
    # To leave the environment, simply type the command
    $deactivate
    ```

    - dev libs

## 3._vs 2._

- print, exec to func
- raise Exception to func
- // vs / for floor division
- no tuples or lists as args in func
- String formatting syntax has changed
- new class declaration
