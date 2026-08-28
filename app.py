import streamlit as st

st.set_page_config(
    page_title="AI Financial Control",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Financial Control")
st.subheader("Smart control of your personal finances")

# Sidebar
st.sidebar.header("Financial Information")

income = st.sidebar.number_input(
    "Monthly Income (₹)",
    min_value=0,
    value=50000,
    step=1000
)

budget = st.sidebar.number_input(
    "Monthly Expense Budget (₹)",
    min_value=0,
    value=30000,
    step=1000
)

expenses = st.sidebar.number_input(
    "Current Expenses (₹)",
    min_value=0,
    value=18000,
    step=500
)

# Calculations
remaining = income - expenses
budget_used = (expenses / budget) * 100 if budget > 0 else 0

# Dashboard
st.markdown("## 📊 Financial Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("💵 Income", f"₹{income:,.0f}")
col2.metric("💸 Expenses", f"₹{expenses:,.0f}")
col3.metric("💰 Remaining", f"₹{remaining:,.0f}")

if budget_used >= 90:
    risk = "🔴 HIGH"
elif budget_used >= 70:
    risk = "🟠 MEDIUM"
else:
    risk = "🟢 LOW"

col4.metric("⚠️ Risk Level", risk)

st.divider()

# Budget
st.markdown("## 📈 Budget Control")

st.write(f"Budget used: **{budget_used:.1f}%**")

st.progress(min(budget_used / 100, 1.0))

# AI recommendations
st.markdown("## 🤖 AI Financial Control")

if budget_used >= 90:
    st.error(
        "⚠️ Warning: You are close to exceeding your monthly budget. "
        "Reduce unnecessary spending."
    )
elif budget_used >= 70:
    st.warning(
        "⚠️ Your spending is increasing. "
        "Try to control non-essential expenses."
    )
else:
    st.success(
        "✅ Your spending is currently under control."
    )

# Savings
st.markdown("## 🎯 Savings Recommendation")

if remaining > 0:
    recommended_saving = remaining * 0.5

    st.info(
        f"Based on your current finances, you could consider saving "
        f"around **₹{recommended_saving:,.0f}** this month."
    )
else:
    st.error("Your expenses are higher than your income.")

# AI question
st.markdown("## 💬 Ask AI Financial Controller")

question = st.text_input(
    "Ask a financial question",
    placeholder="Example: Can I spend ₹5000?"
)

if question:

    if "5000" in question:
        if remaining >= 5000:
            st.success(
                "✅ Yes. Based on the current information, "
                "you can afford ₹5,000."
            )
        else:
            st.error(
                "❌ I recommend avoiding this expense because "
                "your remaining balance is too low."
            )
    else:
        st.info(
            "I can help analyze your budget, spending and savings."
        )

st.divider()

st.caption(
    "AI Financial Control • Hackathon Prototype"
)
