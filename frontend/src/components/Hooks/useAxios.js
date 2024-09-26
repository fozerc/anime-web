import axios from "axios";
import {useState} from "react";

export const useAxios = () => {
    const [state, setState] = useState({
        loading: true,
        data: null,
        error: null,
    })

    const updateState = (state, response) => {
        setState({
            ...state,
            data: response.data,
            loading: false,
        })
    }

    const sendRequest = async (url, type, data) => {
        try {
            let response;
            if (!url) {
                return
            }
            if (type === 'get' || type === 'delete') {
                response = await axios[type](url)
                console.log(response.data[0].name)
                updateState(state, response)
            } else {
                response = await axios[type](url, data)
                updateState(state, response)
            }
        } catch (error) {
            throw error
        }
    }
    return {state, sendRequest}
}