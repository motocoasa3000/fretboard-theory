# music_theory.py

# 1. The Chromatic Scale: All 12 notes. Using sharps for consistency.
CHROMATIC_NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# 2. Standard Guitar Tuning (6 strings, from low to high)
STANDARD_TUNING = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'] # Adding octave numbers for clarity, though for scales it's often irrelevant.

# 3. Scale Formulas: Defined by the sequence of intervals (in half-steps) from the root.
SCALE_FORMULAS = {
    "major": [2, 2, 1, 2, 2, 2, 1],           # Whole, Whole, Half, Whole, Whole, Whole, Half
    "natural_minor": [2, 1, 2, 2, 1, 2, 2],
    "major_pentatonic": [2, 2, 3, 2, 3],
    "minor_pentatonic": [3, 2, 2, 3, 2],
    "harmonic_minor": [2, 1, 2, 2, 1, 3, 1],  # Let's add a more complex one to show depth.
}

# 4. Chord Formulas: Defined by the intervals (in half-steps) that make up the chord.
CHORD_FORMULAS = {
    "maj": [0, 4, 7],       # Root, Major 3rd, Perfect 5th
    "min": [0, 3, 7],       # Root, Minor 3rd, Perfect 5th
    "dim": [0, 3, 6],       # Root, Minor 3rd, Diminished 5th
    "7": [0, 4, 7, 10],     # Dominant 7th: Root, Maj 3, Perf 5, Min 7
    "maj7": [0, 4, 7, 11],  # Major 7th: Root, Maj 3, Perf 5, Maj 7
    "min7": [0, 3, 7, 10],  # Minor 7th: Root, Min 3, Perf 5, Min 7
}

# music_theory.py (continued)

def get_note_index(note_name):
    """
    Finds the position of a note in the CHROMATIC_NOTES list, ignoring octave.
    Example: get_note_index('C#') -> 1, get_note_index('Eb') -> 3 (But we use D#)
    """
    base_note = note_name[0]  # Get just the letter part (C, D, E, etc.)
    if len(note_name) > 1 and note_name[1] == 'b':
        # Handle flats by converting them to sharps for simplicity in our model.
        # This is a music theory logic decision! C# and Db are enharmonic equivalents.
        flat_to_sharp = {'Cb': 'B', 'Db': 'C#', 'Eb': 'D#', 'Fb': 'E', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'}
        base_note = flat_to_sharp.get(note_name[:2], base_note) # Use the first two chars if it's a flat
    else:
        base_note = note_name # It's a natural or sharp

    try:
        return CHROMATIC_NOTES.index(base_note)
    except ValueError:
        raise ValueError(f"Note '{note_name}' is not a valid note name.")

def get_notes_in_scale(root_note, scale_type):
    """
    Generates the notes of a scale based on its formula.
    Example: get_notes_in_scale('C', 'major') -> ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    """
    if scale_type not in SCALE_FORMULAS:
        raise ValueError(f"Unknown scale type: {scale_type}")

    root_index = get_note_index(root_note)
    scale_intervals = SCALE_FORMULAS[scale_type]

    current_index = root_index
    scale_notes = [CHROMATIC_NOTES[root_index]] # Start with the root note

    for interval in scale_intervals:
        current_index = (current_index + interval) % len(CHROMATIC_NOTES)
        scale_notes.append(CHROMATIC_NOTES[current_index])

    return scale_notes

# Let's test our function immediately!
if __name__ == "__main__":
    # Quick test to see if our logic works
    print("C Major Scale:", get_notes_in_scale('C', 'major'))
    print("A Minor Pentatonic Scale:", get_notes_in_scale('A', 'minor_pentatonic'))
    print("Gb Major Scale:", get_notes_in_scale('Gb', 'major')) # Should handle flats
