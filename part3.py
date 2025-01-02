from midiutil import MIDIFile

# Create a new MIDI file with one track
midi = MIDIFile(1)

# Track and tempo settings
track = 0
channel = 9  # Percussion channel in MIDI
tempo = 120  # Tempo in beats per minute
midi.addTrackName(track, 0, "Snare Drum")
midi.addTempo(track, 0, tempo)

# Dynamics: Velocity levels
mezzo_forte = 96  # mf
mezzo_piano = 64  # mp
accented = 110    # Slightly louder than normal

# Note durations (in beats)
sixteenth = 0.25  # Sixteenth note duration
eighth = 0.5      # Eighth note duration

# Time to keep track of where to place notes
time = 0

# Measure 1: Sixteenth notes with flams and accents (mf)
# Start with a sixteenth rest
time += sixteenth

# Add flams
midi.addNote(track, channel, 38, time, sixteenth / 2, mezzo_forte)  # Grace note (flam)
midi.addNote(track, channel, 38, time + sixteenth / 2, sixteenth, mezzo_forte)  # Main hit
time += sixteenth

# Add sixteenth notes
for _ in range(4):  # Group of five notes
    midi.addNote(track, channel, 38, time, sixteenth, mezzo_forte)
    time += sixteenth

# Add another flam
midi.addNote(track, channel, 38, time, sixteenth / 2, mezzo_forte)  # Grace note
midi.addNote(track, channel, 38, time + sixteenth / 2, sixteenth, mezzo_forte)  # Main hit
time += sixteenth

# Measure 2: Repeated sixteenth notes with accents (mp)
# Add repeated notes with accents
for i in range(8):  # 8 sixteenth notes
    velocity = accented if (i == 4 or i == 7) else mezzo_piano  # Accents on specific beats
    midi.addNote(track, channel, 38, time, sixteenth, velocity)
    time += sixteenth

# Save the MIDI file
output_path = "snare_drum_tempo_120.mid"
with open(output_path, "wb") as output_file:
    midi.writeFile(output_file)

print(f"Snare drum MIDI file saved to {output_path}")