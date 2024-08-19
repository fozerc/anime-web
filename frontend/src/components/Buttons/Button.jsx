import './button.css';

export const Button = ({children, isActive, ...props}) => {
    return (
        <button
            {...props}
            className={isActive ? 'button active' : 'button'}>{children}</button>
    )
}