import {Buttons} from "./Main_Components/Buttons.jsx";
import {TabsSections} from "./Main_Components/TabsSections.jsx";
import {useState} from "react";
import {Feedback} from "./Main_Components/Feedback.jsx";
import {EffectSection} from "./EffectSection.jsx";

export const Main = () => {

    const [activeTab, setActiveTab] = useState('effect');

    return (
        <main>
            <TabsSections active={activeTab} onChange={(current) => setActiveTab(current)}/>
            {activeTab === 'main' && <div>главная страница</div>}
            {activeTab === 'characters' && <Buttons/>}
            {activeTab === 'feedback' && <Feedback />}
            {activeTab === 'effect' && <EffectSection />}
        </main>
    )
}