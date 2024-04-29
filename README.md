# Sprint 1

The /Sprint1 directory contains files related to the first sprint.

# Sprint 2

The /Sprint2 directory contains files related to the second sprint. 

In this directory there are 2 subdirectories with are the two packages related to the implementation of FieryDragons.
The Engine package defines an abstract set of classes and functions to aid in the development of any general game using pygame.
The FieryDragons package implements the game "Fiery Dragons" using the Engine and pygame. 

The main code for the Engine is located in /Sprint2/Engine/src/fit3077engine/ and contains submodules for:
 - Events system
 - GameObject system
 - Utilities
The main code for FieryDragons is located in /Sprint2/FieryDragons/src/fierydragons/ and contains submodules for:
 - Events extensions
 - Concrete GameObjects
 - Extra utilities

The two packages can be installed by ensuring you have Python 3.11+ installed as well as pip and running, while in /Sprint2
```bash
$ pip install -e Engine
$ pip install -e FieryDragons
```

The game can then be run with
```bash
$ python3 -m fierydragons
```
Or whatever the name for the Python executable is in your path.

Alternatively, you can run the provided executable file (in the submission) on Windows 10+ without any required dependencies or setup. All dependencies are bundled in the exe.
To build this executable (on Windows) navigate to the /Sprint2 directory and execute:
```bash
$ pip install pyinstaller
$ pyinstaller -F ./FieryDragons/src/fierydragons/__main__.py
```
Which should create a directory /Sprint2/dist with \_\_main\_\_.exe inside which can be run to play the game on Windows systems.

# Demo Content

In the /Demo directory is:
 - /MidSemesterDemo directory. Containing some test implementation of various ideas done during the midsemester break prior to the release of the assignment brief in order to get a grasp of pygame.
 - /Sprint2ECSAttempt directory. Containing the game implemented using an entity component system. This was the initial design before being abandoned in favour of the submitted design. More details in the report.
