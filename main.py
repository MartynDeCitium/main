import streamlit as st
st.title("VSCode")
st.subheader("proga")
st.header("3141412")
st.text("rabotay")
st.markdown("**python**")
st.markdown("[Google](http://www.google.com)")
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

code="""
print("qwerty)
def funct():
      return 0;"""
st.code(code)