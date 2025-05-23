import streamlit as st
from PIL import Image
from io import BytesIO
from datetime import datetime

#CSSファイルの読み込み
def local_css(fname):
    with open(fname) as f:
        css=f.read()
        st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)

local_css("form.css")

if 'posts' not in st.session_state:
    st.session_state.posts=[]

st.title('X模倣版') #アプリのタイトル

with st.form(key="post_form",clear_on_submit=True):
    post_text=st.text_input('投稿内容の入力') #テキストの入力
    post_image=st.file_uploader('画像を選択してください',type=['jpg','jpeg','png']) #画像の選択
    submitted=st.form_submit_button('投稿')


#投稿内容の表示と警告
if submitted:
    if post_text or post_image:
        st.success('投稿完了')
        image=None
        if post_image:
            image=post_image.getvalue()
        st.session_state.posts.append({ #同一のリストに文字と画像を保存
            'text':post_text,
            'image':image,
            'time':datetime.now().strftime('%Y-%m-%d %H:%M:%S') #投稿時間の記録
            })

    else:
        st.warning('投稿内容を入力してください')


for post in reversed(st.session_state.posts): #新しい順で表示
    if post["text"]:
        st.text("投稿内容")
        st.markdown(f'<div class="post_text">{post["text"]}</div>',unsafe_allow_html=True)
    if post['image']:
        image=Image.open(BytesIO(post['image']))
        st.image(image,caption='投稿画像',use_column_width=True)
    st.markdown(f'<div class="timestamp">🕒 {post["time"]}</div>',unsafe_allow_html=True)
