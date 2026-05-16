
import streamlit as st
from models.groq_client import client
from analytics.charts import latency_chart
from evaluator.quality_evaluator import evaluate_response
from dashboard.metrics_display import show_summary_metrics
from ranking.leaderboard import rank_models
import time
import pandas as pd


st.set_page_config(
    page_title="LLM Evaluation Platform",
    layout="wide"
)

# Title
st.title("LLM Evaluation Platform")

st.write("Compare multiple LLMs side-by-side")


user_prompt = st.text_area(
    "Enter your prompt:",
    height=150
)


models = [
    "llama-3.3-70b-versatile",
    "meta-llama/llama-4-scout-17b-16e-instruct",
    "llama-3.1-8b-instant"
]


if st.button("Run Evaluation"):

    
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:

        results = []

        
        for model in models:

            start_time = time.time()

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ]
                )

                end_time = time.time()

                latency = round(end_time - start_time, 2)

                answer = response.choices[0].message.content

                input_tokens = response.usage.prompt_tokens
                output_tokens = response.usage.completion_tokens
                total_tokens = response.usage.total_tokens

                tokens_per_second = round(output_tokens / latency, 2)

                response_length = len(answer)

                quality_scores = evaluate_response(client, answer)

                results.append({
                    "Model": model,
                    "Latency": latency,
                    "Input Tokens": input_tokens,
                    "Output Tokens": output_tokens,
                    "Total Tokens": total_tokens,
                    "Tokens/Sec": tokens_per_second,
                    "Response Length": response_length,
                    "Quality Scores": quality_scores,
                    "Response": answer
                })

            except Exception as e:

                results.append({
                    "Model": model,
                    "Latency": "Error",
                    "Input Tokens": 0,
                    "Output Tokens": 0,
                    "Total Tokens": 0,
                    "Tokens/Sec": 0,
                    "Response Length": 0,
                    "Response": str(e)
                })

        
        df = pd.DataFrame(results)

        ranked_df = rank_models(df)
        
        st.subheader("performance metrics")
        show_summary_metrics(df)
    
    
        st.subheader("Evaluation Results")

        st.subheader("Leaderboard")

        st.dataframe(ranked_df)

        st.subheader("Latency Comparison")

        fig = latency_chart(df)

        st.pyplot(fig)

        st.divider()

   
        for result in results:

            st.subheader(result["Model"])

            st.write(f"Latency: {result['Latency']} sec")

            st.write(result["Response"])

            st.divider()

