from app import app, db, Word

words = [
    # Basic Phrases
    Word(category="basic phrases", indonesian="halo",          english="hello"),
    Word(category="basic phrases", indonesian="selamat pagi",  english="good morning"),
    Word(category="basic phrases", indonesian="selamat siang", english="good afternoon"),
    Word(category="basic phrases", indonesian="selamat malam", english="good evening"),
    Word(category="basic phrases", indonesian="apa kabar",     english="how are you"),
    Word(category="basic phrases", indonesian="baik",          english="good / fine"),
    Word(category="basic phrases", indonesian="terima kasih",  english="thank you"),
    Word(category="basic phrases", indonesian="sama-sama",     english="you're welcome"),
    Word(category="basic phrases", indonesian="permisi",       english="excuse me"),
    Word(category="basic phrases", indonesian="maaf",          english="sorry"),
    Word(category="basic phrases", indonesian="sampai jumpa",  english="goodbye"),
    Word(category="basic phrases", indonesian="ya",            english="yes"),
    Word(category="basic phrases", indonesian="tidak",         english="no"),
    Word(category="basic phrases", indonesian="tolong",        english="please / help"),
    # Numbers
    Word(category="numbers", indonesian="nol",      english="zero"),
    Word(category="numbers", indonesian="satu",     english="one"),
    Word(category="numbers", indonesian="dua",      english="two"),
    Word(category="numbers", indonesian="tiga",     english="three"),
    Word(category="numbers", indonesian="empat",    english="four"),
    Word(category="numbers", indonesian="lima",     english="five"),
    Word(category="numbers", indonesian="enam",     english="six"),
    Word(category="numbers", indonesian="tujuh",    english="seven"),
    Word(category="numbers", indonesian="delapan",  english="eight"),
    Word(category="numbers", indonesian="sembilan", english="nine"),
    Word(category="numbers", indonesian="sepuluh",  english="ten"),
    # Colors
    Word(category="colors", indonesian="merah",    english="red"),
    Word(category="colors", indonesian="biru",     english="blue"),
    Word(category="colors", indonesian="kuning",   english="yellow"),
    Word(category="colors", indonesian="hijau",    english="green"),
    Word(category="colors", indonesian="hitam",    english="black"),
    Word(category="colors", indonesian="putih",    english="white"),
    Word(category="colors", indonesian="oranye",   english="orange"),
    Word(category="colors", indonesian="ungu",     english="purple"),
    Word(category="colors", indonesian="merah muda", english="pink"),
    Word(category="colors", indonesian="coklat",   english="brown"),
    Word(category="colors", indonesian="abu-abu",  english="gray"),
    # Grammar Particles
    Word(category="grammar particles", indonesian="di",     english="at / in / on (location)"),
    Word(category="grammar particles", indonesian="ke",     english="to (direction)"),
    Word(category="grammar particles", indonesian="dari",   english="from"),
    Word(category="grammar particles", indonesian="dan",    english="and"),
    Word(category="grammar particles", indonesian="atau",   english="or"),
    Word(category="grammar particles", indonesian="yang",   english="which / that / who (relative marker)"),
    Word(category="grammar particles", indonesian="dengan", english="with"),
    Word(category="grammar particles", indonesian="untuk",  english="for / in order to"),
    Word(category="grammar particles", indonesian="sudah",  english="already (perfective marker)"),
    Word(category="grammar particles", indonesian="sedang", english="currently (progressive marker)"),
    Word(category="grammar particles", indonesian="akan",   english="will (future marker)"),
    Word(category="grammar particles", indonesian="juga",   english="also / too"),
    Word(category="grammar particles", indonesian="bukan",  english="not (for nouns)"),
    Word(category="grammar particles", indonesian="tidak",  english="not (for verbs/adjectives)"),
    # Pronouns
    Word(category="pronouns", indonesian="saya",   english="I / me (formal)"),
    Word(category="pronouns", indonesian="aku",    english="I / me (informal)"),
    Word(category="pronouns", indonesian="kamu",   english="you (informal)"),
    Word(category="pronouns", indonesian="Anda",   english="you (formal)"),
    Word(category="pronouns", indonesian="dia",    english="he / she"),
    Word(category="pronouns", indonesian="kami",   english="we (excludes listener)"),
    Word(category="pronouns", indonesian="kita",   english="we (includes listener)"),
    Word(category="pronouns", indonesian="mereka", english="they"),
    Word(category="pronouns", indonesian="ini",    english="this"),
    Word(category="pronouns", indonesian="itu",    english="that"),
]

with app.app_context():
    db.create_all()
    Word.query.delete()
    db.session.add_all(words)
    db.session.commit()
    print(f"Seeded {len(words)} words successfully.")