import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import WordList from "./components/WordList";
import Flashcard from "./components/Flashcard";
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
  const [mode, setMode] = useState("list");
  const [cardIndex, setCardIndex] = useState(0);

  useEffect(() => {
    if (selected === "all") {
      fetchAllWords().then((res) => setWords(res.data));
    } else {
      fetchByCategory(selected).then((res) => setWords(res.data));
    }
    setCardIndex(0);
  }, [selected]);

  function handleNext() {
    setCardIndex((prev) => (prev + 1) % words.length);
  }

  function handlePrev() {
    setCardIndex((prev) => (prev - 1 + words.length) % words.length);
  }

  return (
    <div className="app">
      <Navbar
        categories={CATEGORIES}
        selected={selected}
        onSelect={(cat) => {
          setSelected(cat);
          setCardIndex(0);
        }}
      />

      <main className="content">
        <div className="mode-toggle">
          <button
            className={mode === "list" ? "active" : ""}
            onClick={() => setMode("list")}
          >
            List
          </button>
          <button
            className={mode === "flashcard" ? "active" : ""}
            onClick={() => setMode("flashcard")}
          >
            Flashcards
          </button>
        </div>

        <h2 className="category-title">
          {selected === "all"
            ? "All Words"
            : selected.charAt(0).toUpperCase() + selected.slice(1)}
        </h2>

        {mode === "list" && <WordList words={words} />}

        {mode === "flashcard" && words.length > 0 && (
          <>
            <p className="card-counter">
              {cardIndex + 1} / {words.length}
            </p>
            <Flashcard
              word={words[cardIndex]}
              onNext={handleNext}
              onPrev={handlePrev}
            />
          </>
        )}
      </main>
    </div>
  );
}

export default App;