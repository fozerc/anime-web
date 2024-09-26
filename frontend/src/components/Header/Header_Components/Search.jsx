import axios from "axios";
import {useAxios} from "../../Hooks/useAxios.js";
import {useRef} from "react";


export const Search = () => {
    const {state, sendRequest} = useAxios()
    console.log(state);
    const inputRef = useRef(null)
    return (
        <div>
            <form onSubmit={e => {
                e.preventDefault()
                const searchTerms = inputRef.current.value
                console.log(searchTerms)
                sendRequest(`http://localhost:8000/api/global-search?query=${searchTerms}`, 'get')
            }}>
                <label htmlFor="site-seatch">Search your anime or manga here!</label>
                <input
                    ref={inputRef}
                    type="search"
                    id="site-search"
                    name="site-seatch" placeholder="Search..."/>
                <button type={"submit"}>Search</button>
            </form>
        </div>
    )
}

