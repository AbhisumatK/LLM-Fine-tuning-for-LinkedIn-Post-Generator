import streamlit as st
from few_shot_learning import Few_Shot_posts
from post_gen import post_generator

def main():
    st.title("LinkedIn Post Generator")
    col1, col2 = st.columns(2)
    f = Few_Shot_posts()
    with col1:
        tag_ = st.selectbox("Title", f.get_tags())

    with col2:
        length_ = st.selectbox("Length", ["Short", "Medium", "Long"])

    if st.button("Generate"):
        with st.spinner("Generating post..."):
            post = post_generator(tag_, length_)
        st.write(post)


if __name__ == "__main__":
    main()