import {Button} from "../../Buttons/Button.jsx";
import {useState} from "react";

export const Feedback = () => {
    const [name, setName] = useState('');
    const [reason, setReason] = useState('help');
    const [hasError, setHasError] = useState(true);

    const handleChangeName = (event) => {
        setName(event.target.value);
        console.log(event.target.value.trim().length === 0)
        setHasError(event.target.value.trim().length === 0);
    }

    return (
        <section className="feedback-section">
            <h3>обратная связь</h3>

            <div className="feedback-container">
                <form action="">
                    <label htmlFor="name">Ваше имя</label>
                    <input style={{
                        border: hasError ? '2px solid red' : '2px solid green',
                    }} type="text" id='name' className='control' value={name} onChange={handleChangeName}/>
                    <label htmlFor="reason">Причина обращения</label>
                    <select name="reason" id="reason" value={reason} onChange={event => setReason(event.target.value)}>
                        <option value="error">Ошибка</option>
                        <option value="help">Нужна помощь</option>
                        <option value="suggest">Предолжение</option>
                    </select>
                    <Button disabled={hasError}>Отправить</Button>
                </form>
            </div>

            <pre>
                name: {name}
                reason: {reason}
            </pre>
        </section>
    )
}