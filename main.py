from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from plyer import audio
from kivy.utils import platform



KV = '''
MDScreen:
    MDRaisedButton:
        id: record_button
        text: "Iniciar Gravação"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.toggle_recording()
'''

class AudioRecorderApp(MDApp):
    is_android = False
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        is_android = True

    def build(self):
        if self.is_android:
            request_permissions([Permission.RECORD_AUDIO, Permission.WRITE_EXTERNAL_STORAGE])
        
        return Builder.load_string(KV)

    def toggle_recording(self):
        if not self.is_recording:
            # Iniciar gravação
            self.start_recording()
        else:
            # Parar gravação
            self.stop_recording()

    def start_recording(self):
        self.root.ids.record_button.text = "Parar Gravação"
        self.is_recording = True
        # Caminho onde o áudio será salvo
        self.audio_file = "/sdcard/gravacao.mp4"  # Certifique-se de que o caminho de escrita é válido no Android
        # Iniciar gravação usando plyer
        audio.start(filename=self.audio_file)

    def stop_recording(self):
        self.root.ids.record_button.text = "Iniciar Gravação"
        self.is_recording = False
        # Parar gravação
        audio.stop()
        print(f"Gravação salva em: {self.audio_file}")

if __name__ == "__main__":
    AudioRecorderApp().run()
