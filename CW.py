import streamlit as st
import pandas as pd


def main():
    st.title("Record Search App")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the DataFrame
        # st.write("## Your Records:")
        # st.write(df)

        # Search functionality
        search_query = st.text_input("Enter search query:")
        if search_query:
            # Perform case-insensitive search in all columns
            filtered_df = df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)
            result_df = df[filtered_df]

            if not result_df.empty:
                st.write("## Search Results:")
                st.write(result_df)
            else:
                st.warning("No matching records found.")


if __name__ == "__main__":
    main()
