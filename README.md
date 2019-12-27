# Numerical Analysis

This repository contains the codes, documents and assignments for **MCSC 6020G - Numerical Analysis** offered in Fall 2019 at Ontario Tech University.

Assignments submitted to _Prof. Lennaert van Veen_

## Project - Reduced Basis Method for Toy Problems
The reduced basis models of the project use [RBniCS](http://mathlab.sissa.it/rbnics) library which implements several reduced order modelling techniques in finite element framework [FEniCS](https://fenicsproject.org/).
*	All files part of this submission are in the directory ```Project/```
	*	```thermal_block/``` contains all the required data and code for the heat conduction problem.
	* ```navier_stokes/``` contains all the required data and code for the fluid flow problem.
	*	```latex/``` contains all the raw files and figures for the report.
	*	The report is titled ```Project_Report.pdf```
	*	```presentation/``` contains all the raw files and figures for the presentation.
	*	The presentation is titled ```Project_Report.pdf```

* _Note:_ Upon running, the computational results for each problem get saved in new subdirectories created within ```thermal_block/``` and  ```navier_stokes/```. [ParaView](https://www.paraview.org/) was used to post-process the results from finite element and RB methods. The error and speedup plots were generated using ```Pyplot``` from the ```*.csv``` files generated during the error and speedup analyses.    

**Prequisites**
1. FEniCS (>= 2018.1.0, python 3), with PETSc, SLEPc, petsc4py and slepc4py for computations during the offline stage. Download and build instructions are available at [FEniCS Download](https://fenicsproject.org/download/).
2. numpy and scipy for computations suring the online stage.
3. To install RBniCS:
	* Clone from the public repository using ```git clone https://gitlab.com/RBniCS/RBniCS.git```
	* Install the package using ```python3 setup.py install```

**Instructions to run the project**
1. Clone this repository using ```git clone git@github.com:parikshitbajpai/numerical_analysis.git``` or if already cloned pull changes using ```git pull```
2. On terminal, navigate to the cloned directory - ```numerical_analysis/```
3. Select one of the options to execute
	*	To run the thermal block case, ```make run-thermal_block```
	*	To run the Navier Stokes backward facing step case, ```make run-navier_stokes```

## Assignment 4
*	All files part of this submission are in the directory ```Assignment_4/```

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
