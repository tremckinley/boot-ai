import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
args = sys.argv[1:]

#print(args)

if (len(args)< 1):
    print("You need a prompt!")
    exit(1)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=args[0]
)

if ("--verbose" in args):
    #print(response.usage_metadata)
    print("User prompt:", args[0])
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)


print("Response:")
print(response.text)
