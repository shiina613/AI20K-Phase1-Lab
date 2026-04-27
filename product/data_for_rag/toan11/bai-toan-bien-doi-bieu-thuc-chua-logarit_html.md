# Bài toán biến đổi biểu thức chứa logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
Bài viết tổng hợp các công thức biến đổi logarit và hướng dẫn giải một số bài toán liên quan đến biến đổi biểu thức chứa logarit, đây là dạng toán cơ bản trong chương trình Giải tích 12 chương 2.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## A. KIẾN THỨC CẦN NẮM VỮNG
1. So sánh hai logarit cũng cơ số: Cho số dương $a \ne 1$ và các số dương $b$, $c$:

+ Khi $a > 1$ thì ${\log _a}b > {\log _a}c \Leftrightarrow b > c.$

+ Khi $0 < a < 1$ thì ${\log _a}b > {\log _a}c \Leftrightarrow b < c.$

Hệ quả: Cho số dương $a \ne 1$ và các số dương $b$, $c$:

+ Khi $a > 1$ thì ${\log _a}b > 0 \Leftrightarrow b > 1.$

+ Khi $0 < a < 1$ thì ${\log _a}b > 0 \Leftrightarrow b < 1.$

+ ${\log _a}b = {\log _a}c \Leftrightarrow b = c.$

2. Logarit của một tích: Cho ba số dương $a$, ${b_1}$, ${b_2}$ với $a \ne 1$, ta có: ${\log _a}\left( {{b_1}.{b_2}} \right) = {\log _a}{b_1} + {\log _a}{b_2}.$

3. Logarit của một thương: Cho ba số dương $a$, ${b_1}$, ${b_2}$ với $a \ne 1$, ta có: ${\log _a}\frac{{{b_1}}}{{{b_2}}} = {\log _a}{b_1} – {\log _a}{b_2}.$ Đặc biệt: với $a,b > 0$, $a \ne 1$, ta có ${\log _a}\frac{1}{b} = – {\log _a}b.$

4. Logarit của lũy thừa: Cho $a,b > 0$, $a \ne 1$, với mọi $\alpha$, ta có: ${\log _a}{b^\alpha } = \alpha {\log _a}b.$ Đặc biệt: ${\log _a}\sqrt[n]{b} = \frac{1}{n}{\log _a}b.$

5. Công thức đổi cơ số: Cho ba số dương $a$, $b$, $c$ với $a \ne 1$, $c \ne 1$ ta có: ${\log _a}b = \frac{{{{\log }_c}b}}{{{{\log }_c}a}}.$ Đặc biệt: ${\log _a}c = \frac{1}{{{{\log }_c}a}}$ và ${\log _{{a^\alpha }}}b = \frac{1}{\alpha }{\log _a}b$ với $\alpha \ne 0.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 1: Tính giá trị biểu thức: $B = 2{\log _2}12 + 3{\log _2}5$ $– {\log _2}15 – {\log _2}150.$

Ta có: $B = 2{\log _2}12 + 3{\log _2}5$ $– {\log _2}15 – {\log _2}150$ $= 2{\log _2}\left( {{2^2}.3} \right) + 3{\log _2}5$ $– {\log _2}3.5 – {\log _2}\left( {{{2.3.5}^2}} \right)$ $= 2\left( {2 + {{\log }_2}3} \right) + 3{\log _2}5$ $– \left( {{{\log }_2}3 + {{\log }_2}5} \right)$ $– \left( {1 + {{\log }_2}3 + 2{{\log }_2}5} \right)$ $= 3.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 2: Cho $a,b > 0$ và $a,b \ne 1$. Tính giá trị biểu thức $P = {\log _{\sqrt a }}{b^2} + \frac{2}{{{{\log }_{\frac{a}{b}}}a}}.$

Ta có: $P = {\log _{\sqrt a }}{b^2} + \frac{2}{{{{\log }_{\frac{a}{{{b^2}}}}}a}}$ $= 4{\log _a}b + 2{\log _a}\frac{a}{{{b^2}}}$ $= 4{\log _a}b + 2\left( {{{\log }_a}a – {{\log }_a}{b^2}} \right) = 2.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 3: Cho $a$, $b$ là các số thực dương và $ab \ne 1$ thỏa mãn ${\log _{ab}}{a^2} = 3$ thì giá trị của ${\log _{ab}}\sqrt[3]{{\frac{a}{b}}}$ bằng bao nhiêu?

${\log _{ab}}\sqrt[3]{{\frac{a}{b}}} = \frac{1}{3}{\log _{ab}}\frac{a}{b} = \frac{1}{3}{\log _{ab}}\frac{{{a^2}}}{{ab}}$ $= \frac{1}{3}\left( {{{\log }_{ab}}{a^2} – {{\log }_{ab}}ab} \right)$ $= \frac{1}{3}\left( {{{\log }_{ab}}{a^2} – 1} \right).$

Giả thiết ${\log _{ab}}{a^2} = 3$ nên ${\log _{ab}}\sqrt[3]{{\frac{a}{b}}} = \frac{1}{3}(3 – 1) = \frac{2}{3}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 4: Cho $x = 2000!$. Tính giá trị của biểu thức $A = \frac{1}{{{{\log }_2}x}} + \frac{1}{{{{\log }_3}x}} + \ldots + \frac{1}{{{{\log }_{2000}}x}}.$

Ta có $A = {\log _x}2 + {\log _x}3 + \ldots + {\log _x}2000$ $= {\log _x}(1.2.3…2000) = {\log _x}x = 1.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 5: Có tất cả bao nhiêu số dương $a$ thỏa mãn đẳng thức ${\log _2}a + {\log _3}a + {\log _5}a$ $= {\log _2}a.{\log _3}a.{\log _5}a?$

${\log _2}a + {\log _3}a + {\log _5}a$ $= {\log _2}a.{\log _3}a.{\log _5}a$ $\Leftrightarrow {\log _2}a + {\log _3}2.{\log _2}a + {\log _5}2.{\log _2}a$ $= {\log _2}a.{\log _3}5.{\log _5}a.{\log _5}a$ $\Leftrightarrow {\log _2}a.\left( {1 + {{\log }_3}2 + {{\log }_5}2} \right)$ $= {\log _2}a.{\log _3}5.\log _5^2a$ $\Leftrightarrow {\log _2}a.\left( {1 + {{\log }_3}2 + {{\log }_5}2 – {{\log }_3}5.\log _5^2a} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{{\log }_2}a = 0}\\
{1 + {{\log }_3}2 + {{\log }_5}2 – {{\log }_3}5.\log _5^2a = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = 1}\\
{{{\log }_5}a = \pm \sqrt {\frac{{1 + {{\log }_3}2 + {{\log }_5}2}}{{{{\log }_3}5}}} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = 1}\\
{a = {5^{\frac{{\sqrt {1 + {{\log }_3}2 + {{\log }_5}2} }}{{{{\log }_3}5}}}}}
\end{array}} \right.
$$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 6: Tính giá trị của biểu thức $P = \ln \left( {\tan {1^0}} \right) + \ln \left( {\tan {2^0}} \right)$ $+ \ln \left( {\tan {3^0}} \right) + \ldots + \ln \left( {\tan {{89}^0 }} \right).$

$P = \ln \left( {\tan {1^0}} \right) + \ln \left( {\tan {2^0}} \right)$ $+ \ln \left( {\tan {3^0}} \right) + \ldots + \ln \left( {\tan {{89}^0 }} \right)$ $= \ln \left( {\tan {1^0 }.\tan {2^0 }.\tan {3^0 } \ldots \tan {{89}^0 }} \right)$ $= \ln \left( {\tan {1^0 }.\tan {2^0 }.\tan {3^0 } \ldots \tan {{45}^0 }.\cot {{44}^0 }.\cot {{43}^0 } \ldots \cot {1^0 }} \right)$ $= \ln \left( {\tan {{45}^0 }} \right) = \ln 1 = 0$ (vì $\tan \alpha \cdot \cot \alpha = 1$).

<!-- chunk:8 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 7: Cho $a$, $b$ là các số thực dương thỏa mãn $a \ne 1$, $a \ne \sqrt b$ và ${\log _a}b = \sqrt 3 .$ Tính $P = {\log _{\frac{{\sqrt b }}{a}}}\sqrt {\frac{b}{a}} .$

$P = \frac{{{{\log }_a}\sqrt {\frac{b}{a}} }}{{{{\log }_a}\frac{{\sqrt b }}{a}}} = \frac{{\frac{1}{2}\left( {{{\log }_a}b – 1} \right)}}{{{{\log }_a}\sqrt b – 1}}$ $= \frac{{\frac{1}{2}(\sqrt 3 – 1)}}{{\frac{1}{2}{{\log }_a}b – 1}}$ $= \frac{{\sqrt 3 – 1}}{{\sqrt 3 – 2}} = – 1 – \sqrt 3 .$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 8: Tính giá trị của biểu thức $P = {\log _{{a^2}}}\left( {{a^{10}}{b^2}} \right) + {\log _{\sqrt a }}\left( {\frac{a}{{\sqrt b }}} \right) + {\log _{\sqrt[3]{b}}}{b^{ – 2}}$ (với $0 < a \ne 1$, $0 < b \ne 1$).

$P = {\log _{{a^2}}}\left( {{a^{10}}{b^2}} \right)$ $+ {\log _{\sqrt a }}\left( {\frac{a}{{\sqrt b }}} \right) + {\log _{\sqrt[3]{b}}}{b^{ – 2}}$ $= \frac{1}{2}\left[ {{{\log }_a}{a^{10}} + {{\log }_a}{b^2}} \right]$ $+ 2\left[ {{{\log }_a}a – {{\log }_a}\sqrt b } \right]$ $+ 3.( – 2){\log _b}b$ $= \frac{1}{2}\left[ {10 + 2{{\log }_a}b} \right]$ $+ 2\left[ {1 – \frac{1}{2}{{\log }_a}b} \right] – 6 = 1.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 9: Cho $a$, $b$ là hai số thực dương khác $1$ và thỏa mãn $\log _a^2b – 8{\log _b}\left( {a\sqrt[3]{b}} \right) = – \frac{8}{3}$. Tính giá trị biểu thức $P = {\log _a}\left( {a\sqrt[3]{{ab}}} \right) + 2017.$

$\log _a^2b – 8{\log _b}(a\sqrt[3]{b}) = – \frac{8}{3}$ $\Leftrightarrow \log _a^2b – 8\left( {{{\log }_b}a + \frac{1}{3}} \right) = – \frac{8}{3}$ $\Leftrightarrow \log _a^2b – \frac{8}{{{{\log }_a}b}} = 0$ $\Leftrightarrow {\log _a}b = 2.$

$P = {\log _a}(a\sqrt[3]{{ab}}) + 2017$ $= {\log _a}{a^{\frac{4}{3}}} + \frac{1}{3}{\log _a}b + 2017$ $= \frac{4}{3} + \frac{2}{3} + 2017 = 2019.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Dạng toán 2. Biểu diễn một logarit theo các logarit cho trước.
Để tính ${\log _a}b$ theo $m = {\log _a}x$, $n = {\log _a}y$ ta biến đổi $b = {a^\alpha }{x^\beta }{y^\gamma }$ từ đó suy ra ${\log _a}b = {\log _a}\left( {{a^\alpha }{x^\beta }{y^\gamma }} \right) = \alpha + m\beta + n\gamma .$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 10: Cho ${\log _2}6 = a$. Tính giá trị của ${\log _3}18$ theo $a$?

Ta có: $a = {\log _2}6 = {\log _2}(2.3)$ $= 1 + {\log _2}3$ $\Rightarrow {\log _3}2 = \frac{1}{{a – 1}}.$

Suy ra ${\log _3}18 = {\log _3}\left( {{{2.3}^2}} \right) = {\log _3}2 + 2$ $= \frac{1}{{a – 1}} + 2 = \frac{{2a – 1}}{{a – 1}}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 11: Cho $a = {\log _3}15$, $b = {\log _3}10$. Tính giá trị của ${\log _{\sqrt 3 }}50$ theo $a$, $b$?

Ta có $a = {\log _3}15 = {\log _3}(3.5)$ $= 1 + {\log _3}5$ $\Rightarrow {\log _3}5 = a – 1.$

Khi đó ${\log _{\sqrt 3 }}50 = 2{\log _3}(5.10)$ $= 2\left( {{{\log }_3}5 + {{\log }_3}10} \right)$ $= 2(a – 1 + b).$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 12: Cho ${\log _{27}}5 = a$, ${\log _8}7 = b$, ${\log _2}3 = c.$ Tính giá trị của ${\log _6}35$ theo $a$, $b$, $c$?

Ta có:

${\log _{27}}5 = a \Rightarrow {\log _3}5 = 3a.$

${\log _8}7 = b \Rightarrow {\log _2}7 = 3b.$

$\Rightarrow {\log _2}5 = {\log _2}3.{\log _3}5 = 3ac.$

$\Rightarrow {\log _6}35 = \frac{{{{\log }_2}35}}{{{{\log }_2}6}}$ $= \frac{{{{\log }_2}5.{{\log }_2}7}}{{{{\log }_2}2.{{\log }_2}3}} = \frac{{3(ac + b)}}{{1 + c}}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 13: Đặt $a = {\log _2}3$, $b = {\log _5}3.$ Hãy biểu diễn ${\log _6}45$ theo $a$ và $b.$

Ta có: ${\log _6}45 = \frac{{{{\log }_2}45}}{{{{\log }_2}6}}$ $= \frac{{{{\log }_2}{3^2}.5}}{{{{\log }_2}2.3}} = \frac{{2{{\log }_2}3 + {{\log }_2}5}}{{1 + {{\log }_2}3}}$ $= \frac{{2{{\log }_2}3 + {{\log }_2}3.{{\log }_3}5}}{{1 + {{\log }_2}3}}$ $= \frac{{2a + a.\frac{1}{b}}}{{1 + a}} = \frac{{a + 2ab}}{{ab + b}}.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 14: Biết $a = {\log _2}5$, $b = {\log _5}3$. Khi đó giá trị của ${\log _{24}}15$ được tính theo $a$ và $b$ là?

${\log _{24}}15 = \frac{{{{\log }_2}15}}{{{{\log }_2}24}}$ $= \frac{{{{\log }_2}3.5}}{{{{\log }_2}{{3.2}^3}}} = \frac{{{{\log }_2}3 + {{\log }_2}5}}{{{{\log }_2}3 + 3}}$ $= \frac{{{{\log }_2}3 + {{\log }_2}3.{{\log }_3}5}}{{{{\log }_2}3 + 3}}$ $= \frac{{a + a \cdot \frac{1}{b}}}{{3 + a}} = \frac{{a + ab}}{{ab + 3b}}.$

<!-- chunk:17 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 15: Cho ${\log _{12}}27 = a$. Khi đó giá trị của ${\log _6}16$ được tính theo $a$ là?

Ta có $a = {\log _{12}}27$ $= \frac{{{{\log }_2}27}}{{{{\log }_2}12}} = \frac{{3{{\log }_2}3}}{{2 + {{\log }_2}3}}$ $\Rightarrow {\log _2}3 = \frac{{2a}}{{3 – a}}$ $\Rightarrow {\log _6}16 = \frac{{4(3 – a)}}{{3 + a}}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 16: Cho $a = {\log _2}3$, $b = {\log _3}5$, $c = {\log _7}2$. Khi đó giá trị của biểu thức ${\log _{140}}63$ được tính theo $a$, $b$, $c$ là?

${\log _{140}}63 = \frac{{{{\log }_2}63}}{{{{\log }_2}140}}$ $= \frac{{{{\log }_2}{3^2}.7}}{{{{\log }_2}{2^2}5.7}}$ $= \frac{{2{{\log }_2}3 + {{\log }_2}7}}{{2 + {{\log }_2}5 + {{\log }_2}7}}$ $= \frac{{2{{\log }_2}3 + \frac{1}{{{{\log }_7}2}}}}{{2 + {{\log }_2}3.{{\log }_3}5 + {{\log }_7}2}}$ $= \frac{{2a + \frac{1}{c}}}{{2 + ab + \frac{1}{c}}}$ $= \frac{{1 + 2ac}}{{1 + 2c + abc}}.$

<!-- chunk:19 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 17: Cho số thực $x$ thỏa mãn $\log x = \frac{1}{2}\log 3a – 2\log b + 3\log \sqrt c$ ($a$, $b$, $c$ là các số thực dương). Hãy biểu diễn $x$ theo $a$, $b$, $c.$

Ta có $\log x = \frac{1}{2}\log 3a – 2\log b + 3\log \sqrt c$ $\Leftrightarrow \log x = \log \sqrt {3a} – \log {b^2} + \log \sqrt {{c^3}}$ $\Leftrightarrow \log x = \log \frac{{\sqrt {3a{c^3}} }}{{{b^2}}}$ $\Leftrightarrow x = \frac{{\sqrt {3a{c^3}} }}{{{b^2}}}.$

<!-- chunk:20 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 18: Cho $a = {\log _4}3$, $b = {\log _{25}}2$. Hãy tính ${\log _{60}}\sqrt {150}$ theo $a$, $b.$

${\log _{60}}\sqrt {150} = \frac{1}{2}\frac{{{{\log }_{25}}150}}{{{{\log }_{25}}60}}$ $= \frac{1}{2}\frac{{{{\log }_{25}}25 + {{\log }_{25}}2 + {{\log }_{25}}3}}{{{{\log }_{25}}5 + {{\log }_{25}}4 + {{\log }_{25}}3}}$ $= \frac{{1 + {{\log }_{25}}2 + 2{{\log }_4}3.{{\log }_{25}}2}}{{2{{\log }_{25}}5 + 4{{\log }_{25}}2 + 4{{\log }_4}3.{{\log }_{25}}2}}$ $= \frac{{1 + a + 2ab}}{{1 + 4b + 4ab}}.$

<!-- chunk:21 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 19: Biết ${\log _{27}}5 = a$, ${\log _8}7 = b$, ${\log _2}3 = c$ thì ${\log _{12}}35$ tính theo $a$, $b$, $c$ bằng?

Ta có ${\log _{27}}5 = \frac{1}{3}{\log _3}5 = a$ $\Leftrightarrow {\log _3}5 = 3a$, ${\log _8}7 = \frac{1}{3}{\log _2}7 = b$ $\Leftrightarrow {\log _2}7 = 3b.$

Mà ${\log _{12}}35 = \frac{{{{\log }_2}(7.5)}}{{{{\log }_2}\left( {{{3.2}^2}} \right)}}$ $= \frac{{{{\log }_2}7 + {{\log }_2}5}}{{{{\log }_2}3 + 2}}$ $= \frac{{{{\log }_2}7 + {{\log }_2}3.{{\log }_3}5}}{{{{\log }_2}3 + 2}}$ $= \frac{{3b + c.3a}}{{c + 2}} = \frac{{3(b + ac)}}{{c + 2}}.$

<!-- chunk:22 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 20: Cho ${\log _{12}}27 = a$ thì ${\log _6}16$ tính theo $a$ là?

$a = {\log _{12}}27$ $= \frac{{{{\log }_3}27}}{{{{\log }_3}12}} = \frac{3}{{1 + 2{{\log }_3}2}}$ $\Rightarrow {\log _3}2 = \frac{{3 – a}}{{2a}}.$

${\log _6}16 = \frac{{{{\log }_3}16}}{{{{\log }_3}6}}$ $= \frac{{4{{\log }_3}2}}{{1 + {{\log }_3}2}}$ $= \frac{{4\frac{{3 – a}}{{2a}}}}{{1 + \frac{{3 – a}}{{2a}}}}$ $= \frac{{4(3 – a)}}{{a + 3}}.$

<!-- chunk:23 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 21: Xét các số thực $a$, $b$ thỏa mãn $a > b > 1$. Tìm giá trị nhỏ nhất ${P_{\min }}$ của biểu thức $P = \log _{\frac{a}{b}}^2\left( {{a^2}} \right) + 3{\log _b}\left( {\frac{a}{b}} \right).$

Với điều kiện đề bài, ta có: $P = \log _{\frac{a}{b}}^2\left( {{a^2}} \right) + 3{\log _b}\left( {\frac{a}{b}} \right)$ $= {\left[ {2{{\log }_{\frac{a}{b}}}a} \right]^2} + 3{\log _b}\left( {\frac{a}{b}} \right)$ $= 4{\left[ {{{\log }_{\frac{a}{b}}}\left( {\frac{a}{b}b} \right)} \right]^2} + 3{\log _b}\left( {\frac{a}{b}} \right).$

Đặt $t = {\log _{\frac{a}{b}}}b > 0$ (vì $a > b > 1$), ta có $P = 4{(1 + t)^2} + \frac{3}{t}$ $= 4{t^2} + 8t + \frac{3}{t} + 4 = f(t).$

Ta có ${f^\prime }(t) = 8t + 8 – \frac{3}{{{t^2}}}$ $= \frac{{8{t^3} + 8{t^2} – 3}}{{{t^2}}}$ $= \frac{{(2t – 1)\left( {4{t^2} + 6t + 3} \right)}}{{{t^2}}}.$

Vậy ${f^\prime }(t) = 0 \Leftrightarrow t = \frac{1}{2}.$

Khảo sát hàm số, ta có ${P_{\min }} = f\left( {\frac{1}{2}} \right) = 15.$

<!-- chunk:24 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 22: Biết ${\log _{27}}5 = a$, ${\log _8}7 = b$, ${\log _2}3 = c$ thì ${\log _{12}}35$ tính theo $a$, $b$, $c$ bằng?

Ta có ${\log _{27}}5 = \frac{1}{3}{\log _3}5 = a$ $\Leftrightarrow {\log _3}5 = 3a$, ${\log _8}7 = \frac{1}{3}{\log _2}7 = b$ $\Leftrightarrow {\log _2}7 = 3b.$

Mà ${\log _{12}}35 = \frac{{{{\log }_2}(7.5)}}{{{{\log }_2}\left( {{{3.2}^2}} \right)}}$ $= \frac{{{{\log }_2}7 + {{\log }_2}5}}{{{{\log }_2}3 + 2}}$ $= \frac{{{{\log }_2}7 + {{\log }_2}3.{{\log }_3}5}}{{{{\log }_2}3 + 2}}$ $= \frac{{3b + c.3a}}{{c + 2}} = \frac{{3(b + ac)}}{{c + 2}}.$

<!-- chunk:25 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 23: Đặt $a = {\log _3}4$, $b = {\log _5}4$. Hãy biểu diễn ${\log _{12}}80$ theo $a$ và $b.$

Ta có ${\log _{12}}80 = {\log _{12}}\left( {{4^2}.5} \right)$ $= {\log _{12}}{4^2} + {\log _{12}}5$ $= 2{\log _{12}}4 + \frac{1}{{{{\log }_5}12}}$ $= \frac{2}{{{{\log }_4}12}} + \frac{1}{{{{\log }_5}4 + {{\log }_5}3}}$ $= \frac{2}{{{{\log }_4}4 + {{\log }_4}3}} + \frac{1}{{b + {{\log }_5}3}}.$

Từ $a = {\log _3}4 \Rightarrow {\log _4}3 = \frac{1}{a}$ $\Rightarrow {\log _5}3 = {\log _5}4.{\log _4}3$ $= b.\frac{1}{a} = \frac{b}{a}.$

$\Rightarrow {\log _{12}}80 = \frac{2}{{1 + \frac{1}{a}}} + \frac{1}{{b + \frac{b}{a}}}$ $= \frac{{2a}}{{a + 1}} + \frac{a}{{b(a + 1)}}$ $= \frac{{a + 2ab}}{{ab + b}}.$

<!-- chunk:26 level:3 source:https://toanmath.com/2018/10/bai-toan-bien-doi-bieu-thuc-chua-logarit.html -->
## Ví dụ 24: Cho $a$, $b$ là các số hữu tỉ thỏa mãn ${\log _2}\sqrt[6]{{360}} – {\log _2}\sqrt 2$ $= a{\log _2}3 + b{\log _2}5.$ Tính $a + b.$

Ta có ${\log _2}\sqrt[6]{{360}} – {\log _2}\sqrt 2$ $= {\log _2}\sqrt[6]{{360}} – {\log _2}\sqrt[6]{8}$ $= {\log _2}\sqrt[6]{{\frac{{360}}{8}}} = \frac{1}{6}{\log _2}45$ $= \frac{1}{3}{\log _2}3 + \frac{1}{6}{\log _2}5.$

Theo đề bài ta có ${\log _2}\sqrt[6]{{360}} – {\log _2}\sqrt 2$ $= a{\log _2}3 + b{\log _2}5$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{a = \frac{1}{3}}\\
{b = \frac{1}{6}}
\end{array}} \right.
$$
 $\Rightarrow a + b = \frac{1}{2}.$