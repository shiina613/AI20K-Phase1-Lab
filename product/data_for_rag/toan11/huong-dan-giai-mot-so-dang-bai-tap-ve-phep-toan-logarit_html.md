# Hướng dẫn giải một số dạng bài tập về phép toán logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
Bài viết trình bày định nghĩa, tính chất và phương pháp giải một số dạng bài tập thường gặp về phép toán logarit trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## A. TÓM TẮT SÁCH GIÁO KHOA

1. Định nghĩa: Cho $a>0$, $a \ne 1$ và $b > 0.$

Ta gọi: Số $\alpha$ là logarit theo cơ số $a$ của số $b$ nếu ${a^\alpha } = b.$ Kí hiệu: ${\log _a}b = \alpha .$

Vậy ${\log _a}b = \alpha \Leftrightarrow {a^\alpha } = b.$

Nhận xét: Từ định nghĩa ta suy ra:

${\log _a}1 = 0$, ${\log _a}a = 1.$

${\log _a}\left( {{a^\alpha }} \right) = \alpha$ và ${a^{{{\log }_a}b}} = b.$

2. Tính chất:

2.1. So sánh hai logarit cùng cơ số:
Cho $b, c > 0$, ta có:

+ Khi $a > 1$: ${\log _a}b > {\log _a}c \Leftrightarrow b > c.$

+ Khi $0 < a < 1$: ${\log _a}b > {\log _a}c \Leftrightarrow b < c.$

Cho $0 < a \ne 1$ và $b,c > 0$:

+ ${\log _a}b > 0$ $\Leftrightarrow$ $a$ và $b$ cùng lớn hơn $1$ hay cùng nhỏ hơn $1.$

+ ${\log _a}b < 0$ $\Leftrightarrow a < 1 < b$ hay $b < 1 < a.$

2.2. Các quy tắc tính logarit:
Cho $0 < a \ne 1$ và $b,c > 0$. Ta có:

a) ${\log _a}(b.c) = {\log _a}b + {\log _a}c.$

b) ${\log _a}\left( {\frac{b}{c}} \right) = {\log _a}b – {\log _a}c.$ Đặc biệt ${\log _a}\frac{1}{b} = – {\log _a}b.$

c) ${\log _a}{b^\alpha } = \alpha {\log _a}b.$ Đặc biệt ${\log _a}\sqrt[n]{b} = \frac{1}{n}{\log _a}b$ $\left( {n \in {Z^ + }} \right).$

2.3. Đổi cơ số của logarit:

Với $0 < a,b \ne 1$ và $c > 0$ và $\alpha \ne 0.$

${\log _b}c = \frac{{{{\log }_a}c}}{{{{\log }_a}b}}$ hay ${\log _a}b.{\log _b}c = {\log _a}c.$

${\log _a}b = \frac{1}{{{{\log }_b}a}}$ hay ${\log _a}b.{\log _b}a = 1.$

${\log _{{a^n}}}{c^m} = \frac{m}{n}{\log _a}c.$

Chú ý:

+ Khi $a = 10$ thì ${\log _{10}}x$ gọi là logarit thập phân, ký hiệu là $\log x$ (hoặc $\lg x$).

+ Khi $a = e$ thì ${\log _e}x$ gọi là logarit tự nhiên (hay logarit nê-pe), ký hiệu là $\ln x.$

+ Nếu $x = {10^n}$ thì $\log x = n.$

+ Với $x \ge 1$ tùy ý ta có: $n \le \log x < n + 1$ $\Rightarrow {10^n} \le x < {10^{n + 1}}.$

Suy ra: Nếu $n \le \log x < n + 1$ thì $x$ có $n+1$ chữ số.

<!-- chunk:2 level:2 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Vấn đề 1: Tính toán logarit.

1. PHƯƠNG PHÁP:

Để tính logarit ta sử dụng:

1. Định nghĩa logarit:

Cho $a>0$, $a \ne 1$ và $b > 0.$ Ta có: $\alpha = {\log _a}b \Leftrightarrow {a^\alpha } = b.$

2. Các tính chất của logarit:
${\log _a}1 = 0$, ${\log _a}a = 1.$

${\log _a}{a^b} = b.$

${a^{{{\log }_a}b}} = b.$

${\log _a}(b.c) = {\log _a}b + {\log _a}c.$

${\log _a}\left( {\frac{b}{c}} \right) = {\log _a}b – {\log _a}c.$

${\log _a}{b^\alpha } = \alpha {\log _a}b$ $(\alpha \in R).$

${\log _a}\frac{1}{b} = – {\log _a}b.$

${\log _a}\sqrt[n]{b} = \frac{1}{n}{\log _a}b.$

3. Công thức đổi cơ số của logarit:

Với $0 < a$, $b \ne 1$ và $c> 0$ và $\alpha \ne 0.$

${\log _b}c = \frac{{{{\log }_a}c}}{{{{\log }_a}b}}$ hay ${\log _a}b.{\log _b}c = {\log _a}c.$

${\log _a}b = \frac{1}{{{{\log }_b}a}}$ hay ${\log _a}b.{\log _b}a = 1.$

${\log _{{a^\alpha }}}c = \frac{1}{\alpha }{\log _a}c.$

2. CÁC VÍ DỤ:

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 1: Tính các giá trị sau:

$A = \frac{{{{\log }_{\frac{1}{7}}}32}}{{{{\log }_7}15 – {{\log }_7}30}}.$

$B = {\log _5}\sqrt 3 – \frac{1}{2}{\log _5}12 + {\log _5}250.$

$A = \frac{{{{\log }_{\frac{1}{7}}}32}}{{{{\log }_7}15 – {{\log }_7}30}}$ $= \frac{{ – {{\log }_7}32}}{{{{\log }_7}\frac{{15}}{{30}}}}$ $= \frac{{ – {{\log }_7}32}}{{{{\log }_7}\frac{1}{2}}}$ $= \frac{{ – {{\log }_7}{2^5}}}{{ – {{\log }_7}2}}$ $= \frac{{5{{\log }_7}2}}{{{{\log }_7}2}} = 5.$

$B = {\log _5}\sqrt 3 – \frac{1}{2}{\log _5}12 + {\log _5}250$ $= \frac{1}{2}{\log _5}3 – \frac{1}{2}{\log _5}12 + {\log _5}250$ $= \frac{1}{2}{\log _5}\frac{3}{{12}} + {\log _5}250$ $= \frac{1}{2}{\log _5}{2^{ – 2}} + {\log _5}50$ $= – {\log _5}2 + {\log _5}250$ $= {\log _5}\frac{{250}}{2} = {\log _5}125 = 3.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 2:

a. Rút gọn biểu thức sau: $A = {\log _{\frac{1}{4}}}\left( {{{\log }_3}4.{{\log }_2}3} \right).$

b. Cho ${\log _2}14 = a$, tính ${\log _{49}}32$ theo $a.$

a) $A = {\log _{\frac{1}{4}}}\left( {{{\log }_3}4.{{\log }_2}3} \right)$ $= {\log _{\frac{1}{4}}}\left( {{{\log }_2}4} \right)$ $= {\log _{{2^{ – 2}}}}\left( {{{\log }_2}{2^2}} \right)$ $= – \frac{1}{2}{\log _2}2 = – \frac{1}{2}.$

b) Ta có: ${\log _2}14 = a$ $\Leftrightarrow {\log _2}2 + {\log _2}7 = a$ $\Leftrightarrow {\log _2}7 = a – 1.$

Do đó: ${\log _{49}}32 = {\log _{{7^2}}}{2^5}$ $= \frac{5}{2}{\log _7}2 = \frac{5}{{2(a – 1)}}.$

## Bài tập

## Bài tập 1. Hãy tìm logarit của mỗi số sau theo cơ số $3:$

$81\sqrt 3 .$

$\frac{{\sqrt 3 }}{{\sqrt[3]{3}.\sqrt[6]{3}}}.$

$\frac{{\sqrt[3]{{3\sqrt[5]{3}}}}}{9}.$

$\frac{{27}}{{\sqrt[3]{{9\sqrt[4]{3}}}}}.$

2. Tính:

${\log _{\frac{1}{5}}}125.$

${\log _{0,5}}\frac{{8\sqrt 2 }}{{2\sqrt[3]{4}}}.$

${\log _{\frac{1}{4}}}\frac{{\sqrt[3]{2}}}{{64}}.$

${\log _{\frac{1}{{\sqrt[3]{6}}}}}36\sqrt 6 .$

3. Tính:

${3^{{{\log }_3}18}}.$

${3^{5{{\log }_3}2}}.$

${\left( {\frac{1}{8}} \right)^{1 + {{\log }_2}5}}.$

${\left( {\frac{1}{{32}}} \right)^{ – 1 – {{\log }_{0,5}}5}}.$

4. Hãy tính:

a. $A = 2{\log _{64}}12 + {\log _{2\sqrt 2 }}\sqrt {15} + {\log _8}20.$

b. $B = \frac{1}{2}{\log _7}36 – {\log _{49}}196 – 3{\log _7}\sqrt[3]{{21}}.$

c. $C = \frac{{\left( {{{\log }_5}36 – {{\log }_5}12} \right){{\log }_9}49}}{{{{\log }_5}7}}.$

d. $D = {36^{{{\log }_6}5}} + {10^{1 – \log 2}} – {8^{{{\log }_2}3}}.$

## Bài tập 5. Đơn giản các biểu thức:

a. $M = \log \frac{1}{8} + \frac{1}{2}\log 4 + 4\log \sqrt 2 .$

b. $N = \log \frac{4}{9} + \frac{1}{2}\log 36 + \frac{3}{2}\log \frac{9}{2} – \frac{1}{2}\log 2.$

c. $P = \log 81\sqrt 3 – 2\log \frac{{27}}{{16}} + \log \sqrt {108} .$

d. $Q = \log \frac{1}{8} – \log 0,375 + 2\log \sqrt {0,5625} .$

6. Hãy tính:

a. $\ln \sqrt e + \ln \frac{1}{{e\sqrt[3]{e}}}.$

b. $5\ln \frac{{{e^{ – 1}}}}{{\sqrt e }} + 4\ln \left( {{e^2}\sqrt e } \right).$

## Bài tập 7. Đơn giản các biểu thức:

a. $A = {\left( {\ln a + {{\log }_a}e} \right)^2} + {\ln ^2}a – \log _a^2e.$

b. $B = 2\ln a + 3{\log _a}e$ $– \frac{3}{{\ln a}} – \frac{2}{{{{\log }_a}e}} + 2\ln 10{\log _a}e.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Vấn đề 2: So sánh hai logarit.

1. PHƯƠNG PHÁP:

Để so sánh hai logarit ta áp dụng các kết quả sau:

1. Nếu $a >1$ thì: ${\log _a}M > {\log _a}N \Leftrightarrow M > N > 0.$

2. Nếu $0<a< 1$ thì: ${\log _a}M > {\log _a}N \Leftrightarrow 0 < M < N.$

3. Nếu $0 < a < b < 1$ hay $1 < a < b$ thì:

${\log _a}x > {\log _b}x \Leftrightarrow x > 1.$

${\log _a}x < {\log _b}x \Leftrightarrow 0 < x < 1.$

## Bài tập 4. ${\log _a}b > 0$ $\Leftrightarrow a\Leftrightarrow a$ và $b$ cùng lớn hơn $1$ hay cùng nhỏ hơn $1.$

2. CÁC VÍ DỤ:

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 1: Hãy so sánh hai số sau:

a) $m = {\log _{\sqrt 3 }}\frac{3}{5}$ với $n = {\log _{\sqrt 3 }}\frac{7}{9}.$

b) $m = {\log _{\sqrt 2 – 1}}15$ với $n = {\log _{\sqrt 2 – 1}}2.$

a) Ta có: $a = \sqrt 3 > 1$ và $\frac{3}{5} < \frac{7}{9}$ nên ${\log _{\sqrt 3 }}\frac{3}{5} < {\log _{\sqrt 3 }}\frac{7}{9}.$

Vậy $m<n.$

b) Ta có: $a = \sqrt 2 – 1 < 1$ và $15 > 2$ nên ${\log _{\sqrt 2 – 1}}15 < {\log _{\sqrt 2 – 1}}2.$

Vậy $m < n.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 2: So sánh hai số sau: $m = {\log _{\frac{1}{3}}}8$ với $n = {\log _{115}}2.$

Ta có: $\frac{1}{3} < 1$ và $8>1$ nên ${\log _{\frac{1}{3}}}8 < 0.$

$115 > 1$ và $2 > 1$ nên ${\log _{115}}2 > 0.$

Vậy $m < n.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 3: So sánh hai số sau: $m = {\log _3}4$ với $n = {\log _2}3.$

Ta có:

$m = {\log _3}4 = {\log _{{3^2}}}{4^2} = {\log _9}16.$

$n = {\log _2}3 = {\log _{{2^3}}}{3^3} = {\log _8}27.$

Ta có:

$8 > 1$ và $27 > 16$ nên ${\log _8}27 > {\log _8}16$ $(1).$

$8 < 9$ và $16 > 1$ nên ${\log _8}16 > {\log _9}16$ $(2).$

Từ $(1)$ và $(2)$ suy ra $m<n.$

## Bài tập
## Bài tập 1. So sánh các số sau:

a. ${\log _3}4$ với ${\log _4}\frac{1}{3}.$

b. ${3^{{{\log }_7}1,4}}$ với ${7^{{{\log }_5}0,92}}.$

c. $\log 2 + \log 3$ với $\log 5.$

d. $\log 13 – \log 3$ với $\log 6.$

e. $2\ln 2 – \ln 5$ với $\log 1,1.$

f. $1 + 2\log 3$ với $\log 89.$

## Bài tập 2. So sánh các số sau:

a. ${\log _7}29$ với ${\log _3}5.$

b. ${\log _{0,3}}0,8$ với ${\log _{0,2}}0,3.$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Vấn đề 3: Biểu diễn một logarit theo các logarit khác.
1. PHƯƠNG PHÁP:
Để biểu diễn ${\log _a}b$ theo ${\log _c}d$ ta đưa ${\log _a}b$ về logarit theo cơ số $c$ và viết $a$ và $b$ thành tích hay thương của các lũy thừa theo cơ số $c$ và $d.$

Áp dụng tính chất logarit của tích và của thương ta suy ra kết quả.

2. CÁC VÍ DỤ:

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 1: Cho $\alpha = {\log _2}3$ và $\beta = {\log _2}5.$ Hãy tính ${\log _{225}}(2700).$

Ta có: ${\log _{225}}(2700) = \frac{{{{\log }_2}2700}}{{{{\log }_2}225}}$ $= \frac{{{{\log }_2}\left( {{2^2}{{.3}^3}{{.5}^2}} \right)}}{{{{\log }_2}\left( {{3^2}{{.5}^2}} \right)}}$ $= \frac{{2{{\log }_2}2 + 3{{\log }_2}3 + 2{{\log }_2}5}}{{2{{\log }_2}3 + 2{{\log }_2}5}}$ $= \frac{{2 + 3\alpha + 2\beta }}{{2\alpha + 2\beta }}.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 2: Biểu diễn theo $a = \ln 2$ các số sau:

$\ln 16$, $\ln 0,125$, $\frac{1}{8}\ln \frac{1}{4} – \frac{1}{4}\ln \frac{1}{8}.$

$\ln 16 = \ln {2^4} = 4\ln 2 = 4a.$

$\ln 0,125 = \ln \frac{1}{8} = – 3\ln 2 = – 3a.$

$\frac{1}{8}\ln \frac{1}{4} – \frac{1}{4}\ln \frac{1}{8}$ $= \frac{1}{8}\ln {2^{ – 2}} – \frac{1}{4}\ln {2^{ – 3}}$ $= – \frac{1}{4}\ln 2 + \frac{3}{4}\ln 2$ $= \frac{1}{2}\ln 2 = \frac{1}{2}a.$

## Bài tập
## Bài tập 1. Hãy biểu diễn các logarit sau qua $\alpha$ và $\beta :$

a. ${\log _{\sqrt 3 }}50$, nếu ${\log _3}15 = \alpha$, ${\log _3}10 = \beta .$

b. ${\log _4}1250$, nếu ${\log _2}5 = \alpha .$

c. ${\log _{30}}1350$, nếu ${\log _{30}}5 = a$ và ${\log _{30}}3 = b.$

## Bài tập 2. Biểu diễn các số sau đây theo $a = \ln 2$, $b = \ln 5$.

a) $\ln 500.$

b) $\ln \frac{{16}}{{25}}.$

c) $\ln 6,25.$

d) $\ln \frac{1}{2} + \ln \frac{2}{3} + \ldots + \ln \frac{{98}}{{99}} + \ln \frac{{99}}{{100}}.$

## Bài tập 3. Biểu diễn theo $a = \ln 2$, $b = \ln 3$ các số sau:

$\ln 36$, $\ln \frac{1}{{12}}$, $\ln 21 + 2\ln 14 – 3\ln 0,875.$

## Bài tập 4. Biết ${\log _a}b = 3$, ${\log _a}c = – 2$, hãy tính ${\log _a}x.$

a) $x = {a^3}{b^2}\sqrt c .$

b) $x = \frac{{{a^4}\sqrt[3]{b}}}{{{c^3}}}.$

<!-- chunk:12 level:2 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Vấn đề 4: Tìm giá trị của $x$ thỏa mãn hệ thức logarit.
1. PHƯƠNG PHÁP:
Sử dụng các công thức biến đổi logarit đưa hệ thức đã cho về dạng:

${\log _a}f(x) = {\log _a}g(x).$

Từ đó ta có:
\left\{ {\begin{array}{l}
{f(x) = g(x)}\\
{f(x) > 0{\rm{ \:hay\: }}g(x) > 0}
\end{array}} \right..
Giải hệ ta tìm được $x.$

2. CÁC VÍ DỤ:
Ví dụ: Tìm $x$ biết ${\log _3}\left( {{x^2} – 1} \right) + {\log _9}\left( {{x^2} – 1} \right) = \frac{3}{2}.$

${\log _3}\left( {{x^2} – 1} \right) + {\log _9}\left( {{x^2} – 1} \right) = \frac{3}{2}$ $\Leftrightarrow {\log _3}\left( {{x^2} – 1} \right) + \frac{1}{2}{\log _3}\left( {{x^2} – 1} \right) = \frac{3}{2}$ $\Leftrightarrow {\log _3}\left( {{x^2} – 1} \right) = 1.$

$\Leftrightarrow {x^2} – 1 = 3$ $\Leftrightarrow {x^2} = 4$ $\Leftrightarrow {x^2} = 4.$

## Bài tập
## Bài tập 1. Tìm $x$ biết:

a. ${\log _{x – 1}}(4x – 4) = 2.$

b. ${\log _2}\left( {{x^3} + 2{x^2}} \right) = 4.$

c. ${\log _3}\left( {{x^3} + 2} \right) = 3.$

d. ${\log _{\frac{1}{6}}}\left( {{x^2} – 4x – 6} \right) = – 1.$

## Bài tập 2. Trong mỗi trường hợp sau, hãy tìm $x$ theo $a$ và $b$ $(a,b > 0)$:

a. ${\log _3}x = 4{\log _3}a + 7{\log _3}b.$

b. ${\log _5}x = 2{\log _5}a – 3{\log _5}b.$

## Bài tập 3. Tìm $x$ biết:

a. ${\log _x}(24 + x) = 3.$

b. ${\log _x}\frac{1}{{64}} = \frac{{ – {{\log }_{\sqrt 2 }}2}}{{{{\log }_{12}}2 + {{\log }_{12}}6}}.$

**Vấn đề 5: Chứng minh đẳng thức chứa logarit.

****1. PHƯƠNG PHÁP:**

Áp dụng các công thức biến đổi logarit, công thức đổi cơ số để biến đổi vế này thành vế kia, hai vế cùng bằng một đại lượng khác.

2. VÍ DỤ:

<!-- chunk:13 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 1: Cho $a$, $b$, $c$ là ba số dương và $c \ne 1.$

Chứng minh rằng: ${a^{{{\log }_c}b}} = {b^{{{\log }_c}a}}.$

Áp dụng công thức ${a^{{{\log }_a}b}} = b$, ta có:

${a^{{{\log }_c}b}} = {\left( {{b^{{{\log }_b}a}}} \right)^{{{\log }_c}b}}$ $= {b^{{{\log }_c}b.{{\log }_b}a}} = {b^{{{\log }_c}a}}.$

Vậy đẳng thức được chứng minh.

<!-- chunk:14 level:3 source:https://toanmath.com/2019/08/huong-dan-giai-mot-so-dang-bai-tap-ve-phep-toan-logarit.html -->
## Ví dụ 2: Cho $a$, $b$, $c$ là các số dương và khác $1.$

Chứng minh rằng: $\frac{{{{\log }_a}c}}{{{{\log }_{ab}}c}} = 1 + {\log _a}b.$

Ta có: Vế trái $= {\log _c}ab.{\log _a}c$ $= \left( {{{\log }_c}a + {{\log }_c}b} \right){\log _a}c$ $= {\log _a}c.{\log _c}a + {\log _a}c.{\log _c}b$ $= 1 + {\log _a}b$ $=$ Vế phải.

Vậy đẳng thức đã được chứng minh.

## Bài tập

## Bài tập 1. Chứng minh: $\frac{7}{{16}}\ln (3 + 2\sqrt 2 ) – 4\ln (\sqrt 2 + 1)$ $– \frac{{25}}{8}\ln (\sqrt 2 – 1) = 0.$

## Bài tập 2. Chứng minh rằng:

a. Nếu
\left\{ {\begin{array}{l}
{{a^2} + {b^2} = 7ab}\\
{a > 0,b > 0}
\end{array}} \right.
thì ${\log _7}\frac{{a + b}}{3} = \frac{1}{2}\left( {{{\log }_7}a + {{\log }_7}b} \right).$

b. Nếu
\left\{ {\begin{array}{l}
{{x^2} + 4{y^2} = 12xy}\\
{x > 0,y > 0}
\end{array}} \right.
$$
 thì $2\log (x + 2y) = \log x + \log y + 4\log 2.$

## Bài tập 3. Chứng minh: ${a^{\sqrt {{{\log }_a}b} }} – {b^{\sqrt {{{\log }_b}a} }} = 0.$

## Bài tập 4. Cho $0 < a \ne 1$, $0 < x \ne 1$ và $n \in N*$. Chứng minh: $\frac{1}{{{{\log }_a}x}} + \frac{1}{{{{\log }_{{a^2}}}x}} + \ldots + \frac{1}{{{{\log }_{{a^n}}}x}} = \frac{{n(n + 1)}}{{2{{\log }_a}x}}.$

## Bài tập 5. Cho $a = {\log _{12}}18$ và $b = {\log _{24}}54.$ Chứng minh rằng: $5(a – b) + ab = 1.$