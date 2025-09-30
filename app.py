'''
 FLASK APP FOR
 WHATSAPP THREAT DETECTION

 ----------------------------------
 RUNS THE FLASK APP
 LINKS THE FRONTEND TO THE BACKEND

'''
# IMPORTING ALL THE NESSECARY LIBRARIES
from flask import Flask, request, render_template
import os
from logic import process_chat
from logic import detect_ai_image


# Flask minimal app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/result_text', methods=['GET', 'POST'])
def result_text():
    if request.method == 'POST':
        chat = request.form.get('chat')

       
        processed = process_chat(chat)
        return render_template('result_text.html', chat=processed['processed_chat'], is_threat=processed['is_threat'])

@app.route('/result_image', methods=['GET', 'POST'])    
def result_image():   
    if request.method == 'POST':
        image_path = request.files.get('image')
        image_path.save('static/image.png')       

        AI_generated = detect_ai_image('static/image.png') 
        return render_template('result_image.html', image_path='static/image.png', AI_generated=AI_generated)

# RUN THE MAIN FILE
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
   
 
