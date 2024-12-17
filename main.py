import streamlit as st

# Define MBTI information
data = {
    "INTJ": {
        "career": "🌟 전략가형인 INTJ는 논리적 사고와 독창성으로 유명합니다. 그들은 데이터 분석가, 소프트웨어 개발자, 경영 컨설턴트, 과학자 같은 직업에 잘 맞습니다.",
        "compatible": "😎 ENFP 및 ENTP와 잘 어울리며, 서로의 차이점을 보완하면서도 자극을 주는 관계를 형성합니다."
    },
    "INTP": {
        "career": "🌈 아이디어 뱅크인 INTP는 분석적 사고와 창의성으로 문제 해결에 능합니다. 소프트웨어 엔지니어, 철학자, 연구원, 데이터 과학자 같은 직업이 적합합니다.",
        "compatible": "😍 ENTJ 및 ENFP와 잘 어울리며, 서로의 논리와 열정을 공유하며 협력할 수 있습니다."
    },
    "ENTJ": {
        "career": "💡 리더십의 대명사인 ENTJ는 목표 달성을 위해 강력한 추진력을 보입니다. 기업가, 경영진, 프로젝트 매니저, 변호사 같은 직업에 잘 맞습니다.",
        "compatible": "🌐 INTP 및 INFP와 좋은 관계를 유지할 수 있으며, 서로의 강점을 활용하여 시너지 효과를 냅니다."
    },
    "ENTP": {
        "career": "🚀 토론의 왕 ENTP는 끝없는 호기심과 창의성으로 새로운 아이디어를 창출합니다. 창업가, 마케팅 전문가, 변호사, 컨설턴트 같은 직업에 적합합니다.",
        "compatible": "🌞 INFJ 및 INTJ와 잘 어울리며, 서로의 차이점을 활용하여 혁신적인 아이디어를 만들어냅니다."
    },
    "INFJ": {
        "career": "🧘🏻‍♂️ 이상주의자인 INFJ는 타인의 감정에 공감하고 의미 있는 목표를 추구합니다. 상담사, 작가, 교사, 인권 활동가 같은 직업에 적합합니다.",
        "compatible": "🙏 ENFP 및 ENTP와 잘 맞으며, 서로의 비전을 공유하며 깊이 있는 관계를 형성합니다."
    },
    "INFP": {
        "career": "🌈 예술적 감성과 깊은 내면을 가진 INFP는 창의적인 활동을 선호합니다. 작가, 예술가, 상담사, 그래픽 디자이너 같은 직업에 잘 맞습니다.",
        "compatible": "🍀 ENFJ 및 ENTJ와 좋은 관계를 맺으며, 서로의 열정과 비전을 존중합니다."
    },
    "ENFJ": {
        "career": "🌍 사람 중심의 리더인 ENFJ는 사람을 돕고 이끄는 능력이 뛰어납니다. 교사, 코치, 인사 전문가, 정치인 같은 직업에 적합합니다.",
        "compatible": "💛 INFP 및 ISFP와 잘 어울리며, 서로의 감정과 가치를 존중합니다."
    },
    "ENFP": {
        "career": "🌈 자유로운 영혼 ENFP는 열정과 창의력으로 새로운 경험을 추구합니다. 마케터, 콘텐츠 크리에이터, 여행 작가, 강연자 같은 직업에 적합합니다.",
        "compatible": "💕 INFJ 및 INTJ와 잘 어울리며, 서로의 차이점을 매력으로 느끼며 긍정적인 관계를 형성합니다."
    }
}

# Streamlit UI 설정
st.title('MBTI에 따른 직업 및 궁합 추천 🌟')
st.write("MBTI 유형을 선택하면, 그에 맞는 직업 추천과 잘 어울리는 유형을 알려드립니다! 😉")

# MBTI 선택 드롭다운 메뉴
selected_mbti = st.selectbox('당신의 MBTI를 선택해주세요 📚', list(data.keys()))

# 선택한 MBTI에 맞는 직업과 궁합 정보 표시
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형의 직업 추천 🚀")
    st.write(data[selected_mbti]['career'])
    
    st.subheader(f"{selected_mbti} 유형과 잘 어울리는 사람들 😍")
    st.write(data[selected_mbti]['compatible'])

st.write("\n\n**Tip:** MBTI는 참고용일 뿐, 개인의 개성은 MBTI로 다 설명할 수 없어요! 🌟")

