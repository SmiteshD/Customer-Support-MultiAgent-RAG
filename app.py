import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "23837011-2700-44de-aaa4-11497945f277"
FLOW_ID = "60fb2c3e-7045-45c7-aad6-2d93eec11c39"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "customer" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()