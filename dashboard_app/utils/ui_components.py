import streamlit as st

def section_header(number, text):
    '''
    Creates a section header with a number in a green circle and text with a horizontal line.
    '''
    st.html(f"""
    <style>
        .section-row {{
            display: flex;
            align-items: center;
            margin-top: 30px;
            margin-bottom: 5px;
        }}
        .section-number {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 12px;
        }}
        .section-text {{
            font-size: 20px;
            font-weight: 600;
            white-space: nowrap;
        }}
        .section-line {{
            border-bottom: 1px solid #4CAF5022;
            flex-grow: 1;
            margin-left: 12px;
        }}
    </style>

    <div class="section-row">
        <div class="section-number">{number}</div>
        <div class="section-text">{text}</div>
        <div class="section-line"></div>
    </div>
    """)