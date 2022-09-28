import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

import topologic

v = topologic.Vertex.ByCoordinates(0,0,0)
st.write(v)