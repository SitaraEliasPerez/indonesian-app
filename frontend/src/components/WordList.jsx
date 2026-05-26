import { useEffect, useState } from "react";
import api from "../api";

export default function WordList() {
    const [words, setWords] = useState([]);

    useEffect(() => {
        api.get("/words").then((res) => setWords(res.data));
    }, []);


    return (
        <ul>
            {words.map((w) => (
                <li key={w.id}>{w.indonesian} - {w.english}</li>
            ))}
        </ul>
    );
}