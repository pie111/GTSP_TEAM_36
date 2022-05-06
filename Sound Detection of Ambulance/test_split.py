import os
from pydub import AudioSegment
from pydub.utils import make_chunks

audio = AudioSegment.from_file("test0.wav",format="wav")
chunk_length_ms = 3000  # pydub calculates in millisec
chunks = make_chunks(audio, chunk_length_ms)  # Make chunks of three sec

    # Export all of the individual chunks as wav files

for k, chunk in enumerate(chunks):
    chunk_name = "audio{}chunk{}.wav".format("test0.wav", k)
    print("exporting", chunk_name)

    chunk.export(chunk_name, format="wav")
