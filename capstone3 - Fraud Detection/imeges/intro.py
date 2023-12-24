import streamlit as st

def main():
    # Set the page title
    st.title("")

    html_temp = """
        <div style="background-color:#FFB6C1;padding:10px">
        <h2 style="color:black;text-align:center; font-family: 'Helvetica', sans-serif;">Fraud Detection Application</h2>
        </div>"""
    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add margin after the title
    st.markdown("<br>", unsafe_allow_html=True)  # Add margin after the title
    st.markdown("<br>", unsafe_allow_html=True)  # Add margin after the title
    
    # Display an image with margin above and below
    st.image("fraud-7065116_1280.png", use_column_width=True, caption="", output_format="PNG")
    st.markdown("<br>", unsafe_allow_html=True)  # Add margin after the image

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Left side (project info)
    with col1:
        st.markdown(
            """
            ## Project Overview

            This fraud detection application is designed to help businesses identify and prevent fraudulent activities. Our system utilizes advanced machine learning algorithms to analyze data in real-time and provide instant insights.

            Key Features:
            - Real-time fraud detection
            - Secure data processing
            - Machine learning algorithms

            Get started today and enhance your business security.
            """,
            unsafe_allow_html=True
        )

    # Right side (title and video)
    with col2:
        # Video
        st.video("https://www.youtube.com/watch?v=c6P32ZCL4b0")

                # Icon and Get Started link
    st.markdown(
            """
            <div style="text-align: center; border: 2px solid #FFB6C1; padding: 10px; border-radius: 5px;">
                <a href=' http://172.20.10.2:8502' style='color: #FFB6C1; font-size: 20px; text-decoration: none;'>
                    <span class="iconify" data-icon="ic:baseline-play-arrow" data-inline="false" style="color:#FFB6C1; font-size: 24px; vertical-align: middle;"></span>
                    Get Started
                </a>
            </div>
            """,
            unsafe_allow_html=True
    )
if __name__ == "__main__":
    main()