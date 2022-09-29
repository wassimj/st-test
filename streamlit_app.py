import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

from topologicpy import topologic

v1 = topologic.Vertex.ByCoordinates(0,0,0)
v2 = topologic.Vertex.ByCoordinates(10,10,10)
e1 = topologic.Edge.ByStartVertexEndVertex(v1, v2)
c1 = e1.Centroid()
st.write(c1.X(), c1.Y(), c1.Z())

