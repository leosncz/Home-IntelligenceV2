# Home-IntelligenceV2
**Software that gives any home a brain.**
## What is it ?
This software, when **easily** connected to a microphone and a webcam, is able to understand its world, perform orders in multiple languages with its speech recognition and order analysis engine.</br></br>
It is also capable of interacting with every residents in a customizable way.</br>
The final goal is to connect this system to a home API like Jeedom in order for the system to control it.

## For now ?
It is still in development. </br></br>
Actual state: </br>
![example](images_for_github/demo.png)
![example](images_for_github/demo2.png)

## Installation
You only need **python 3.7** and install dependencies in **installation** file.</br>
Then, download one of the speech recognition language model at https://alphacephei.com/vosk/models, and put its content in the **model** directory.</br>
The last step is to download and put in **darknet** folder the neural net file **yolov3.weights** at https://pjreddie.com/media/files/yolov3.weights.</br>
You can start **main.py**.</br>

Working:
- server
- cv
- speech recognition
</br>
WIP:
- order analysis engine
- interactions
- database system
