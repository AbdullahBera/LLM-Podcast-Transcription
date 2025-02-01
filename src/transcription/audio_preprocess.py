import os
from pydub import AudioSegment


class AudioPreprocessor:
    """
    A class to handle audio file preprocessing, including format conversion and resampling.
    """

    def __init__(self, sample_rate=16000):
        """
        Initializes the AudioPreprocessor with a default sample rate.
        """
        self.sample_rate = sample_rate

    def convert_to_wav(self, input_file, output_file=None):
        """
        Converts a file to WAV format.
        """
        if not output_file.endswith(".wav"):
            output_file += ".wav"

        try:
            audio = AudioSegment.from_file(input_file)
            audio.export(output_file, format="wav")
            print(f"Converted {input_file} to {output_file}")
        except Exception as e:
            print(f"Failed to convert {input_file} to {output_file}: {e}")

    def resample_audio(self, input_file):
        """
        Resamples an audio file to the specified sample rate and saves it as a new file.
        """
        audio = AudioSegment.from_file(input_file)
        audio = audio.set_frame_rate(self.sample_rate)

        output_file = os.path.splitext(input_file)[0] + f"_{self.sample_rate}.wav"

        audio.export(output_file, format="wav")
        print(f"Resample {input_file} to {self.sample_rate} Hz")
        return output_file

    def preprocess_audio(self, input_file):
        """
        Converts and resamples an audio file, ensuring it is in WAV format.
        """
        if not input_file.endswith(".wav"):
            wav_file = input_file.replace(os.path.splitext(input_file)[1], ".wav")
            self.convert_to_wav(input_file, wav_file)
        else:
            wav_file = input_file

        resampled_file = self.resample_audio(wav_file)

        if wav_file != resampled_file:
            os.remove(wav_file)
            print(f"Deleted intermediate file {wav_file}")

        print(f"Preprocessed file {input_file} to {resampled_file}")

        return resampled_file
