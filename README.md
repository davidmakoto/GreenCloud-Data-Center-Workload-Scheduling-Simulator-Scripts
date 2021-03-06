# GreenCloud-Data-Center-Workload-Scheduling-Simulator-Scripts
Scripts used to aid in running different types of simulations of workload scheduling algorithms using GreenCloud simulator. Part of Summer research under Dr. Xunfei Jiang funded by the Louis Stokes Alliance for Minotiry Participation program.

# Usage
Two primary scripts are included, one that automates the running different configurations and creation of unique output directories, and the second that plots trace files. Below are more details as well as screenshots of directory configuration as well as the command to the run scripts.


### run_sims.py
Runs GreenCloud simulator via command line options with a number of different options specified in lists. Script also creates unique output directories for generated trace files labeled by the data center configuration (e.g. three-tier debug), scheduler chosen, and date/time. Currently, script only cycles through a few topologies and 6 workload scheduling algorithms. To run, place this script inside /home/greencloud/greencloud directory (same as "run" executable, shown in screenshot of ls command below). While running, it's necessary to hit enter after each simulation is complete in terminal window before the next configuration is run by the script.
![run sims](https://user-images.githubusercontent.com/20344260/136677369-cc5ea3fc-dbb4-40f2-8d72-a1e1d26eb24c.png)

### plot_trace.py
Simple script that plots a two column trace file onto the x-y axis using plotly.express library. Trace file directory must be hardcoded along with column titles (which are not clearly specified in output trace files). 
Update: plot_trace.py no longer necessary to extract comma seperated values from space seperated values. Can bypass plot_trace.py entirely and copy paste data into excel/sheets. For google sheets, paste entire .tr file into single cell, then select Data->Split text to columns. Keeping for reference to further automate plotting of data/
