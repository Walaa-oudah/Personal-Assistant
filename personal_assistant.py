import speech_recognition as sr
import mysql.connector
import openai
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Set your API key
openai.api_key = 'WRITE YOUR API KEY HERE'

def record_and_transcribe():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_sphinx(audio)
            print("You said:", text)
            return text
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return None

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the updated model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except openai.error.AuthenticationError:
        return "Authentication error: Please check your API key."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')  # Change language if needed
        tts.save("output.mp3")
        os.system("start output.mp3")  # For Windows
        # os.system("afplay output.mp3")  # For macOS
        # os.system("mpg321 output.mp3")  # For Linux
        print("Speech generated and played.")
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")

def save_text_to_file(text):
    if text:
        with open("output.txt", "a") as file:
            file.write(text + "\n")
        print("Text written to output.txt")

def insert_text_to_database(text):
    """Insert text into the database."""
    if text:
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # Replace with your MySQL password
                database='personal_assistant'  # Updated database name
            )
            cursor = conn.cursor()

            # Insert the text into the output_txt table
            cursor.execute('INSERT INTO output_txt (output) VALUES (%s)', (text,))
            conn.commit()
            print("Text inserted into the database")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()
                print("Database connection closed")

if __name__ == "__main__":
    print("Starting speech recognition. Press Ctrl+C to exit.")
    try:
        while True:
            transcribed_text = record_and_transcribe()
            if transcribed_text:
                save_text_to_file(transcribed_text)
                insert_text_to_database(transcribed_text)
                chatgpt_response = get_openai_response(transcribed_text)
                text_to_speech(chatgpt_response)
    except KeyboardInterrupt:
        print("\nExiting...")
