import os
import pyaudio
import numpy as np
import time

# Create a global pyaudio object and a stream object
pa = pyaudio.PyAudio()

# Define a callback function that processes the audio data
def callback(in_data, frame_count, time_info, status):
    # Convert the audio data to a NumPy array
    audio_data = np.fromstring(in_data, dtype=np.int16)

    # Calculate the average volume of the audio data
    average_volume = np.mean(audio_data)

    # Set the LEDs on or off depending on the average volume
    if average_volume > threshold:
        os.system("./setleds +scroll")
    else:
        os.system("./setleds -scroll")

    # Return the audio data and a flag to continue the stream
    return (in_data, pyaudio.paContinue)

# Open the stream in a non-blocking mode with the callback function
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, stream_callback=callback)

# Set a threshold value for the average volume
threshold = 200

if __name__ == "__main__":
    try:
        # Start the stream
        stream.start_stream()

        # Keep the program running until an exception occurs
        while stream.is_active():
            time.sleep(0.01)
    except Exception as e:
        print(e)
        # Stop and close the stream and terminate the pyaudio object
        stream.stop_stream()
        stream.close()
        pa.terminate()
