import {Button} from "../../Buttons/Button.jsx";

export const TabsSections = ({active, onChange}) => {
    return (
        <section style={{marginBottom: "2rem"}}>
            <Button isActive={active === 'main'} onClick={() => onChange('main')}>Главная</Button>
            <Button isActive={active === 'characters'} onClick={() => onChange('characters')}>Персонажи</Button>
            <Button isActive={active === 'feedback'} onClick={() => onChange('feedback')}>Обратная связь</Button>
            <Button isActive={active === 'effect'} onClick={() => onChange('effect')}>effect</Button>
        </section>
    )
}