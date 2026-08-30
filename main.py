import streamlit as st
import pandas as pd
import resend

st.title("🚀 Outbound Engine")

# Security Input
resend_api_key = st.sidebar.text_input("Resend API Key", type="password")

uploaded_file = st.file_uploader("Upload Target Leads CSV", type=["csv"])
subject = st.text_input("Subject", "Quick question for your business")
body = st.text_area("Message Body", "Hi {Name},\n\nWe build custom outreach engines...")

if st.button("Start Outreach Campaign"):
    if uploaded_file and resend_api_key:
        resend.api_key = resend_api_key
        df = pd.read_csv(uploaded_file)
        
        for index, row in df.iterrows():
            lead_name = row['Name'] if 'Name' in row else 'there'
            custom_body = body.replace("{Name}", str(lead_name))
            
            try:
                resend.Emails.send({
                    "from": "onboarding@resend.dev",
                    "to": row['Email'],
                    "subject": subject,
                    "text": custom_body
                })
                st.success(f"Sent to {row['Email']}")
            except Exception as e:
                st.error(f"Failed to send to {row['Email']}: {e}")
                
        st.balloons()
