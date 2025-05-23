import streamlit as st
from PIL import Image

if 'posts' not in st.session_state:
    st.session_state.posts=[]
if 'images' not in st.session_state:
    st.session_state.posts=[]

st.title('X模倣版') #アプリのタイトル

post=st.text_input('投稿内容の入力') #テキストの入力
upload_file=st.file_uploader('画像を選択してください',type=['jpg','jpeg','png']) #画像の選択


#投稿内容の表示と警告
if st.button('投稿'):
    if post:
        st.success('投稿完了')
        st.session_state.posts.append(post)
        if upload_file:
            image=Image.open(upload_file)
            st.session_state.posts.append(image)
            st.image(image,caption="アップロードされた画像",use_column_width=True)
    else:
        st.warning('投稿内容を入力してください')

for post in st.session_state.posts:
    st.text_area('投稿内容',post)
