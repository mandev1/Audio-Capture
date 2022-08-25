# Audio-Capture
Source Code of Audio Capture for Smart Speaker

## Introduction
Audio capture is one of the techniques used to
get information from the victim by using the microphone. This technique
take advantage of the sound processing services built into the smart speaker to
record sound secretly.

Audio Capture works by activating the microphone feature on the device,
especially on smart speakers that have received this program and can
record secretly. This program is also used as a smart communication line
speaker to the perpetrators of the crime to send the results of the conversation that has been
recorded.

## How it Works
In this case, the skills created are a program to
record the user's conversation, and the recording is received by  Command and Control (CnC).
Skills are inserted into the smart speaker and waiting to be activated. After
skills are activated, the smart speaker can record the conversation of users who are around 
smart speakers. The recording results are sent via the internet network
and can be accepted by CnC.

![image](https://user-images.githubusercontent.com/101856662/186625480-f2517078-69fa-4823-a7d3-4dc0d77e3299.png)

## Source Code
The audio capture program uses the skills and client system and is programmed
using the python programming language. The skills program is in charge of
receive the sound heard by the smart speaker, to get information from
user. These skills are entered into the smart speaker and registered as
services available for smart speakers. The client program is used to receive the results of the audio capture
on smart speakers.

### Client side
The client program is entered and executed on CnC to
receive recording instructions from smart speaker via network.
How client work is explained in the image below.

![image](https://user-images.githubusercontent.com/101856662/186627108-782a59f9-d891-4dba-85c9-b7827143e1d0.png)

### Server Side
Skills quietly listens to all the talk going on around
smart speaker and the conversation data is stored and transmitted periodically
to CnC.
Every time there is a pause in the conversation, the previous recorded data is immediately accommodated
in a variable and sent to CnC via a set link included in skills. Each finished sending data from the previous conversation,
skills continues to do its job of recording the next conversation and
sent back to CnC. How skills work is explained in the image below.

![image](https://user-images.githubusercontent.com/101856662/186626036-68364cf2-368d-401a-a6d0-ba49e5c3bb59.png)

## Result
### City
![audio_capture(city)](https://user-images.githubusercontent.com/101856662/186627818-a8154a9b-7586-45a4-9887-0f943e5718c6.PNG)

### Region
![audio_capture(country)](https://user-images.githubusercontent.com/101856662/186627828-6e925903-4707-469c-b970-2a3e09e060af.PNG)

### Phone Number
![audio_capture(num_phonenum)](https://user-images.githubusercontent.com/101856662/186627831-657d095a-5b53-473e-b706-1e0551a7277e.PNG)

### Person Name
![audio_capture(person)](https://user-images.githubusercontent.com/101856662/186627836-7afbbb14-2774-4639-816a-9496471812f5.PNG)

### Pin Code
![audio_capture(pin)](https://user-images.githubusercontent.com/101856662/186627839-b937fd85-7806-403b-8834-370d0a9ddd95.PNG)


## Information 
All of Audio Capture files are located in Result Folder
