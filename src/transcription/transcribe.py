import os
import datetime
from audio_preprocess import AudioPreprocessor
import whisper

class AudioTranscriber:
    """
    A class to handle audio preprocessing, transcription, and saving transcription
    """

    def __init__(
        self,
        model_name="base",
        output_folder="/Users/bera/Desktop/projects/LLM-Podcast-Transcription/data/transcriptions",
    ):
        """
        Initializes the AudioTranscriber with a Whisper model and output folder.
        """
        self.model_name = model_name
        self.output_folder = output_folder
        self.model = whisper.load_model(model_name)
        self.preprocessor = AudioPreprocessor(sample_rate=16000)
        self._ensure_output_folder_exists()

    def _ensure_output_folder_exists(self):
        """
        Creates the output folder if it does not exist.
        """
        os.makedirs(self.output_folder, exist_ok=True)

    def preprocess_audio(self, input_file):
        """
        Preprocesses the audio file by converting and resampling it.
        """
        print(f"Preprocessing audio file: {input_file}")
        processed_file = self.preprocessor.preprocess_audio(input_file)
        return processed_file

    def transcribe(self, audio_file):
        """
        Transcribes a preprocessed audio file.
        """
        print(f"Transcribing {audio_file} using Whisper ({self.model_name} model)...")
        result = self.model.transcribe(audio_file)
        transcription = result["text"]
        return transcription

    def save_transcription(self, transcription, input_file):
        """
        Saves the transcription to the output folder.
        """
        base_name = os.path.basename(input_file).split(".")[0]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_folder, f"{base_name}_{timestamp}.txt")
        with open(output_file, "w") as f:
            f.write(transcription)
        print(f"Saved transcription to {output_file}")
        return output_file

    def process_audio(self, input_file):
        """
        Full pipeline: preprocesses the audio, transcribes it, and saves the transcription.
        """
        preprocessed_file = self.preprocess_audio(input_file)

        transcription = self.transcribe(preprocessed_file)

        output_file = self.save_transcription(transcription, input_file)

        return output_file

input_file = "/Users/bera/Desktop/projects/LLM-Podcast-Transcription/data/audio/li_lu.mp3"
transcriber = AudioTranscriber(model_name="base")
result = transcriber.process_audio(input_file)