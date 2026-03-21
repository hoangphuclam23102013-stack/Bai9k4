
import streamlit as st
st.set_page_config(page_title="Thu vien dong vat", page_icon=":question:", layout='wide')
st.title('Thu vien dong vat')
st.write('Hay chon 1 con vat, toi se hien thi thong tin con vat')
Tinh_cach = {
    'con meo': ['https://tiengdong.com/wp-content/uploads/Tieng-meo-keu-www_tiengdong_com.mp3', 'https://hoanghamobile.com/tin-tuc/wp-content/uploads/2024/08/anh-con-meo-cute.jpg', 'https://www.tiktok.com/@3conmeota/video/7503908811447471367'],
    'con cho':['https://tiengdong.com/wp-content/uploads/Tieng-cho-sua-www_tiengdong_com.mp3', 'https://img.tripi.vn/cdn-cgi/image/width=700,height=700/https://gcs.tripi.vn/public-tripi/tripi-feed/img/482759ycb/anh-mo-ta.png', 'https://www.youtube.com/watch?v=GuS4-F7zGkI']}
cols = st.columns(len(Tinh_cach))
chon = None
for i, (con_vat, tinh_cach) in enumerate(Tinh_cach.items()):
    with cols[i]:
        if cols[i].button(con_vat):
            chon = con_vat
if chon:
    with st.expander(chon):
         st.write('Am thanh: ')
         st.audio(Tinh_cach[chon][0], format = 'audio/mp3')
         st.write('Hinh anh: ')
         st.image(Tinh_cach[chon][1])
         st.write('Video: ')
         st.video(Tinh_cach[chon][2], format = 'video/mp4')
