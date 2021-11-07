# HSG-Alarm-Clock-2021

** update decription based on description in code **

Project Language: Python
Group ID: 95

## Table of contents
* [Introduction](#Introduction)
* [General-Content](#General-Content)
* [Repository](#Repository)
* [Installations](#Installations)
  
## Introduction
This is a mandatory group project  of the courses “HS21-7,789,1.00 Skills: Programming with Advanced Computer Languages” supervised by Dr. Mario Silic in the autumn semester 2021, at the University of St. Gallen. The project was done in a group of six people: Patrick Aoun, Rachel Dingemanse, Andras Krämer, Josef Krutel, Mariana Tomas Mendes and Yi Zheng.

## General-Content
The programme consists of a customized alarm clock integrated with the city bus schedule, which helps HSG students to never run late for university again, saving them from the struggles of missing the bus and having to walk up the hill. Most students who live in the city centre of St. Gallen need to either walk to university or take the bus number 5 or 9 from the train station. Due to convenience, bus number 9 is favoured by most of the students as it stops right next to uni. Therefore, our alarm clock works with the bus number 9 schedule. Moreover, for simplicity, we have designed the alarm for departure from the St. Gallen train station only, as most students take the bus from here to arrive to uni. 

The program offers students a special alarm setting system by providing the following features: First, the user is asked to tick a box if he/she wants to go to university. If the user does not tick the box then the time he/she sets is the time of the alarm. Here, the programme is used as a regular alarm clock. If the user needs to go to uni, they have to input the time they need to be at university. Furthermore, the user is asked how long they need to get ready by inputting the necessary hours/minutes. This includes breakfast, morning routines, time for the travel to the bus station, etc. The programme compares the arrival times of the bus number 9 at the university (departing from the train station) to the indicated preferred arrival time of the user at university and selects the bus, which has the closest timely arrival. According to the bus schedule, the bus needs six minutes to get from the train station to the university. The departure time of the student is calculated by deducting 6 minutes from the arrival time of Bus 9 at uni. From this departure time, the programme deducts the time it takes the user to get ready and be at the bus station. The output is the time of the alarm. The programme allows the user to customize the alarm ringing tone by inputting an URL (e.g. Youtube Link).

## Repository
There are five files distributed within this repository. "README.md" is used for a project description as well as instructions. "XX.ipynb" and "XX.py" contain code. 

## Installations 
To do our analysis we use these programs: 
* Python 3.9 (This program was developed for and tested with Python 3.9. The program may also work with previous Python versions, but this was not tested.)
* Anaconda 3
* Jupyter Notebook
* ADD the other program we used

To run our code you will need the following packages: 
* UPDATE numpy, pandas, matplotlib.pyplot, pylab, sklearn, statsmodels.api, tkinter 
