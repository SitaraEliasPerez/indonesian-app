import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import WordList from "./components/WordList";
import { fetchAllWords, fetchByCategory } from "./api";
import "./App.css";

const CATEGORIES = [
  "basic phrases",
  "numbers",
  "colors",
  "grammar particles",
  "pronouns",
];

function App() {
  const [words, setWords] = useState([]);
  const [selected, setSelected] = useState("all");

  useEffect(() => {
    if (selected === "all") {
      fetchAllWords().then((res) => setWords(res.data));
    } else {
      fetchByCategory(selected).then((res) => setWords(res.data));
    }
  }, [selected]);

  return (
    <div className="app">
      <Navbar
        categories={CATEGORIES}
        selected={selected}
        onSelect={setSelected}
      />
      <main className="content">
        <h2 className="category-title">
          {selected === "all"
            ? "All Words"
            : selected.charAt(0).toUpperCase() + selected.slice(1)}
        </h2>
        <WordList words={words} />
      </main>
    </div>
  );
}

export default App;