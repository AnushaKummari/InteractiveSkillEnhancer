import signal
import wave
import warnings

try:
    import pyaudio
    HAS_PYAUDIO = True
except Exception:
    pyaudio = None
    HAS_PYAUDIO = False
    warnings.warn("pyaudio not available. Audio recording will be disabled.", RuntimeWarning)

from PyQt5.QtCore import QThread


class AudioRecorder:
    """Audio recorder wrapper.

    If pyaudio is not installed, the recorder becomes a no-op that logs a warning.
    This allows the app to run on systems without audio dependencies.
    """

    def __init__(self):
        self.channels = 1
        self.sample_rate = 44100
        self.chunk = 1024
        self.audio_location = "Backend/MediaRecorder/audio.wav"

        if HAS_PYAUDIO:
            self.audio_format = pyaudio.paInt16
            self.audio = pyaudio.PyAudio()
        else:
            self.audio_format = None
            self.audio = None
            self.recording = False

    def start_recording(self):
        if not HAS_PYAUDIO:
            print("Warning: pyaudio not installed — audio recording disabled.")
            return

        self.recording = True
        self.frames = []

        self.stream = self.audio.open(format=self.audio_format,
                                      channels=self.channels,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

        print("recording")
        self.worker = RecordWorker(self.stream, self.frames, self.chunk)
        self.worker.start()
        signal.signal(signal.SIGINT, self.on_worker_finished)

    def stop_recording(self):
        if not HAS_PYAUDIO:
            print("pyaudio not available — nothing to stop.")
            return

        self.recording = False
        self.worker.stop()
        self.stream.stop_stream()
        self.stream.close()

        wf = wave.open(self.audio_location, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("recording stopped — file saved")

    def on_worker_finished(self, *args, **kwargs):
        if not HAS_PYAUDIO:
            return

        self.recording = False
        try:
            self.stream.stop_stream()
            self.stream.close()
        except Exception:
            pass

        wf = wave.open(self.audio_location, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()


class RecordWorker(QThread):
    def __init__(self, stream, frames, chunk):
        super().__init__()
        self.stream = stream
        self.frames = frames
        self.chunk = chunk
        self.is_running = True

    def run(self):
        while self.is_running:
            try:
                data = self.stream.read(self.chunk)
            except Exception:
                # stream read can fail if device is removed or closed
                break
            self.frames.append(data)

    def stop(self):
        self.is_running = False
