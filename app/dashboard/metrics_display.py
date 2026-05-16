import streamlit as st


def show_summary_metrics(df):

    fastest_model = df.loc[df["Latency"].idxmin()]

    highest_throughput = df.loc[df["Tokens/Sec"].idxmax()]

    st.markdown("## Performance Metrics")

    col1, col2 = st.columns(2)

    with col1:

        with st.container():

            st.markdown("""
            ### Fastest Model
            """)

            st.metric(
                label="Latency",
                value=fastest_model["Model"],
                delta=f"{fastest_model['Latency']} sec"
            )

    with col2:

        with st.container():

            st.markdown("""
            ### Highest Throughput
            """)

            st.metric(
                label="Tokens/Sec",
                value=highest_throughput["Model"],
                delta=f"{highest_throughput['Tokens/Sec']}"
            )

    st.markdown("---")