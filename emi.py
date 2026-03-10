# importing Libraries used to run the program
import streamlit as st
import matplotlib.pyplot as plt

# design
st.title("EMI Calculator of 🏠Home/🚗Car Loan & 🧮 FD Return calculator")

st.subheader("Select what type of analysis you want to do here")

# initializing session state
if "selected" not in st.session_state:
    st.session_state.selected = None

# creating selection buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Home/Car Loan 🚗", use_container_width=True):
        st.session_state.selected = "loan"
with col2:
    if st.button("🧮 FD Return calculator", use_container_width=True):
        st.session_state.selected = "fd"

# Loan Calculator Section
if st.session_state.selected == "loan":
    P = st.number_input("Enter Principal Amount/Requirement of Loan Amount", min_value=0.0)
    st.write("You need loan of :-", P)

    R = st.number_input("Please Enter Your Annual Interest Rate:", min_value=0.0)
    st.write("Your Interest Rate is ", R)

    N = st.number_input("Please Enter loan Tenure in Years:- ", min_value=1)
    n = N * 12

    if P > 0 and n > 0:
        if R == 0:
            EMI = P / n
            TEMI = P  
        else:
            r = R / 12 / 100
            EMI = P * r * (1 + r)**n / ((1 + r)**n - 1)
            TEMI = EMI * n

        co1, co2 = st.columns(2)
        with co1:
            st.write("Monthly EMI ", round(EMI, 2))
            st.write("Principal Amount ", P)
            st.write("Interest Amount ", round(TEMI - P, 2))
            st.write("Total Amount Payable ", round(TEMI, 2))

        with co2:
            TI = TEMI - P
            # data and labels
            sizes = [P, TI]
            lab = ['Principal Amount', 'Interest Amount']
            colors = ['red', 'blue']
            explode = (0, 0.1)
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=lab, autopct='%1.1f%%', startangle=90,
                   colors=colors, explode=explode, shadow=True)
            ax.axis('equal') 
            ax.set_title("Loan Payment Breakdown")
            fig.tight_layout()

        
            st.pyplot(fig)

elif st.session_state.selected == "fd":
    st.subheader("Compounding will be Annually")
    P = st.number_input("Enter Amount To Invest", min_value=0.0)
    R1 = st.number_input("Enter Annual Interest Rate", min_value=0.0)
    t = st.number_input("Enter Tenure of your FD in Years", min_value=1)
    
    if P > 0 and R1 > 0 and t > 0:
        r1 = R1 / 100
        n1 = 1  # compounded annually
        g = n1 * t
        A = P * (1 + r1 / n1) ** g
        st.write("Maturity Amount:-", round(A, 2))
        st.write("💰 Interest Earned:-", round(A - P, 2))