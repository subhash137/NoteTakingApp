import React from 'react'
import { useState,useEffect } from 'react'

function NoteListpage() {
  let [notes, setNotes] = useState([])
  useEffect(
    ()=>{getNotes()},[]
  )

  let getNotes = async () =>{

    let response = await fetch('http://127.0.0.1:8000/notes/')
    let data = await response.json()
   
    setNotes(data)

  }
  return (
    <div>
    <div>{notes.map((note,index)=>(
        <h1>{note.body}</h1>

    ))}</div>
    </div>
  )
}

export default NoteListpage