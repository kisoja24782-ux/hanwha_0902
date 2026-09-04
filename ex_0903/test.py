import streamlit as st
import pandas as pd
import numpy as np


# df = pd.DataFrame({
#     'first column' : [1, 2, 3, 4],
#     'second column' : [10, 20, 30, 40]
# })

# st.write("반가워 스트림릿")

#df  # 이렇게 출력가능

# st.write(df)  # 이렇게도 출력가능

# datframe = np.random.randn(10,20)
# st.dataframe(datframe)

thirdframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns= ('col %d' % i for i in range(20))
)

st.dataframe(thirdframe.style.highlight_max(axis = 0))

# st.title("Yooooooooooooooooooooooooo")
# st.title("_Streamlit_ is :blue[cool] :sunglasses:")
# st.header("This is a header with a divider", divider="gray")
# st.header("These headers have rotating dividers", divider=True)
# st.header("One", divider=True)
# st.header("Two", divider=True)
# st.header("Three", divider=True)
# st.header("Four", divider=True)

# st.subheader("This is a subheader with a divider", divider="gray")
# st.subheader("These subheaders have rotating dividers", divider=True)
# st.subheader("One", divider=True)
# st.subheader("Two", divider=True)
# st.subheader("Three", divider=True)
# st.subheader("Four", divider=True)

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)

st.badge("New")
st.badge("Success", icon = ":material/check:", color= "green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

st.caption("This si a string that explains something above.")
st.caption("A caption with _italics_ :blue[color] and emojis :sunglasses:")

st.write("This is some text.")
st.slider("This is a slider", 0, 100, (25, 75))
st.divider()
st.write("This text is between the horizontal rules.")
st.divider()

def get_user_name():
    return 'John'


with st.echo():
    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    user_name = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, user_name, punctuation)



foo = 'bar'
st.write('Done!')


