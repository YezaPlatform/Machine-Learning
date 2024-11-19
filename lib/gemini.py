import google.generativeai as genai
import base64
import json
import os
from dotenv import load_dotenv


load_dotenv()


google_api_key=os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=google_api_key)

model = os.getenv('MODEL')
safety_settings_b64 = os.getenv('SAFETY_SETTINGS_B64')
generation_config_b64 = os.getenv('GENERATION_CONFIG_b64')
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
generation_config = json.loads(base64.b64decode(generation_config_b64))


gemini = genai.GenerativeModel(model_name=model)


def generate_disease_info(disease_name):

  template_prompt = f"""
  You are a knowledgeable agricultural assistant. Provide the following details for the crop disease "{disease_name}":

  1. **Short and precise definition**: Summarize the disease, including the crop(s) affected, common symptoms, and typical causes.
  2. **Best practices for prevention and treatment**: Give practical, research-backed advice on managing and preventing the disease, specifying any recommended treatments, environmental controls, and regular maintenance.

  Use an informative, concise, and suggestive tone.
  """
  response = gemini.generate_content(
      template_prompt,
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=False,
  )

  if generation_config.get("candidate_count", 1) == 1:
      return(response.text)
  
