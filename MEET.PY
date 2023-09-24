import os
import openai
import json
from docx import Document

# Initialize OpenAI API (Make sure to set your API key in the environment)
openai.api_key = "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"


# Function to transcribe audio
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

def abstract_summary_extraction(transcription, context):
    full_text = context + "\n" + transcription
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Summarize the following transcribed voice journal entry by Ryan into a concise abstract paragraph. Be mindful of potential transcription errors"
            },
            {
                "role": "user",
                "content": full_text
            }
        ]
    )
    return response['choices'][0]['message']['content']

def meeting_minutes(transcription, context):
    abstract_summary = abstract_summary_extraction(transcription, context)
    return {
        'abstract_summary': abstract_summary,
    }

def save_as_docx(minutes, transcription, filename):
    doc = Document()
    
    # Add header for filename
    doc.add_heading(f'Meeting Minutes for {filename}', 0)
    
    # Add the transcription
    doc.add_heading('Transcription', level=1)
    doc.add_paragraph(transcription)
    doc.add_paragraph()
    
    # Add the meeting minutes
    for key, value in minutes.items():
        heading = ' '.join(word.capitalize() for word in key.split('_'))
        doc.add_heading(heading, level=1)
        doc.add_paragraph(value)
        doc.add_paragraph()
        
    doc.save(filename)

# Main script
if __name__ == "__main__":
    # Read the context from context.txt
    with open("context.txt", "r") as f:
        context = f.read()

    for filename in os.listdir('.'):
        if filename.endswith('.mp3'):
            print(f"Processing {filename}...")
            transcription = transcribe_audio(filename)
            
            # Generate the meeting minutes
            minutes = meeting_minutes(transcription, context)
            
            # Save both the transcription and the meeting minutes to a single DOCX file
            doc_filename = filename.replace('.mp3', '_minutes.docx')
            save_as_docx(minutes, transcription, doc_filename)
            
            print(f"Saved meeting minutes and transcription for {filename} as {doc_filename}")

