import streamlit as st
import pandas as pd
import hydralit_components as hc
from streamlit_option_menu import option_menu
from streamlit_extras.dataframe_explorer import dataframe_explorer

#make it look nice from the start
st.set_page_config(layout='wide', initial_sidebar_state='collapsed',)

# specify the primary menu definition
menu_data = [
    {'icon': "fa-solid fa-radar", 'label': "General Ledger",
     'submenu': [{'id': 'subid11', 'icon': "fa fa-paperclip", 'label': "New Journal"},
                 {'id': 'subid12', 'icon': "far fa-chart-bar", 'label': "Approve Journal"},
                 {'id': 'subid13', 'icon': "fa fa-database", 'label': "Enquire Transaction"}]},

    {'icon': "fa-solid fa-radar", 'label': "Sub Ledgers",
     'submenu': [{'id': 'subid14', 'icon': "fa fa-paperclip", 'label': "Accounts Receivable"},
                 {'id': 'subid15', 'icon': "far fa-chart-bar", 'label': "Accounts Payable"},
                 {'id': 'subid16', 'icon': "far fa-chart-bar", 'label': "Inter Company"},
                 {'id': 'subid17', 'icon': "far fa-chart-bar", 'label': "Accounts Payable"},
                 {'id': 'subid18', 'icon': "far fa-chart-bar", 'label': "Payroll"},
                 {'id': 'subid19', 'icon': "fa fa-database", 'label': "Inventory"}]},


    {'icon': "far fa-chart-bar", 'label':"Reports"},#no tooltip message
    {'id':' Crazy return value 💀','icon': "far fa-chart-bar", 'label':"Analytics"},
    {'icon': "fas fa-tachometer-alt", 'label':"Reconciliation", 'ttip':"Reconciliation Module"}, #can add a tooltip message
    {'icon': "far fa-copy", 'label':"Setup"},
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=False, #at the top or not
    sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
)
