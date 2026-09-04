export default function WordList({ words }) {
  if (words.length === 0) {
    return <p className="empty">No words found.</p>;
  }

  return (
    <ul className="word-list">
      {words.map((w) => (
        <li key={w.id} className="word-item">
          <span className="indonesian">{w.indonesian}</span>
          <span className="english">{w.english}</span>
        </li>
      ))}
    </ul>
  );
}