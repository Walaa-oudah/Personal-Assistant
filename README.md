# Personal-Assistant

This repository contains all the necessary Python code and supporting files to build a comprehensive personal assistant that integrates Speech-to-Text (STT), OpenAI's conversational model, and Text-to-Speech (TTS) functionalities.

## Note: This Project is related and connected to three different projects Speech-To-Text, Openai-Interact, and Text-To-Speech. This project combines all three together.


# About the Project

The Personal-Assistant Project is a comprehensive Python application designed to deliver a hands-free, voice-controlled experience. It captures your speech, interprets it using AI, and responds with synthesized speech, all while maintaining a log of interactions. This project leverages the strengths of Speech-to-Text, AI, and Text-to-Speech to provide a smooth and responsive user experience. Whether for personal productivity, entertainment, or learning, The Personal-Assistant offers a glimpse into the future of voice-driven computing, showcasing the integration of advanced technologies in a single, cohesive application.

The project is divided into four main functionalities:

1-	Recording and Transcribing Speech: Capturing user speech and converting it into text.

2-	Interacting with OpenAI: Sending the transcribed text to OpenAI and receiving a response.

3-	Converting Text to Speech: Converting the OpenAI-generated response into spoken words.

4-	Storing Data: Saving the transcribed text and AI responses both locally and in a MySQL database.


### Speech Recognition Purpose:

The speech recognition component captures spoken words from the user and converts them into text. This text is then processed by OpenAI to generate a response, making the assistant capable of understanding and acting upon voice commands.


### Structure:

#### 1. Python Script ('record_and_transcribe' function):

  - Audio Capture: Uses the 'speech_recognition' library to record audio from a microphone.

  - Noise Adjustment: Adjusts for ambient noise to improve transcription accuracy.

  - Transcription: Converts the recorded audio into text using the Sphinx recognition engine.


### OpenAI Interaction Purpose:

The OpenAI component processes the user's input text and generates a contextually relevant response. This allows the assistant to provide intelligent and personalized interactions based on the user's spoken queries.


### Structure:

#### 1. Response Generation ('get_openai_response' function):

  - API Communication: Sends the transcribed text to OpenAI's API and retrieves a response.

  - Error Handling: Manages authentication errors and other potential issues during API calls.


### Text-to-Speech Purpose:

The text-to-speech component converts the AI-generated text response into spoken words, making the assistant's responses audible. This enhances user interaction by providing a seamless conversational experience.


### Structure:

#### 1. Speech Synthesis ('text_to_speech' function):

  - Audio File Creation: Converts the response text into an MP3 file using the 'gTTS' library.

  - Optional Playback: Plays the generated audio file using system-specific commands.


### Text and Data Storage Purpose:

All interactions are logged both locally and in a MySQL database. This dual-storage approach ensures data persistence and provides a history of all user interactions, which can be referenced later.


### Structure:

#### 1. File Storage ('save_text_to_file' function):

  - Local Logging: Appends the transcribed text to a file named 'output.txt', maintaining a log of all interactions.

#### 2.	Database Storage ('insert_text_to_database' function):
  - MySQL Interaction: Connects to a MySQL database and inserts the transcribed text into a table named 'output_txt'.


## Expected Results:

#### •	Enhanced Productivity: 
The TPersonal-Assistant will enable users to perform tasks more efficiently through voice commands and AI-driven responses, reducing the need for manual input.

#### •	Natural Voice Interaction: 
The application will offer a seamless interaction experience where spoken words are quickly and accurately transcribed, leading to natural-sounding and contextually relevant responses.

#### •	Persistent Data Logging: 
All interactions will be logged and stored securely, both locally and in a MySQL database, ensuring that users can review and analyze past conversations at any time.

#### •	Integrated AI Experience: 
By combining STT, AI, and TTS, the assistant will deliver a more human-like interaction, making it a valuable tool for a wide range of everyday tasks and applications.

#### •	User-Friendly Interface: 
The application will be designed to be intuitive and easy to use, providing clear instructions and feedback throughout the interaction process.


## Instructions and Navigation

- Install a web server (Apache).

- Install a database (MySQL).

- Use a server-side scripting language (Python).

### [Download and Install XAMPP]: (https://www.apachefriends.org/download.html)

### [Download and Install Visual Studio Code]: (https://code.visualstudio.com/download)

### [Download and Install Arduino IDE]: (https://www.arduino.cc/en/software)

- Install Required Libraries: Install the 'speech_recognition', 'gtts', 'mysql-connector-python', and 'openai' libraries.


### Step 1: Create a MySQL Database:

•  Name the database 'personal_assistant'. 

• 	Define a table named 'output_txt' within this database to store the transcribed speech and AI responses.

```
CREATE DATABASE personal_assistant;
USE personal_assistant;
CREATE TABLE output_txt (
    id INT AUTO_INCREMENT PRIMARY KEY,
    output TEXT NOT NULL
);

```


### Step 2: Python Script Execution:

• Run the main Python script to start the TPersonal-Assistant.

• The application will continuously listen for speech, transcribe it, and generate responses.

• The transcribed text and AI responses will be stored in both a local file ('output.txt') and the 'output_txt' table of the MySQL database.


### Step 3: API Key Setup:

• Set up your OpenAI API key in the script.


### Step 4: Test the Assistant:

• Run the code and Speak into the microphone and observe how the assistant processes your commands, responds, and logs the interactions.

 #### The Run code will respond and gives respond with audio feature will be as shown in the pictures below:

 <div> 
   
<img src="https://github.com/user-attachments/assets/182ddd7a-c7e1-4950-931b-e7eff5e719bb" width="400" height="200">

<img src="https://github.com/user-attachments/assets/42141f89-dfc0-40d2-9f00-7586ff981a83" width="400" height="200">

<img src="https://github.com/user-attachments/assets/5d5ccf31-31a7-4479-a165-a1a2fc782d28" width="600" height="400">

<img src="https://github.com/user-attachments/assets/91f0cfb6-9422-4bee-a06f-5ab3c20a1b76" width="300" height="200">

<img src="https://github.com/user-attachments/assets/91f62c37-982b-4c7e-a8f7-18f2aa90e789" width="800" height="200">

</div>


### Purpose of the project:

This project creates a personal assistant that can:

•Transcribe Speech: Convert spoken words into written text.

•Interact with AI: Use OpenAI's GPT-3.5-turbo model to generate responses to user input.

•Provide Vocal Feedback: Convert the AI's responses back to speech for vocal feedback.

•Store Conversations: Save the transcriptions in both a file and a MySQL database for record-keeping or further analysis.


# Summary:

The Personal-Assistant project demonstrates the powerful integration of Speech-to-Text, OpenAI's conversational capabilities, and Text-to-Speech in a Python application. It acts as a fully functional personal assistant that can understand, process, and respond to user commands while keeping a detailed log of all interactions.


### Technologies Used:

•	Python

•	SpeechRecognition Library

•	Google Text-to-Speech (gTTS) Library

•	OpenAI API

•	MySQL

•	XAMPP (for local server and MySQL database)


## Thank You!
