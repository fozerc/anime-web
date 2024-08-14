import './button.css';

export const Buttons = ({data, onClick, isActive}) => {
    return (
        <button className={isActive ? 'button active' : 'button'} onClick={onClick}>{data}</button>
    )
}