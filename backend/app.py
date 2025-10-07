from flask import Flask, jsonify, request
from flask_cors import CORS
from music_theory import get_notes_in_scale, get_chord_notes, SCALE_FORMULAS, CHORD_FORMULAS
from fretboard import Fretboard

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def home():
#   return jsonify({"message": "Flask server is working! Use /api/scales or /api/scale?root=C&type=major"})

@app.route('/api/scales', methods=['GET'])
def get_available_scales():
    """Returns all available scale types"""
    return jsonify(list(SCALE_FORMULAS.keys()))


@app.route('/api/chords', methods=['GET'])
def get_available_chords():
    """Returns all available chord types"""
    return jsonify(list(CHORD_FORMULAS.keys()))


@app.route('/api/scale', methods=['GET'])
def get_scale():
    """Returns scale notes and fretboard positions"""
    root_note = request.args.get('root', 'C')
    scale_type = request.args.get('type', 'major')

    try:
        print(f"Processing request: root={root_note}, type={scale_type}")  # ADD THIS
        scale_notes = get_notes_in_scale(root_note, scale_type)
        guitar = Fretboard()
        positions = guitar.find_notes(scale_notes)

        return jsonify({
            'scale_notes': scale_notes,
            'fretboard_positions': positions,
            'root_note': root_note,
            'scale_type': scale_type
        })
    except ValueError as e:
        print(f"ERROR: {str(e)}")  # ADD THIS
        return jsonify({'error': str(e)}), 400


@app.route('/api/chord', methods=['GET'])
def get_chord():
    """Returns chord notes and fretboard positions"""
    root_note = request.args.get('root', 'C')
    chord_type = request.args.get('type', 'maj')

    try:
        chord_notes = get_chord_notes(root_note, chord_type)
        guitar = Fretboard()
        positions = guitar.find_notes(chord_notes)

        return jsonify({
            'chord_notes': chord_notes,
            'fretboard_positions': positions,
            'root_note': root_note,
            'chord_type': chord_type
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
