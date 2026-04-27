# Thực hiện các phép toán trên tập số phức

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
Bài viết hướng dẫn phương pháp giải bài toán thực hiện các phép toán trên tập số phức: cộng, trừ, nhân, chia số phức, tìm phần thực và phần ảo của số phức, tính môđun số phức, số phức liên hợp … đây là dạng toán cơ bản trong chương trình Giải tích 12: Số phức.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## I. KIẾN THỨC CẦN NHỚ
1. Các phép toán trên tập số phức
$(a + bi) + (c + di)$ $= (a + c) + (b + d)i.$

$(a + bi) – (c + di)$ $= (a – c) + (b – d)i.$

$(a + bi).(c + di)$ $= (ac – bd) + (bc + ad)i.$

$\frac{{a + bi}}{{c + di}}$ $= \frac{{(a + bi)(c – di)}}{{(c + di)(c – di)}}$ $= \frac{{(ac + bd) + (bc – ad)i}}{{{c^2} + {d^2}}}.$

2. Các định nghĩa

Số phức $z = a + bi$ $\left( {a,b \in R;{i^2} = – 1} \right)$ có phần thực là $a$, phần ảo là $b.$

$a + bi = c + di$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = c}\\
{b = d}
\end{array}} \right..
$$

$z = a + bi$ là số thực khi $b = 0$; $z= a+bi$ là số thuần ảo khi $a=0.$

Số phức $z=a+bi$ có điểm biểu diễn trên mặt phẳng tọa độ $Oxy$ là điểm $M(a;b).$

Môđun của số phức $z = a + bi$ là: $|z| = \sqrt {{a^2} + {b^2}} .$

Số phức liên hợp của số phức $z=a+bi$ là số phức $\bar z = a – bi.$

<!-- chunk:2 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 1: Cho số phức $z = a + bi.$ Số phức ${z^2}$ có phần thực là:

A. $a + b.$

B. ${a^2} – {b^2}.$

C. $a – b.$

D. ${a^2} + {b^2}.$

Lời giải:

$z = a + bi$ $\Rightarrow {z^2} = {a^2} – {b^2} + 2abi$ có phần thực là ${a^2} – {b^2}.$

> **Đáp án: B**

<!-- chunk:3 level:1 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## D. Số phức $z = a + bi = 0$
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 0}\\
{b = 0}
\end{array}} \right..
$$

Lời giải:

Ta có số phức liên hợp của $z = a + bi$ là $\bar z = a – bi.$

> **Đáp án: C**

<!-- chunk:4 level:1 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## D. Điểm $M( – a;b)$ là điểm biểu diễn của $\overline z .$

Lời giải:

Ta có: $z = a + bi$ $\Rightarrow \bar z = a – bi$ $\Rightarrow |\bar z| = \sqrt {{a^2} + {b^2}} .$

$iz$ $= i(a + bi)$ $= – b + ai$ $\Rightarrow |iz| = \sqrt {{a^2} + {b^2}}$ $\Rightarrow |\bar z| = |iz|.$

> **Đáp án: A**

<!-- chunk:5 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 4: Cho số phức $z = 2 – 3i.$ Tìm phần thực $a$ của $z$?

A. $a=2.$

B. $a=3.$

C. $a=-2.$

D. $a=-3.$

Lời giải:

Theo định nghĩa số phức $z = a + bi$ $(a,b \in R)$ có phần thực là $a$ $\Rightarrow z = 2 – 3i$ có phần thực $a=2.$

> **Đáp án: A**

<!-- chunk:6 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 5: Cho hai số phức ${z_1} = i$ và ${z_2} = 3 + 4i.$ Gọi $a$ là phần thực của số phức $z = z_1^{2018} – 2{z_2}.$ Khẳng định nào sau đây là đúng?

A. ${a^2} – 2a = 100.$

B. $a + {a^2} = 72.$

C. $a – {a^2} = – 56.$

D. ${a^2} – a = 42.$

Lời giải:

$z = z_1^{2018} – 2{z_2}$ $= {i^{2018}} – 2(3 + 4i)$ $= {\left( {{i^2}} \right)^{1009}} – 6 – 8i$ $= – 7 – 8i.$

$\Rightarrow a = – 7$ $\Rightarrow a – {a^2} = – 56.$

> **Đáp án: C**

<!-- chunk:7 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 6: Cho số phức $z = a + bi$ $(a,b \in R).$ Phần thực của số phức $z.\bar z$ bằng?

A. ${a^2} – {b^2}.$

B. ${a^2} + {b^2}.$

C. ${a^2}.$

D. ${b^2}.$

Lời giải:

$z.\bar z$ $= (a + bi)(a – bi)$ $= {a^2} + {b^2}$ có phần thực là ${a^2} + {b^2}.$

> **Đáp án: B**

<!-- chunk:8 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 7: Cho số phức $z = 2 + i.$ Phần ảo của số phức ${z^3} + 2{z^2}\bar z + 3$ bằng?

A. $-25.$

B . $21i.$

C. $21.$

D. $25.$

Lời giải:

${z^3} + 2{z^2}\bar z + 3$ $= {(2 + i)^3} + 2{(2 + i)^2}(2 – i) + 3$ $= 25 + 21i$ có phần ảo bằng $21.$

> **Đáp án: C**

<!-- chunk:9 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 8: Cho hai số phức ${z_1} = 3 – 4i$, ${z_2} = 1 + i.$ Tìm phần ảo $b$ của số $z = \frac{{{z_1}}}{{{z_2}}} + \left| {{z_1}} \right|{z_2} + 2i.$

A. $b = \frac{{15}}{2}i.$

B. $b = – \frac{{17}}{2}.$

C. $b = \frac{{17}}{2}.$

D. $b = \frac{{15}}{2}.$

Lời giải:

$z = \frac{{\overline {{z_1}} }}{{{z_2}}} + \left| {{z_1}} \right|{z_2} + 2i$ $= \frac{{3 + 4i}}{{1 + i}} + |3 – 4i|(1 + i) + 2i$ $= \frac{{17}}{2} + \frac{{15}}{2}i$ có phần ảo $b = \frac{{15}}{2}.$

> **Đáp án: D**

<!-- chunk:10 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 9: Hiệu phần thực và phần ảo của số phức $z = (1 + 2i)(3 – i)$ là:

A. $6.$

B. $10.$

C. $5.$

D. $0.$

Lời giải:

Ta có $z = 3 – i + 6i – 2{i^2}$ $= 5 + 5i$ nên hiệu phần thực và phần ảo của $z$ bằng $0.$

> **Đáp án: D**

<!-- chunk:11 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 10: Cho số phức $z = (m + 1 – 2i)(2m + 3 + i)$ với $m$ là tham số thực. Tìm tập hợp tất cả các giá trị của $m$ để $z$ có phần thực bằng $5.$

A. $\left\{ {0, – \frac{5}{2}} \right\}.$

B. $\left\{ {1,\frac{5}{2}} \right\}.$

C. $\left\{ { – 1,\frac{3}{2}} \right\}.$

D. $\left\{ {2, – \frac{5}{3}} \right\}.$

Lời giải:

$z = (m + 1 – 2i)(2m + 3 + i)$ $= 2{m^2} + 5m + 5 + ( – 3m – 5)i.$

$2{m^2} + 5m + 5 = 5$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 0}\\
{m = – \frac{5}{2}}
\end{array}} \right..
$$

> **Đáp án: A**

<!-- chunk:12 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 11: Cho hai số phức $z = 1 + 3i$, $w = 2 – i.$ Tìm phần ảo của số phức $u = \overline z .w.$

A. $5i.$

B. $-7i.$

C. $-7.$

D. $5.$

Lời giải:

$u = \bar z.w$ $= (1 – 3i)(2 – i)$ $= – 1 – 7i$ có phần ảo bằng $-7.$

> **Đáp án: C**

<!-- chunk:13 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 12: Cho số phức $z = 1 – i + {i^3}.$ Tìm phần thực $a$ và phần ảo $b$ của $z.$

A. $a =1$, $b=-2.$

B. $a=-2$, $b=1.$

C. $a=1$, $b=0.$

D. $a=0$, $b=1.$

Lời giải:

$z = 1 – i + {i^3} = 1 – 2i$ $\Rightarrow a = 1$, $b = – 2.$

> **Đáp án: A**

<!-- chunk:14 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 13: Cho số phức $z = 1 + i + {i^2} + \ldots + {i^{2018}}.$ Điểm biểu diễn của số phức $z$ trên mặt phẳng tọa độ là:

A. $M(1;0).$

B. $N(0;1).$

C. $P(1;1).$

D. $Q(1;-1).$

Lời giải:

$z = 1 + i + {i^2} + \ldots + {i^{2018}}$ $= 1.\frac{{1 – {i^{2019}}}}{{1 – i}}$ $= \frac{{1 – {{\left( {{i^2}} \right)}^{1009}}i}}{{1 – i}} = i$ có điểm biểu diễn là $N(0;1).$

> **Đáp án: B**

<!-- chunk:15 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 14: Cho số phức ${z_1} = 1 – 2i$, ${z_2} = – 3 + i.$ Tìm điểm biểu diễn của số phức $z = {z_1} + {z_2}$ trên mặt phẳng tọa độ.

A. $N(4;-3).$

B. $M(2;-5).$

C. $P(-2;-1).$

D. $Q(-1;7).$

Lời giải:

$z = {z_1} + {z_2}$ $= (1 – 2i) + ( – 3 + i)$ $= – 2 – i$ có điểm biểu diễn là $P(-2;-1).$

> **Đáp án: C**

<!-- chunk:16 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 15: Cho số phức $z = (3 + i)(3 – 2i) + {(2 + i)^3}$ có điểm biểu diễn trên mặt phẳng tọa độ $Oxy$ là $M(a;b).$ Tính $T= a + 2b.$

A. $T=-29.$

B. $T=-3.$

C. $T=3.$

D. $T= 29.$

Lời giải:

$z = (3 + i)(3 – 2i) + {(2 + i)^3}$ $= 13 + 8i.$

$\Rightarrow a = 13$, $b = 8$ $\Rightarrow T = a + 2b = 29.$

> **Đáp án: D**

<!-- chunk:17 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 16: Cho hai số phức ${z_1} = (1 + i)(2 + i) – i$, ${z_2} = {(1 + i)^5}$ có các điểm biểu diễn trên mặt phẳng tọa độ $Oxy$ lần lượt là $M$, $N.$ Tính độ dài đoạn $MN.$

A. $MN = \sqrt {13} .$

B. $MN = \sqrt {29} .$

C. $MN = 3\sqrt 5 .$

D. $MN = \sqrt {61} .$

Lời giải:

${z_1} = (1 + i)(2 + i) – i$ $= 1 + 2i$ $\Rightarrow M(1;2)$; ${z_2} = {(1 + i)^5} = – 4 – 4i$ $\Rightarrow N( – 4; – 4).$

$\Rightarrow MN$ $= \sqrt {{{( – 4 – 1)}^2} + {{( – 4 – 2)}^2}}$ $= \sqrt {61} .$

> **Đáp án: D**

<!-- chunk:18 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 17: Cho hai số phức ${z_1} = {(1 + i)^2}$, ${z_2} = \frac{{2 + 4i}}{{{z_1}}}$ có các điểm biểu diễn trên mặt phẳng tọa độ $Oxy$ lần lượt là $M$, $N.$ Tính diện tích $S$ của tam giác $OMN.$

A. $S=1.$

B. $S = \frac{3}{2}.$

C. $S = 2.$

D. $S = \frac{5}{2}.$

Lời giải:

${z_1} = {(1 + i)^2} = 2i$ $\Rightarrow M(0;2)$; ${z_2} = \frac{{2 + 4i}}{{{z_1}}}$ $= \frac{{2 + 4i}}{{2i}} = 2 – i$ $\Rightarrow N(2; – 1).$

$$
\left\{ {\begin{array}{l}
{\overrightarrow {OM} = (0;2)}\\
{\overrightarrow {ON} = (2; – 1)}
\end{array}} \right.
$$
 $\Rightarrow S = \frac{1}{2}\left| {0 \times ( – 1) – 2 \times 2} \right| = 2.$

> **Đáp án: C**

<!-- chunk:19 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 18: Cho số phức $z = 3 – i.$ Tính môđun của số phức $\omega = {z^2} – (1 + i)z + 2.$

A. $|\omega | = 2\sqrt 2 .$

B. $|\omega | = 8.$

C. $|\omega | = 10.$

D. $|\omega | = 100.$

Lời giải:

$\omega = {z^2} – (1 + i)z + 2$ $= {(3 – i)^2} – (1 + i)(3 – i) + 2$ $= 6 – 8i.$

$\Rightarrow |\omega | = \sqrt {{6^2} + {{( – 8)}^2}} = 10.$

> **Đáp án: C**

<!-- chunk:20 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 19: Cho số phức $z = 3 + 4i.$ Tính môđun của số phức $\omega = (z + i)(2 + \bar z) + 3|z|.$

A. $|\omega | = 2669.$

B. $|\omega | = \sqrt {2669} .$

C. $|\omega | = 113.$

D. $|\omega | = \sqrt {113} .$

Lời giải:

$\omega = (z + i)(2 + \bar z) + 3|z|$ $= (3 + 4i + i)(2 + 3 – 4i) + 3|3 + 4i|$ $= 50 + 13i.$

$\Rightarrow |\omega | = \sqrt {{{50}^2} + {{13}^2}} = \sqrt {2669} .$

> **Đáp án: B**

<!-- chunk:21 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 20: Cho hai số phức ${z_1} = 1 – 2i$, ${z_2} = 3 + i.$ Tính môđun của số phức $\omega = \left( {{z_1} + {z_2}} \right){z_1} + \left( {{z_2} + 3} \right)(2 – i).$

A. $|\omega | = 394.$

B. $|\omega | = \sqrt {394} .$

C. $|\omega | = 231.$

D. $|\omega | = \sqrt {231} .$

Lời giải:

$\omega = \left( {{z_1} + {z_2}} \right){z_1} + \left( {{z_2} + 3} \right)(2 – i).$

$= (1 – 2i + 3 + i)(1 – 2i)$ $+ (3 + i + 3)(2 – i)$ $= 15 – 13i.$

$\Rightarrow |\omega | = \sqrt {{{15}^2} + {{( – 13)}^2}} = \sqrt {394} .$

> **Đáp án: B**

<!-- chunk:22 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 21: Cho hai số phức ${z_1} = 2 + mi$, ${z_2} = n + i$ $(m,n \in R).$ Tìm số phức liên hợp của số phức $\omega = 2{z_1} + 3{z_2}.$

A. $\bar \omega = 4 + 3n – (2m + 3)i.$

B. $\bar \omega = 4 + 3n + (2m + 3)i.$

C. $\bar \omega = – 4 – 3n + (2m + 3)i.$

D. $\bar \omega = – 4 – 3n – (2m + 3)i.$

Lời giải:

$\omega = 2{z_1} + 3{z_2}$ $= 2(2 + mi) + 3(n + i)$ $= 4 + 3n + (2m + 3)i.$

$\Rightarrow \bar \omega = 4 + 3n – (2m + 3)i.$

> **Đáp án: A**

<!-- chunk:23 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 22: Cho số phức $z = 2 + mi$ $(m \in R).$ Tìm số phức liên hợp của số phức $\omega = (z + 2)(1 + i) + 3i.$

A. $\bar \omega = 4 – m + (m + 7)i.$

B. $\bar \omega = 4 – m – (m + 7)i.$

C. $\bar \omega = – 4 + m – (m + 7)i.$

D. $\bar \omega = – 4 + m + (m + 7)i.$

Lời giải:

$\omega = (4 + mi)(1 + i) + 3i$ $= 4 – m + (m + 4)i + 3i$ $= 4 – m + (m + 7)i.$

$\Rightarrow \bar \omega = 4 – m – (m + 7)i.$

> **Đáp án: B**

<!-- chunk:24 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 23: Cho số phức $z = 1 + 2i.$ Điểm biểu diễn số phức liên hợp của số phức $\omega = (\overline {z + i} )(2 + i) – 4i$ trong mặt phẳng tọa độ là?

A. $M(5;-9).$

B. $N(-5;-9).$

C. $P(5;9).$

D. $Q(-5;9).$

Lời giải:

$\omega = (\overline {z + i} )(2 + i) – 4i$ $= (1 – 3i)(2 + i) – 4i$ $= 5 – 9i$ $\Rightarrow \bar \omega = 5 + 9i$ có điểm biểu diễn là $P(5;9).$

> **Đáp án: C**

<!-- chunk:25 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 24: Cho số phức $z = m + 2i$ $(m \in R).$ Tìm $m$ để $(z + 3)(1 + 2i)$ là một số thuần ảo.

A. $m=5.$

B. $m=1.$

C. $m=-1.$

D. $m=-5.$

Lời giải:

$(z + 3)(1 + 2i)$ $= (3 + m + 2i)(1 + 2i)$ $= (m – 1) + (2m + 8)i.$

$\Rightarrow (z + 3)(1 + 2i)$ là số thuần ảo khi $m – 1 = 0$ $\Leftrightarrow m = 1.$

> **Đáp án: B**

<!-- chunk:26 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 25: Cho số phức $z = 3 + mi$ $(m \in R).$ Tìm $m$ để $(\bar z + 1)(2 – i)$ là một số thực.

A. $m=8.$

B. $m=2.$

C. $m=-2.$

D. $m=-8.$

Lời giải:

$(\bar z + 1)(2 – i)$ $= (4 – mi)(2 – i)$ $= (8 – m) + ( – 2m – 4)i.$

$\Rightarrow (\bar z + 1)(2 – i)$ là số thực khi $– 2m – 4 = 0$ $\Leftrightarrow m = – 2.$

> **Đáp án: C**

<!-- chunk:27 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 26: Cho số phức $z = m + ni$ $(m,n \in R)$ thỏa mãn $(z + 1)(1 + i) = 3 + 5i.$ Tính $S = m + 2n.$

A. $S=-7.$

B. $S=-5.$

C. $S=5.$

D. $S=7.$

Lời giải:

$(z + 1)(1 + i) = 3 + 5i$ $\Leftrightarrow (m + 1 + ni)(1 + i) = 3 + 5i.$

$\Leftrightarrow m + 1 – n + (m + 1 + n)i = 3 + 5i.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m + 1 – n = 3}\\
{m + 1 + n = 5}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m = 3}\\
{n = 1}
\end{array}} \right.
$$
 $\Rightarrow S = m + 2n = 5.$

> **Đáp án: C**

<!-- chunk:28 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 27: Tìm tất cả các số thực $x$, $y$ sao cho ${x^2} – 1 + yi = – 1 + 2i.$

A. $x = \sqrt 2$, $y = 2.$

B. $x = – \sqrt 2$, $y = 2.$

C. $x = 0$, $y = 2.$

D. $x = \sqrt 2$, $y = – 2.$

Lời giải:

${x^2} – 1 + yi = – 1 + 2i$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^2} – 1 = – 1}\\
{y = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 2}
\end{array}} \right..
$$

> **Đáp án: C**

<!-- chunk:29 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 28: Cho $x,y \in R$ là hai số thực thỏa mãn $\frac{{x + yi}}{{1 – i}} = 3 + 2i.$ Tính $S = x + y + xy.$

A. $S=-9.$

B. $S=-1.$

C. $S=1.$

D. $S=9.$

Lời giải:

Ta có: $\frac{{x + yi}}{{1 – i}} = 3 + 2i$ $\Leftrightarrow x + yi = (3 + 2i)(1 – i)$ $\Leftrightarrow x + yi = 5 – i$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 5}\\
{y = – 1}
\end{array}} \right..
$$

$\Rightarrow S = x + y + xy = – 1.$

> **Đáp án: B**

<!-- chunk:30 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 29: Trên tập số phức cho $(2x + y) + (2y – x)i$ $= (x – 2y + 3) + (y + 2x + 1)i$ với $x,y \in R.$ Tính giá trị của biểu thức $S=x+y.$

A. $S=1.$

B. $S=2.$

C. $S=-1.$

D. $S=-2.$

Lời giải:

Ta có $(2x + y) + (2y – x)i$ $= (x – 2y + 3) + (y + 2x + 1)i.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2x + y = x – 2y + 3}\\
{2y – x = y + 2x + 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 1}
\end{array}} \right.
$$
 $\Rightarrow S = x + y = 1.$

> **Đáp án: A**

<!-- chunk:31 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 30: Cho $x,y \in R$ thỏa mãn $x + 2y + (2x – y)i$ $= 2x + y + (x + 2y)i.$ Tính $S = 2x + 4y.$

A. $S=-1.$

B. $S=0.$

C. $S=1.$

D. $S=2.$

Lời giải:

$x + 2y + (2x – y)i$ $= 2x + y + (x + 2y)i.$

$\Leftrightarrow (x + 2y – 2x – y)$ $+ (2x – y – x – 2y)i = 0.$

$\Leftrightarrow (y – x) + (x – 3y)i = 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = y}\\
{x = 3y}
\end{array}} \right.
$$
 $\Leftrightarrow x = y = 0$ $\Rightarrow S = 2x + 4y = 0.$

> **Đáp án: B**

<!-- chunk:32 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 31: Cho số phức $z = a + bi$ $(a,b \in R)$ thoả mãn $z + 2 + i = |z|.$ Tính $S = 4a + b.$

A. $S=4.$

B. $S=2.$

C. $S=-2.$

D. $S=-4.$

Lời giải:

$z + 2 + i = |z|$ $\Leftrightarrow (a + 2) + (b + 1)i$ $= \sqrt {{a^2} + {b^2}} .$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a + 2 = \sqrt {{a^2} + {b^2}} }\\
{b + 1 = 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{b = – 1}\\
{{{(a + 2)}^2} = {a^2} + 1}\\
{a \ge – 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = – \frac{3}{4}}\\
{b = – 1}
\end{array}} \right.
$$
 $\Rightarrow S = 4a + b = – 4.$

> **Đáp án: D**

<!-- chunk:33 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 32: Cho số phức $z = a + bi$ $(a,b \in R)$ có phần thực gấp ba lần phần ảo và thỏa mãn $(z + 1)(2 – i)$ là một số thuần ảo. Tính $S = a + 4b.$

A. $S = – \frac{{26}}{7}.$

B. $S = – 2.$

C. $S = 2.$

D. $S = \frac{{26}}{7}.$

Lời giải:

$z = a + bi$ có phần thực gấp ba lần phần ảo $\Rightarrow a = 3b$ $(1).$

$(z + 1)(2 – i)$ $= (a + 1 + bi)(2 – i)$ $= (2a + b + 2) + (2b – a – 1)i.$

$(z + 1)(2 – i)$ là số thuần ảo $\Rightarrow 2a + b + 2 = 0$ $(2).$

Từ $(1)$ và $(2)$ $\Rightarrow a = – \frac{6}{7}$, $b = – \frac{2}{7}$ $\Rightarrow S = a + 4b = – 2.$

> **Đáp án: B**

<!-- chunk:34 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 33: Cho hai số phức ${z_1} = 1 + 2i$ và ${z_2} = m – 3 + \left( {{m^2} – 6} \right)i$ $(m \in R).$ Tìm $S$ là tổng tất cả các giá trị $m$ để ${z_1} + {z_2}$ là số thực.

A. $S=0.$

B. $S=2.$

C. $S=4.$

D. $S=-4.$

Lời giải:

${z_1} + {z_2} = m – 2 + \left( {{m^2} – 4} \right)i$; ${z_1} + {z_2}$ là số thực $\Rightarrow {m^2} – 4 = 0$ $\Leftrightarrow m = 2 \vee m = – 2.$

$\Rightarrow S = 2 + ( – 2) = 0.$

> **Đáp án: A**

<!-- chunk:35 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 34: Cho số phức $z = a + bi$ $(a,b \in R)$ có phần ảo gấp đôi phần thực và thỏa mãn $(\bar z + 1)(1 – i)$ là một số thực. Tính $S = 2a + 3b.$

A. $S = – \frac{8}{3}.$

B. $S = – \frac{7}{3}.$

C. $S = \frac{7}{3}.$

D. $S = \frac{8}{3}.$

Lời giải:

$z = a + bi$ có phần ảo gấp đôi phần thực $\Rightarrow b = 2a$ $(1).$

$(\bar z + 1)(1 – i)$ $= (a + 1 – bi)(1 – i)$ $= (a + 1 – b) + ( – a – 1 – b)i.$

$(\bar z + 1)(1 – i)$ là số thực $\Rightarrow – a – b – 1 = 0$ $(2).$

Từ $(1)$ và $(2)$ $\Rightarrow a = – \frac{1}{3}$, $b = – \frac{2}{3}$ $\Rightarrow S = 2a + 3b = – \frac{8}{3}.$

> **Đáp án: A**

<!-- chunk:36 level:3 source:https://toanmath.com/2020/03/thuc-hien-cac-phep-toan-tren-tap-so-phuc.html -->
## Ví dụ 35: Cho số phức $z = a + bi$ $(a,b \in R)$ thỏa mãn $|z + 1 + i| = |\bar z + 2 + i|$ và $(2z + 1)(1 + i)$ có phần thực bằng phần ảo. Tính $S = a+3b.$

A. $S = – \frac{9}{2}.$

B. $S = – \frac{3}{2}.$

C. $S = \frac{3}{2}.$

D. $S = \frac{9}{2}.$

Lời giải:

$|z + 1 + i| = |\bar z + 2 + i|$ $\Leftrightarrow |a + 1 + (b + 1)i|$ $= |a + 2 + (1 – b)i|.$

$\Leftrightarrow \sqrt {{{(a + 1)}^2} + {{(b + 1)}^2}}$ $= \sqrt {{{(a + 2)}^2} + {{(1 – b)}^2}} .$

$\Leftrightarrow {a^2} + 2a + 1 + {b^2} + 2b + 1$ $= {a^2} + 4a + 4 + 1 – 2b + {b^2}$ $\Leftrightarrow 2a – 4b = – 3$ $(1).$

$(2z + 1)(1 + i)$ $= (2a + 1 + 2bi)(1 + i)$ $= (2a + 1 – 2b) + (2a + 1 + 2b)i.$

$(2z + 1)(1 + i)$ có phần thực bằng phần ảo.

$\Rightarrow 2a + 1 – 2b = 2a + 1 + 2b$ $\Rightarrow b = 0$ $(2).$

Từ $(1)$ và $(2)$ suy ra $a = – \frac{3}{2}$, $b = 0$ $\Rightarrow S = a + 3b = – \frac{3}{2}.$

> **Đáp án: B**