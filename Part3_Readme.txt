Code Features:

    Tempo:
        Set to 120 BPM using midi.addTempo(track, 0, 120).

    Flams:
        Represented as two quick notes (grace note and main note) with slight time separation.

    Accents:
        Louder hits are added for > marks using increased velocity (110).

    Dynamics:
        mf (mezzo forte) for the first measure.
        mp (mezzo piano) for the second measure.

    Sticking:
        Represented implicitly through alternating dynamics or accents.

How to Use:

    Save the code as a .py file.
    Install the midiutil library using pip install midiutil.
    Run the script on your machine.
    The generated MIDI file snare_drum_tempo_120.mid can be opened in any MIDI software (e.g., MuseScore, GarageBand) to listen to the drum pattern.