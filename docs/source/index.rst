Welcome to Multi-Process Export's documentation!
=======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Getting started
===============

Follow the directions for installing the standard interface template. Copy the files from this
repository, and place them in the standard interface template's repository area on your local
file system. The python files under multi_process_export follow the same structure as the ones
in the standard interface template.

Purpose
=======

The purpose of this repository is to demonstrate how to use multiple processes to
export files. XMS uses multiple threads to communicate with these processes, and safely
give appropriate responses.

The advantages to this approach include:

- Performance can be improved when there are many files, or one of the files takes a long time to write.
- While developing the model interface, a crash in one of the scripts will not cause the entire export operation to fail.

The drawbacks to this approach include:

- It is harder to give feedback to the user on progress.
- There is additional overhead in launching multiple scripts.

As a general rule, this approach to writing files for a simulation is discouraged. However, it
it is appropriate to use this approach when the performance benefits of using multiple processes
outweighs the need to give the user feedback.
