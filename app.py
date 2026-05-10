"""

Name: Hernan Ramoz

Course: ADD 100

Project: Finance Flow (Improved Version)

Description:

This improved web app helps users understand their monthly finances.

It includes better instructions, formatted results, personalized advice,

and a savings and investment suggestion.

"""

import streamlit as st

WELCOME_MESSAGE = "Finance Flow 💰"

PROGRAM_MESSAGE = "Enter your monthly financial information below to see how much money you have left."

def calculate_balance(income, expenses, debt):

    return income - expenses - debt

def format_currency(amount):

    return "${:,.2f}".format(amount)

def show_summary(balance):

    st.subheader("📊 Financial Summary")

    formatted_balance = format_currency(balance)

    st.write("💵 Money left after expenses and debt:", formatted_balance)

    if balance < 0:

        st.error("⚠️ You are spending more than you earn.")

        st.write("👉 Advice: Try to reduce expenses or increase your income before saving or investing.")

    elif balance == 0:

        st.warning("⚠️ You have no money left this month.")

        st.write("👉 Advice: Try to reduce small expenses so you can start saving money.")

    else:

        st.success("✅ Good job! You still have money left.")

        st.write("👉 Advice: You can save or invest your extra money.")

        st.subheader("🏦 Savings and Investment Suggestion")

        savings = balance * 0.30

        investment = balance * 0.20

        emergency_money = balance * 0.50

        st.write("💵 Suggested savings:", format_currency(savings))

        st.write("📈 Suggested investment:", format_currency(investment))

        st.write("🛡️ Emergency / extra money:", format_currency(emergency_money))

        st.info("Tip: Saving and investing can help you build a better financial future.")

        progress_value = min(balance / 5000, 1.0)

        st.progress(progress_value)

def main():

    st.set_page_config(

        page_title="Finance Flow",

        page_icon="💰",

        layout="centered"

    )

    st.title(WELCOME_MESSAGE)

    st.write(PROGRAM_MESSAGE)

    st.markdown("""

    ### 🧾 Instructions

    - Enter your *monthly income*

    - Enter your *total monthly expenses*

    - Enter your *monthly debt payments*

    - Click *Calculate My Balance* to see your result

    """)

    st.divider()

    st.subheader("💼 Enter Your Financial Data")

    income = st.number_input("💰 Monthly Income ($):", min_value=0.0, step=100.0)

    expenses = st.number_input("🧾 Monthly Expenses ($):", min_value=0.0, step=100.0)

    debt = st.number_input("💳 Monthly Debt Payments ($):", min_value=0.0, step=50.0)

    st.divider()

    if st.button("📊 Calculate My Balance"):

        balance = calculate_balance(income, expenses, debt)

        show_summary(balance)

        st.info("ℹ️ Note: This app gives a simple estimate of your finances.")

main()