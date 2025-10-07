# music_theory.py
CHROMATIC_NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
STANDARD_TUNING = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']

SCALE_FORMULAS = {
    "major": [2, 2, 1, 2, 2, 2, 1],
    "natural_minor": [2, 1, 2, 2, 1, 2, 2],
    "major_pentatonic": [2, 2, 3, 2, 3],
    "minor_pentatonic": [3, 2, 2, 3, 2],
    "harmonic_minor": [2, 1, 2, 2, 1, 3, 1],
}

CHORD_FORMULAS = {
    "maj": [0, 4, 7],
    "min": [0, 3, 7],
    "dim": [0, 3, 6],
    "7": [0, 4, 7, 10],
    "maj7": [0, 4, 7, 11],
    "min7": [0, 3, 7, 10],
}


def get_note_index(note_name):
    """
    Finds the position of a note in the CHROMATIC_NOTES list, ignoring octave.
    Example: get_note_index('C#') -> 1, get_note_index('Eb') -> 3, get_note_index('E2') -> 4
    """
    # Remove octave number if present (e.g., 'E2' becomes 'E', 'A#4' becomes 'A#')
    base_note = note_name.rstrip('0123456789')

    if len(base_note) > 1 and base_note[1] == 'b':
        # Handle flats by converting them to sharps
        flat_to_sharp = {'Cb': 'B', 'Db': 'C#', 'Eb': 'D#', 'Fb': 'E', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'}
        base_note = flat_to_sharp.get(base_note, base_note)

    try:
        return CHROMATIC_NOTES.index(base_note)
    except ValueError:
        raise ValueError(f"Note '{note_name}' (base: '{base_note}') is not a valid note name.")

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
    scale_notes = [CHROMATIC_NOTES[root_index]]

    for interval in scale_intervals:
        current_index = (current_index + interval) % len(CHROMATIC_NOTES)
        scale_notes.append(CHROMATIC_NOTES[current_index])

    return scale_notes

def get_chord_notes(root_note, chord_type):
    """
    Generates the notes of a chord based on its formula.
    Example: get_chord_notes('C', 'maj') -> ['C', 'E', 'G']
    """
    if chord_type not in CHORD_FORMULAS:
        raise ValueError(f"Unknown chord type: {chord_type}")

    root_index = get_note_index(root_note)
    chord_intervals = CHORD_FORMULAS[chord_type]

    chord_notes = []
    for interval in chord_intervals:
        note_index = (root_index + interval) % len(CHROMATIC_NOTES)
        chord_notes.append(CHROMATIC_NOTES[note_index])

    return chord_notes

if __name__ == "__main__":
    # Test the functions
    print("C Major Scale:", get_notes_in_scale('C', 'major'))
    print("A Minor Pentatonic:", get_notes_in_scale('A', 'minor_pentatonic'))
    print("C Major Chord:", get_chord_notes('C', 'maj'))
    print("D Minor Chord:", get_chord_notes('D', 'min'))
