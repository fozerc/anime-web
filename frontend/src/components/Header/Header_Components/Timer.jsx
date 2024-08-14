import {useState} from "react";

export const Timer = () => {
    const [now, setNow] = useState(new Date());
    setInterval(() => setNow(new Date()), 1000);

    return (
        <div className="timer">{now.toLocaleString()}</div>
    )
}
