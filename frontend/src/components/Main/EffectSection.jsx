import {Button} from "../Buttons/Button.jsx";
import {Modal} from "../Modal/Modal.jsx";
import {useState} from "react";

export const EffectSection = () => {
    const [modal, setModal] = useState(false);

    function openModal() {
        setModal(true);
    }

    return (
        <section>
            <h3>Effects</h3>

            <Button onClick={openModal}>Открыть информацию</Button>

            <Modal open={modal}>
                <h3>Hello from modal</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam aliquid assumenda consectetur eos
                    inventore nihil repellendus velit voluptatibus. A adipisci, aliquid architecto aut culpa dolorem
                    eaque excepturi fugit illum in magni nobis nostrum officia omnis placeat quibusdam similique, totam
                    veniam voluptatem voluptatibus! Deleniti error eveniet illum quasi similique sunt totam?</p>
                <Button onClick={() => setModal(false)}>Close modal</Button>
            </Modal>
        </section>
    )
}