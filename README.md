# nlp-proj3
Project 3: Conversational Interface

Group Members: Jiapeng Liu, Ka Wong, Tomi Inouye

GitHub repository: https://github.com/liujjpp/nlp-proj3

Rasa is used in this project, therefore, the module `uvloop` is needed. `uvloop` is only supported on Linux or Mac machines, so please install the project one of the so said machines to be able to install all dependencies.

## Directions for setup:

### Use virtualenv for handling dependencies

### Requirements
* Python 3
* Pip 3
* Mac or Linux machine

### Installation
#### Mac/Linux Instructions
```bash
$ pip3 install virtualenv
```

```bash
$ virtualenv -p python3 venv
```

```bash
$ source venv/bin/activate
```

```bash
$ pip install -r requirements.txt
```
### Running the project
To start chatting with the rasa bot, run `rasa shell`, otherwise to retrain the rasa bot using modified data from `/data/*`, run `rasa train`.