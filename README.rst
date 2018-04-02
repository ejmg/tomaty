tomaty
===============
*"you say tomato, I say stop wasting my time with lame python portmanteaus"*

.. side by side images not allowed by github
.. .. image:: https://raw.githubusercontent.com/ejmg/tomaty/master/img/macOS.png
..   :width: 38 %
..   :align: center
.. image:: https://raw.githubusercontent.com/ejmg/tomaty/master/img/ubuntu-unity.png

tomaty is a pomodoro app featuring basic stats tracking and notifications with many more features on the way.

.. contents::

why
=====

the primary motivation for yet another pomodoro app was that none of the others I could find were:
  1. native
  2. not an electron app
  3. simple but feature robust (flexible for user preferences)

goals
=====

while tomaty's current release is limited in features, i'm already working hard on another major release. 

the following features should be available in the coming ``2.0.0`` release:
  1. To-Do list
  2. basic settings page for user configuration
  3. setting: continuous mode
  4. setting: pausing (rather than resetting)
  5. setting: dark theme
  6. ... *and more!*

If you would like to see how things are going, checkout the project page for `tomaty v2 <https://github.com/ejmg/tomaty/projects/2>`_.

contributing
============
... *please do!*

there are plenty of `open issues <https://github.com/ejmg/tomaty/issues>`_
i've created for enhancing tomaty. just let me know if you are working on one so i can prioritize my time elsewhere on the project.

installing
==========

dependencies
------------

this is a python3 project. please use python3.

tomaty is built with `Gtk <https://www.gtk.org/>`_ using python's pyGObject bindings, `gi <https://pygobject.readthedocs.io/en/latest/index.html>`_.

the docs there have `instructions for essentially all major operating systems <https://pygobject.readthedocs.io/en/latest/getting_started.html>`_
, please use them!

pypi
----
1. (preferably) create a virtual environment
2. using pip: ``pip install tomaty``

if you get errors about user privileges, particularly on linux or mac, try ``pip install --user tomaty``. avoid using ``sudo`` whenever possible in terms of install ``pip`` packages.

To update, simply ``pip install --upgrade tomaty``. Be sure to do this often, I am constantly adding enhancements and patching bugs 🐛.

locally
-------
1. install the version you want from github
2. enter the directory of your local clone
3. using pip: ``pip install -e .``

Assuming you are tracking master, a simple ``git pull origin master`` will do for updates.

problems
--------

if you have problems installing and or getting a development setup going, please let me know in the issues and i can try to help. for mac users, checkout gabby's `comments <https://github.com/ejmg/tomaty/issues/43>`_ to see if they help you.


forks
=====
some friend(s) of mine have already started porting this project to other languages. you should check them out!

- `boxcar-willie <https://github.com/bitemyapp/boxcar-willie>`_ - tomaty... but in rust-lang. by `@bitemyapp <https://github.com/bitemyapp>`_
