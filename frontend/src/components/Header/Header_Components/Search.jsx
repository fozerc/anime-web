import {useAxios} from "../../Hooks/useAxios.js";
import {useContext, useRef} from "react";
import {SearchContext, useDataContext} from "./context.js";


export const Search = () => {
    const {state, sendRequest} = useAxios()
    const inputRef = useRef(null)
    const [data, setData] = useDataContext()

    const handleSearch = async (searchTerms) => {
        await sendRequest(`http://localhost:8000/api/global-search?query=${searchTerms}`, 'get')
        if (state.data) {
            setData(state.data[0])
        }
    }

    return (
        <div>
            <form onSubmit={e => {
                e.preventDefault()
                const searchTerms = inputRef.current.value
            }}>
                <label htmlFor="site-seatch">Search your anime or manga here!</label>
                <input
                    ref={inputRef}
                    type="search"
                    id="site-search"
                    name="site-seatch" placeholder="Search..."/>
                <button type={"submit"}>Search</button>
                <div>
                    <p>{data.name}</p>
                </div>
            </form>
        </div>
    )
}

