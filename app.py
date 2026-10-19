from flask import Flask, render_template_string

app = Flask(__name__)

# Sua ten hai nguoi tai day
TEN_NGUOI_YEU = "Em Yeu"
TEN_NGUOI_GUI = "Nguoi thuong cua em"

PAGE = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gửi em yêu 💗</title>
<style>
:root{--pink:#d65f98;--deep:#a84d7d;--text:#75445f}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;color:var(--text);font-family:"Segoe UI",Arial,sans-serif;background:linear-gradient(145deg,#ffe5ef 0%,#f2e8ff 55%,#fff2e7 100%);overflow-x:hidden}
main{width:min(760px,92%);margin:0 auto;padding:28px 0 45px;text-align:center;position:relative;z-index:1}
.kicker{letter-spacing:3px;font-size:12px;text-transform:uppercase}
.hero-flower{font-size:54px;margin:18px 0 4px;animation:sway 3s ease-in-out infinite}
h1{font-family:Georgia,serif;color:var(--pink);font-size:clamp(35px,8vw,58px);margin:8px 0 12px}
.subtitle{line-height:1.8;margin:0 auto 24px;max-width:540px}
.card{background:rgba(255,255,255,.86);border:2px solid rgba(255,255,255,.95);border-radius:26px;padding:24px;margin:18px 0;box-shadow:0 12px 36px #b86d9620;backdrop-filter:blur(8px)}
.envelope{font-size:66px;margin:0 0 8px}
h2{color:var(--deep);font-family:Georgia,serif;margin:8px 0 12px}
p{line-height:1.85}
button{border:0;border-radius:999px;padding:13px 20px;cursor:pointer;font-size:15px;font-weight:700;color:white;background:linear-gradient(100deg,#ec91b9,#aa94e9);box-shadow:0 6px 15px #b46b9a2b;transition:transform .2s}
button:active{transform:scale(.97)}
.letter{display:none;text-align:left;margin-top:22px;padding:20px;background:#fff2f8;border-radius:18px}
.letter.show{display:block;animation:appear .45s ease}
.letter p{margin:0 0 15px}
.salute{text-align:center;font-family:Georgia,serif;color:var(--deep);font-size:24px;font-weight:bold;margin-bottom:18px}
.secret{display:none;background:#fff0f7;padding:18px;border-radius:18px;margin-top:18px;line-height:1.9}
.secret.show{display:block;animation:appear .4s ease}
.footer{margin-top:30px;font-size:13px;opacity:.8}
.float-layer{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.float-heart{position:absolute;bottom:-35px;animation:floatUp linear forwards;opacity:.8}
@keyframes floatUp{to{transform:translateY(-110vh) rotate(35deg);opacity:0}}
@keyframes appear{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes sway{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}}
@media(max-width:480px){main{width:92%;padding-top:22px}.card{padding:18px;border-radius:22px}.letter{padding:16px}button{width:100%}}
</style>
</head>
<body>
<div class="float-layer" id="floatLayer"></div>
<main>
  <div class="kicker">✿ MỘT MÓN QUÀ NHỎ DÀNH RIÊNG CHO EM ✿</div>
  <div class="hero-flower">💐</div>
  <h1>Happy 20/10</h1>
  <p class="subtitle">Gửi <strong>{{ girl }}</strong> — cô gái đặc biệt trong lòng anh.<br>Có một điều anh muốn nói với em bằng cả sự chân thành. 💗</p>

  <section class="card">
    <div class="envelope" id="envelope">💌</div>
    <h2>Một lá thư dành cho em</h2>
    <p>Em hãy mở lá thư này khi có một chút thời gian nhé. Anh đã gửi vào đây rất nhiều điều muốn nói với em.</p>
    <button id="openLetter">💌 Mở thư tình</button>

    <article class="letter" id="letter">
      <div class="salute">Gửi em yêu của anh 💗</div>
      <p>Anh đã nghĩ rất lâu không biết nên viết gì cho em trong ngày đặc biệt này. Anh muốn viết thật nhiều để em hiểu được tình cảm của anh, nhưng rồi anh nhận ra có những điều dù viết bao nhiêu câu chữ cũng khó mà nói hết được. Vậy nên hôm nay, anh muốn dành cho em một lá thư, không phải để nói những lời hoa mỹ nhất, mà để kể em nghe những điều thật lòng anh vẫn luôn giữ trong tim.</p>
      <p>Em biết không, trước khi gặp em, anh vẫn sống những ngày bình thường như bao ngày khác. Sáng thức dậy, làm những việc cần làm, rồi lại kết thúc một ngày. Nhưng từ khi có em, những điều bình thường ấy dường như có thêm một chút ý nghĩa. Anh bắt đầu mong chờ những tin nhắn, mong được nghe em kể chuyện, mong được biết hôm nay em vui hay buồn. Có những lúc chẳng có chuyện gì đặc biệt xảy ra, nhưng chỉ cần được nói chuyện với em thôi, anh cũng cảm thấy ngày hôm đó đáng yêu hơn một chút.</p>
      <p>Anh không biết từ lúc nào em trở thành người mà anh muốn chia sẻ nhiều điều đến vậy. Có những chuyện nhỏ xíu anh cũng muốn kể em nghe, có những khoảnh khắc vui vẻ anh muốn em là người đầu tiên biết đến. Đôi khi anh chỉ muốn hỏi em rằng hôm nay có mệt không, đã ăn uống đầy đủ chưa, có chuyện gì khiến em buồn lòng không. Những câu hỏi có thể chẳng lớn lao gì, nhưng phía sau chúng là sự quan tâm mà anh thật lòng muốn dành cho em.</p>
      <p>Anh thích em, không chỉ vì những lúc em vui vẻ hay những khi em xinh đẹp nhất. Anh còn thương cả những lúc em mệt mỏi, những khi em chẳng muốn nói chuyện với ai, những lúc em suy nghĩ nhiều và không biết phải chia sẻ cùng ai. Anh không cần em phải lúc nào cũng tỏ ra mạnh mẽ trước mặt anh. Nếu có ngày em cảm thấy yếu lòng, em vẫn có thể dựa vào anh một chút. Em không cần phải luôn ổn, bởi vì anh biết rằng ai cũng có những ngày không dễ dàng.</p>
      <p>Anh cũng hiểu rằng yêu nhau không có nghĩa là lúc nào chúng ta cũng hiểu được suy nghĩ của đối phương. Sẽ có những lúc anh nói điều gì đó chưa đúng, có những lúc em buồn mà anh lại vô tình không nhận ra. Có thể chúng ta sẽ giận nhau vì những chuyện nhỏ nhặt, hoặc đôi khi vì cả hai đều muốn được thấu hiểu nên chẳng ai chịu nói ra trước. Nhưng anh mong rằng dù có chuyện gì xảy ra, chúng ta vẫn nhớ lý do vì sao mình bắt đầu, vẫn dành cho nhau đủ kiên nhẫn để lắng nghe và đủ chân thành để sửa đổi.</p>
      <p>Anh không muốn trở thành người chỉ biết nói thương em mỗi khi mọi chuyện tốt đẹp. Anh muốn học cách thể hiện tình yêu bằng những điều thiết thực hơn. Là khi anh nhớ hỏi han em sau một ngày dài, là khi anh chịu lắng nghe thay vì vội vàng phán xét, là khi anh biết nhận lỗi nếu mình sai, và là khi anh cố gắng trưởng thành hơn để tình yêu của chúng ta có thể bình yên hơn từng ngày.</p>
      <p>Nếu có lúc anh chưa làm tốt, anh mong em cho anh cơ hội để hiểu em hơn. Anh không hứa rằng mình sẽ chẳng bao giờ mắc sai lầm, nhưng anh mong mỗi sai lầm đều giúp anh biết cách yêu em tốt hơn. Anh muốn em cảm nhận được rằng tình cảm của anh không chỉ nằm trong những tin nhắn ngọt ngào, mà còn ở cách anh trân trọng em khi chúng ta ở bên nhau và cả khi mỗi người đang bận rộn với cuộc sống riêng.</p>
      <p>Em à, anh mong em đừng bao giờ cảm thấy mình phải trở thành một người khác mới xứng đáng được yêu thương. Em không cần phải hoàn hảo, không cần phải luôn vui vẻ, cũng không cần phải cố gắng làm hài lòng tất cả mọi người. Em cứ là chính em, cứ theo đuổi những điều em thích, cứ có những ước mơ của riêng mình. Anh mong được nhìn thấy em trưởng thành, tự tin và hạnh phúc với cuộc sống của em. Anh muốn được đồng hành cùng em trên hành trình ấy, cùng cổ vũ em khi em cố gắng và cùng vui với em khi em đạt được điều mình mong muốn.</p>
      <p>Anh cũng mong em luôn biết cách thương lấy bản thân mình. Đừng thức quá khuya chỉ vì những chuyện khiến em buồn, đừng tự trách mình quá nhiều khi có điều gì không như ý, và đừng quên rằng em cũng xứng đáng được nghỉ ngơi sau những ngày cố gắng. Anh có thể không ở cạnh em trong mọi khoảnh khắc, nhưng anh luôn mong em biết rằng em có giá trị, có những điều đáng quý của riêng mình và xứng đáng được đối xử bằng sự tử tế.</p>
      <p>Có lẽ điều anh mong nhất trong tình yêu này không phải là chúng ta phải có thật nhiều món quà đắt tiền hay những khoảnh khắc lãng mạn như trong phim. Anh chỉ mong chúng ta có thể cùng nhau trải qua những ngày bình thường mà vẫn thấy vui. Cùng đi ăn một món mình thích, cùng kể nhau nghe những câu chuyện không đầu không cuối, cùng cười vì những chuyện ngốc nghếch, hoặc chỉ đơn giản là ngồi cạnh nhau mà không cần phải làm điều gì đặc biệt.</p>
      <p>Anh muốn sau này, khi nhắc về những ngày tháng chúng ta đã đi qua, cả hai có thể mỉm cười vì đã từng dành cho nhau những điều chân thành. Anh muốn chúng ta có những kỷ niệm mà nhiều năm sau vẫn nhớ, những câu chuyện mà mỗi lần kể lại vẫn thấy vui, và những khoảnh khắc khiến mình biết rằng quãng thời gian ở bên nhau đã thật sự có ý nghĩa.</p>
      <p>Anh không thể biết trước tương lai sẽ như thế nào. Cuộc sống có thể thay đổi, mỗi người sẽ có thêm những trách nhiệm, những khó khăn và những mục tiêu riêng. Nhưng nếu chúng ta vẫn còn yêu thương nhau, vẫn còn muốn lắng nghe và cùng nhau cố gắng, anh mong chúng ta sẽ không dễ dàng từ bỏ chỉ vì những lúc mọi thứ trở nên khó khăn. Anh muốn tình yêu của mình không chỉ đẹp ở lúc bắt đầu, mà còn đủ chân thành để được vun đắp qua từng ngày.</p>
      <p>Nhân ngày 20/10, anh muốn dành cho em những lời chúc thật dịu dàng. Chúc em luôn xinh đẹp theo cách riêng của mình, luôn có đủ sức khỏe để làm những điều em yêu thích, đủ tự tin để theo đuổi ước mơ và đủ bình yên để tận hưởng những điều nhỏ bé trong cuộc sống. Chúc những ngày sắp tới của em có nhiều tiếng cười hơn nước mắt, có nhiều niềm vui hơn lo lắng, và luôn có những người thật lòng yêu thương em ở bên cạnh.</p>
      <p>Nếu hôm nay em nhận được nhiều lời chúc, anh hy vọng lá thư này sẽ là một món quà nhỏ khiến em nhớ lâu hơn một chút. Anh không biết những dòng chữ này có thể khiến em cảm động đến đâu, nhưng anh đã viết chúng bằng tất cả những điều chân thành mà anh muốn gửi đến em.</p>
      <p>Cảm ơn em vì đã cho anh cơ hội được biết em, được quan tâm em và được gọi em là người anh thương. Cảm ơn những lần em dành thời gian cho anh, những lúc em lắng nghe anh kể chuyện, những tin nhắn tưởng chừng bình thường và cả những khoảnh khắc mà có thể em đã quên nhưng anh vẫn âm thầm trân trọng.</p>
      <p>Anh không cần em phải trả lời lá thư này bằng những lời thật dài. Anh chỉ mong khi đọc xong, em hiểu rằng tình cảm anh dành cho em là điều anh nghiêm túc nâng niu. Anh muốn chúng ta có thể nói với nhau những điều thật lòng, cùng học cách trưởng thành và cùng xây dựng một tình yêu mà cả hai đều cảm thấy được yêu thương, được tôn trọng và được là chính mình.</p>
      <p><strong>Em à, nếu có ai hỏi anh điều gì khiến anh vui khi nghĩ về em, có lẽ anh sẽ chẳng biết bắt đầu từ đâu.</strong> Bởi vì có quá nhiều điều nhỏ bé đã khiến em trở nên đặc biệt trong lòng anh. Anh chỉ biết rằng giữa cuộc sống có rất nhiều người đến rồi đi, anh thật sự trân trọng việc chúng ta đã gặp nhau và có cơ hội viết nên câu chuyện của riêng mình.</p>
      <p>Ngày 20/10, anh chúc cô gái anh thương có một ngày thật đẹp. Mong em luôn giữ được nụ cười, luôn có những điều để hy vọng và luôn nhớ rằng em không cần phải làm điều gì lớn lao mới xứng đáng được yêu thương.</p>
      <p>Và nếu được nói với em một điều sau tất cả những dòng chữ này, anh chỉ muốn nói rằng: <strong>Cảm ơn em vì đã đến. Cảm ơn em vì đã là chính em. Và cảm ơn em vì đã cho anh một người để thương, một người để nhớ, một người khiến anh muốn cố gắng trở thành phiên bản tốt hơn của chính mình.</strong></p>
      <p>Anh không biết tương lai sẽ viết tiếp câu chuyện của chúng ta bằng những điều gì, nhưng anh hy vọng khi cả hai cùng nhìn về phía trước, chúng ta vẫn muốn nắm tay nhau và cùng bước tiếp.</p>
      <p><strong>Anh thương em. Không phải chỉ riêng ngày 20/10, mà còn trong những ngày bình thường chẳng có dịp gì đặc biệt.</strong> 💗</p>
      <p>Mong em luôn bình an, luôn hạnh phúc và luôn cảm nhận được sự chân thành trong tình yêu này.</p>
      <p style="text-align:right"><strong>Thương em thật nhiều — hôm nay, ngày mai và những ngày chúng ta còn chọn ở bên nhau. 💌<br>{{ boy }}</strong></p>
    </article>
  </section>

  <section class="card">
    <div style="font-size:42px">🐱🌷</div>
    <h2>Một điều bí mật...</h2>
    <p>Có một lời nhắn nhỏ anh muốn dành riêng cho em.</p>
    <button id="secretButton">✨ Khám phá bất ngờ</button>
    <div class="secret" id="secret">
      💖 Giữa rất nhiều người trên thế giới, anh thật vui vì người anh thương là em.<br>
      Anh không mong mọi ngày đều hoàn hảo, chỉ mong những ngày không hoàn hảo ấy, chúng ta vẫn chọn lắng nghe và thương nhau.<br>
      <strong>Em luôn là một điều thật đáng quý đối với anh. 🥰</strong>
    </div>
  </section>
  <button id="heartButton" style="max-width:300px">💗 Gửi em một cơn mưa tim</button>
  <div class="footer">Được làm bằng tất cả sự chân thành ♡ Dành riêng cho {{ girl }} · 20/10 🌸</div>
</main>
<script>
const openLetter = document.getElementById('openLetter');
const letter = document.getElementById('letter');
openLetter.addEventListener('click', () => {
  letter.classList.toggle('show');
  const opened = letter.classList.contains('show');
  openLetter.textContent = opened ? '💗 Gấp thư lại' : '💌 Mở thư tình';
  document.getElementById('envelope').textContent = opened ? '💖' : '💌';
});
document.getElementById('secretButton').addEventListener('click', () => {
  const secret = document.getElementById('secret');
  secret.classList.toggle('show');
  document.getElementById('secretButton').textContent =
    secret.classList.contains('show') ? '💗 Anh nói hết rồi đó' : '✨ Khám phá bất ngờ';
});
document.getElementById('heartButton').addEventListener('click', () => {
  const layer = document.getElementById('floatLayer');
  const emojis = ['💗','💕','💖','🌸','✨'];
  for (let i = 0; i < 24; i++) {
    const heart = document.createElement('span');
    heart.className = 'float-heart';
    heart.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    heart.style.left = Math.random() * 100 + '%';
    heart.style.fontSize = (18 + Math.random() * 20) + 'px';
    heart.style.animationDuration = (2.5 + Math.random() * 2.5) + 's';
    layer.appendChild(heart);
    setTimeout(() => heart.remove(), 5200);
  }
});
setInterval(() => {
  const layer = document.getElementById('floatLayer');
  const heart = document.createElement('span');
  heart.className = 'float-heart';
  heart.textContent = ['♡','💗','🌸'][Math.floor(Math.random() * 3)];
  heart.style.left = Math.random() * 100 + '%';
  heart.style.fontSize = (12 + Math.random() * 14) + 'px';
  heart.style.animationDuration = (5 + Math.random() * 4) + 's';
  layer.appendChild(heart);
  setTimeout(() => heart.remove(), 9500);
}, 900);
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE, girl=TEN_NGUOI_YEU, boy=TEN_NGUOI_GUI)

if __name__ == "__main__":
    print("Website 20/10 dang chay!")
    print("Mo Chrome tai: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
