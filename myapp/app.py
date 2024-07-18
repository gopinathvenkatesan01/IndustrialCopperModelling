from math import prod
import streamlit as st
from datetime import date
import pickle
import numpy as np


def main():
    page_icon_url = "https://github.com/user-attachments/assets/69df246e-ddca-4992-826a-e44889ddd698"
    st.set_page_config(
        page_title="Industrial Copper Modelling ",
        page_icon=page_icon_url,
        layout="wide",
    )
    st.subheader("⏩ Industrial **Copper Modelling** | _By Gopi_ ")

    country_values = [
        25.0,
        26.0,
        27.0,
        28.0,
        30.0,
        32.0,
        38.0,
        39.0,
        40.0,
        77.0,
        78.0,
        79.0,
        80.0,
        84.0,
        89.0,
        107.0,
        113.0,
    ]

    status_values = [
        "Won",
        "Lost",
        "Draft",
        "To be approved",
        "Not lost for AM",
        "Wonderful",
        "Revised",
        "Offered",
        "Offerable",
    ]

    status_dict = {
        "Lost": 0,
        "Won": 1,
        "Draft": 2,
        "To be approved": 3,
        "Not lost for AM": 4,
        "Wonderful": 5,
        "Revised": 6,
        "Offered": 7,
        "Offerable": 8,
    }

    item_type_values = ["W", "WI", "S", "PL", "IPL", "SLAWR", "Others"]

    item_type_dict = {
        "W": 5.0,
        "WI": 6.0,
        "S": 3.0,
        "Others": 1.0,
        "PL": 2.0,
        "IPL": 0.0,
        "SLAWR": 4.0,
    }

    application_values = [
        2.0,
        3.0,
        4.0,
        5.0,
        10.0,
        15.0,
        19.0,
        20.0,
        22.0,
        25.0,
        26.0,
        27.0,
        28.0,
        29.0,
        38.0,
        39.0,
        40.0,
        41.0,
        42.0,
        56.0,
        58.0,
        59.0,
        65.0,
        66.0,
        67.0,
        68.0,
        69.0,
        70.0,
        79.0,
        99.0,
    ]

    product_ref_values = [
        611728,
        611733,
        611993,
        628112,
        628117,
        628377,
        640400,
        640405,
        640665,
        164141591,
        164336407,
        164337175,
        929423819,
        1282007633,
        1332077137,
        1665572032,
        1665572374,
        1665584320,
        1665584642,
        1665584662,
        1668701376,
        1668701698,
        1668701718,
        1668701725,
        1670798778,
        1671863738,
        1671876026,
        1690738206,
        1690738219,
        1693867550,
        1693867563,
        1721130331,
        1722207579,
    ]

    # Custom CSS for the submit button
    st.markdown(
        """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 80px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        border: 2px solid #4CAF50;
    }
    .stButton button:hover {
        background-color: white;
        color: #4CAF50;
    }
    .prediction_win{
        font-size: 50px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-top: 20px;
    }
    .prediction_lost{
        font-size: 50px;
        font-weight: bold;
        color: #eb0707;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    win_predictor, price_predictor = st.tabs(["Win Predictor", "Price Predictor"])

    with win_predictor:
        st.info("*Values Refered are based on given Data")
        with st.form("win_predictor_form"):
            col1, col2, col3 = st.columns([0.5, 0.1, 0.5])
            with col1:
                item_date = st.date_input(
                    label="Item Date",
                    min_value=date(2020, 7, 1),
                    max_value=date(2021, 5, 31),
                    value=date(2020, 7, 1),
                )

                quantity_tons_log = st.text_input(
                    label="*Quantity Tons Log (Min: 0.00001 & Max: 1000000000)"
                )

                country = st.selectbox(label="Country", options=country_values)

                item_type = st.selectbox(label="Item Type", options=item_type_values)

                thickness_log = st.number_input(
                    label="Thickness", min_value=0.1, max_value=2500000.0, value=1.0
                )

                product_ref = st.selectbox(
                    label="Product Ref", options=product_ref_values
                )

            with col3:
                delivery_date = st.date_input(
                    label="Delivery Date",
                    min_value=date(2020, 8, 1),
                    max_value=date(2022, 2, 28),
                    value=date(2020, 8, 1),
                )

                customer = st.text_input(
                    label="*Customer ID (Min: 12458000 & Max: 2147484000)"
                )
                selling_price_log = st.text_input(
                    label="*Selling Price (Min: 0.1 & Max: 100001000)"
                )

                application = st.selectbox(
                    label="Application", options=application_values
                )

                width = st.number_input(
                    label="Width", min_value=1.0, max_value=2990000.0, value=1.0
                )
                st.write(" ")
                submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                with open("models\classification_model.pkl", "rb") as f:
                    model = pickle.load(f)

                    user_test_data = np.array(
                        [
                            [
                                customer,
                                country,
                                item_type_dict[item_type],
                                application,
                                width,
                                product_ref,
                                np.log(float(quantity_tons_log)),
                                np.log(float(thickness_log)),
                                np.log(float(selling_price_log)),
                                item_date.day,
                                item_date.month,
                                item_date.year,
                                delivery_date.day,
                                delivery_date.month,
                                delivery_date.year,
                            ]
                        ]
                    )
                    y_prediction = model.predict(user_test_data)

                    win_status = "WIN" if y_prediction == 1 else "LOST"
                    if y_prediction == 1:
                        st.markdown(
                            f"<div class='prediction_win'>{win_status}</div>",
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            f"<div class='prediction_lost'>{win_status}</div>",
                            unsafe_allow_html=True,
                        )
            except ValueError as e:
                st.warning("Please Provide Valid QuantityTons/CustomerID/SellingPrice")
            except Exception as e:
                st.warning(e)

    with price_predictor:
        st.info("*Values Refered are based on given Data")
        with st.form("price_predictor_form"):
            col1, col2, col3 = st.columns([0.5, 0.1, 0.5])
            with col1:
                item_date = st.date_input(
                    label="Item Date",
                    min_value=date(2020, 7, 1),
                    max_value=date(2021, 5, 31),
                    value=date(2020, 7, 1),
                )

                quantity_tons_log = st.text_input(
                    label="*Quantity Tons Log (Min: 0.00001 & Max: 1000000000)"
                )

                status = st.selectbox(label="Status", options=status_values)

                country = st.selectbox(label="Country", options=country_values)

                item_type = st.selectbox(label="Item Type", options=item_type_values)

                product_ref = st.selectbox(
                    label="Product Ref", options=product_ref_values
                )

            with col3:
                delivery_date = st.date_input(
                    label="Delivery Date",
                    min_value=date(2020, 8, 1),
                    max_value=date(2022, 2, 28),
                    value=date(2020, 8, 1),
                )

                thickness_log = st.number_input(
                    label="Thickness", min_value=0.1, max_value=2500000.0, value=1.0
                )

                customer = st.text_input(
                    label="*Customer ID (Min: 12458000 & Max: 2147484000)"
                )

                application = st.selectbox(
                    label="Application", options=application_values
                )

                width = st.number_input(
                    label="Width", min_value=1.0, max_value=2990000.0, value=1.0
                )
                st.write(" ")
                submitted = st.form_submit_button("Submit")
            # with col5:
            # Submit button

        # Display the values after the form is submitted
        if submitted:
            try:
                file_path = "models\\regression_model.pkl"
                with open(file_path, "rb") as f:
                    model = pickle.load(f)

                    user_test_data = np.array(
                        [
                            [
                                customer,
                                country,
                                status_dict[status],
                                item_type_dict[item_type],
                                application,
                                width,
                                product_ref,
                                np.log(float(quantity_tons_log)),
                                np.log(float(thickness_log)),
                                item_date.day,
                                item_date.month,
                                item_date.year,
                                delivery_date.day,
                                delivery_date.month,
                                delivery_date.year,
                            ]
                        ]
                    )
                    y_prediction = model.predict(user_test_data)
                    selling_price = np.exp(y_prediction[0])

                    selling_price = round(selling_price, 2)

                    if selling_price > 0:
                        st.markdown(
                            f" <div class='prediction_win'>The Predicted Price is {selling_price}</div>",
                            unsafe_allow_html=True,
                        )

                    else:
                        st.markdown(
                            f"<div class='prediction_lost'>The Predicted Price is {selling_price}</div>",
                            unsafe_allow_html=True,
                        )

            except ValueError as e:
                st.warning("Please Provide Valid QuantityTons/CustomerID")
            except Exception as e:
                st.warning(e)


if __name__ == "__main__":
    main()
