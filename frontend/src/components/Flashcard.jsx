import { useState } from "react";

export default function Flashcard({ word, onNext, onPrev })
{
    const [flipped, setFlipped] = useState(false);

    function handleFlip()
    {
        setFlipped(!flipped);
    }

    function handleNext()
    {
        setFlipped(false);
        onNext();
    }

    function handlePrev()
    {
        setFlipped(false);
        onPrev();
    }

    return (
    <div className="flashcard-container">
      <div
        className={`flashcard ${flipped ? "flipped" : ""}`}
        onClick={handleFlip}
      >
        <div className="flashcard-front">
          <p className="flashcard-label">Indonesian</p>
          <p className="flashcard-word">{word.indonesian}</p>
          <p className="flashcard-hint">Click to reveal</p>
        </div>
        <div className="flashcard-back">
          <p className="flashcard-label">English</p>
          <p className="flashcard-word">{word.english}</p>
          <p className="flashcard-hint">Click to flip back</p>
        </div>
      </div>

      <div className="flashcard-controls">
        <button onClick={handlePrev}>← Prev</button>
        <button onClick={handleNext}>Next →</button>
      </div>
    </div>
  );
}