import streamlit as st
import random

player_num = 15
name = []
role = []


col1, col2, col3 = st.beta_columns(3)

roles1 = ['Godfather', 'Jadoogar', 'Terrorist', 'Mafia_Sadeh', 'Gholdor']
roles2 = ['Doctor', 'ZerehPoosh', 'Keshish', 'Masih', 'Postchi']
roles3 = ['Citizen', 'Cowboy', 'Shooter', 'BabaNoel', 'Tofangdar']

with col1:
    for i, rol in enumerate(roles1):
        name_ = st.text_input(f"Player {i+1}:", key=str(i))
        if name_ != "": name.append(str(i+1)+"-"+name_)
    for i, rol in enumerate(roles1):
        if st.checkbox(rol) == True: role.append(rol)

with col2:
    for i, rol in enumerate(roles2):
        i = i + 5
        name_ = st.text_input(f"Player {i+1}:", key=str(i))
        if name_ != "": name.append(str(i+1)+"-"+name_)
    for i, rol in enumerate(roles2):
        i = i + 5
        if st.checkbox(rol) == True: role.append(rol)

with col3:
    for i, rol in enumerate(roles3):
        i = i + 10
        name_ = st.text_input(f"Player {i+1}:", key=str(i))
        if name_ != "": name.append(str(i+1)+"-"+name_)
    for i, rol in enumerate(roles3):
        i = i + 10
        if st.checkbox(rol) == True: role.append(rol)


Shuffle = st.checkbox("Shuffle")
random.shuffle(role)
st.write(dict(zip(name , role)))

# if Shuffle == True: 
#     random.shuffle(role)
#     st.write(dict(zip(name , role)))

