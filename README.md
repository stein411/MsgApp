# README
This is a messaging application created for the HackOH/IO Hackathon 2019.
The chat app uses node.js, c++, python, and mongoDB. This also uses Microsoft's Azure services for text-to-speech processing. To run the program, follow the steps below.

### Requirements
*If you do not want to use the text-to-speech capability, you may use Windows as the OS
`Linux (tested on Ubuntu 18.04)`
`node.js (apt-get install nodejs)`
`python 3+ (apt-get install python)`
`sudo` priviliges

# Initializing Text-to-Speech
### Note this is optional

# How does Text-to-Speech work?
Text-to-Speech uses Microsoft's Azure Cognitive Speech neural network to convert a line of text to speech. The [file](helloworld.cpp) takes an input from a [file](lines_to_synth) and converts it to speech. The original code was found at this [link](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-text-to-speech-cpp-linux). The messaging app can write to the `lines_to_synth` file and that app runs the `run.sh` shell script to run the program.

Azure survices must be initialized as found at this 
https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-js-node

