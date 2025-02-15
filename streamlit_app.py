import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])
st.write(os.environ["db_username"])
# And the root-level secrets are also accessible as environment variables:

import os
st.write(
	"Has environment variables been set:",
	os.environ["db_username"] == st.secrets["db_username"])
