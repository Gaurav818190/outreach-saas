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
                })import streamlit as st
import pandas as pd
import resend

st.title("🚀 Outbound Engine")

# Security Input
resend_api_key = st.sidebar.text_input("Resend API Key", type="password")
sender_name = st.sidebar.text_input("Your Name / Brand", "Gaurav")

uploaded_file = st.file_uploader("Upload Target Leads CSV", type=["csv"])
subject = st.text_input("Subject", "Quick question for your business")
body = st.text_area("Message Body", "Hi {Name},\n\nWe build custom outreach engines for {Company}...")

if st.button("Start Outreach Campaign"):
    if uploaded_file and resend_api_key:
        resend.api_key = resend_api_key
        df = pd.read_csv(uploaded_file)
        
        success_count = 0
        progress_bar = st.progress(0)
        total_rows = len(df)
        
        for index, row in df.iterrows():
            lead_name = row['Name'] if 'Name' in row else "there"
            lead_email = row['Email'] if 'Email' in row else None
            lead_company = row['Company'] if 'Company' in row else "your company"
            
            if lead_email:
                custom_body = body.replace("{Name}", str(lead_name)).replace("{Company}", str(lead_company))
                
                params = {
                    "from": f"{sender_name} <onboarding@resend.dev>",
                    "to": [lead_email],
                    "subject": subject,
                    "html": f"<p>{custom_body.replace(chr(10), '<br>')}</p>",
                }
                
                try:
                    email = resend.Emails.send(params)
                    success_count += 1
                except Exception as e:
                    st.error(f"Failed to send to {lead_email}: {e}")
            
            progress_bar.progress((index + 1) / total_rows)
            
        st.success(f"Campaign completed! Successfully sent {success_count} emails.")
    else:
        st.warning("Please upload a CSV file and enter your Resend API Key.")
                st.success(f"Sent to {row['Email']}")
            except Exception as e:import streamlit as st
import pandas as pd
import resend

st.title("🚀 Outbound Engine")

# Security and Customization Inputs
resend_api_key = st.sidebar.text_input("Resend API Key", type="password")
sender_name = st.sidebar.text_input("Your Name / Brand", "Gaurav")

uploaded_file = st.file_uploader("Upload Target Leads CSV", type=["csv"])
subject = st.text_input("Subject", "Quick question for your business")
body = st.text_area("Message Body", "Hi {Name},\n\nWe build custom outreach engines for {Company}...")

if st.button("Start Outreach Campaign"):
    if uploaded_file and resend_api_key:
        resend.api_key = resend_api_key
        df = pd.read_csv(uploaded_file)
        
        success_count = 0
        progress_bar = st.progress(0)
        total_rows = len(df)
        
        for index, row in df.iterrows():
            lead_name = row['Name'] if 'Name' in df.columns else "there"
            lead_email = row['Email'] if 'Email' in df.columns else None
            lead_company = row['Company'] if 'Company' in df.columns else "your company"
            
            if lead_email:
                custom_body = body.replace("{Name}", str(lead_name)).replace("{Company}", str(lead_company))
                
                params = {
                    "from": f"{sender_name} <onboarding@resend.dev>",
                    "to": [lead_email],
                    "subject": subject,
                    "html": f"<p>{custom_body.replace(chr(10), '<br>')}</p>",
                }
                
                try:
                    email = resend.Emails.send(params)
                    success_count += 1
                except Exception as e:
                    st.error(f"Failed to send to {lead_email}: {e}")
            
            progress_bar.progress((index + 1) / total_rows)
            
        st.success(f"Campaign completed! Successfully sent {success_count} emails.")
    else:
        st.warning("Please upload a CSV file and enter your Resend API Key.")
                st.error(f"Failed to send to {row['Email']}: {e}")
                
        st.balloons()import streamlit as st
import pandas as pd
import resend

st.title("🚀 Outbound Engine")

resend_api_key = st.sidebar.text_input("Resend API Key", type="password")
sender_name = st.sidebar.text_input("Your Name / Brand", "Gaurav")

uploaded_file = st.file_uploader("Upload Target Leads CSV", type=["csv"])
subject = st.text_input("Subject", "Quick question for your business")
body = st.text_area("Message Body", "Hi {Name},\n\nWe build custom outreach engines for {Company}...")

if st.button("Start Outreach Campaign"):
    if uploaded_file and resend_api_key:
        resend.api_key = resend_api_key
        df = pd.read_csv(uploaded_file)
        
        success_count = 0
        progress_bar = st.progress(0)
        total_rows = len(df)
        
        for index, row in df.iterrows():
            lead_name = row['Name'] if 'Name' in df.columns else "there"
            lead_email = row['Email'] if 'Email' in df.columns else None
            lead_company = row['Company'] if 'Company' in df.columns else "your company"
            
            if lead_email:
                custom_body = body.replace("{Name}", str(lead_name)).replace("{Company}", str(lead_company))
                
                params = {
                    "from": f"{sender_name} <onboarding@resend.dev>",
                    "to": [lead_email],
                    "subject": subject,
                    "html": f"<p>{custom_body.replace(chr(10), '<br>')}</p>",
                }
                
                try:
                    email = resend.Emails.send(params)
                    success_count += 1
                except Exception as e:
                    st.error(f"Failed to send to {lead_email}: {e}")
            
            progress_bar.progress((index + 1) / total_rows)
            
        st.success(f"Campaign completed! Successfully sent {success_count} emails.")
    else:
        st.warning("Please upload a CSV file and enter your Resend API Key.")
