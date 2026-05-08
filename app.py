import streamlit as st
import pandas as pd
import sys, os, re, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from generate_ppt import load_athlete_data, generate_ppt_bytes
from datetime import datetime
from io import BytesIO

st.set_page_config(page_title="멘탈 프로파일 생성기", page_icon="🧠", layout="centered")
st.markdown("""
<style>
.stButton>button{width:100%;background:#1a1a2e;color:white;border:none;padding:.6rem 1rem;border-radius:8px;font-size:15px;font-weight:500}
.stButton>button:hover{background:#16213e}
.stDownloadButton>button{width:100%;background:#0f7a5a;color:white;border:none;padding:.7rem 1rem;border-radius:8px;font-size:15px;font-weight:600}
</style>
""", unsafe_allow_html=True)

st.title("🧠 멘탈 프로파일 PPT 생성기")
st.caption("엑셀 데이터 → 선수별 심리측정 결과 PPT 자동 생성")
st.divider()

col1, col2 = st.columns(2)
with col1:
    excel_file = st.file_uploader("📊 엑셀 파일", type=["xlsx","xls"])
with col2:
    ppt_file = st.file_uploader("📑 PPT 템플릿", type=["pptx"])

if excel_file and ppt_file:
    try:
        df = pd.read_excel(excel_file, sheet_name='개인측정코딩')
        athletes = df['성명'].dropna().tolist()
    except Exception as e:
        st.error(f"엑셀 오류: {e}"); st.stop()

    st.divider()
    mode = st.radio("생성 방식", ["선수 한 명", "전체 선수 일괄 생성"], horizontal=True)
    ppt_bytes = ppt_file.read()

    if mode == "선수 한 명":
        selected = st.selectbox("선수 선택", athletes)
        if st.button("PPT 생성하기 →"):
            with st.spinner(f"{selected} 선수 PPT 생성 중..."):
                try:
                    data = load_athlete_data(df, selected)
                    result = generate_ppt_bytes(ppt_bytes, data)
                    today = datetime.today().strftime("%Y%m%d")
                    sport_safe = re.sub(r'[,/ ]','_', data['sport']).strip('_')
                    fname = f"{today}_{sport_safe}_{selected}_멘탈프로파일.pptx"
                    st.success(f"✅ {selected} 선수 PPT 완성!")
                    with st.expander("📋 점수 요약"):
                        c1,c2,c3 = st.columns(3)
                        c1.metric("낙관성", f"{data['optimism']}/30")
                        c2.metric("특성불안", f"{data['trait_anxiety']}/30")
                        c3.metric("상태자신감", f"{data['state_confidence']}/30")
                        c1.metric("인지불안", f"{data['cognitive_anxiety']}/30")
                        c2.metric("신체불안", f"{data['somatic_anxiety']}/30")
                        c3.metric("능력입증", f"{round(data['sc_ability'],1)}/5")
                    st.download_button("⬇️ 다운로드", data=result, file_name=fname,
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
                except Exception as e:
                    st.error(f"오류: {e}")

    else:
        st.info(f"총 {len(athletes)}명 PPT를 생성합니다.")
        if st.button(f"전체 {len(athletes)}명 일괄 생성 →"):
            zip_buf = BytesIO(); errors = []
            progress = st.progress(0, text="생성 중...")
            status = st.empty()
            with zipfile.ZipFile(zip_buf, 'w') as zf:
                for i, name in enumerate(athletes):
                    status.write(f"⏳ {name} 처리 중... ({i+1}/{len(athletes)})")
                    try:
                        data = load_athlete_data(df, name)
                        result = generate_ppt_bytes(ppt_bytes, data)
                        today = datetime.today().strftime("%Y%m%d")
                        sport_safe = re.sub(r'[,/ ]','_', data['sport']).strip('_')
                        zf.writestr(f"{today}_{sport_safe}_{name}_멘탈프로파일.pptx", result)
                    except Exception as e:
                        errors.append(f"{name}: {e}")
                    progress.progress((i+1)/len(athletes))
            status.empty()
            st.success(f"✅ {len(athletes)-len(errors)}명 완성!" +
                      (f" ({len(errors)}명 오류)" if errors else ""))
            if errors:
                with st.expander("오류 목록"):
                    [st.write(e) for e in errors]
            zip_buf.seek(0)
            st.download_button("⬇️ 전체 ZIP 다운로드", data=zip_buf.read(),
                file_name=f"멘탈프로파일_전체_{datetime.today().strftime('%Y%m%d')}.zip",
                mime="application/zip")

else:
    st.info("👆 엑셀 파일과 PPT 템플릿을 업로드해주세요.")
    with st.expander("사용 방법"):
        st.markdown("""
        1. **엑셀 파일** 업로드 (`개인측정코딩` 시트 포함)
        2. **PPT 템플릿** 업로드
        3. 선수 선택 후 **PPT 생성** 클릭
        4. 완성 파일 **다운로드**
        > 전체 선수 일괄 생성 시 ZIP으로 한 번에 받을 수 있어요.
        """)
