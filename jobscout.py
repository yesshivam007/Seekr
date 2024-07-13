import streamlit as st
from lists import *


"Information Technology (IT)",
"Healthcare",
"Finance & Banking",
"Marketing & Advertising",
"Sales",
"Education",
"Engineering",
"Manufacturing & Production",
"Construction",
"Human Resources",
"Legal",
"Media & Communications",
"Hospitality & Tourism",
"Real Estate",
"Transportation & Logistics",
"Arts & Design",
"Science & Research",
"Non-Profit & NGOs",
"Government & Public Administration"
def jobscout_input():
    col1, col2 = st.columns(2)
    with col1:
        sector = st.selectbox('Sector',sectors)
    with col2:
        if sector == "Information Technology (IT)":
            subsector = st.selectbox('Sub-Sector', IT_subsectors)
        elif sector == "Healthcare":
            subsector = st.selectbox('Sub-Sector', healthcare_subsectors)
        elif sector == "Finance & Banking":
            subsector = st.selectbox('Sub-Sector', finance_banking_subsectors)
        elif sector == "Marketing & Advertising":
            subsector = st.selectbox('Sub-Sector', marketing_advertising_subsectors)
        elif sector == "Sales":
            subsector = st.selectbox('Sub-Sector', sales_subsectors)
        elif sector == "Education":
            subsector = st.selectbox('Sub-Sector', education_subsectors)
        elif sector == "Engineering":
            subsector = st.selectbox('Sub-Sector', engineering_subsectors)
        elif sector == "Manufacturing & Production":
            subsector = st.selectbox('Sub-Sector', manufacturing_production_subsectors)
        elif sector == "Construction":
            subsector = st.selectbox('Sub-Sector', construction_subsectors)
        elif sector == "Human Resources":
            subsector = st.selectbox('Sub-Sector', human_resources_subsectors)
        elif sector == "Legal":
            subsector = st.selectbox('Sub-Sector', legal_subsectors)
        elif sector == "Media & Communications":
            subsector = st.selectbox('Sub-Sector', media_communications_subsectors)
        elif sector == "Hospitality & Tourism":
            subsector = st.selectbox('Sub-Sector', hospitality_tourism_subsectors)
        elif sector == "Real Estate":
            subsector = st.selectbox('Sub-Sector', real_estate_subsectors)
        elif sector == "Transportation & Logistics":
            subsector = st.selectbox('Sub-Sector', transportation_logistics_subsectors)
        elif sector == "Arts & Design":
            subsector = st.selectbox('Sub-Sector', arts_design_subsectors)
        elif sector == "Science & Research":
            subsector = st.selectbox('Sub-Sector', science_research_subsectors)
        elif sector == "Non-Profit & NGOs":
            subsector = st.selectbox('Sub-Sector', non_profit_ngos_subsectors)
        elif sector == "Government & Public Administration":
            subsector = st.selectbox('Sub-Sector', government_public_administration_subsectors)

    col1, col2 = st.columns(2)
    with col1:
        if subsector == "Software Development":
            job_role = st.selectbox('Job Role', IT_software_development)
        elif subsector == "Data Science & Analytics":
            job_role = st.selectbox('Job Role', IT_data_science_analytics)
        elif subsector == "Cybersecurity":
            job_role = st.selectbox('Job Role', IT_cybersecurity)
        elif subsector == "Cloud Computing":
            job_role = st.selectbox('Job Role', IT_cloud_computing)
        elif subsector == "Networking":
            job_role = st.selectbox('Job Role', IT_networking)
        elif subsector == "IT Support":
            job_role = st.selectbox('Job Role', IT_support)
        elif subsector == "Artificial Intelligence":
            job_role = st.selectbox('Job Role', IT_artificial_intelligence)
        elif subsector == "Database Management":
            job_role = st.selectbox('Job Role', IT_database_management)
        elif subsector == "Medical Practitioners":
            job_role = st.selectbox('Job Role', healthcare_medical_practitioners)
        elif subsector == "Nursing":
            job_role = st.selectbox('Job Role', healthcare_nursing)
        elif subsector == "Allied Health":
            job_role = st.selectbox('Job Role', healthcare_allied_health)
        elif subsector == "Healthcare Administration":
            job_role = st.selectbox('Job Role', healthcare_healthcare_administration)
        elif subsector == "Mental Health":
            job_role = st.selectbox('Job Role', healthcare_mental_health)
        elif subsector == "Accounting":
            job_role = st.selectbox('Job Role', finance_banking_accounting)
        elif subsector == "Banking":
            job_role = st.selectbox('Job Role', finance_banking_banking)
        elif subsector == "Financial Analysis":
            job_role = st.selectbox('Job Role', finance_banking_financial_analysis)
        elif subsector == "Insurance":
            job_role = st.selectbox('Job Role', finance_banking_insurance)
        elif subsector == "FinTech":
            job_role = st.selectbox('Job Role', finance_banking_fintech)
        elif subsector == "Digital Marketing":
            job_role = st.selectbox('Job Role', marketing_advertising_digital_marketing)
        elif subsector == "Market Research":
            job_role = st.selectbox('Job Role', marketing_advertising_market_research)
        elif subsector == "Creative Roles":
            job_role = st.selectbox('Job Role', marketing_advertising_creative_roles)
        elif subsector == "Advertising":
            job_role = st.selectbox('Job Role', marketing_advertising_advertising)
        elif subsector == "Sales Management":
            job_role = st.selectbox('Job Role', sales_sales_management)
        elif subsector == "Direct Sales":
            job_role = st.selectbox('Job Role', sales_direct_sales)
        elif subsector == "Retail":
            job_role = st.selectbox('Job Role', sales_retail)
        elif subsector == "Teaching":
            job_role = st.selectbox('Job Role', education_teaching)
        elif subsector == "Educational Administration":
            job_role = st.selectbox('Job Role', education_educational_administration)
        elif subsector == "Support Roles":
            job_role = st.selectbox('Job Role', education_support_roles)
        elif subsector == "Civil Engineering":
            job_role = st.selectbox('Job Role', engineering_civil_engineering)
        elif subsector == "Mechanical Engineering":
            job_role = st.selectbox('Job Role', engineering_mechanical_engineering)
        elif subsector == "Electrical Engineering":
            job_role = st.selectbox('Job Role', engineering_electrical_engineering)
        elif subsector == "Chemical Engineering":
            job_role = st.selectbox('Job Role', engineering_chemical_engineering)
        elif subsector == "Software Engineering":
            job_role = st.selectbox('Job Role', engineering_software_engineering)
        elif subsector == "Production Management":
            job_role = st.selectbox('Job Role', manufacturing_production_production_management)
        elif subsector == "Quality Control":
            job_role = st.selectbox('Job Role', manufacturing_production_quality_control)
        elif subsector == "Operations":
            job_role = st.selectbox('Job Role', manufacturing_production_operations)
        elif subsector == "Construction Management":
            job_role = st.selectbox('Job Role', construction_construction_management)
        elif subsector == "Skilled Trades":
            job_role = st.selectbox('Job Role', construction_skilled_trades)
        elif subsector == "Architecture":
            job_role = st.selectbox('Job Role', construction_architecture)
        elif subsector == "Recruitment":
            job_role = st.selectbox('Job Role', human_resources_recruitment)
        elif subsector == "Employee Relations":
            job_role = st.selectbox('Job Role', human_resources_employee_relations)
        elif subsector == "Compensation & Benefits":
            job_role = st.selectbox('Job Role', human_resources_compensation_benefits)
        elif subsector == "Lawyers":
            job_role = st.selectbox('Job Role', legal_lawyers)
        elif subsector == "Paralegals & Legal Assistants":
            job_role = st.selectbox('Job Role', legal_paralegals_legal_assistants)
        elif subsector == "Judiciary":
            job_role = st.selectbox('Job Role', legal_judiciary)
        elif subsector == "Journalism":
            job_role = st.selectbox('Job Role', media_communications_journalism)
        elif subsector == "Public Relations":
            job_role = st.selectbox('Job Role', media_communications_public_relations)
        elif subsector == "Broadcasting":
            job_role = st.selectbox('Job Role', media_communications_broadcasting)
        elif subsector == "Hotel Management":
            job_role = st.selectbox('Job Role', hospitality_tourism_hotel_management)
        elif subsector == "Travel & Tourism":
            job_role = st.selectbox('Job Role', hospitality_tourism_travel_tourism)
        elif subsector == "Food & Beverage":
            job_role = st.selectbox('Job Role', hospitality_tourism_food_beverage)
        elif subsector == "Fine Arts":
            job_role = st.selectbox('Job Role', arts_design_fine_arts)
        elif subsector == "Graphic Design":
            job_role = st.selectbox('Job Role', arts_design_graphic_design)
        elif subsector == "Performing Arts":
            job_role = st.selectbox('Job Role', arts_design_performing_arts)
        elif subsector == "Property Management":
            job_role = st.selectbox('Job Role', real_estate_property_management)
        elif subsector == "Development":
            job_role = st.selectbox('Job Role', real_estate_development)
        elif subsector == "Transportation Management":
            job_role = st.selectbox('Job Role', transportation_logistics_transportation_management)
        elif subsector == "Supply Chain":
            job_role = st.selectbox('Job Role', transportation_logistics_supply_chain)
        elif subsector == "Warehouse Operations":
            job_role = st.selectbox('Job Role', transportation_logistics_warehouse_operations)
        elif subsector == "Life Sciences":
            job_role = st.selectbox('Job Role', science_research_life_sciences)
        elif subsector == "Physical Sciences":
            job_role = st.selectbox('Job Role', science_research_physical_sciences)
        elif subsector == "Research & Development":
            job_role = st.selectbox('Job Role', science_research_research_development)
        elif subsector == "Program Management":
            job_role = st.selectbox('Job Role', non_profit_ngos_program_management)
        elif subsector == "Fundraising":
            job_role = st.selectbox('Job Role', non_profit_ngos_fundraising)
        elif subsector == "Advocacy":
            job_role = st.selectbox('Job Role', non_profit_ngos_advocacy)
        elif subsector == "Public Policy":
            job_role = st.selectbox('Job Role', government_public_administration_public_policy)
        elif subsector == "Public Administration":
            job_role = st.selectbox('Job Role', government_public_administration_public_administration)
        elif subsector == "Law Enforcement":
            job_role = st.selectbox('Job Role', government_public_administration_law_enforcement)

    with col2:
        opportunity_type = st.radio('Seeking', ['Job', 'Internship'], horizontal=True)
    
    return None