import {animes} from "../../../../data.js";
import {Button} from "../../Buttons/Button.jsx";
import {useState} from "react";

export const Buttons = () => {

    const [contentType, setContentType] = useState(null);

    const clickHandler = (anime) => {
        setContentType(anime);
    }
    return (

        <>
            <div className="buttons-container">
                {animes.map((anime) => (
                    <Button
                        onClick={() => clickHandler(anime)}
                        key={anime.name}
                        isActive={contentType && contentType.name === anime.name}
                    >{anime.name}</Button>
                ))}
            </div>
            <div className="anime-container">
                {!contentType && <p>нажми на кнопку</p>}
                {contentType && (
                    <div>
                        <h2>{contentType.name}</h2>
                        <p>Year of Issue: {contentType.year_of_issue}</p>
                        <img src={contentType.photo} alt={contentType.name}/>
                    </div>
                )}
            </div>
        </>
    )
}
