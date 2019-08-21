# IR2 - AfD statement search
## Second attempt to develop a fully functioning search engine
This application relies on Elasticsearch and Python to function. To set up the project with all dependencies, follow these steps closely.
### To set up Elasticsearch
1. Go to [the Elasticsearch website](https://www.elastic.co/de/start)
2. For Ubuntu, choose the "Linux 64-bit" version at the "Get Elasticsearch" field and download it.
3. Extract the downloaded package and navigate into the extracted folder via the command line. If you see the `bin` folder in there, you're alright, if not, navigate deeper inside until you see the bin folder.
4. enter `bin/elasticsearch` on the command line. Leave the terminal open with elasticsearch running.

#### Set Up Python
Python should already be installed on Ubuntu, make sure to check on the command line with `python3 -V`. If it's not installed, do `sudo apt-get install python3`.
It is necessary to install some libraries for this project in python, therefore pip is needed: `sudo apt-get install python3-pip`.
Now to installing the necessary libraries:
* `pip install -U Flask`
* `pip install -U flask-paginate`
* `pip install Elasticsearch`.

### Set Up the Search

While elasticsearch is running in one terminal, execute in a different terminal window:
* `python3 restructuring.py`
* `app.py`. It is critical that they are executed one after the other.

Then, open `http://127.0.0.1:8000/` in your browser (or click [this](http://127.0.0.1:8000/) link). You can now enter your search terms!
End the program with `Ctrl+C`.

