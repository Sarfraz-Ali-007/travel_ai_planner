import streamlit as st
from utils.chain import generate_plan

st.set_page_config(page_title="AI Travel Planner", page_icon="🧳")

st.title("🧳 AI Travel Planner")
st.write("Plan your perfect trip with AI")

# Inputs
destination = st.text_input("Destination (e.g. Dubai, Paris, Karachi)")
budget = st.text_input("Budget (e.g. 500 USD or 150000 PKR)")
days = st.number_input("Number of Days", min_value=1, max_value=30)
travel_type = st.selectbox(
    "Travel Type",
    ["Solo", "Family", "Adventure", "Luxury", "Budget"]
)

# Button
if st.button("Generate Travel Plan"):
    if destination:
        with st.spinner("Planning your trip..."):
            result = generate_plan(destination, budget, days, travel_type)

        st.success("Your Travel Plan is Ready!")

        st.markdown("## 🧠 AI Travel Plan")
        st.write(result)
    else:
        st.warning("Please enter destination")

st.markdown("---")
st.caption("⚠️ AI-generated plan. Always verify local travel conditions.")