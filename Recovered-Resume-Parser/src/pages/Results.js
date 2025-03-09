import { useEffect, useState } from "react";
import axios from "axios";

function Results() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/results").then(response => setResults(response.data));
  }, []);

  return (
    <div>
      <h2>Candidate Rankings</h2>
      <ul>
        {results.map((candidate, index) => (
          <li key={index}>{candidate.name} - {candidate.match_score}</li>
        ))}
      </ul>
    </div>
  );
}

export default Results;
