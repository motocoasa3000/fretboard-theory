import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE = 'http://127.0.0.1:5001';

function App() {
  const [scales, setScales] = useState([]);
  const [chords, setChords] = useState([]);
  const [selectedRoot, setSelectedRoot] = useState('C');
  const [selectedType, setSelectedType] = useState('major');
  const [mode, setMode] = useState('scale');
  const [fretboardData, setFretboardData] = useState(null);
  const [loading, setLoading] = useState(false);

  const rootNotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

  useEffect(() => {
    // Load available scales and chords
    axios.get(`${API_BASE}/api/scales`).then(response => setScales(response.data));
    axios.get(`${API_BASE}/api/chords`).then(response => setChords(response.data));

    // Load initial data
    fetchFretboardData();
  }, []);

  const fetchFretboardData = async () => {
    setLoading(true);
    try {
      const endpoint = mode === 'scale' ? 'scale' : 'chord';
      const url = `${API_BASE}/api/${endpoint}?root=${selectedRoot}&type=${selectedType}`;
      console.log("Fetching from URL:", url);
      const response = await axios.get(url);
      setFretboardData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      alert('Error connecting to server. Make sure your Flask backend is running on port 5001.');
    }
    setLoading(false);
  };

  const handleModeChange = (newMode) => {
    setMode(newMode);
    setSelectedType(newMode === 'scale' ? 'major' : 'maj');
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>🎸 Fretboard Theorist</h1>
        <p>Visualize scales and chords on the guitar fretboard</p>
      </header>

      <div className="controls">
        <select
          value={mode}
          onChange={(e) => handleModeChange(e.target.value)}
        >
          <option value="scale">Scale</option>
          <option value="chord">Chord</option>
        </select>

        <select
          value={selectedRoot}
          onChange={(e) => setSelectedRoot(e.target.value)}
        >
          {rootNotes.map(note => (
            <option key={note} value={note}>{note}</option>
          ))}
        </select>

        <select
          value={selectedType}
          onChange={(e) => setSelectedType(e.target.value)}
        >
          {(mode === 'scale' ? scales : chords).map(type => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>

        <button onClick={fetchFretboardData} disabled={loading}>
          {loading ? 'Loading...' : 'Show on Fretboard'}
        </button>
      </div>

      {fretboardData && (
        <div className="current-selection">
          <h2>{fretboardData.root_note} {fretboardData.scale_type || fretboardData.chord_type}</h2>
          <p>Notes: {fretboardData.scale_notes?.join(' - ') || fretboardData.chord_notes?.join(' - ')}</p>
        </div>
      )}

      <div className="fretboard-container">
        {fretboardData && (
          <FretboardVisualization positions={fretboardData.fretboard_positions} />
        )}
      </div>
    </div>
  );
}

const FretboardVisualization = ({ positions }) => {
  const strings = [0, 1, 2, 3, 4, 5];
  const frets = 12;

  const positionsByString = {};
  positions.forEach(pos => {
    if (!positionsByString[pos[0]]) positionsByString[pos[0]] = [];
    positionsByString[pos[0]].push({ fret: pos[1], note: pos[2] });
  });

  return (
    <div className="fretboard">
      <div className="fret-numbers">
        {Array.from({ length: frets + 1 }, (_, i) => (
          <div key={i} className="fret-number">{i}</div>
        ))}
      </div>

      {strings.map(stringIndex => (
        <div key={stringIndex} className="guitar-string">
          <div className="string-label">{['E', 'A', 'D', 'G', 'B', 'E'][stringIndex]}</div>

          {Array.from({ length: frets + 1 }, (_, fret) => {
            const position = positionsByString[stringIndex]?.find(p => p.fret === fret);
            return (
              <div key={fret} className="fret">
                {position ? (
                  <div className="note-marker" title={`${position.note} - Fret ${fret}`}>
                    {position.note.replace('#', '♯')}
                  </div>
                ) : (
                  <div className="fret-space"></div>
                )}
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export default App;