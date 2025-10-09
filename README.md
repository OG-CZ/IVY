# I.V.Y.

### Intelligent Voice for You

## Installation

It's recommended to use a virtual environment to keep dependencies isolated

```bash
python -m venv venvivy
```

Then, if you have installed to activate:

```bash
# On windows:
venvivy\Scripts\activate
# On MacOS/Linux:
source venvivy/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Lastly, install vosk for offline speech model recognition

https://alphacephei.com/vosk/models == vosk-model-en-us-0.22

> If you are on VSCode you must select the python interpreter that you locally created
