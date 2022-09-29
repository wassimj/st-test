import streamlit as st

st.title('🎈 TopologicPy is on PyPI!')

from topologicpy import topologic

st.write("v1 = topologic.Vertex.ByCoordinates(0,0,0)")
st.write("v2 = topologic.Vertex.ByCoordinates(10,10,10)")
st.write("e1 = topologic.Edge.ByStartVertexEndVertex(v1, v2)")
st.write("c1 = e1.Centroid()")
st.write("st.write(c1.X(), c1.Y(), c1.Z())")
v1 = topologic.Vertex.ByCoordinates(0,0,0)
v2 = topologic.Vertex.ByCoordinates(10,10,10)
e1 = topologic.Edge.ByStartVertexEndVertex(v1, v2)
c1 = e1.Centroid()
st.write(c1.X(), c1.Y(), c1.Z())

