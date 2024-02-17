import streamlit as st
from Logic import utils
import time
from enum import Enum
import random


class color(Enum):
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"
    YELLOW = "#FFFF00"


def search_time(start, end):
    st.success(f"Search took: {end - start} seconds")


def search_handling(
    search_button,
    search_title_terms,
    search_abstract_terms,
    search_max_num,
    search_weight,
    search_method,
):
    if search_button:
        corrected_title = utils.correct_text(search_title_terms, utils.bigram_index)
        corrected_abstract = utils.correct_text(
            search_abstract_terms, utils.bigram_index
        )
        corrected = corrected_title + " " + corrected_abstract

        if (
            corrected_title != search_title_terms
            or corrected_abstract != search_abstract_terms
        ):
            st.warning(f"Your search terms were corrected to: {corrected}")
            search_title_terms = corrected_title
            search_abstract_terms = corrected_abstract

        with st.spinner("Searching..."):
            time.sleep(0.5)  # for showing the spinner! (can be removed)
            start_time = time.time()
            result = utils.search(
                search_title_terms,
                search_abstract_terms,
                search_max_num,
                search_method,
                search_weight,
            )
            end_time = time.time()
            if len(result) == 0:
                st.warning("No results found!")
                return

            search_time(start_time, end_time)

            for i in range(len(result)):
                card = st.columns(1)
                info = utils.get_paper_by_id(result[i][0], utils.papers_dataset)
                with card[0].container():
                    st.title(info["Title"])
                    st.markdown(f"[Link to paper]({info['URL']})")
                    st.write(f"Relevance Score: {result[i][1]}")
                    st.write(info["Abstract"])
                    with st.expander("Authors"):
                        num_authors = len(info["Authors"])

                        for j in range(num_authors):
                            st.write(info["Authors"][j])

                    topic_card = st.columns(1)
                    with topic_card[0].container():
                        st.write("Topics:")
                        num_topics = len(info["Related Topics"])
                        for j in range(num_topics):
                            st.markdown(
                                f"<span style='color:{random.choice(list(color)).value}'>{info['Related Topics'][j]}</span>",
                                unsafe_allow_html=True,
                            )
                    st.divider()


def main():
    st.title("Search Engine")
    st.write(
        "This is a simple search engine for academic papers. You can search through Semantic Scholar dataset and find the most relevant papers to your search terms."
    )
    st.markdown(
        '<span style="color:yellow">Developed By: AmirHossein Razlighi</span>',
        unsafe_allow_html=True,
    )

    search_title_terms = st.text_input("Seacrh in title")
    search_abstract_terms = st.text_input("Search in abstract")
    with st.expander("Advanced Search"):
        search_max_num = st.number_input(
            "Maximum number of results", min_value=5, max_value=100, value=10, step=5
        )
        search_weight = st.slider(
            "Weight of title in search",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.1,
        )
        search_method = st.selectbox(
            "Search method",
            ("ltn-lnn", "ltc-lnc", "okapi25"),
        )

    search_button = st.button("Search!")

    search_handling(
        search_button,
        search_title_terms,
        search_abstract_terms,
        search_max_num,
        search_weight,
        search_method,
    )


if __name__ == "__main__":
    main()
