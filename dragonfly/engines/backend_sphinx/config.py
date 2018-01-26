"""
Default CMU Pocket Sphinx engine class configuration module
"""

from sphinxwrapper import DefaultConfig
from pyaudio import paInt16
import os

# Configuration for the Pocket Sphinx decoder.
DECODER_CONFIG = DefaultConfig()
# Silence the decoder output by default.
DECODER_CONFIG.set_string("-logfn", os.devnull)

# Keyword arguments given to the PyAudio.open method for opening a stream from a
# microphone. PyAudio streams are used by the engine to recognise speech from audio.
# You may wish to change the values to be optimal for the models you are using;
# Sphinx models require quite specific audio input to recognise speech correctly.
# The values below should work for the default US English models.
PYAUDIO_STREAM_KEYWORD_ARGS = {
    "input": True,              # stream is an input stream
    "format": paInt16,          # 16-bit rate
    "channels": 1,              # one channel (mono)
    "rate": 16000,              # 16kHz sample rate
    "frames_per_buffer": 2048,  # frames per buffer set to 2048
}

# User language for the engine to use.
LANGUAGE = "en"

# Timeout in seconds for speaking the next part of a rule involving dictation. Rules
# like this currently have to be pronounced with pauses between grammar and
# dictation parts. The timeout does not include the first part of such rules.
# If this value is 0, there will be no timeout.
NEXT_PART_TIMEOUT = 1

# Timeout in seconds for starting repetition of a rule involving dictation.
# This is for rules that wrap elements in a Repetition element, perhaps for command
# chaining, and only applies to rules that have been completely spoken one or more
# times.
# If timeout occurs before speech is started, then the rule is processed, otherwise
# a repetition of the rule starts. If there is currently one or more complete
# recognitions and a further repetition is not completed, then the words
# recognised so far will processed.
# If this value is 0, the engine will process repeating rules as soon as one
# complete recognition happens.
# If this value is -1, the engine will wait until there is an incomplete recognition
# to process the repetitions.
REPETITION_TIMEOUT = 0
