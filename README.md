# IR2 - AfD statement search
## About
This application is, fully functioning, a search engine to search through all the statements made by the political party _AfD_ in the German parliament.
The installation steps are described for an entirely new Ubuntu 18.04 OS with no other prerequisites.
## Developing a fully functioning search engine
This application relies on Elasticsearch and Python to function. To set up the project with all dependencies, follow these steps closely.
### set up Elasticsearch
1. Go to [the Elasticsearch website](https://www.elastic.co/de/start)
2. For Ubuntu, choose the "Linux 64-bit" version at the "Get Elasticsearch" field and download it.
3. Extract the downloaded package and navigate into the extracted folder via the command line. If you see the `bin` folder in there, you're alright, if not, navigate deeper inside until you see the bin folder.
4. enter `bin/elasticsearch` on the command line. Leave the terminal open with elasticsearch running.

### set up Python
Python should already be installed on Ubuntu, make sure to check the version on the command line with `python3 -V`. If it's not installed, do `sudo apt-get install python3`.
It is necessary to install some libraries for this project in python, therefore pip is needed: `sudo apt-get install python3-pip`.
Now to installing the necessary libraries:
* `pip install -U Flask`
* `pip install -U flask-paginate`
* `pip install Elasticsearch`.

### set up the search interface

On the command line, navigate to the directory where you want to have the search folder. Then, enter:  
`git clone https://github.com/richaude/IR2.git`  
A folder named "IR2" should appear. Navigate inside this folder.  

Now execute the following, while elasticsearch is running in a different terminal window:  
* `python3 restructuring.py`
* `python3 app.py` 

It is critical that they are executed one after the other. You should now see something like:
~~~~
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 429-858-882
~~~~

Then, open `http://127.0.0.1:8000/` in your browser (or click [this](http://127.0.0.1:8000/) link). You can now enter your search terms!
End the program with `Ctrl+C`.

