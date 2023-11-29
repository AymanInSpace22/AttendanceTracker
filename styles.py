import base64
from PIL import Image


# Define CSS to target the Streamlit dark overlay
remove_black_overlay = '''
<style>
.stApp {
    background: none; /* Remove default Streamlit background */
}

.stBlock {
    display: none; /* Hide the Streamlit black overlay */
}
</style>
'''

page_bg_color = '''
<style>
body {
background-image: url("https://github.githubassets.com/images/modules/site/copilot/react/hero-bg-lg.jpg");
background-size: cover;
}
</style>
'''

# sidebar_bg = """ [data-testid="stSidebar"] {   background: rgba(0, 0, 0, 0); } """ 
sidebar_bg = '''
<style>
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, .5);
}
</style>
'''

# hiding footer and top bar
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""




# login = '''
# <p style="font: 55px Arial; font-weight: bold; color: white;">Login</p>
# '''

attendance = '''
<p style="font: 55px Arial; font-weight: bold; color: white;">Attendance Tracking</p>
'''

rainbow_divider = '''
<div style="height: 4px; background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);"></div>
'''




# additional background images
# https://images.unsplash.com/photo-1697899001862-59699946ea29?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D    







login = '''
<p style="font: 4.5rem Arial; font-weight: bold; color: white; text-align: center; background: -webkit-linear-gradient(black, white); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Login</p>
'''



custom_styles = """
<style>
/* Customize Streamlit Button */
div[data-testid="stButton"] button {
    background-color: #191970; /* Change button background color */
    color: white; /* Change button text color */
}

/* Customize Streamlit Text Input */
div[data-testid="stTextInput"] input {
    background-color: #000000; /* Change text input background color */
    color: #FFFFFF; /* Change text input text color */
    border-color: #FFFFFF; /* Change text input border color */
}

div[data-testid="stDateInput"] input {
    background-color: #000000; /* Change text input background color */
    color: #FFFFFF; /* Change text input text color */
    border-color: #FFFFFF; /* Change text input border color */
}

/* Customize Streamlit Select Box */
div[data-testid="stSelectbox"] > div > div {
    background-color: #000000; /* Change select box background color */
    color: #FFFFFF; /* Change select box text color */
    border-color: #FFFFFF; /* Change select box border color */
}

</style>
"""


