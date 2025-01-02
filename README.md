If the beats sound too fast when the tempo is set to 120, you should verify that the note durations (e.g., sixteenth, eighth, quarter) match the intended rhythm and the time increments (time += duration) align correctly.

In the code:

# Note durations (in beats)
sixteenth = 0.25  # Sixteenth note = 1/4 of a beat
eighth = 0.5      # Eighth note = 1/2 of a beat
quarter = 1.0     # Quarter note = 1 beat

    The tempo = 120 means 120 beats per minute, or 2 beats per second.
    At this tempo:
        A quarter note lasts 0.5 seconds.
        An eighth note lasts 0.25 seconds.
        A sixteenth note lasts 0.125 seconds.

Key Areas to Check

    Note Durations: Ensure the note durations (sixteenth, eighth, etc.) match the intended rhythm. If you mistakenly set sixteenth notes to 0.125 instead of 0.25, the rhythm will double in speed.

    Time Increments: Verify that time += duration increments align correctly with the rhythm. For example:
        For sixteenth notes, time should increment by 0.25 beats.
        For quarter notes, time should increment by 1.0 beats.

    Tempo Setting: The tempo in MIDIFile.addTempo(track, time, tempo) determines the global beats per minute (BPM). Ensure it's correctly set to 120.