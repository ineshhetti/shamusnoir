from midiutil import MIDIFile

# Create a new MIDI file with one track
midi = MIDIFile(1)

# Track and tempo settings
track = 0
channel = 9  # Percussion channel in MIDI
tempo = 120  # Allegro tempo
midi.addTrackName(track, 0, "Snare Drum")
midi.addTempo(track, 0, tempo)

# Dynamics: Velocity levels
fortissimo = 127  # ff
piano = 64        # p
pianissimo = 32   # pp

# Note durations (in beats)
sixteenth = 0.25
eighth = 0.5
quarter = 1.0

# Time to keep track of where to place notes
time = 0

# Measure 1 (ff, accented hits)
for _ in range(4):  # Repeat accented sixteenth notes
    midi.addNote(track, channel, 38, time, sixteenth, fortissimo)  # Snare hit
    time += sixteenth

# Measure 2 (p, softer hits with accents)
for i in range(8):  # Eight sixteenth notes, some accented
    velocity = piano if i % 2 == 0 else fortissimo
    midi.addNote(track, channel, 38, time, sixteenth, velocity)  # Snare hit
    time += sixteenth

# Measure 3 (crescendo, pp to p)
for i in range(8):  # Eight sixteenth notes with increasing volume
    velocity = pianissimo + int(i * (piano - pianissimo) / 7)  # Gradual crescendo
    midi.addNote(track, channel, 38, time, sixteenth, velocity)  # Snare hit
    time += sixteenth

# Measure 4 (pp, final soft notes)
for _ in range(4):  # Four sixteenth notes, very soft
    midi.addNote(track, channel, 38, time, sixteenth, pianissimo)
    time += sixteenth

# Save the MIDI file
output_path = "snare_drum_allegro.mid"
with open(output_path, "wb") as output_file:
    midi.writeFile(output_file)

print(f"Snare drum pattern saved to {output_path}")