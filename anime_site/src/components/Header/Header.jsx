import {Search, Timer} from "./Header_Components/index.js";
import {SearchContext} from "./Header_Components/context.js";
import {useState} from "react";

export const Header = () => {
    const [data, setData] = useState({});
    return (
        <header>
            <SearchContext.Provider value={{data, setData}}>
                <Timer/>
                <Search/>
            </SearchContext.Provider>
        </header>
    );
}
