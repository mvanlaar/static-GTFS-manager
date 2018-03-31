# static-GTFS-manager
A browser-based user interface for creating, editing, exporting of static GTFS (General Transit Feed Specification Reference) schedules management for a public transit authority.

**Note: Program is still in development. Use at own risk!**

This project is the result of a collaboration between WRI ([World Resources Institute](http://wri-india.org/)) and KMRL ([Kochi Metro Rail Limited](http://kochimetro.org)). 

Initially developed for use by KMRL, the source code has been open-sourced so it can grow and get better with community inputs and help for creating GTFS feeds for other transit agencies too.

The GTFS data pre-loaded in the program is of Kochi Metro, Kerala, India which on March 16, 2018 became India's first transit agency to release its schedules data in the global standard static GTFS format as free and open data. 

See the [KMRL open data portal](https://kochimetro.org/open-data/) and some news articles: [1](http://www.newindianexpress.com/cities/kochi/2018/mar/17/kochi-metro-adopts-open-data-system-to-improve-access-to-its-services-1788342.html), [2](http://indianexpress.com/article/india/kochi-metro-throws-open-transit-data-to-public-on-the-lines-of-london-new-york-5100381/), [3](http://www.thehindu.com/news/cities/Kochi/open-data-to-improve-commuter-experience/article23275844.ece), [4](http://www.thehindu.com/news/cities/Kochi/kmrl-moves-a-step-ahead-to-open-up-transit-data/article23247617.ece).

This program adheres to the static GTFS (General Transit Feed Specification Reference) open transit data specs as published by Google Transit here: <https://developers.google.com/transit/gtfs/reference/>  
It also implements a [GTFS extension for translations](https://developers.google.com/transit/gtfs/reference/gtfs-extensions#translations) of stops and routes names to facilitate multilingual use of the data.

Lead programmer up till April 2018: [Nikhil VJ](https://answerquest.github.io) from Pune, India.


## Run on your system
#### On Ubuntu / Linux OS
1. Open Terminal (linux command prompt) and clone this repo to your side:  
`git clone https://github.com/WRI-Cities/static-GTFS-manager.git`

2.  Navigate into the folder created.  
`cd static-GTFS-manager`

3. Install the libraries requirements:  
`sudo pip3 install -r requirements.txt`

4. Run web_wrapper.py in python3:  
`python3 web_wrapper.py`

5. The program should load in a new web browser tab. You can now operate the program from your web browser. In case it doesn't load up, see the terminal for the URL, it is most likely `http://localhost:5000/` or so.

6. See the terminal for instructions and reporting of various processes. There are some recurring warnings which you can ignore, like `WARNING:tornado.access:404 GET /favicon.ico (::1) 1.35ms`

7. The program will keep running while you operate on the browser. To terminate the program, come back to the Terminal and press `Ctrl+C` or close the window.

8. Note: there is a password input box at top right corner. For any operation involving editing, import or export of data, the password should be typed in as a basic precaution against data tampering. The password can be accessed by reading the `web_wrapper.py` file. This is just a rudimentary precaution against unintended edits for now; it is NOT a security feature. Otherwise for browsing through the app and seeing info (ie, read operations), no password is required.


#### On Windows OS
To do! But Anaconda package is a good place to start, and similar steps to be followed. *Coming soon: a binary .exe to make the program stand-alone.*

## GTFS feed Export
The end output of this program is a gtfs.zip file having your transit agency's static GTFS data. See the **Commit and Export GTFS** section on the main page for the same.

## GTFS feed Import
From the main page, you can import a different GTFS feed in a .zip file. Structure of a feed zip must be as per GTFS specs and standard practices:  
```
gtfs.zip
 ˪ stops.txt
 ˪ routes.txt
 ˪ trips.txt
 ˪ stop_times.txt
 ˪ ...
 ```
Please keep all your files with lowercase `.txt` extension, and keep them up at root level in the zip archive, not inside any folders.

Kindly validate your GTFS zip prior to importing.

In the import process, the program creates a backup ZIP of the current data and then imports your data into its database. You can see the backup listed later on under Past Commits section on the home page.



## Improvements, Feedback
Please see the [Issues](https://github.com/WRI-Cities/static-GTFS-manager/issues) section for seeing existing program improvement efforts, feedback, questions. Please make sure you search through all the issues ([click here](https://github.com/WRI-Cities/static-GTFS-manager/issues?utf8=%E2%9C%93&q=) for full list) before filing a new one : it might already be covered in another.

**Invitation**: This project invites active participation from professionals in the coding and GTFS fields to join in to take it forward. Please feel free to fork, write your fixes/enhancements and create a pull request.

## Program technical info
Recommended browser to use : Chrome or Chromium.

The core program is a Python3 script. It launches a simple web server via `Tornado` module, and waits for asynchronous GET and POST requests.

These requests are made by the front-end HTML files as they are loaded in the browser and user navigates the program (which is like a typical website). There is javascript running various functions on the browser side, and it makes GET or POST calls to the API.

## Gratitude for open source solutions
This project stands on the shoulders of several solutions that have been shared open source. Sharing mentions below.

#### Open source libraries used on Javascript side : 
- Leaflet.js for maps
- Tabulator.js for tables
- Bootstrap for general page design
- Jquery and Jquery UI for some UI components like autocomplete
- Papa.parse for CSV parsing

#### Open source libraries used on Python side : 
- Tornado for web server with asynchronous features
- TinyDB for portable JSON database
- several modules for various operations, like json, os, time, datetime, xmltodict, csv, pandas, collections, zipfile, webbrowser

#### Many snippets
In addition to this, there are several code snippets used throughout the program that were found from online forums like stackoverflow and on various tech blogs. The links to the sources of the snippets are mentioned in comments in the program. Here is a shoutout to all the contributors on these forums and blogs : ***Thank You!***

####Personal mentions
Big thanks to Srinivas from Hyderabad, India for connecting folks together and sharing guidance, and to Devdatta from Pune, India for a sharing a very simple [working example](https://github.com/devdattaT/sampleTornadoApp) to learn about Tornado web server serving asynchronous from.

## Things to watch out for

#### Note for larger datasets use
With larger GTFS datasets, the python program can take time to process things and send a callback. So please be patient on the browser end after clicking a button here or there. This is especially true for the Schedules page where some deep trawling through the database is involved. Also, presently the database json file can be of large size in lower 100s of MBs for large datasets that have 1000s of trips. So please keep sufficient disk space available. Suggestions are invited for database optimization, while keeping key requirements in consideration. See the issues section for a discussion on which database to use.

#### Feature limitations
- Schedules with frequencies not currently supported. WIP.
- Deleting stops, routes, trips is currently disabled as this will require deep database operations. WIP.  
(example: if a stop is to be deleted, it needs to be dropped from every trip having it, with the sequence and timings appropriately updated. And this needs to be done with adequate precautions, user needs to know exactly what all is going to change before proceeding.)
- New trips cannot be added to a route as yet. WIP.
- XML upload feature is WIP.