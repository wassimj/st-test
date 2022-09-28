import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

from topologicpy import topologic as tp

v = tp.Vertex.ByCoordinates(0,0,0)
st.write(v)