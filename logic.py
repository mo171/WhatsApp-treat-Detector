'''
THIS IS A LOGIC FILE WHERE EVERY BACKEND LOGIC OCCESING IS DONE
MADE TO KEEP THE APP MODULAR

'''

# IMPORTING ALL THE NESSECARY LIBRARIES
from dotenv import load_dotenv
from wsgiref import headers
import requests
import os

load_dotenv()


# THIS FUNCTION PROCCESSES THE CHAT AND IDENTIFIES IF IT POSSES POTENTAIL THREAT USING KEYOWRDS.
def process_chat(chat):
    """

    IDENTIFIES IF THE WHATSAPP CHAT POSSES POTENTAIL THREAT USING KEYOWRDS.
    RETURNS A DICT WITH PROCCESD CHAT AND IS_THREAT

    """
    processed_chat = chat.lower()
    threat_keywords = ["forwarded", "fw:", "fwd:", "shared via", "forwarded message", "buy now", "click here", "limited offer", "urgent", "act fast", "winner", "congratulations", "free", "prize", "risk-free", "guaranteed", "latest news", "breaking news", "new finnancial opportunity", "exclusive deal", "special promotion", "important update", "security alert", "account suspended", "verify your account", "password reset", "login attempt", "unauthorized access", "war", "news", "earthquake", "flood", "hurricane", "tsunami", "disaster", "emergency", "alert", "warning", "crisis", "pandemic", "outbreak", "epidemic", "health scare"]

    is_threat = any(keyword in processed_chat for keyword in threat_keywords) # USED FOR CHECKING KEYWORDS IN LIST AND MATCHING AND RETURNS A BOOLEAN VALUE USING ANY

    return {
        "processed_chat": processed_chat,
        "is_threat": is_threat
    }


#---------------------------------------------------------------------------------------

# INITAILIZING THE VARIABLES FOR IMAGE AI DETECTION
# AI DETECTION USING HUGGING FACE API
API_URL = "https://api-inference.huggingface.co/models/umm-maybe/AI-image-detector"

HF_API_KEY = os.getenv('HF_API_KEY')



headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
}

# FUNCTION TO DETECT IF THE IMAGE IS AI GENERATED OR NOT
def detect_ai_image(filename):

    with open(filename, "rb") as f:
        data = f.read()

    response = requests.post(API_URL, headers={"Content-Type": "image/jpeg", **headers}, data=data)
    list = response.json()
    dict=list[0]
    status=dict.get("label")
    print(status)

    if status == "artificial":
        AI_generated = True
    else:       
        AI_generated = False

    return AI_generated
        

  

