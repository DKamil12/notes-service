from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
notes: Dict[int, str] = {}  # Словарь: id -> заметка
note_id = 0  # Счётчик заметок

class Note(BaseModel):
    content: str

@app.post("/notes/")
def create_note(note: Note):
    global note_id
    note_id += 1
    notes[note_id] = note.content
    return {"id": note_id, "content": note.content}

@app.get("/notes/{note_id}")
def read_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, "content": notes[note_id]}

@app.get("/notes/")
def list_notes():
    return [{"id": i, "content": text} for i, text in notes.items()]

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return {"message": "Note deleted"}
