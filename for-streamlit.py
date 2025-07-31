import streamlit as st
import numpy as np
from pydub import AudioSegment
import io

# Función para generar la pista MIDI a partir de una frase
def generar_pista_midi(frase):
    eventos_midi = []
    for letra in frase:
        if letra.isalpha():  # Solo procesar letras del alfabeto
            midi_pitch = (ord(letra.lower()) - ord('a')) % 12 + 60  # Mapeo a notas MIDI
            eventos_midi.append((midi_pitch, 0, 500))  # Duración fija para cada nota
    return eventos_midi

# Función para calcular la frecuencia a partir de una letra
def letra_a_frecuencia(letra):
    # Mapa de frecuencias para las notas de la escala pentatónica
    escala_pentatonica = {'a': 440, 'b': 494, 'c': 523, 'd': 587, 'e': 659, 'f': 698, 'g': 784}
    return escala_pentatonica.get(letra.lower(), 0)  # Devolver la frecuencia o 0 si no está en la escala

# Función para generar un tono sinusoidal
def generar_tono_sinusoidal(frecuencia, duracion, fs):
    t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)
    return np.sin(2 * np.pi * frecuencia * t)

# Función para generar la canción pentatónica
def generar_cancion_pentatonica(frase, velocidad=2):
    eventos_midi = generar_pista_midi(frase)

    # Crear un AudioSegment vacío
    cancion = AudioSegment.silent()

    # Frecuencia de muestreo
    fs = 44100

    # Reducción de la duración de cada tono
    velocidad /= 2

    # Generar el sonido para cada evento de nota MIDI
    for midi_pitch, _, duracion in eventos_midi:
        # Calcular la frecuencia correspondiente al tono MIDI utilizando la escala pentatónica
        frecuencia = letra_a_frecuencia(chr(midi_pitch))

        # Reducir la duración del tono
        duracion *= velocidad

        # Generar un tono de audio para la nota MIDI
        tono = generar_tono_sinusoidal(frecuencia, duracion / 1000, fs)

        # Convertir el tono a un segmento de audio
        tono_audio = np.int16(tono * 32767)
        segmento_audio = AudioSegment(tono_audio.tobytes(), frame_rate=fs, sample_width=2, channels=1)

        # Agregar el tono al AudioSegment de la canción
        cancion += segmento_audio

    # Exportar la canción a un archivo de audio
    with st.spinner("Generando el sigilo acústico..."):
        archivo_audio = "pentatonic_sigil.wav"
        cancion.export(archivo_audio, format="wav")

    # Visualizar el audio
    st.audio(archivo_audio, format="audio/wav")

    # Botón de descarga
    with io.open(archivo_audio, "rb") as file:
        audio_bytes = file.read()
    st.download_button(
        label="Descargar sigilo acústico",
        data=audio_bytes,
        file_name="Sigilo_acustico.wav",
        mime="audio/wav"
    )

    st.success(f"Sigil acústico generado exitosamente como '{archivo_audio}'.")

# Interfaz de usuario con Streamlit
st.title("Generador de Sigilos Acusticos")
st.text("Creado por: Frater cha0smagick para el blog grimoriomagiadelcaos.blogspot.com ")
frase = st.text_input("Ingrese la frase para generar el sigil acústico:")
velocidad = st.slider("Velocidad de la canción", 0.1, 5.0, 2.0, 0.1)
if st.button("Generar Canción"):
    generar_cancion_pentatonica(frase, velocidad)
