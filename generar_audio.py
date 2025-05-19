from gtts import gTTS
from pydub import AudioSegment
import os

musica = AudioSegment.from_mp3("base.mp3").apply_gain(-5)

with open("frases.txt", "r", encoding="utf-8") as f:
    frases = f.readlines()

voz_total = AudioSegment.silent(duration=1000)
for frase in frases:
    frase = frase.strip()
    if frase:
        tts = gTTS(frase, lang='es')
        tts.save("temp.mp3")
        voz = AudioSegment.from_mp3("temp.mp3").apply_gain(-18)
        voz_total += voz + AudioSegment.silent(duration=1500)

veces = int(musica.duration_seconds // voz_total.duration_seconds) + 1
voz_loop = voz_total * veces
voz_final = voz_loop[:len(musica)]

mezcla = musica.overlay(voz_final)
mezcla.export("musica_subliminal.mp3", format="mp3")
print("✅ Listo: 'musica_subliminal.mp3' fue generado.")
