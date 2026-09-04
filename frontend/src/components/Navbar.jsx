export default function Navbar({ categories, selected, onSelect }) {
  return (
    <nav className="navbar">
      <span className="navbar-brand">Indonesian</span>
      <ul className="navbar-links">
        <li>
          <button
            className={selected === "all" ? "active" : ""}
            onClick={() => onSelect("all")}
          >
            All
          </button>
        </li>
        {categories.map((cat) => (
          <li key={cat}>
            <button
              className={selected === cat ? "active" : ""}
              onClick={() => onSelect(cat)}
            >
              {cat.charAt(0).toUpperCase() + cat.slice(1)}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
}