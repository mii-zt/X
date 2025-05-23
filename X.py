import streamlit as st

st.title('X模倣版') #アプリのタイトル

post=st.text_input('投稿内容の入力') #テキストの入力

#投稿内容の表示と警告
if st.button('投稿'):
    if post:
        st.success('投稿完了')
        st.text_area('投稿内容',post)
    else:
        st.warning('投稿内容を入力してください')

