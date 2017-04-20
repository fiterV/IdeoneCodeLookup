================
IdeoneCodeLookup
================

Overview
========

A script, that let you find the code on `Ideone <https://ideone.com>`_ substring of which matches some `RegExp <https://en.wikipedia.org/wiki/Regular_expression>`_


Installation
============

For Debian based systems::

    ./install.sh


Usage
========

::

    ideoneSearcher -r REGEXP -c AMOUNT OF RECENT PAGES TO WANT TO LOOK THROUGH**

Examples
========

::

   ideoneSearcher -r bits -c 2

Finds links for all codes that have **bits** substring in them, from first **2** pages.



