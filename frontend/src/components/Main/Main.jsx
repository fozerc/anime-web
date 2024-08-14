import {Buttons} from "./Main_Components/Buttons.jsx";
import {TabsSections} from "./Main_Components/TabsSections.jsx";
import {useState} from "react";

export const Main = () => {

    const [activeTab, setActiveTab] = useState('main');

    return (
        <main>
            <TabsSections active={activeTab} onChange={(current) => setActiveTab(current)}/>

            {activeTab === 'main' && <div>главная страница</div>}
            {activeTab === 'characters' && <Buttons/>}
        </main>
    )
}