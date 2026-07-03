import os

import requests
import streamlit as st

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

PAGES = {
    "🏠 Home": "home",
    "🚚 Freight Cost Prediction": "freight",
    "📄 Invoice Risk Prediction": "invoice",
    "ℹ️ About Project": "about",
}

CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.25rem;
    }
    .sub-header {
        font-size: 1.15rem;
        color: #4b5563;
        margin-bottom: 1.5rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        min-height: 220px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
    }
    .feature-card h3 {
        margin-top: 0;
        color: #111827;
    }
    .metric-card {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        border-radius: 14px;
        padding: 1.25rem;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #047857;
    }
    .workflow-step {
        background: #ffffff;
        border: 1px solid #dbeafe;
        border-radius: 12px;
        padding: 0.85rem 1rem;
        text-align: center;
        font-weight: 600;
        color: #1d4ed8;
    }
    .sidebar-brand {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.5rem;
    }
    div[data-testid="stSidebar"] {
        background-color: #f9fafb;
    }
</style>
"""


def inject_css() -> None:
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def call_api(endpoint: str, payload: dict) -> dict:
    url = f"{API_BASE_URL}{endpoint}"
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def render_home() -> None:
    st.markdown('<p class="main-header">AI Powered Invoice Intelligence System</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Machine learning platform for freight cost validation and invoice risk detection.</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        This application combines two production ML models to help finance and operations teams
        validate invoices faster, reduce manual audit effort, and identify cost leakage early.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>Freight Cost Prediction</h3>
                <p>Companies receive thousands of freight invoices every month. Manual verification
                is slow and error-prone. The regression model predicts expected freight cost so teams
                can quickly spot overcharging and cost leakage.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>Invoice Risk Detection</h3>
                <p>Accounts payable teams process large invoice volumes daily. Manual auditing is
                expensive and time-consuming. The classification model automatically flags suspicious
                invoices for review.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Business Impact")
    st.markdown(
        "Real-world applications include **Finance**, **Procurement**, **Supply Chain**, "
        "**Audit**, and **Accounts Payable** workflows."
    )

    st.info("Use the sidebar to navigate to prediction pages and run live inference through the FastAPI backend.")


def render_freight_page() -> None:
    st.markdown("## Freight Cost Prediction")
    st.write("Enter invoice details to predict the expected freight cost.")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            invoice_quantity = st.number_input("Invoice Quantity", min_value=1.0, value=100.0, step=1.0)
            invoice_dollars = st.number_input("Invoice Dollars", min_value=0.0, value=5000.0, step=100.0)
            freight = st.number_input("Freight", min_value=0.0, value=50.0, step=1.0)

        with col2:
            days_po_to_invoice = st.number_input("Days PO to Invoice", min_value=0.0, value=5.0, step=1.0)
            total_item_quantity = st.number_input("Total Item Quantity", min_value=0.0, value=100.0, step=1.0)
            total_item_dollars = st.number_input("Total Item Dollars", min_value=0.0, value=5000.0, step=100.0)

    if st.button("Predict Freight Cost", type="primary", use_container_width=True):
        payload = {
            "invoice_quantity": invoice_quantity,
            "invoice_dollars": invoice_dollars,
            "freight": freight,
            "days_po_to_invoice": days_po_to_invoice,
            "total_item_quantity": total_item_quantity,
            "total_item_dollars": total_item_dollars,
        }

        try:
            result = call_api("/predict/freight", payload)
            predicted_cost = result["predicted_freight_cost"]

            st.success("Prediction completed successfully.")
            st.markdown(
                f"""
                <div class="metric-card">
                    <div>Predicted Freight Cost</div>
                    <div class="metric-value">${predicted_cost:,.2f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.metric(label="Predicted Freight Cost", value=f"${predicted_cost:,.2f}")

            with st.expander("Model features used"):
                st.json(result["features_used"])

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to the API. Start the backend with `uvicorn main:app --reload`.")
        except requests.exceptions.HTTPError as exc:
            detail = exc.response.json().get("detail", "Prediction request failed.")
            st.error(detail)
        except Exception:
            st.error("An unexpected error occurred while predicting freight cost.")


def render_invoice_page() -> None:
    st.markdown("## Invoice Risk Prediction")
    st.write("Enter invoice attributes to classify the invoice as Normal or Flagged.")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            invoice_quantity = st.number_input("Invoice Quantity", min_value=1.0, value=100.0, step=1.0, key="inv_qty")
            invoice_dollars = st.number_input("Invoice Dollars", min_value=0.0, value=5000.0, step=100.0, key="inv_dol")
            freight = st.number_input("Freight", min_value=0.0, value=50.0, step=1.0, key="inv_freight")

        with col2:
            total_item_quantity = st.number_input(
                "Total Item Quantity", min_value=0.0, value=100.0, step=1.0, key="inv_total_qty"
            )
            total_item_dollars = st.number_input(
                "Total Item Dollars", min_value=0.0, value=5000.0, step=100.0, key="inv_total_dol"
            )

    if st.button("Predict Invoice Risk", type="primary", use_container_width=True):
        payload = {
            "invoice_quantity": invoice_quantity,
            "invoice_dollars": invoice_dollars,
            "freight": freight,
            "total_item_quantity": total_item_quantity,
            "total_item_dollars": total_item_dollars,
        }

        try:
            result = call_api("/predict/invoice", payload)
            label = result["label"]
            probability = result["probability"]

            if result["flag_invoice"] == 1:
                st.warning(f"Prediction: **{label}** — review recommended (risk probability: {probability:.2%})")
            else:
                st.success(f"Prediction: **{label}** (risk probability: {probability:.2%})")

            st.metric(label="Prediction", value=label)
            st.metric(label="Flag Probability", value=f"{probability:.2%}")

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to the API. Start the backend with `uvicorn main:app --reload`.")
        except requests.exceptions.HTTPError as exc:
            detail = exc.response.json().get("detail", "Prediction request failed.")
            st.error(detail)
        except Exception:
            st.error("An unexpected error occurred while predicting invoice risk.")


def render_about_page() -> None:
    st.markdown("## About Project")

    st.markdown("### Business Problem")
    st.write(
        "Organizations lose money through invoice cost leakage and audit risk. Freight overcharges "
        "and suspicious invoice patterns are difficult to detect manually at scale."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Invoice Cost Leakage")
        st.write("Unexpected freight charges and mismatched invoice totals create hidden financial loss.")
    with col2:
        st.markdown("#### Audit Risk")
        st.write("High-risk invoices can pass through AP workflows without timely review.")

    st.markdown("### Machine Learning Modules")
    st.markdown(
        """
        - **Freight Cost Prediction (Regression):** Random Forest Regressor predicts expected freight cost.
        - **Invoice Flagging (Classification):** XGBoost classifier flags high-risk invoices.
        """
    )

    st.markdown("### Workflow")
    workflow_cols = st.columns(5)
    steps = ["Database", "Feature Engineering", "Machine Learning", "Prediction", "Business Decision"]
    for col, step in zip(workflow_cols, steps):
        with col:
            st.markdown(f'<div class="workflow-step">{step}</div>', unsafe_allow_html=True)

    st.markdown("↓", unsafe_allow_html=True)

    with st.expander("Technical Architecture"):
        st.markdown(
            """
            - **Frontend:** Streamlit dashboard (this app)
            - **Backend:** FastAPI REST API (`/predict/freight`, `/predict/invoice`)
            - **Inference:** Shared Python inference modules loaded once at API startup
            - **Models:** Pre-trained artifacts stored in project model directories
            """
        )


def main() -> None:
    st.set_page_config(
        page_title="Invoice Intelligence System",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_css()

    with st.sidebar:
        st.markdown('<p class="sidebar-brand">Invoice Intelligence</p>', unsafe_allow_html=True)
        st.caption("AI-powered freight and invoice analytics")
        page = st.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
        st.divider()
        st.markdown(f"**API:** `{API_BASE_URL}`")

    current_page = PAGES[page]

    if current_page == "home":
        render_home()
    elif current_page == "freight":
        render_freight_page()
    elif current_page == "invoice":
        render_invoice_page()
    elif current_page == "about":
        render_about_page()


if __name__ == "__main__":
    main()
