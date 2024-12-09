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


#if st.sidebar.button('click me too'):
#  st.info('You clicked at: {}'.format(datetime.datetime.now()))

#get the id of the menu item clicked
#st.info(f"{menu_id}")



ledinfo, journal_type, journal_date, journal_ccy  = st.columns(4)

def menu():

    @st.dialog("Select Information: ")
    def vote():
        # st.write(f"Why is {item} your favorite?")
        ledger = st.selectbox("Select Ledger:", ("L_TFIS_UK_TB", "L_TT_UK_TB", "L_NORWAY", "L_TYCO_HOLDINGS_UK"))
        period = st.selectbox("Select Period:", ("Oct-24", "Nov-24", "Dec-24", "Jan-25"))
        Journal_Type = st.selectbox("Journal Type:", ("Reversal", "Non-Reversal"))
        Journal_Name = st.text_input("Enter Journal Name")
        Journal_Category = st.selectbox("Journal Category:", ("Reclass", "Adjustment", "Provision", "Accrual"))

        if st.button("Submit"):
            st.session_state.vote = {"ledger": ledger, "period": period}
            st.rerun()

    with st.sidebar:
        selected = option_menu("Navigation", ["Ledger", 'Period', 'Journal_Type', 'Journal_Name', 'Journal_Category'],
                               icons=['house', 'gear', 'gear', 'gear', 'gear'], menu_icon="cast", default_index=0)

    if "vote" not in st.session_state:
        # st.write("Vote for your favorite")
        if selected == "Ledger":
            vote()
        elif selected == "Period":
            vote()
        elif selected == "Journal_Type":
            vote()
        elif selected == "Journal_Name":
            vote()
        elif selected == "Journal_Category":
            vote()


    with ledinfo:
        global comp_code
        st.info(f"Company Code: FSYS")
        st.info(f"Journal Type: Reversal")
    with journal_type:
        global comp_name
        comp_name = st.info(f"Company Name: TFIS_UK")
        st.info(f"Category: Reclass")
    with journal_date:
        st.info("Batch Reference: Auto")
        st.info("Net PL Impact: $100.00")
    with journal_ccy:
        st.info(f"Journal Name: Provision_Reclas")
        st.info("Transction Date: 11-30-2024")

    fn = "C:/Users/jshar32/OneDrive - Johnson Controls/Files/Process Improvement/Iscala UBR/MJE_Sample.xlsx"
    df1 = pd.read_excel(fn)
    df1 = pd.DataFrame(df1)
    df1['Loc'] = df1['Loc'].astype(str)
    df1['Acc'] = df1['Acc'].astype(str)
    st.dataframe(df1, use_container_width=True, hide_index=True)

def menu_adv():
    with st.sidebar:
        selected = option_menu("Navigation", ["Ledger", 'Period'],
                               icons=['house', 'gear'], menu_icon="cast", default_index=0)

    @st.dialog("Select Information: ")
    def vote(item):
        # st.write(f"Why is {item} your favorite?")
        ledger = st.selectbox("Select Ledger:", ("L_TFIS_UK_TB", "L_TT_UK_TB", "L_NORWAY", "L_TYCO_HOLDINGS_UK"))
        period = st.selectbox("Select Period:", ("Oct-24", "Nov-24", "Dec-24", "Jan-25"))
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "ledger": ledger, "period": period}
            st.rerun()

    if "vote" not in st.session_state:
        # st.write("Vote for your favorite")
        if selected == "Ledger":
            vote("A")
        elif selected == "Period":
            vote("B")

    with st.sidebar.popover("Select Options"):
        Journal_Type = st.selectbox("Journal Type:", ("Reversal", "Non-Reversal"))
        Journal_Name = st.text_input("Enter Journal Name")
        Journal_Category = st.selectbox("Journal Category:", ("Reclass", "Adjustment", "Provision", "Accrual"))
    with ledinfo:
        st.info("Company Code: FSYS")
        st.info(f"Journal Type: Reversal")
        st.info("Transction Date: 11-30-2024")
        st.info("Currency: GBP")
    with journal_type:
        st.info("Company Name: Tyco Fire Integreted Solutions")
        st.info(f"Category: Reclass")
        st.info("Month-End Date: Nov-24")
        st.info("Exchange Rate: 1.2993")
    with journal_date:
        st.info("Batch Reference: Auto")
        st.info("Balance Type: Actual")
        st.info("Reversal Year: 2024")
        st.info("Reporting Rate: USD")
    with journal_ccy:
        st.info(f"Journal Name: Provision_Reclas")
        st.info("Net PL Impact: $100.00")
        st.info("Reversal Month: 11")
        st.info("User: JSHAR32")
    fn = "C:/Users/jshar32/OneDrive - Johnson Controls/Files/Process Improvement/Iscala UBR/MJE_Sample.xlsx"
    df1 = pd.read_excel(fn)
    df1 = pd.DataFrame(df1)
    df1['Loc'] = df1['Loc'].astype(str)
    df1['Acc'] = df1['Acc'].astype(str)
    st.dataframe(df1, use_container_width=True, hide_index=True)


on = st.toggle("Advanced Values")

if menu_id == 'subid11':
    if on:
        menu_adv()
    else:
        menu()
