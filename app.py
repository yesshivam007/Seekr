# Imports
import streamlit as st
from streamlit_navigation_bar import st_navbar
import json
from func import pdf_to_text, get_scores, get_report, get_cover_letter, jobscout_input
from lists import *


# Page Setup: Configure, Navbar, Title
st.set_page_config(
    page_title='Seekr',
    page_icon= 'res/logo.svg',
    layout='wide',
)

navbar = st_navbar(
    ['FitCheck', 'CoverCraft', 'Compare Ideal', 'JobScout'],
    logo_path='res/logo.svg', 
    logo_page='Home')

st.title('Seekr: Your Next Job, Simplified')


# Data
with open('data/data.txt', 'r') as file:
    data = json.load(file)
    data_saved = data['data_saved']
    resume = data['resume']
    job_description = data['job_description']
    company_name = data['company_name']
    position_name = data['position_name']
    type = data['type']

# Outputs
with open('data/outputs.txt', 'r') as file:
    output_data = json.load(file)
    clarity_score = output_data['clarity_score']
    ATS_score = output_data['ATS_score']
    selection_chances = output_data['selection_chances']
    report = output_data['report']
    cover_letter = output_data['cover_letter']

# Job Scout Data
with open('data/jobscout_data.txt', 'r') as file:
    jobscout_data = json.load(file)

    sector = jobscout_data['sector']
    subsector = jobscout_data['subsector']
    job_role = jobscout_data['job_role']
    opportunity_type = jobscout_data['opportunity_type']

# Main Inputs
def main_inputs():
    resume = st.file_uploader('Resume', type='pdf')
    job_description = st.text_area('Job Description')
    col1, col2, col3 = st.columns(3)
    with col1:
        company_name = st.text_input('Company Name')
    with col2:
        position_name = st.text_input('Position Name')
    with col3:
        type = st.radio('Position', ['Job', 'Internship'], horizontal=True)


    # Save Data
    col1, col2, col3 = st.columns(3)
    with col2:
        col1, col2, col3 = st.columns(3)
        with col2:
            button = st.button('Save Data')

    if button:
        progress_bar = st.progress(50)
        resume = pdf_to_text(resume)
        progress_bar.progress(100)

        data = {
                'data_saved': 'True',
                'resume': resume,
                'job_description': job_description,
                'company_name': company_name,
                'position_name': position_name,
                'type': type
                }
        
        with open('data/data.txt', 'w') as file:
            json.dump(data, file)
    
    return None

# Dislay FitCheck Function
def display_output(clarity_score, ATS_score, selection_chances, report):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Clarity')
        st.title(clarity_score)

    with col2:
        st.header('ATS Compatibility')
        st.title(ATS_score)

    with col3:
        st.header('Selection Chances')
        st.title(f'{selection_chances}%')

    st.write(report)

    return None 
   
# FitCheck
def resume_report(resume, job_description, type):

    global clarity_score
    global ATS_score
    global selection_chances
    global report

    col1, col2, col3 = st.columns(3)
    with col2:
        col1, col2, col3 = st.columns(3)
        with col2:
            button = st.button('Generate Report')
    
    if button:
        progress_bar = st.progress(33)

        clarity_score, ATS_score, selection_chances = get_scores(resume, job_description, type)
        progress_bar.progress(66)
        report = get_report(resume, job_description, type)
        progress_bar.progress(100)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header('Clarity')
            st.title(clarity_score)

        with col2:
            st.header('ATS Compatibility')
            st.title(ATS_score)

        with col3:
            st.header('Selection Chances')
            st.title(f'{selection_chances}%')

        st.write(report)

        output_data = {
                    "clarity_score":clarity_score, 
                    "ATS_score":ATS_score,
                    "selection_chances":selection_chances,
                    "report":report,
                    "cover_letter":""
                    }
        
        with open('data/outputs.txt', 'w') as file:
            json.dump(output_data, file)
    
    return None

# CoverCraft
def cover_page(resume, job_description, type, company_name, position_name):

    global cover_letter

    col1, col2, col3 = st.columns(3)
    with col2:
        col1, col2, col3 = st.columns(3)
        with col2:
            button = st.button('Generate Letter')
    
    if button:
        progress_bar = st.progress(50)

        cover_letter = get_cover_letter(resume, job_description, type, position_name, company_name)
        progress_bar.progress(100)

        output_data = {
                    "clarity_score":clarity_score, 
                    "ATS_score":ATS_score,
                    "selection_chances":selection_chances,
                    "report":report,
                    "cover_letter":cover_letter
                    }
        
        with open('data/outputs.txt', 'w') as file:
            json.dump(output_data, file)

        st.write(cover_letter)

    return None
    
# Navbar Routing
if navbar == 'Home':
    if resume != "" and job_description != "":
        st.warning("Data saved, to upload new data click below", icon='⚠️')
        col1, col2, col3 = st.columns(3)
        with col2:
            col1, col2, col3 = st.columns(3)
            with col2:
                button = st.button('New Data')
        if button:
            data = {
                "data_saved": "False", 
                "resume":"", 
                "job_description": "", 
                "company_name": "", 
                "position_name": "", 
                "type": ""
            }

            with open('data/data.txt', 'w') as file:
                json.dump(data, file)

            main_inputs()
    elif resume == "" and job_description =="":
        main_inputs()

elif navbar == 'FitCheck':
    if data_saved == 'False':
        st.warning('First upload and save data in "Home" section', icon='⚠️')
    elif data_saved == 'True':
        if clarity_score != '' and ATS_score != '':
            st.warning('To generate new FitCheck, upload new data in "Home" section', icon='⚠️')
            display_output(clarity_score, ATS_score, selection_chances, report)
        elif clarity_score == '' and ATS_score == '':
            resume_report(resume, job_description, type)

elif navbar == 'CoverCraft':
    if data_saved == 'False':
        st.warning('First upload and save data in "Home" section', icon='⚠️')
    elif data_saved == 'True':
        if cover_letter != '':
            st.warning('To generate new CoverCraft, upload new data in "Home" section', icon='⚠️')
            st.write(cover_letter)
        elif cover_letter == '': 
            cover_page(resume, job_description, type, company_name, position_name)

elif navbar == 'Compare Ideal Resumes':
    st.warning('This section is under developement and not published yet!', icon='⚠️')

elif navbar == 'JobScout':
    if opportunity_type !="" and subsector != '':

        st.write(f"""
                Sector: {sector} \n
                Subsector: {subsector} \n
                Job Role: {job_role} \n
                Seeking: {opportunity_type} \n
                 """)
        
        st.warning('Data already taken, to choose new click below', icon='⚠️')
        col1, col2, col3 = st.columns(3)
        with col2:
            col1, col2, col3 = st.columns(3)
            with col2:
                button = st.button('New Data')
        
        if button:
            jobscout_data = {
                "sector": "",
                "subsector": "",
                "job_role": "",
                "opportunity_type": ""
            }

            with open('data/jobscout_data.txt', 'w') as file:
                json.dump(jobscout_data, file)

            jobscout_input()

    elif opportunity_type =="" and subsector == '':
        jobscout_input()




