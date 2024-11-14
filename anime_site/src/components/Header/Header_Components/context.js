import {createContext, useContext} from "react";

export const SearchContext = createContext(undefined)

export const useDataContext = () => {
    const data = useContext(SearchContext)

    if (data === undefined) {
        throw new Error("useDataContext must be used within the context")
    }

    return data
}