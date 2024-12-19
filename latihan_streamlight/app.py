import streamlit as st

#st.title('hallo mabro')
#st.markdown('selamat datang di rumah coding')
#st.image('download.jpeg', caption='ini gambarnya')

dashboard = st.Page('./fitur/dashboard.py', title ='dashboard')
nabung = st.Page('./fitur/nabung.py', title ='menabung')

pg = st.navigation(
    {
    'menu utama' :[dashboard],
    'transaksi': [nabung],
    
     }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua']=[]
pg.run()