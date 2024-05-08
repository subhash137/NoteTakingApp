import { useState,useEffect } from 'react'
import styled from 'styled-components'
import './App.css'
import Header from './components/header.jsx'
import NoteListpage  from './pages/NoteListpage.jsx'

function App() {
  


  return (
    
    <Container>
      <Header />
      <NoteListpage />
      
     
      
      Click on the Vite and React logos to learn more
      
    </Container>
  )
}

export default App

const Container = styled.div`

color: red;
`
