import axios from "axios";
import {useState} from "react";

export const useAxios = () => {
    const [state, setState] = useState({
        loading: true,
        data: null,
        error: null,
    })

    // const updateState = (state, response) => {
    //     console.log("updateState", state, response)
    //     setState({
    //         ...state,
    //         data: response.data,
    //         error: null,
    //         loading: false,
    //     })
    // }

    const sendRequest = async (url, type, data) => {
        setState({ loading: true, data: null, error: null });
        try {
            let response;
            if (!url) {
                return
            }
            if (type === 'get' || type === 'delete') {
                response = await axios[type](url)
            } else {
                response = await axios[type](url, data)
            }
            setState({
                data: response.data,
                error: null,
                loading: false,
            })
        } catch (error) {
            if (error.response && error.response.status === 404) {
                setState({
                    loading: false,
                    error: error.response.data,
                    data: null,
                })
            }
        }
    }
    console.log(state)
    return {state, sendRequest}
}