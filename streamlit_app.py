import streamlit as st
import edge_tts
import asyncio


TEXT = """뉴스타파와 시민단체 3곳은 오는 31일 윤석열 대통령이 검찰총장 시절에 쓴 특활비와 업추비 자료를 수령할 예정입니다.
현직 대통령의 세금 사용 실태가 어땠을지 반드시 취재와 검증이 필요한 부분입니다.
그 결과물은 약 한 달 뒤, 검찰예산 검증보도 ‘시즌2’를 통해 공개할 계획입니다.
끝으로 현재 진행 중인 검찰 특활비 문제에 대한 국회 국정조사 및 특검 도입 논의를 위한 청원 사이트 링크를 공유합니다.
우리가 낸 세금을 흥청망청 쓰면서 어떤 감시와 검증도 거부하는 검찰 특활비 제도의 개혁에 동의하신다면 동참해주시기를 부탁드립니다."""

VOICE = "ko-KR-SunHiNeural"
OUTPUT_FILE = "test.mp3"

VOICE_dict = {"male": "ko-KR-InJoonNeural",
              "female": "ko-KR-SunHiNeural"}


async def create_tts(TEXT_inp, gender) -> None:

    communicate = edge_tts.Communicate(TEXT_inp, VOICE_dict[gender])
    await communicate.save(OUTPUT_FILE)


async def amain() -> None:

    st.header("edge_tts in streamlit cloud")

    gender = st.selectbox("#### TTS 성별 선택", ["male", "female"], index=1)
    TEXT_inp = st.text_area("#### TTS 문장 입력", value=TEXT, height=20)

    if st.button("Submit"):
        await create_tts(TEXT_inp, gender)

        audio_file = open(OUTPUT_FILE,'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')
    else:
        st.write("문장을 입력하신 후 Submit 버튼을 눌러주세요.")

asyncio.run(amain())