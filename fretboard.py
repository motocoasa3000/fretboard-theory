# fretboard.py
from music_theory import CHROMATIC_NOTES, STANDARD_TUNING, get_note_index

class Fretboard:
    def __init__(self, tuning=STANDARD_TUNING, num_frets=12):
        self.tuning = tuning
        self.num_frets = num_frets
        self.num_strings = len(tuning)
        self.notes = self._initialize_notes()

    def _initialize_notes(self):
        """
        Creates a 2D list (list of lists) representing the fretboard.
        fretboard[string][fret] = note_name
        """
        fretboard = []
        for string_index, open_note in enumerate(self.tuning):
            string_notes = []
            open_note_index = get_note_index(open_note)
            for fret in range(self.num_frets + 1):
                note_index = (open_note_index + fret) % len(CHROMATIC_NOTES)
                string_notes.append(CHROMATIC_NOTES[note_index])
            fretboard.append(string_notes)
        return fretboard

    def find_notes(self, target_notes):
        """
        Finds all positions on the fretboard where a note in the target_notes list appears.
        Returns a list of tuples: (string_index, fret, note_name)
        """
        found_positions = []
        for string_idx in range(self.num_strings):
            for fret in range(self.num_frets + 1):
                note = self.notes[string_idx][fret]
                if note in target_notes:
                    found_positions.append((string_idx, fret, note))
        return found_positions

    def visualize_fretboard(self, highlight_notes=None):
        """
        Creates a simple text-based visualization of the fretboard.
        If highlight_notes is provided, it will mark those notes.
        """
        if highlight_notes is None:
            highlight_notes = []

        print("Guitar Fretboard (0 is open string)")
        print("String | " + " ".join(f"Fret {fret:2}" for fret in range(self.num_frets + 1)))
        print("-" * (10 + self.num_frets * 6))

        string_names = ['Low E', 'A', 'D', 'G', 'B', 'High E']
        for string_idx, string_name in enumerate(string_names):
            display_string = f"{string_name:>6} | "
            for fret in range(self.num_frets + 1):
                note = self.notes[string_idx][fret]
                display_note = f"[{note}]" if note in highlight_notes else f" {note} "
                display_string += f"{display_note:>5}"
            print(display_string)

if __name__ == "__main__":
    guitar = Fretboard()
    c_major_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    print("Visualizing the entire fretboard:")
    guitar.visualize_fretboard()

    print("\nVisualizing the C Major scale on the fretboard:")
    guitar.visualize_fretboard(highlight_notes=c_major_scale)