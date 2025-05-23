import streamlit as st
from PIL import Image
from io import BytesIO

if 'posts' not in st.session_state:
    st.session_state.posts=[]

st.title('X模倣版') #アプリのタイトル

post=st.text_input('投稿内容の入力') #テキストの入力
upload_file=st.file_uploader('画像を選択してください',type=['jpg','jpeg','png']) #画像の選択


#投稿内容の表示と警告
if st.button('投稿'):
    if post:
        st.success('投稿完了')
        image=None
        if upload_file:
            image=upload_file.getvalue()
        st.session_state.posts.append({ #同一のリストに文字と画像を保存
            'text':post,
            'image':image
            })    
    else:
        st.warning('投稿内容を入力してください')


for post in reversed(st.session_state.posts): #新しい順で表示
    st.text_area('投稿内容',post['text'],height=100)
    if post['image']:
        image=Image.open(BytesIO(post['image']))
        st.image(image,caption='投稿画像',use_column_width=True)
