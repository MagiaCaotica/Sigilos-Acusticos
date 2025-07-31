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
    archivo_audio = "pentatonic_sigil.wav"
    cancion.export(archivo_audio, format="wav")

    print(f"Canción generada exitosamente como '{archivo_audio}'.")

# Frase de ejemplo
frase_ejemplo = "estalamondamijalamondapara"

# Generar la canción con escala pentatónica y mayor velocidad
generar_cancion_pentatonica(frase_ejemplo, velocidad=0.5)
