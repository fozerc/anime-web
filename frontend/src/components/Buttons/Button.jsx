import './button.css';

export const Button = ({children, onClick, isActive}) => {
    return (
        <button className={isActive ? 'button active' : 'button'} onClick={onClick}>{children}</button>
    )
}