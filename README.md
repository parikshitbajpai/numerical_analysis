# Numerical Analysis

This repository contains the codes, documents and assignments for **MCSC 6020G - Numerical Analysis** offered in Fall 2019 at Ontario Tech University.

Assignments submitted to _Prof. Lennaert van Veen_

## Assignment 3
*	All files part of this submission are in the directory ```Assignment_3/```
	*	```src/``` contains all the python scripts.
	*	```latex/``` contains all the raw files and figures for the report.
	*	The report is titled ```Assignment_3.pdf```

**Instructions to run Assignment 3**
1. Clone this repository using ```git clone git@github.com:parikshitbajpai/numerical_analysis.git``` or if already cloned pull changes using ```git pull```
2. On terminal, navigate to the cloned directory - ```numerical_analysis/```
3. Select one of the options to execute
	*	To run with randomnly selected initial estimate of roots ```make run-random```. Note that this method may or may not converge and might have to be run multiple times to get results.
	*	To run with initial estimate of roots equal to one ```make run-ones```. Note that this method may only converge for $\lambda$ close to 0.
	*	To clean up the python build files execute ```make clean```

## Assignment 2
*	All files part of this submission are in the directory ```Assignment_2/```
	*	```src/``` contains all the python scripts.
	*	```latex/``` contains all the raw files and figures for the report.
	*	The report is titled ```Assignment_2.pdf```
* Change directory to ```src/``` and run ```python run_newton.py``` to reproduce manufactured solution.

## Midterm Presentation
The midterm presentation can be found in ```Midterm_Presentation```. The source files for building presentation are in the directory ```Midterm_Presentation/latex```

## Assignment 1
*	All files part of this submission are in the directory ```Assignment_1/```
	*	```src/``` contains all the python scripts.
	*	```latex/``` contains all the raw files and figures for the report.
	*	The report is titled ```Assignment_1.pdf```

**Instructions to run Assignment 1**
1. Clone this repository using ```git clone git@github.com:parikshitbajpai/numerical_analysis.git```
2. On terminal, navigate to the cloned directory - ```numerical_analysis/```
3. Select one of the options to execute
	*	To run both _Cofactor expansion_ and _LUP factorisation_ methods execute ```make run-A1```
	*	To run only _Cofactor expansion_ execute ```make run-cofactor```
	*	To run only _LUP factorisation_ execute ```make run-lu```
	*	To clean up the python build files execute ```make clean```
