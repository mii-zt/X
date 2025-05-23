import streamlit as st
from PIL import Image
from io import BytesIO

if 'posts' not in st.session_state:
    st.session_state.posts=[]

st.title('X模倣版') #アプリのタイトル

with st.form(key="post_form",clear_on_submit=True):
    st.session_state.post_text=st.text_input('投稿内容の入力') #テキストの入力
    st.session_state.post_image=st.file_uploader('画像を選択してください',type=['jpg','jpeg','png']) #画像の選択
    submitted=st.form_submit_button('投稿')


#投稿内容の表示と警告
if submitted:
    if st.session_state.post_text:
        st.success('投稿完了')
        image=None
        if st.session_state.post_image:
            image=st.session_state.post_image.getvalue()
        st.session_state.posts.append({ #同一のリストに文字と画像を保存
            'text':st.session_state.post_text,
            'image':image
            })

    else:
        st.warning('投稿内容を入力してください')


for post in reversed(st.session_state.posts): #新しい順で表示
    st.text_area('投稿内容',post['text'],height=100)
    if post['image']:
        image=Image.open(BytesIO(post['image']))
        st.image(image,caption='投稿画像',use_column_width=True)
