import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="20/10 - Gửi Mẹ Yêu",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Quicksand:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(145deg, #fff0f6, #ffe0ec, #fff5f8);
    color: #71334c;
    font-family: 'Quicksand', sans-serif;
}
header, footer, #MainMenu {visibility: hidden;}
.block-container {
    max-width: 850px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
.hero {
    text-align: center;
    padding: 2rem 1rem;
    border: 1px solid white;
    border-radius: 28px;
    background: rgba(255,255,255,.65);
    box-shadow: 0 12px 35px rgba(174,69,111,.12);
}
.eyebrow {
    letter-spacing: .15em;
    color: #bd587e;
    font-size: .8rem;
    font-weight: 700;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    color: #b43f70;
    font-size: clamp(2.4rem, 8vw, 4rem);
    margin: .6rem 0;
}
.hero-sub {
    line-height: 1.9;
    color: #87415d;
}
.card {
    background: rgba(255,255,255,.82);
    border: 1px solid white;
    border-radius: 24px;
    padding: 1.5rem;
    margin: 1.2rem 0;
    box-shadow: 0 10px 28px rgba(174,69,111,.09);
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #b43f70;
    text-align: center;
    margin: .4rem 0 1rem;
}
.poem {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1rem, 3.5vw, 1.25rem);
    line-height: 2.05;
    color: #87415d;
    text-align: center;
}
.letter {
    white-space: pre-line;
    font-size: 1rem;
    line-height: 2;
    color: #704055;
}
.signature {
    font-family: 'Playfair Display', serif;
    color: #b43f70;
    text-align: right;
    font-size: 1.3rem;
    margin-top: 1rem;
}
.wish-pill {
    display: inline-block;
    background: #fff0f6;
    color: #a73562;
    border: 1px solid #ffd2e2;
    border-radius: 999px;
    padding: .5rem .8rem;
    margin: .2rem;
    font-weight: 700;
    font-size: .85rem;
}
div.stButton > button {
    background: linear-gradient(100deg, #e66d98, #c94e7c);
    color: white;
    border: 0;
    border-radius: 999px;
    padding: .75rem 1.2rem;
    font-weight: 700;
}
div.stButton > button:hover {
    color: white;
    border: 0;
}
.footer {
    text-align: center;
    color: #a65c79;
    line-height: 1.9;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Hieu ung hoa roi
components.html("""
<div id="petals"></div>
<style>
#petals {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
}
.petal {
    position: absolute;
    top: -30px;
    animation: fall linear infinite;
    opacity: .7;
}
@keyframes fall {
    to { transform: translateY(110vh) rotate(450deg); }
}
</style>
<script>
const root = document.getElementById('petals');
const flowers = ['🌸', '🌷', '💗', '✿'];
for (let i = 0; i < 18; i++) {
    const p = document.createElement('span');
    p.className = 'petal';
    p.textContent = flowers[Math.floor(Math.random()*flowers.length)];
    p.style.left = Math.random()*100 + '%';
    p.style.fontSize = (14+Math.random()*14) + 'px';
    p.style.animationDuration = (9+Math.random()*12) + 's';
    p.style.animationDelay = (-Math.random()*15) + 's';
    root.appendChild(p);
}
</script>
""", height=0)

# PHAN DAU TRANG
st.markdown("""
<div class="hero">
    <div style="font-size:2rem">🌷 🌸 💗 🌸 🌷</div>
    <div class="eyebrow">
        20 THÁNG 10 · NGÀY PHỤ NỮ VIỆT NAM
    </div>
    <div class="hero-title">Gửi Mẹ Yêu</div>
    <div class="hero-sub">
        Một món quà nhỏ dành cho người phụ nữ đặc biệt nhất trong lòng con.<br>
        <b>Chúc mẹ luôn hạnh phúc, bình an và được yêu thương thật nhiều.</b>
    </div>
</div>
""", unsafe_allow_html=True)

# PHẦN HIỂN THỊ ẢNH LOCAL
st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
st.image(
    "me_va_con.JPG", 
    caption="Một bó hoa nhỏ thay lời con muốn nói 💐", 
    use_container_width=True
)

# BAI THO 20/10 CUA ME
st.markdown("""
<div class="card">
    <div style="text-align:center;font-size:1.8rem">
        🌷 🌷 🌷
    </div>
    <div class="section-title">Lời chúc con gửi mẹ</div>
    <div class="poem">
        Ngày Phụ nữ Việt Nam hai mươi tháng Mười,<br>
        Chúc mẹ sức khỏe, luôn vui yêu đời.<br>
        Hạnh phúc, xinh đẹp, rạng ngời,<br>
        Mong mẹ luôn trẻ, nụ cười trên môi.<br><br>
        Mong mẹ cùng cha sức khỏe dồi dào,<br>
        Cuộc sống an lành, hạnh phúc bên nhau.<br>
        Gia đình êm ấm trước sau,<br>
        Tiếng cười hạnh phúc dài lâu tháng ngày. <span style="color:#e35c91">❤</span>
    </div>
    <div style="text-align:center;font-size:1.8rem;margin-top:1rem">
        💐 💐 💐
    </div>
</div>
""", unsafe_allow_html=True)

# NHUNG DIEU CON MONG
st.markdown("""
<div class="card" style="text-align:center">
    <div style="font-size:3rem">💗</div>
    <div class="section-title">Điều cả gia đình mong nhất</div>
    <p style="font-family:'Playfair Display',serif;font-size:1.2rem;line-height:1.9;color:#a73562">
        Mong mẹ luôn khỏe mạnh, cha luôn bình an,<br>
        và gia đình mình mãi là nơi đầy ắp yêu thương.
    </p>
    <span class="wish-pill">💗 Bình an</span>
    <span class="wish-pill">🌷 Sức khỏe</span>
    <span class="wish-pill">✨ Niềm vui</span>
    <span class="wish-pill">🌸 Hạnh phúc</span>
</div>
""", unsafe_allow_html=True)

# LA THU DANH RIENG CHO ME
st.markdown(
    '<div class="section-title">💌 Lá thư nhỏ dành cho mẹ</div>',
    unsafe_allow_html=True
)

if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

if st.button("💌 Mở lời chúc của con", use_container_width=True):
    st.session_state.letter_open = not st.session_state.letter_open

if st.session_state.letter_open:
    st.markdown("""
    <div class="card">
        <div class="letter">Mẹ yêu của con,

Nhân ngày 20/10, con chúc mẹ và bà ngoại luôn mạnh khỏe, vui vẻ, xinh đẹp và lúc nào cũng giữ được nụ cười trên môi. Chúc cha và mẹ luôn  tươi tắn, mạnh khoẻ và lúc nào cũng yêu đời.❤️🌷💐🌸🌺🌻

Chúc mẹ 20/10 thật vui và hạnh phúc!</div>
        <div class="signature">Con của mẹ 💗</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    🌷🌷🌷🌷🌷🌷<br>
    <b>20.10.2026 🌷</b>
</div>
""", unsafe_allow_html=True)
