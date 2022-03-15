import streamlit as st

import pandas as pd

import pickle
with open('model.pkl', 'rb') as fp:
    model = pickle.load(fp)
    
    
st.header('Predicting The Water Quality Index')
html_string = "<h6>Fill the Details to know the Water Quality Index</h6>"
st.markdown(html_string, unsafe_allow_html=True)


st.markdown("#### N-Pressure hydrocephalus(N-PH)")
npH=st.number_input('Enter the Normal pressure hydrocephalus(N-PH)',format="%.3f")

st.markdown("#### N-Dissolved Oxygen(N-DO)")
ndo=st.number_input('Enter the N-Dissolved oxygen(N-DO)',format="%.3f")

st.markdown("#### N-Biochemical Oxygen Demand(N-BOD")
nbdo=st.number_input('Enter the N-Biochemical oxygen Demand(N-BOD)',format="%.3f")

st.markdown("#### Conductivity")
nec=st.number_input('Enter the Conductivity',format="%.3f")

st.markdown("#### Nitrate-n and Nitrite-n ")
nna=st.number_input('Enter the Nitrate-n and Nitrite-n ',format="%.3f")

st.markdown("#### Fecal Coliform")
nco=st.number_input('Enter the Fecal Coliform',format="%.3f")






button=st.button('Predict')




if button:
        
    predict_1={'npH':[],'ndo':[],'nbdo':[],'nec':[],'nna':[],'nco':[]}
    Pred_data=pd.DataFrame(predict_1)
    Pred_data=Pred_data.append({'npH':npH,'ndo':ndo,'nbdo':nbdo,'nec':nec,'nna':nna,'nco':nco},ignore_index=True)
    fer= model.predict(Pred_data)

    if (25>=fer>=20):
        st.success('The Water Quality is Excellent ')
    elif(50>=fer>=26):
        st.success('The Water Quality is Good')
    elif(75>=fer>=51):
        st.error('The Water Quality is Poor')
    elif(100>=fer>=101):
        st.error('The Water Quality is Very Poor')
    else:
        st.error('The Water Quality is Unsuitable')


#     trix = f"<marquee>{final}</marquee>"
#     st.markdown(trix, unsafe_allow_html=True)
    
    
    
    
    
    
    
    