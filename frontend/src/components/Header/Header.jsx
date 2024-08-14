import { animes } from "../../../data.js";
import { Buttons } from "../Buttons/Button.jsx";
import { useState } from "react";

export const Header = () => {
    const [contentType, setContentType] = useState(null);

    const clickHandler = (anime) => {
        setContentType(anime);
    }

    return (
        <header>
            <div className="buttons-container">
                {animes.map((anime) => (
                    <Buttons
                        onClick={() => clickHandler(anime)}
                        key={anime.name}
                        data={anime.name}
                        isActive={contentType.name === anime.name}
                    />
                ))}
            </div>
            <div className="anime-container">
                {!contentType && <p>нажми на кнопку</p>}
                {contentType && (
                    <div>
                        <h2>{contentType.name}</h2>
                        <p>Year of Issue: {contentType.year_of_issue}</p>
                        <img src={contentType.photo} alt={contentType.name} />
                    </div>
                )}
            </div>
        </header>
    );
}
