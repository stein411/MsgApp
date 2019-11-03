# README
This is a messaging application created for the HackOH/IO Hackathon 2019.
The chat app uses node.js, c++, python, and mongoDB. This also uses [Microsoft's Azure](https://azure.microsoft.com/en-us/services/cognitive-services/) services for text-to-speech processing. To run the program, follow the steps below.

### Requirements
| Requirement |
| ------------ |
|`Linux (tested on Ubuntu 18.04)` |
|`node.js (apt-get install nodejs)` |
|`python 3+ (apt-get install python)` |
|`sudo` priviliges |

# Initializing Text-to-Speech
For the first time running the application, you must run [`compile.sh`](compile.sh) by running the following bash command:
```bash
./compile.sh
```
You will need sudo privileges for this to run. If you want to manually configure your OS follow the steps provided on this [website](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-text-to-speech-cpp-linux).

You can also run the text-to-speech processing alone by modifying [`lines_to_synth`](lines_to_synth) by replacing the top line with a line of text. The processor only reads the top line of the file. Then run the following bash command:
```bash
./run.sh
```
Make sure your computer's sound is at a high volume.

# How does Text-to-Speech work?
Text-to-Speech uses Microsoft's Azure Cognitive Speech neural network to convert a line of text to speech. The [c++ speech file](helloworld.cpp) takes an input from a [file](lines_to_synth) and converts it to speech. The original code was found at this [link](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-text-to-speech-cpp-linux). The messaging app can write to the `lines_to_synth` file and that app runs the `run.sh` shell script to run the `text_to_speech_program`.

Azure survices must be initialized as found at this 
https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-js-node

