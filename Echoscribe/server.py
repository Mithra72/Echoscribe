import os
from flask import Flask, request, jsonify, render_template
import assemblyai as aai
from werkzeug.utils import secure_filename

# You must add your API key here
aai.settings.api_key = "ASSEMBLYAI_API_KEY"

app = Flask(__name__)
# Set a temporary upload folder for files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Handle the file upload and transcription
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Check if a file was uploaded
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Secure the filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the temporary file
        file.save(filepath)

        # Transcribe the audio file using AssemblyAI
        try:
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(filepath)
            
            if transcript.status == aai.TranscriptStatus.error:
                return jsonify({'error': transcript.error}), 500
            
            return jsonify({'transcript': transcript.text}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up the temporary file
            if os.path.exists(filepath):
                os.remove(filepath)

# Run the server
if __name__ == '__main__':
    # Using '0.0.0.0' makes the server accessible from other devices on the network.
    # Set host to '127.0.0.1' (localhost) for local development only.
    app.run(debug=True, host='127.0.0.1')
