# Bài toán chuyển động

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/bai-toan-chuyen-dong.html -->
Bài viết hướng dẫn phương pháp giải bài toán chuyển động thường gặp trong các đề thi trắc nghiệm Toán 12 và đề thi THPT Quốc gia môn Toán.

## A. PHẠM VI ỨNG DỤNG

**1**. Các bài toán về quãng đường. Chẳng hạn:

+ Tính quãng đường mà vật di chuyển sau một khoảng thời gian.

+ Tính quãng đường xa nhất, gần nhất của một đối tượng di chuyển.

+ Tính quãng đường mà một đối tượng có thể đi được trong bài toán chuyển động nhanh dần, chậm dần đều.

**2**. Tìm gia tốc của một đối tượng chuyển động.

**3**. Tìm vận tốc tức thời tại một thời điểm, vận tốc lớn nhất, vận tốc nhỏ nhất của đối tượng chuyển động.

… … …

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/bai-toan-chuyen-dong.html -->
## B. CƠ SỞ CỦA PHƯƠNG PHÁP

1. Quãng đường của vật A di chuyển trong khoảng thời gian $t$ với vận tốc $v$ là: $s = v.t$ là công thức tính trong chuyển động đều. Tuy nhiên, trong thực tế một đối tượng không thể di chuyển với một vận tốc cố định, bởi lẽ quá trình chuyển động phụ thuộc rất nhiều những yếu tố ngoại cảnh như: bề mặt đường, hình dáng đường, độ dốc … Do đó, thực tế chúng ta có thể tính toán cho một thời điểm nhất định nào đó.

2. Xét mối quan hệ giữa các đại lượng vận tốc, quãng đường và thời gian ta có:

+ Đạo hàm của quãng đường là vận tốc: $s'(t) = v(t).$

+ Nguyên hàm của vận tốc là quãng đường: $s(t) = \int v (t)dt.$

Trong đó: $s(t)$ và $v(t)$ lần lượt là quãng đường và vận tốc tại thời điểm $t.$

3. Xét mối liên hệ giữa gia tốc, vận tốc tại thời điểm $t$ là:

+ Đạo hàm của vận tốc chính là gia tốc: $v'(t) = a(t).$

+ Nguyên hàm của gia tốc chính là vận tốc: $v(t) = \int a (t)dt.$

Trong đó: $a(t)$ và $v(t)$ lần lượt là gia tốc và vận tốc tại thời điểm $t.$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/12/bai-toan-chuyen-dong.html -->
## C. CHÚ Ý

Một số trường hợp vật chuyển động nhanh dần đều, chậm dần đều … trong một khoảng thời gian $t \in [a;b]$ thì:

+ Quãng đường vật đi được: $s(t) = \int_a^b v (t)dt.$

+ Vận tốc vật di chuyển: $v(t) = \int_a^b a (t)dt.$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/12/bai-toan-chuyen-dong.html -->
## D. CÂU HỎI TRẮC NGHIỆM VẬN DỤNG

## Câu 1. Một vật chuyển động trên đường thẳng có tọa độ xác định theo phương trình $x = 6 + 7{t^2} + 2{t^3}$ (m). Gia tốc của vật ở thời điểm $t= 2s$ là:

A. $38$ $m/{s^2}.$

B. $9$ $m/{s^2}.$

C. $26$ $m/{s^2}.$

D. $2$ $m/{s^2}.$

Hướng dẫn giải:

Ta có gia tốc là đạo hàm cấp $2$ của chuyển động: $a(t) = x”(t)$ $= 14 + 12t.$

Vậy gia tốc của vật ở thời điểm $t = 2s$ là: $a(2) = 14 + 12.2 = 38.$

> **Đáp án: A**

## Câu 2. Sau khi phát hiện một bệnh dịch, các chuyên gia y tế ước tính số người nhiễm bệnh kể từ ngày xuất hiện bệnh nhân đầu tiên đến ngày thứ $t$ là $f(t) = 45{t^2} – {t^3}$ (kết quả khảo sát được trong tháng $8$ vừa qua). Nếu xem $f'(t)$ là tốc độ truyền bệnh (người/ngày) tại thời điểm $t.$ Hỏi tốc độ truyền bệnh sẽ lớn nhất vào ngày thứ bao nhiêu?

A. $12.$

B. $30.$

C. $20.$

D. $15.$

Hướng dẫn giải:

Tốc độ truyền bệnh (người/ngày) tại thời điểm $t$ là $f'(t) = 90t – 3{t^2}.$

Ta thấy $f'(t)$ là một Parabol có hệ số $a = -3 < 0$ nên $f'(t)$ đạt giá trị lớn nhất khi $t=15$ (s). Khi đó, tốc độ truyền bệnh lớn nhất là $f'(15) = 675.$

> **Đáp án: D**

## Câu 3. Một chất điểm chuyển động thẳng trên trục với biểu thức tọa độ $x = \frac{1}{3}{t^3} – 2{t^2} + 6t + 1$ (cm), $t$ tính theo giây (s). Hỏi từ thời điểm $t=0,5s$ đến thời điểm $t=5s$ thì vận tốc lớn nhất của chất điểm là bao nhiêu?

A. ${v_{\max }} = 1$ (cm/s).

B. ${v_{\max }} = \frac{{68}}{3}$ (cm/s).

C. ${v_{\max }} = \frac{{23}}{3}$ (cm/s).

D. ${v_{\max }} = 11$ (cm/s).

Hướng dẫn giải:

Vận tốc tại thời điểm $t$ giây là $v(t) = (x)’$ $= {t^2} – 4t + 6.$

Lập BBT của hàm số $v(t)$ trên đoạn $[0,5;5].$

$\Rightarrow {v_{\max }} = 11$ cm/s.

> **Đáp án: D**

## Câu 4. Một chất điểm chuyển động thẳng trên trục với biểu thức tọa độ $x = \frac{1}{3}{t^3} – 2{t^2} + 6t + 1$ (cm), $t$ tính theo giây (s). Hỏi từ thời điểm $t = 1s$ đến thời điểm $t = 5s$ thì vận tốc nhỏ nhất của chất điểm là bao nhiêu?

A. ${v_{\min }} = 1$ (cm/s).

B. ${v_{\min }} = 2$ (cm/s).

C. ${v_{\min }} = \frac{{23}}{3}$ (cm/s).

D. ${v_{\min }} = \frac{{13}}{3}$ (cm/s).

Hướng dẫn giải:

Vận tốc tại thời điểm $t$ giây là:

$v(t) = (x)’$ $= {t^2} – 4t + 6$ $= {(t – 2)^2} + 2 \ge 2$ $\Rightarrow {v_{\min }} = 2$ cm/s.

> **Đáp án: B**

## Câu 5. Cho chuyển động thẳng xác định bởi phương trình $S = \frac{1}{2}\left( {{t^4} + 3{t^2}} \right)$, $t$ được tính bằng giây, $S$ được tính bằng mét. Tìm vận tốc của chuyển động tại $t=4$ (giây).

A. $v = 140$ m/s.

B. $v=150$ m/s.

C. $v= 200$ m/s.

D. $v=0$ m/s.

Hướng dẫn giải:

Ta có vận tốc của chuyển động tại $t$ (giây):

$S'(t) = v(t)$ $= \left( {\frac{{{t^4}}}{2} + \frac{3}{2}{t^2}} \right)’$ $= 2{t^3} + 3t$ $\Rightarrow v(4) = 140$ m/s.

> **Đáp án: A**

## Câu 6. Một chất điểm chuyển động theo qui luật $s = 6{t^2} – {t^3}$ (trong đó $t$ là khoảng thời gian tính bằng giây mà chất điểm bắt đầu chuyển động). Tính thời điểm $t$ (giây) mà tại đó vận tốc (m/s) của chuyển động đạt giá trị lớn nhất.

A. $t = 2.$

B. $t=4.$

C. $t=1.$

D. $t=3.$

Hướng dẫn giải:

Ta có vận tốc của chuyển động tại $t$ (giây):

$v(t) = \left( {6{t^2} – {t^3}} \right)’$ $= 12t – 3{t^2}.$

Suy ra $\max v(t) = 12$ khi $t= 2.$

> **Đáp án: A**

## Câu 7. Một con cá hồi bơi ngược dòng để vượt một khoảng cách là $400$ km. Vận tốc dòng nước là $10$ km/h. Nếu vận tốc bơi của cá khi nước đứng yên là $v$ (km/h) thì năng lượng tiêu hao của cá trong $t$ giờ được cho bởi công thức $E(v) = c{v^3}t$, trong đó $c$ là một hằng số dương, $E$ được tính bằng jun. Tìm vận tốc của cá khi nước đứng yên để năng lượng tiêu hao là ít nhất.

A. $12$ (km/h).

B. $15$ (km/h).

C. $18$ (km/h).

D. $20$ (km/h).

Hướng dẫn giải: Thời gian cá hồi bơi ngược dòng để vượt một khoảng cách là $400$ km là: $\frac{{400}}{{v – 10}}$ (h).

Suy ra công thức $E(v) = c{v^3}t = c\frac{{400{v^3}}}{{v – 10}}.$

Ta thay thế các đáp án của đề vào ta được bảng sau:

A. $12$ (km/h)
$E = 345600c$

B. $15$ (km/h)
$E = 270000c$

C. $18$ (km/h)
$E = 291600c$

D. $20$ (km/h)
$E = 3200000$

> **Đáp án: B**

## Câu 8. Một xà lan bơi ngược dòng sông để vượt qua một khoảng cách $30$ km. Vận tốc dòng nước là $6$ km/h. Nếu vận tốc của xà lan khi nước đứng yên là $v$ (km/h) thì lượng dầu tiêu hao của xà lan trong $t$ giờ được cho bởi công thức: $E(v) = c{v^3}t$ trong đó $c$ là một hằng số, $E$ được tính bằng lít. Tìm vận tốc của xà lan khi nước đứng yên để lượng dầu tiêu hao là nhỏ nhất.

A. $v=18$ (km/h).

B. $v = 12$ (km/h).

C. $v= 24$ (km/h).

D. $v = 9$ (km/h).

Hướng dẫn giải:

Thời gian xà lan bơi ngược dòng để vượt một khoảng cách $30$ km là: $\frac{{30}}{{v – 6}}$ (h).

Suy ra công thức $E(v) = c{v^3}t = c\frac{{30{v^3}}}{{v – 6}}.$

Ta thay thế bốn đáp án của đề vào ta được bảng sau:

A. $18$ (km/h)
$E = 14580c$

B. $12$ (km/h)
$E = 8640c$

C. $24$ (km/h)
$E = 23040c$

D. $9$ (km/h)
$E = 7290c$

> **Đáp án: D**

## Câu 9. Một con cá hồi bơi ngược dòng để vượt một khoảng cách là $200$ km. Vận tốc của dòng nước là $8$ km/h. Nếu vận tốc bơi của cá khi nước đứng yên là $v$ (km/h) thì năng lượng tiêu hao của cá trong $t$ giờ được cho bởi công thức: $E(v) = c{v^3}t$ (trong đó $c$ là một hằng số dương, $E$ được tính bằng jun). Tìm vận tốc bơi của cá khi nước đứng yên để năng lượng tiêu hao là ít nhất.

A. $12$ km/h.

B. $9$ km/h.

C. $10$ km/h.

D. $15$ km/h.

Hướng dẫn giải:

Thời gian cá hồi bơi ngược dòng để vượt qua khoảng cách $200$ km là: $\frac{{200}}{{v – 8}}$ (h).

Suy ra công thức $E(v) = c{v^3}t = c\frac{{200{v^3}}}{{v – 8}}.$

Ta thay thế các đáp án của đề vào ta được bảng sau:

A. $12$ (km/h)
$E = 86400c$

B. $9$ (km/h)
$E =145800c$

C. $10$ (km/h)
$E = 100000c$

D. $15$ (km/h)
$E = 96 429c$

> **Đáp án: A**

## Câu 10. Một đoàn tàu chuyển động thẳng khởi hành từ một nhà ga. Quãng đường $S(t)$ đi được của đoàn tàu là một hàm số của thời gian $t$ (s), hàm số đó là $S(t) = 6{t^2} – {t^3}.$ Thời điểm $t$ (s) mà tại đó vận tốc $v$ (m/s) của chuyển động đạt giá trị lớn nhất là:

A. $t = 6s.$

B. $t = 4s.$

C. $t = 2s.$

D. $t = 5s.$

Hướng dẫn giải:

Ta có $v(t) = S'(t)$ $= 12t – 3{t^2}$ $= f(t)$ và $f'(t) = 12 – 6t = 0$ $\Leftrightarrow t = 2.$

> **Đáp án: C**

## Câu 11. Một đoàn tàu chuyển động thẳng khởi hành từ một nhà ga. Biết quãng đường đi được của đoàn tàu là một hàm số theo thời gian $y = f(t)$ $= {t^3} – 3{t^2} + 9t + 35.$ Tính vận tốc lớn nhất đạt được trong thời gian từ khi khởi hành đến $5$ giờ sau đó (biết đơn vị vận tốc là km/h).

A. $35$ (km/h).

B. $130$ (km/h).

C. $42$ (km/h).

D. $54$ (km/h).

Hướng dẫn giải:

Ta có vận tốc đoàn tàu là hàm số theo thời gian $y = g(t)$ $= f'(t) = 3{t^2} – 6t + 9.$

Xét trên đoạn $[0;5]$, ta có $g'(t) = 0$ $\Leftrightarrow t = 1$ $\Rightarrow \max g(5) = 54$ km/h.

Vậy vận tốc lớn nhất đạt được trong thời gian từ khi khởi hành đến $5h$ sau đó là $54$ km/h.

> **Đáp án: D**

## Câu 12. Một nhà sản xuất máy ghi âm với chi phí là $40$ đôla/cái. Ông ước tính rằng nếu máy ghi âm bán được với giá $x$ đôla/cái thì mỗi tháng khách hàng sẽ mua $(120-x)$ cái. Biểu diễn lợi nhuận hàng tháng của nhà sản xuất bằng một hàm theo giá bán (gọi hàm lợi nhuận là $f(x)$ và giá bán là $x$), khi đó hàm cần tìm là:

A. $f(x) = – {x^2} + 120x.$

B. $f(x) = – {x^2} + 120x + 40.$

C. $f(x) = {x^2} – 120x + 40.$

D. $f(x) = – {x^2} + 160x – 4800.$

Hướng dẫn giải:

Lợi nhuận hàng tháng của nhà sản xuất là:

$f(x) = (120 – x)x – (120 – x)40$ $= – {x^2} + 160x – 4800.$

> **Đáp án: D**

## Câu 13. Một vật chuyển động với vận tốc $v(t)$ (m/s) có gia tốc $v'(t) = \frac{3}{{t + 1}}$ $\left( {m/{s^2}} \right).$ Vận tốc ban đầu của vật là $6$ (m/s). Hỏi vận tốc của vật sau $10$ giây (làm tròn kết quả đến hàng đơn vị).

A. $13$ (m/s).

B. $3$ (m/s).

C. $0,43$ (m/s).

D. $5,43$ (m/s).

Hướng dẫn giải:

Ta có: $v(t) = \int {\frac{3}{{t + 1}}} dt$ $= 3\ln (t + 1) + c.$

Mà $v(0) = 6$ $\Rightarrow c = 6$ $\Rightarrow v(t) = 3\ln (t + 1) + 6.$

$v(10) = 3\ln 11 + 6 \approx 13$ (m/s).

Kết quả: $13$ (m/s).

> **Đáp án: A**

## Câu 14. Vận tốc của một vật chuyển động là $v(t) = \frac{1}{{2\pi }} + \frac{{\sin (\pi t)}}{\pi }$ (m/s). Tính quãng đường di chuyển của vật đó trong khoảng thời gian $1,5$ giây (làm tròn kết quả đến hàng phần trăm).

A. $1,43$ (m/s).

B. $0,43$ (m/s).

C. $0,34$ (m/s).

D. $0,54$ (m/s).

Hướng dẫn giải:

Quãng đường $S = \int_0^{15} {\left[ {\frac{1}{{2\pi }} + \frac{{\sin (\pi t)}}{\pi }} \right]dt}$ $= \frac{3}{{4\pi }} + \frac{1}{{{\pi ^2}}} \approx 0,34.$

> **Đáp án: C**

## Câu 15. Vận tốc của một vật chuyển động là $v(t) = 1,2 + \frac{{{t^2} + 4}}{{t + 3}}$ (m/s). Tính quãng đường di chuyển của vật đó trong khoảng thời gian $4$ giây (làm tròn kết quả đến hàng phần trăm).

A. $11,81$ (m/s).

B. $8,89$ (m/s).

C. $10,89$ (m/s).

D. $12,18$ (m/s).

Hướng dẫn giải:

Quãng đường mà vật đi được trong khoảng thời gian $4$ (s) là:

$S(t) = \int_0^4 {\left( {1,2 + \frac{{{t^2} + 4}}{{t + 3}}} \right)dt}$ $= \int_0^4 {\left( {t – 1,8 + \frac{{13}}{{t + 3}}} \right)dt} .$

$= \left. {\frac{1}{2}{{(t – 1,8)}^2}} \right|_0^4$ $+ \left. {13\ln (t + 3)} \right|_0^4$ $\approx 11,81$ (m).

> **Đáp án: A**

## Câu 16. Một xe chở hàng chạy với vận tốc $25$ m/s thì tài xế đạp phanh; từ thời điểm đó, xe chuyển động chậm dần đều với vận tốc $v(t) = – 2t + 25$ (m/s), trong đó $t$ là khoảng thời gian tính bằng giây, kể từ lúc bắt đầu đạp phanh. Hỏi từ lúc đạp phanh đến khi dừng hẳn, xe còn di chuyển bao nhiêu mét?

A. $\frac{{625}}{4}$ m.

B. $\frac{{625}}{2}$ m.

C. $2$ m.

D. $\frac{{25}}{2}$ m.

Hướng dẫn giải:

Xe chở hàng còn đi thêm được $\frac{{25}}{2}$ giây.

Quãng đường cần tìm là: $S = \int_0^{\frac{{25}}{2}} {( – 2t + 25)dt}$ $= \frac{{625}}{4}$ (m).

> **Đáp án: B**

## Câu 17. Một ô tô đang chạy với tốc độ $36$ km/h thì hãm phanh, chuyển động chậm dần đều với phương trình vận tốc $v = 10 – 0,5t$ (m/s). Hỏi ô tô chuyển động được quãng đường bao nhiêu thì dừng lại?

A. $100$ m.

B. $200$ m.

C. $300$ m.

D. $400$ m.

Hướng dẫn giải:

Ta có: ${v_0} = 36$ km/h $=10$ m/s ứng với ${t_0} = 0.$

${v_1} = 10 – 0,5{t_1} = 0$ nên ${t_1} = 20.$

Do đó: quãng đường $S = \int_0^{20} {( – 0,5t + 10)dt = 100}$ (m).

> **Đáp án: A**

## Câu 18. Bạn Minh ngồi trên máy bay đi du lịch thế giới với vận tốc chuyển động của máy bay là $v(t) = 3{t^2} + 5$ (m/s). Quãng đường máy bay bay từ giây thứ $4$ đến giây thứ $10$ là:

A. $820$ m.

B. $252$ m.

C. $1134$ m.

D. $966$ m.

Hướng dẫn giải:

Quãng đường máy bay bay từ giây thứ $4$ đến giây thứ $10$ là:

$S = \int_4^{10} {\left( {3{t^2} + 5} \right)dt}$ $= 966$ m.

> **Đáp án: D**

## Câu 19. Một vật chuyển động chậm dần đều với vận tốc $v(t) = 160 – 10t$ (m/s). Quãng đường mà vật chuyển động từ thời điểm $t = 0$ (s) đến thời điểm mà vật dừng lại là:

A. $1028$ m.

B. $1280$ m.

C. $1308$ m.

D. $1380$ m.

Hướng dẫn giải:

Gọi ${t_0}$ là thời điểm vật dừng lại. Ta có $v\left( {{t_0}} \right) = 0.$ Suy ra ${t_0} = 6.$

Vậy $S = \int_0^{16} {(160 – 10t)dt}$ $= 1280$ (m).

> **Đáp án: A**

## Câu 20. Một vật chuyển động với vận tốc thay đổi theo thời gian được tính bởi công thức $v(t) = 3t + 2$ (m/s), thời gian tính theo đơn vị giây, quãng đường vật đi được tính theo đơn vị mét. Biết tại thời điểm $t = 2s$ thì vật đi đến quãng đường là $10$ m. Hỏi tại thời điểm $t = 30s$ thì vật đi được quãng đường là bao nhiêu?

A. $1410$ m.

B. $1140$ m.

C. $300$ m.

D. $240$ m.

Hướng dẫn giải:

Quãng đường tại thời gian $t:$ $S(t) = \int {(3t + 2)dt}$ $= \frac{3}{2}{t^2} + 2t + C.$

Mà $S(2) = 10$ $\Rightarrow C = 0$ $\Rightarrow S(t) = \frac{3}{2}{t^2} + 2t.$

Tại thời điểm $t = 30s$ $\Rightarrow S(30) = 1410.$

> **Đáp án: A**

## Câu 21. Một ô tô xuất phát với vận tốc ${v_1}(t) = 2t – 10.$ Sau khi đi được một khoảng thời gian ${t_1}$ thì bất ngờ gặp chướng ngại vật và đạp phanh gấp với vận tốc ${v_2}(t) = 20 – 4t$ (m/s) và đi thêm một khoảng thời gian ${t_2}$ nữa thì dừng lại. Biết tổng thời gian ${t_1}$ từ lúc xuất phát đến lúc dừng lại là $4$ (s). Hỏi xe đã đi được quãng đường là bao nhiêu mét?

A. $57$ m.

B. $64$ m.

C. $50$ m.

D. $47$ m.

Hướng dẫn giải:

Đến lúc phanh vận tốc của xe là: $2{t_1} + 10$, đó cũng là vận tốc khởi điểm cho quãng đường đạp phanh; sau khi đi thêm ${t_2}$ thì vận tốc là $0$ nên:

$2{t_1} + 10 = 20 – 4{t_2}$ $\Leftrightarrow {t_1} + 2{t_2} = 5.$

Lại có ${t_1} + {t_2} = 4$ lập hệ được 
$$
\left\{ {\begin{array}{l}
{{t_1} = 3s}\\
{{t_2} = 1s}
\end{array}} \right..
$$

Tổng quãng đường đi được là: $S = \int_0^3 {(2t + 10)dt}$ $+ \int_0^1 {(20 – 4t)dt} = 57$ (m).

> **Đáp án: A**

## Câu 22. Một ô tô chạy với vận tốc $20$ m/s thì người lái xe đạp phanh còn được gọi là “thắng”. Sau khi đạp phanh, ô tô chuyển động chậm dần đều với vận tốc $v(t) = – 40t + 20$ (m/s). Trong đó $t$ là khoảng thời gian tính bằng giây kể từ lúc bắt đầu đạp phanh. Quãng đường ô tô di chuyển từ lúc đạp phanh đến khi dừng hẳn là bao nhiêu?

A. $2$ m.

B. $3$ m.

C. $4$ m.

D. $5$ m.

Hướng dẫn giải:

Lấy mốc thời gian là lúc ô tô bắt đầu phanh $(t =0).$

Gọi $T$ là thời điểm ô tô dừng lại. Khi đó vận tốc lúc dừng là $v(T)=0.$

Vậy thời gian từ lúc đạp phanh đến lúc dừng là:

$v(T) = 0$ $\Leftrightarrow – 40T + 20 = 0$ $\Leftrightarrow T = \frac{1}{2}.$

Gọi $s(t)$ là quãng đường ô tô đi được trong khoảng thời gian $T.$

Ta có $v(T) = s'(t)$ suy ra $s(t)$ là nguyên hàm của $v(T).$

Vậy trong $\frac{1}{2}s$ ô tô đi được quãng đường là: $\int_0^{\frac{1}{2}} {( – 40t + 20)dt} = 5$ m.

> **Đáp án: D**

## Câu 23. Một vật chuyển động với vận tốc $v(t)$ (m/s) có gia tốc $a(t) = 3{t^2} + t$ $\left( {m/{s^2}} \right).$ Vận tốc ban đầu của vật là $2$ (m/s). Hỏi vận tốc của vật sau $2s$?

A. $10$ m/s.

B. $12$ m/s.

C. $16$ m/s.

D. $8$ m/s.

Hướng dẫn giải:

Ta có $v(t) = \int a (t)dt$ $= \int {\left( {3{t^2} + t} \right)dt}$ $= {t^3} + \frac{{{t^2}}}{2} + C.$

Vận tốc ban đầu của vật là $2$ m/s $\Rightarrow v(0) = 2$ $\Rightarrow C = 2.$

Vậy vận tốc của vật sau $2s$ là: $v(2)=12$ (m/s).

> **Đáp án: B**