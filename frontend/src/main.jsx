import React, {Fragment} from 'react'
import ReactDOM from 'react-dom/client'
import {App} from './App.jsx'
import './index.css'
import {Header} from "./components/Header/Header.jsx";

ReactDOM.createRoot(document.getElementById('root')).render(
  <Fragment>
      <App />
  </Fragment>,
)
