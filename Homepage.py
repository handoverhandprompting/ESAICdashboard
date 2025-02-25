import streamlit as st
from models import baseline_model, prediction_model
from layout_css import expander_layout
from streamlit_extras.stylable_container import stylable_container

if '_language' not in st.session_state:
    st.session_state['_language'] = 'chinese'


def home_content():
    """
    Type your CHINESE homepage here
    """
    st.header('國立臺灣大學醫學院附設醫院 心臟衰竭藥事照護服務')
    st.header('歡迎使用 一節課 ESAIC 互動式數位工具')
    
    st.write('您知道為什麼要吃這些藥嗎？')
    st.write('您對於藥品有很多疑問嗎？')
    st.write('您想要看懂自己的抽血報告嗎？')
    st.write('您希望更瞭解自己目前心臟衰竭的情況嗎？')
    
    st.header('您的需求，我們都聽到了')
    st.header('藥師通通都可以耐心為您解答')
              
    st.write('有了這個互動式數位工具之後')
    st.write('您可以用更簡單的方式來瞭解這些問題')
    
def home_content_en():
    """
     Type your ENGLISH homepage here
    """
    st.header('Welcome to the ESAIC Dashboards')
    st.header('What are the ESAIC Dashboards?')
    st.write('The ESAIC dashboards are interactive digital tools developed using Streamlit, based on predictive models constructed through Cox proportional hazards regression. These dashboards are designed to support healthcare professionals in guiding patients through sacubitril/valsartan (S/V) therapy by providing visual representations of risk factors and survival probabilities. This website incorporates two distinct dashboards: one tailored for patients initiating S/V therapy and another for those continuing treatment. The models underpinning these dashboards were developed using electronic medical record data from patients with heart failure with reduced ejection fraction (HFrEF) treated at National Taiwan University Hospital (NTUH), a leading tertiary medical center in Taipei, Taiwan. The predictive model for S/V initiation was built using a stepwise variable selection approach within a Cox proportional-hazards model, incorporating time-dependent covariates to capture dynamic changes over time. 14 key covariates were identified as significant predictors. The predictive model for S/V continuation was developed using similar methodologies, identifying 20 key covariates.')
    st.write('We hypothesize that these dashboards, by presenting actionable and modifiable risk factors derived from our predictive models, will enhance patient understanding of the benefits and risks associated with S/V therapy. By offering an intuitive format displaying hazard ratios and survival curves across different clinical scenarios based on patient-specific data, the dashboards aim to empower patients to take a proactive role in their treatment journey and improve adherence to prescribed regimens. This digital platform is designed to facilitate a clearer understanding of treatment benefits and risks through a visual format, assisting both patients and healthcare practitioners in optimizing patient education.') 
    st.header('How to use the ESAIC Dashboards?')
    st.write('Access to this website is restricted to licensed healthcare professionals specializing in heart failure management. The ESAIC dashboards do not collect, store, or access any user data. To begin, healthcare professionals can create a reference condition based on a the current clinical profile of a patient. By adjusting additional clinical covariates and updating their values, users can explore alternative scenarios and observe how these factors influence prognosis, hazard ratios, and survival probabilities. It is important to note that this prognostic tool is NOT intended to dictate clinical decision-making. Rather, it serves as an objective informational resource for healthcare providers and patients, helping to identify modifiable risk factors and assess potential benefits associated with treatment adjustments.

def run():
    st.set_page_config(layout="wide")
    expander_layout()

    # Set default language
    if '_language' not in st.session_state:
        st.session_state['_language'] = 'chinese'

    with st.container():
        col, but_col = st.columns([5, 1])
        with but_col:
            language_button = st.selectbox('Language/語言', ['繁體中文', 'English'])
            if language_button == '繁體中文':
                st.session_state['_language'] = 'chinese'
            elif language_button == 'English':
                st.session_state['_language'] = 'english'

    if st.session_state['_language'] == 'chinese':
        home_content()
    elif st.session_state['_language'] == 'english':
        home_content_en()
    else:
        st.session_state['_language'] = 'chinese'
        st.experimental_rerun()


if __name__ == '__main__':
    run()
