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
