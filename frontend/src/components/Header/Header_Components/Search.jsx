import {useAxios} from "../../Hooks/useAxios.js";
import {useEffect, useRef} from "react";
import {useDataContext} from "./context.js";


export const Search = () => {
    const {state, sendRequest} = useAxios()
    const inputRef = useRef(null)
    const {data, setData} = useDataContext()

    const handleSearch = async (searchTerms) => {
        await sendRequest(`http://localhost:8000/api/global-search?query=${searchTerms}`, 'get')

    }

    useEffect(() => {
        if (state.data) {
            setData(state.data[0])
        }
    }, [state.data, setData]);

    return (
        <div>
            <form onSubmit={e => {
                e.preventDefault()
                const searchTerms = inputRef.current.value
                handleSearch(searchTerms)
            }}>
                <label htmlFor="site-seatch">Search your anime or manga here!</label>
                <input
                    ref={inputRef}
                    type="search"
                    id="site-search"
                    name="site-seatch" placeholder="Search..."/>
                <button type={"submit"}>Search</button>
                <div>
                    {state.error ? (
                        <p>{state.error}</p>
                    ) : (
                        <>
                            <p>{data.name}</p>
                            <p>{data.description}</p>
                        </>
                    )
                    }
                </div>
            </form>
        </div>
    )
}

