from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPEN_AI_KEY = getenv("OPEN_AI_KEY")  # Put your open AI key here
GMAIL_APP_PASSWORD = getenv("GMAIL_APP_PASSWORD")  # Put your gmail app password here
ADD_GDRIVE_ZAP_URL = getenv("ADD_GDRIVE_ZAP_URL")  # Put zappier webhook workflow here, This webhook uploads the file to GDrive
LaTeX_COMPILER_URL = "https://latexonline.cc/compile?command=xelatex&text="
