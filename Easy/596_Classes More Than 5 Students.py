import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - consider the corner case that the dataframe is empty
    - groupby `class` and filter `class` which the number of students at least five -> value_counts
    - return dataframe with column `class`
    """
    if courses.empty:
        return courses[["class"]]
    else:
        values = courses["class"].value_counts().loc[lambda x : x>=5].index.to_list()
        pass_courses = pd.DataFrame({
            "class": values
        })
        return pass_courses
