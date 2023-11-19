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
background-image: url("https://images.unsplash.com/photo-1695569292033-95db9ad99cf8?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''

title = '''
<h1 style="color: orange;">Hello World</h1>
'''

login = '''
<p style="font: 55px Arial; font-weight: bold; text-shadow: 3px 3px DeepSkyBlue; color: white;">Login</p>
'''

attendance = '''
<p style="font: 55px Arial; font-weight: bold; text-shadow: 3px 3px DeepSkyBlue; color: white;">Attendance Tracking</p>
'''

rainbow_divider = '''
<div style="height: 4px; background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);"></div>
'''

# additional background images
# https://images.unsplash.com/photo-1697899001862-59699946ea29?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D