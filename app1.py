import requests
import ssl
import streamlit as st
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# GUI for user input
st.title("AI Document Generator")
input_data = st.text_input("Which document you would like to create?")
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"  # Chrome-specific User-Agent string
}

if st.button("Get Response"):
    session = requests.Session()
    session.verify = False
    response = session.post("http://5277-107-167-177-75.ngrok-free.app/predict",
			     json={'query': input_data},
			     headers=headers)
    
    try:
        json_response = response.json()
        # Display the response as an h2-like title
        st.markdown(f"{json_response['response']}")
    except ValueError:
        st.write("Error: Response is not JSON format")
