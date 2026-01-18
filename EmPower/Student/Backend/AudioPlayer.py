import os
import threading
import time

# Try to import pygame and pyaudio. If not available, provide safe fallbacks so
# the app doesn't crash; the MusicPlayer will be a no-op implementation.
try:
    import pygame
except Exception:
    pygame = None

try:
    import pyaudio
except Exception:
    pyaudio = None


class MusicPlayer:
    """Simple wrapper for music playback. If pygame or pyaudio is missing,
    methods will be no-ops and will log a message instead of raising.
    """

    def __init__(self, music_file_path):
        self.music_file_path = music_file_path
        self.play_music_continuously = False
        self.music_thread = None

        if pygame is None or pyaudio is None:
            print("Audio modules missing (pygame/pyaudio). Music disabled.")
            self.available = False
            return

        self.available = True
        if self.check_audio_devices():
            try:
                pygame.mixer.init()
            except Exception:
                pass
        else:
            print("No audio device found; audio disabled.")

    def check_audio_devices(self):
        if pyaudio is None:
            return False

        try:
            p = pyaudio.PyAudio()
            info = p.get_host_api_info_by_index(0)
            num_devices = info.get('deviceCount')

            for i in range(num_devices):
                device_info = p.get_device_info_by_host_api_device_index(0, i)
                if device_info.get('maxOutputChannels') > 0:
                    return True
        except Exception:
            return False

        return False

    def play_music(self):
        if not self.available:
            return

        try:
            pygame.mixer.init()
            self.play_music_continuously = True
            pygame.mixer.music.load(self.music_file_path)

            while self.play_music_continuously:
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.5)
                time.sleep(2)
        except Exception as e:
            print("Music playback error:", e)

    def start_music(self):
        if not self.available:
            return
        self.music_thread = threading.Thread(target=self.play_music, daemon=True)
        self.music_thread.start()

    def stop_music(self):
        if not self.available:
            return
        self.play_music_continuously = False
        try:
            pygame.mixer.music.pause()
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()
        except Exception:
            pass
