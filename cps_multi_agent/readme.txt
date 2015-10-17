-----------------------------------------------------------------
Title: CPS multi-agent simulator
Author: Prasanna Kannappan <prasanna at udel dot edu>
Date: Oct 17, 2015
-----------------------------------------------------------------
System requirements
-----------------------------------------------------------------

This package was developed using python 2.7 64-bit distribution.
The testing was done in ubuntu 12.04. The software should be
portable to other operating systems (e.g. mac, windows) if the
appropriate python distribution is available. However, this has
not been verified. Let me know if you have encounter any problems.

-----------------------------------------------------------------
Running Instructions
-----------------------------------------------------------------

There are two executable files in the gui folder. To run any
executable file in linux, open a terminal window and point
to the gui folder. You can use the the cd command to change
directory.

e.g. /home/cps_multi_agent/gui

Once you have changed the directory to the gui directory, then
you can run the executables. For example, o run the cpsGameViewer.py 
executable, use the command below.

./cpsGameViewer.py

If the file does not have executable permissions, then use

python cpsGameViewer.py

If your default version of python is not 2.7 then use

python2.7 cpsGameViewer.py

------------------------------------------------------------------
Executable Reference
------------------------------------------------------------------

1) cpsGameGTS.py

This executable can be used to start a new multi-agent game. There
are several gui controls that can be used to set the parameters of
the game. This simulation can involve an execution time of a few
minutes to few hours based on the parameters of the game. Most of
the gui controls are meant to be straight-forward and easy to use.

2) cpsGameViewer.py

This executable lets you run a pre-recorded game (recording done using
cpsGameGTS.py). It lets you choose a game log file using gui controls 
and allows walking through the game moves sequentially. Some recorded
games can be found in the game_runs folder. There is also a video
game_recording.webm showing the recorded game as displayed by 
cpsGameViewer. The gui controls are self explanatory.

------------------------------------------------------------------
Troubleshooting
------------------------------------------------------------------

1) Missing Dependencies

All the libraries used here can be easily downloaded from python 
repositories. In case you have any missing imports. Try installing
them using pip.

e.g. sudo pip install missing_dependence

2) Changing permissions of a file to executable

Use command:

sudo chmod 755 file_name


