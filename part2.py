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
mezzo_forte = 96  # mf
fortissimo = 127  # ff

# Note durations (in beats)
sixteenth = 0.25
eighth = 0.5
quarter = 1.0

# Time to keep track of where to place notes
time = 0

# Measure 1: Flams and sixteenth notes (mf)
# Flam (grace note + main note)
midi.addNote(track, channel, 38, time, sixteenth / 2, mezzo_forte)  # Grace note
midi.addNote(track, channel, 38, time + sixteenth / 2, sixteenth, mezzo_forte)  # Main note
time += sixteenth

# Regular sixteenth notes
for _ in range(3):
    midi.addNote(track, channel, 38, time, sixteenth, mezzo_forte)  # Snare hit
    time += sixteenth

# Measure 2: Continuous sixteenth notes (ff)
for _ in range(8):
    midi.addNote(track, channel, 38, time, sixteenth, fortissimo)  # Snare hit
    time += sixteenth

# Measure 3: Rolls (simulated with dense sixteenth notes) and rests
# Roll simulation (8 sixteenth notes for a roll)
for _ in range(8):
    midi.addNote(track, channel, 38, time, sixteenth, fortissimo)  # Snare hit
    time += sixteenth

# Quarter note rests
time += quarter * 2  # Two beats of silence

# Save the MIDI file
output_path = "snare_drum_pattern_rolls.mid"
with open(output_path, "wb") as output_file:
    midi.writeFile(output_file)

print(f"Snare drum pattern saved to {output_path}")