import streamlit as st

# Set up the layout
st.title("Dollar Gap + Leverage Calculator")

# User inputs
risk = st.number_input("Enter the amount you want to risk ($):", value=50.00, format="%.2f")
trade_direction = st.selectbox("Choose the trade direction:", ["LONG", "SHORT"])
risk_to_reward = st.number_input("Enter your risk to reward ratio:", value=1.00, format="%.2f")
entry_price = st.number_input("Enter the entry price ($):", value=2.63, format="%.2f")
stop_price = st.number_input("Enter the stop price ($):", value=2.50, format="%.2f")
leverage = st.number_input("Enter the amount of leverage (enter '1' if not using leverage):", value=20, format="%.2f")

# Button to perform calculation
if st.button('Calculate'):
    price_difference = abs(entry_price - stop_price)
    lot_size = risk / price_difference
    if trade_direction == "LONG":
        take_profit_price = entry_price + (price_difference * risk_to_reward)
    else:
        take_profit_price = entry_price - (price_difference * risk_to_reward)

    actual_trade_cost = lot_size * entry_price
    min_equity_required = actual_trade_cost / leverage

    st.write(f"LOT SIZE: {lot_size:.2f}")
    st.write(f"TAKE PROFIT PRICE: {take_profit_price:.2f}")
    st.write(f"ACTUAL TRADE COST: ${actual_trade_cost:.2f}")
    st.write(f"MIN. EQUITY REQUIRED: ${min_equity_required:.2f}")
