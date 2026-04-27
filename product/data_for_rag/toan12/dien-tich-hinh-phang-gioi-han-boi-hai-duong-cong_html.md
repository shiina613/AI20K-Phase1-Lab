# Diện tích hình phẳng giới hạn bởi hai đường cong

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
Bài viết hướng dẫn phương pháp ứng dụng tích phân để tính diện tích hình phẳng giới hạn bởi hai đường cong, đây là dạng toán thường gặp trong chương trình Giải tích 12 chương 3: Nguyên hàm – Tích phân và Ứng dụng.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## I. KIẾN THỨC CẦN NHỚ
1. Cho hai hàm số $y = f(x)$, $y = g(x)$ liên tục trên đoạn $[a;b].$ Diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = f(x)$, $y = g(x)$ và hai đường thẳng $x=a$, $x=b$ là: $S = \int_a^b | f(x) – g(x)|dx.$

2. Xem lại cách khử dấu giá trị tuyệt đối trong công thức tính diện tích hình phẳng.

3. Diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = f(x)$ và $y = g(x)$ cho bởi công thức $S = \int_\alpha ^\beta | f(x) – g(x)|dx$, trong đó $\alpha$, $\beta$ lần lượt là nghiệm nhỏ nhất và lớn nhất của phương trình $f(x) – g(x) = 0.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 1: Gọi $S$ là diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = f(x)$, $y=g(x)$ và hai đường thẳng $x=a$, $x=b$ (phần gạch chéo trong hình vẽ bên).

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-1.png" alt="">

Khẳng định nào sau đây đúng?

A. $S = \int_b^a | f(x) – g(x)|dx.$

B. $S = \int_a^b {[g(x) – f(x)]dx} .$

C. $S = \left| {\int_a^b f (x)dx} \right| – \left| {\int_a^b g (x)dx} \right|.$

D. $S = \int_b^a g (x)dx – \int_b^a f (x)dx.$

Lời giải:

Từ đồ thị ta có $f(x) – g(x) > 0$, $\forall x \in [a;b].$

$\Rightarrow S = \int_a^b | f(x) – g(x)|dx$ $= \int_a^b {[f(x) – g(x)]dx} .$

$= \int_a^b f (x)dx – \int_a^b g (x)dx$ $= \int_b^a g (x)dx – \int_b^a f (x)dx.$

> **Đáp án: D**

<!-- chunk:3 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 2: Gọi $S$ là diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = f(x)$, $y = g(x)$ và hai đường thẳng $x=a$, $x=b$ (phần gạch chéo trong hình vẽ bên).

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-2.png" alt="">

Khẳng định nào sau đây đúng?

A. $S = \int_a^b {[f(x) – g(x)]dx.}$

B. $S = \left| {\int_a^b {[f(x) – g(x)]dx} } \right|.$

C. $S = \left| {\int_a^b f (x)dx} \right| – \left| {\int_a^b g (x)dx} \right|.$

D. $S = \int_a^c {[f(x) – g(x)]dx}$ $– \int_c^b {[f(x) – g(x)]dx} .$

Lời giải:

Từ đồ thị ta có $f(x) – g(x) \ge 0$, $\forall x \in [a;c]$ và $f(x) – g(x) \le 0$, $\forall x \in [c;b].$

$\Rightarrow S = \int_a^b | f(x) – g(x)|dx$ $= \int_a^c {[f(x) – g(x)]dx}$ $– \int_c^b {[f(x) – g(x)]dx} .$

> **Đáp án: D**

<!-- chunk:4 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 3: Gọi ${S_1}$ là diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y = f(x)$, $y = g(x)$ và hai đường thẳng $x = a$, $x = b$ $(a < b)$; ${S_2}$ là diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y = 2018f(x)$, $y = 2018g(x)$ và hai đường thẳng $x=a$, $x=b.$ Khẳng định nào sau đây đúng?

A. ${S_1} > {S_2}.$

B. ${S_1} < {S_2}.$

C. ${S_1} = 2018{S_2}.$

D. ${S_2} = 2018{S_1}.$

Lời giải:

Ta có:

${S_1} = \int_a^b | f(x) – g(x)|dx.$

${S_2} = \int_a^b | 2018f(x) – 2018g(x)|dx$ $= 2018\int_a^b | f(x) – g(x)|dx$ $\Rightarrow {S_2} = 2018{S_1}.$

> **Đáp án: D**

<!-- chunk:5 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 4: Tính diện tích $S$ của hình phẳng giới hạn bởi đồ thị các hàm số $y = {x^2} + x$, $y = 3x$ và hai đường thẳng $x=1$, $x=3.$

A. $S = \frac{2}{3}.$

B. $S = \frac{4}{3}.$

C. $S = 3.$

D. $S = 2.$

Lời giải:

+ Cách 1:

Ta có: $S = \int_1^3 {\left| {{x^2} + x – 3x} \right|dx}$ $= \int_1^3 {\left| {{x^2} – 2x} \right|dx} .$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-3.png" alt="">

$\Rightarrow S = – \int_1^2 {\left( {{x^2} – 2x} \right)dx}$ $+ \int_2^3 {\left( {{x^2} – 2x} \right)dx}$ $= – \left. {\left( {\frac{{{x^3}}}{3} – {x^2}} \right)} \right|_1^2$ $+ \left. {\left( {\frac{{{x^3}}}{3} – {x^2}} \right)} \right|_2^3 = 2.$

> **Đáp án: D**

+ Cách 2:

Xét phương trình ${x^2} + x – 3x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \notin [1;3]}\\
{x = 2 \in [1;3]}
\end{array}} \right..
$$

Do đó: $S = \int_1^3 {\left| {{x^2} – 2x} \right|dx}$ $= \left| {\int_1^2 {\left( {{x^2} – 2x} \right)dx} } \right|$ $+ \left| {\int_2^3 {\left( {{x^2} – 2x} \right)dx} } \right|.$

$= \left| {\left. {\left( {\frac{{{x^3}}}{3} – {x^2}} \right)} \right|_1^2} \right|$ $+ \left| {\left. {\left( {\frac{{{x^3}}}{3} – {x^2}} \right)} \right|_2^3} \right| = 2.$

> **Đáp án: D**

<!-- chunk:6 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 5: Tính diện tích $S$ của hình phẳng giới hạn bởi đồ thị hai hàm số $y = {x^3} – x$ và $y = 3x.$

A. $S=6.$

B. $S=7.$

C. $S=8.$

D. $S=9.$

Lời giải:

Xét phương trình ${x^3} – 4x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 2}
\end{array}} \right..
$$

Do đó $S = \int_{ – 2}^2 {\left| {{x^3} – 4x} \right|dx}$ $= \left| {\int_{ – 2}^0 {\left( {{x^3} – 4x} \right)dx} } \right|$ $+ \left| {\int_0^2 {\left( {{x^3} – 4x} \right)dx} } \right|.$

$= \left| {\left. {\left( {\frac{{{x^4}}}{4} – 2{x^2}} \right)} \right|_{ – 2}^0} \right|$ $+ \left| {\left. {\left( {\frac{{{x^4}}}{4} – 2{x^2}} \right)} \right|_0^2} \right| = 8.$

> **Đáp án: C**

<!-- chunk:7 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 6: Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = {x^3} – x$ và đồ thị hàm số $y = x – {x^2}.$

A. $\frac{{37}}{{12}}.$

B. $\frac{9}{4}.$

C. $\frac{{81}}{{12}}.$

D. $13.$

Lời giải:

Xét phương trình ${x^3} – x – x + {x^2} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = – 2}\\
{x = 1}
\end{array}} \right..
$$

Do đó $S = \int_{ – 2}^1 {\left| {{x^3} + {x^2} – 2x} \right|dx}$ $= \left| {\int_{ – 2}^0 {\left( {{x^3} + {x^2} – 2x} \right)dx} } \right|$ $+ \left| {\int_0^1 {\left( {{x^3} + {x^2} – 2x} \right)dx} } \right|.$

$= \left| {\left. {\left( {\frac{{{x^4}}}{4} + \frac{{{x^3}}}{3} – {x^2}} \right)} \right|_{ – 2}^0} \right|$ $+ \left| {\left. {\left( {\frac{{{x^4}}}{4} + \frac{{{x^3}}}{3} – {x^2}} \right)} \right|_0^1} \right| = \frac{{37}}{{12}}.$

> **Đáp án: A**

<!-- chunk:8 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 7: Tính diện tích $S$ của hình phẳng giới hạn bởi đồ thị hai hàm số $y = {(x – 6)^2}$, $y = 6x – {x^2}.$

A. $S=9.$

B. $S = \frac{9}{2}.$

C. $S=48.$

D. $S = \frac{{52}}{3}.$

Lời giải:

Xét phương trình ${(x – 6)^2} – 6x + {x^2} = 0$ $\Leftrightarrow 2{x^2} – 18x + 36$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 3}\\
{x = 6}
\end{array}} \right..
$$

$\Rightarrow S = \int_3^6 {\left| {2{x^2} – 18x + 36} \right|dx}$ $= \left| {\int_3^6 {\left( {2{x^2} – 18x + 36} \right)dx} } \right|.$

$= \left| {\left. {\left( {\frac{{2{x^3}}}{3} – 9x + 36x} \right)} \right|_3^6} \right| = 9.$

> **Đáp án: A**

<!-- chunk:9 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 8: Diện tích hình phẳng giới hạn bởi đường cong $y = {x^2} + 1$, tiếp tuyến với đường cong này tại điểm $M(2;5)$ và trục $Oy$ bằng:

A. $\frac{5}{{12}}.$

B. $\frac{8}{3}.$

C. $4.$

D. $\frac{{107}}{{12}}.$

Lời giải:

Ta có: $y = {x^2} + 1$ $\Rightarrow y’ = 2x$ $\Rightarrow y'(2) = 4.$

Phương trình tiếp tuyến của đường cong $y = {x^2} + 1$ tại điểm $M(2;5)$ là:

$y – 5 = 4(x – 2)$ $\Leftrightarrow y = 4x – 3.$

Xét phương trình: ${x^2} + 1 – 4x + 3 = 0$ $\Leftrightarrow x = 2.$

$S = \int_0^2 {\left| {{x^2} – 4x + 4} \right|dx}$ $= \int_0^2 {{{(x – 2)}^2}} dx$ $= \left. {\frac{{{{(x – 2)}^3}}}{3}} \right|_0^2 = \frac{8}{3}.$

> **Đáp án: B**

<!-- chunk:10 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 9: Diện tích hình phẳng giới hạn bởi đường cong $y = {x^3} – 3x$ và tiếp tuyến với đường cong này tại điểm $M( – 1;2)$ bằng:

A. ${\frac{9}{4}.}$

B. ${\frac{{15}}{4}.}$

C. ${\frac{{27}}{4}.}$

D. ${\frac{{35}}{4}.}$

Lời giải:

Ta có: $y = {x^3} – 3x$ $\Rightarrow y’ = 3{x^2} – 3$ $\Rightarrow y'( – 1) = 0.$

Phương trình tiếp tuyến của đường cong $y = {x^3} – 3x$ tại điểm $M( – 1;2)$ là:

$y – 2 = 0(x + 1)$ $\Leftrightarrow y = 2.$

Xét phương trình: ${x^3} – 3x – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2}\\
{x = – 1}
\end{array}} \right..
$$

$S = \int_{ – 1}^2 {\left| {{x^3} – 3x – 2} \right|dx}$ $= \left| {\int_{ – 1}^2 {\left( {{x^3} – 3x – 2} \right)dx} } \right|$ $= \left. {\left( {\frac{{{x^4}}}{4} – \frac{{3{x^2}}}{2} – 2x} \right)} \right|_{ – 1}^2$ $= \frac{{27}}{4}.$

> **Đáp án: C**

<!-- chunk:11 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 10: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = {e^{2x}}$, $y = {e^{ – x}}$ và đường thẳng $x=1$ bằng $a.{e^2} + \frac{1}{e} + b$ với $a$, $b$ là các số hữu tỉ. Tính $T = 2a + b.$

A. $T = \frac{5}{2}.$

B. $T = – \frac{5}{2}.$

C. $T = – 1.$

D. $T = – \frac{1}{2}.$

Lời giải:

Xét phương trình ${e^{2x}} – {e^{ – x}} = 0$ $\Leftrightarrow x = 0.$

Do đó $S = \int_0^1 {\left| {{e^{2x}} – {e^{ – x}}} \right|dx}$ $= \left| {\int_0^1 {\left( {{e^{2x}} – {e^{ – x}}} \right)dx} } \right|$ $= \left. {\left( {\frac{{{e^{2x}}}}{2} + {e^{ – x}}} \right)} \right|_0^1$ $= \frac{{{e^2}}}{2} + \frac{1}{e} – \frac{3}{2}.$

$\Rightarrow a = \frac{1}{2}$, $b = – \frac{3}{2}$ $\Rightarrow T = 2a + b = – \frac{1}{2}.$

> **Đáp án: D**

<!-- chunk:12 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 11: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = {e^{2x}} + {e^x}$, $y = 4{e^x} – 2$ bằng $\frac{a}{b} + c\ln 2$ với $\frac{a}{b}$ là phân số tối giản, $c$ là số nguyên. Tính $T = {a^2} + b – c.$

A. $T=9.$

B. $T=1.$

C. $T =15.$

D. $T=13.$

Lời giải:

Xét phương trình ${e^{2x}} + {e^x} – 4{e^x} + 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{e^x} = 1}\\
{{e^x} = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \ln 2}
\end{array}} \right..
$$

Do đó $S = \int_0^{\ln 2} {\left| {{e^{2x}} – 3{e^x} + 2} \right|dx}$ $= \left| {\int_0^{\ln 2} {\left( {{e^{2x}} – 3{e^x} + 2} \right)dx} } \right|.$

$= \left. {\left( {\frac{{{e^{2x}}}}{2} – 3{e^x} + 2x} \right)} \right|_0^{\ln 2}$ $= \frac{3}{2} – 2\ln 2.$

$\Rightarrow a = 3$, $b = 2$, $c = – 2$ $\Rightarrow T = {a^2} + b – c = 13.$

> **Đáp án: D**

<!-- chunk:13 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 12: Tính diện tích $S$ của hình phẳng giới hạn bởi đồ thị hai hàm số $y = x{e^x}$, $y = m{e^x}$ $(m > 1)$ và đường thẳng $x=1.$

A. $S = me – {e^m}.$

B. $S = {e^m} – me.$

C. $S = {e^m} – me – 2e.$

D. $S = me – {e^m} + 2e.$

Lời giải:

Xét phương trình $x{e^x} – m{e^x} = 0$ $\Leftrightarrow x = m.$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-4.png" alt="">

$\Rightarrow S = \int_1^m {\left| {2{e^x} – m{e^x}} \right|dx}$ $= \int_1^m {(m – x)} {e^x}dx.$

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-5.png" alt="">

$\Rightarrow S = \left. {(m – x){e^x}} \right|_1^m$ $+ \left. {{e^x}} \right|_1^m$ $= {e^m} – me.$

> **Đáp án: B**

<!-- chunk:14 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 13: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = 2x\ln x$, $y = 6\ln x$ bằng $a + b\ln 3$ với $a$, $b$ là các số nguyên. Tính $T = 2a + b.$

A. $T = 10.$

B. $T=-7.$

C. $T=7.$

D. $T=-10.$

Lời giải:

Xét phương trình $2x\ln x – 6\ln x = 0$ $\Leftrightarrow (2x – 6)\ln x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 3}\\
{x = 1}
\end{array}} \right..
$$

$\Rightarrow S = \int_1^3 | 2x\ln x – 6\ln x|dx$ $= \left| {\int_1^3 {(2x – 6)} \ln xdx} \right|.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \ln x}\\
{dv = (2x – 6)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{1}{x}dx}\\
{dv = {x^2} – 6x}
\end{array}} \right..
$$

Khi đó $S = \left| {\int_1^3 {(2x – 6)} \ln xdx} \right|$ $= \left| {\left. {\left( {{x^2} – 6x} \right)\ln x} \right|_1^3 – \int_1^3 {(x – 6)dx} } \right|.$

$= \left| {\left. {\left( {{x^2} – 6x} \right)\ln x} \right|_1^3 – \left. {\left( {\frac{{{x^2}}}{2} – 6x} \right)} \right|_1^3} \right|$ $= – 8 + 9\ln 3.$

$\Rightarrow a = – 8$, $b = 9$ $\Rightarrow T = 2a + b = – 7.$

> **Đáp án: B**

<!-- chunk:15 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 14: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = 2\cos x$, $y = 3$ và hai đường thẳng $x = 0$, $x = \frac{\pi }{4}$ bằng $\frac{a}{b}\pi + \frac{{\sqrt 2 }}{c}$ với $\frac{a}{b}$ là phân số tối giản, $c$ là số nguyên. Tính $T = 2a + b + c.$

A. $T=-12.$

B. $T=-9.$

C. $T=9.$

D. $T = 12.$

Lời giải:

Ta có $S = \int_0^{\frac{\pi }{4}} | 2\cos x – 3|dx$ $= \int_0^{\frac{\pi }{4}} {(3 – 2\cos x)dx}$ (vì $2\cos x – 3 < 0$, $\forall x \in \left[ {0;\frac{\pi }{4}} \right]$).

$= \left. {(3x – 2\sin x)} \right|_0^{\frac{\pi }{4}}$ $= \frac{{3\pi }}{4} – \sqrt 2$ $\Rightarrow a = 3$, $b = 4$, $c = – 1$ $\Rightarrow T = 2a + b + c = 9.$

> **Đáp án: C**

<!-- chunk:16 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 15: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = 1 + {\cos ^2}x$, $y = {\sin ^2}x$ và hai đường thẳng $x = 0$, $x = \frac{\pi }{4}$ bằng $\frac{a}{b}\pi + \frac{c}{d}$ với $\frac{a}{b}$, $\frac{c}{d}$ là các phân số tối giản. Tính $T = a + b + c + d.$

A. $T=6.$

B. $T =7.$

C. $T =8.$

D. $T=9.$

Lời giải:

Ta có $S = \int_0^{\frac{\pi }{4}} {\left| {1 + {{\cos }^2}x – {{\sin }^2}x} \right|dx}$ $= \int_0^{\frac{\pi }{4}} | 1 + \cos 2x|dx.$

$= \int_0^{\frac{\pi }{4}} {(1 + \cos 2x)dx}$ (vì ${1 + \cos 2x \ge 0}$, ${\forall x \in \left[ {0;\frac{\pi }{2}} \right]}$).

$= \left. {\left( {x + \frac{1}{2}\sin 2x} \right)} \right|_0^{\frac{\pi }{4}}$ $= \frac{\pi }{4} + \frac{1}{2}$ $\Rightarrow a = 1$, $b = 4$, $c = 1$, $d = 2.$

$\Rightarrow T = a + b + c + d = 8.$

> **Đáp án: C**

<!-- chunk:17 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 16: Cho diện tích hình phẳng giới hạn bởi hai đường cong $y = {x^2}$, $x = {y^2}$ bằng $\frac{a}{b}$ với $\frac{a}{b}$ là các phân số tối giản. Khi đó khoảng cách từ điểm $M(a;b)$ đến điểm $A(2;1)$ bằng:

A. $1.$

B. $\sqrt 5 .$

C. $5.$

D. $\sqrt {29} .$

Lời giải:

Ta có $y = {x^2}$ và $x = {y^2}$ $\Rightarrow x,y \ge 0.$

Khi đó $x = {y^2}$ $\Leftrightarrow y = \sqrt x .$

Xét phương trình ${x^2} – \sqrt x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 1}
\end{array}} \right..
$$

Do đó $S = \int_0^1 {\left| {{x^2} – \sqrt x } \right|dx}$ $= \left| {\int_0^1 {\left( {{x^2} – \sqrt x } \right)dx} } \right|$ $= \left| {\left. {\left( {\frac{{{x^3}}}{3} – \frac{2}{3}x\sqrt x } \right)} \right|_0^1} \right| = \frac{1}{3}.$

$\Rightarrow a = 1$, $b = 3$ $\Rightarrow M(1;3)$ $\Rightarrow MA = \sqrt {{{(2 – 1)}^2} + {{(1 – 3)}^2}} = \sqrt 5 .$

> **Đáp án: B**

<!-- chunk:18 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 17: Diện tích hình phẳng giới hạn bởi các đường $y = \left| {{x^2} – 3x + 2} \right|$, $y = x + 2$ bằng $\frac{a}{b}$ với $\frac{a}{b}$ là phân số tối giản. Khẳng định nào sau đây là đúng?

A. ${a^2} – 4b + 2 = 0.$

B. ${a^2} + b – 58 = 0.$

C. $a + {b^2} – 40 = 0.$

D. $a + 2b = 0.$

Lời giải:

Xét phương trình: $\left| {{x^2} – 3x + 2} \right| = x + 2$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x + 2 \ge 0}\\
{\left[ {\begin{array}{l}
{{x^2} – 3x + 2 = x + 2}\\
{{x^2} – 3x + 2 = – x – 2}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 4}
\end{array}} \right..
$$

Do đó $S = \int_0^4 {\left| {\left| {{x^2} – 3x + 2} \right| – x – 2} \right|dx} = \frac{{31}}{3}$ $\Rightarrow a = 31$, $b = 3$ $\Rightarrow a + {b^2} – 40 = 0.$

> **Đáp án: C**

<!-- chunk:19 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 18: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = {x^2} + 4x$, $y = 2x – m$ $(m > 1)$ và hai đường thẳng $x=0$, $x=2$ bằng $4.$ Khẳng định nào sau đây đúng?

A. $m>5.$

B. $m<2.$

C. $2 < m \le 5.$

D. $m \le 2.$

Lời giải:

Với $m>1$, ta có ${x^2} + 2x + m$ $= {(x + 1)^2} + m – 1 \ge 0$, $\forall x \in R.$

Khi đó: $S = \int_0^1 {\left| {{x^2} + 4x – 2x + m} \right|dx}$ $= \int_0^1 {\left( {{x^2} + 2x + m} \right)dx} .$

$= \left. {\left( {\frac{{{x^3}}}{3} + {x^2} + mx} \right)} \right|_0^1$ $= m + \frac{4}{3}.$

$S = 4$ $\Rightarrow \frac{4}{3} + m = 4$ $\Leftrightarrow m = \frac{8}{3}$ $\Rightarrow 2 < m \le 5.$

> **Đáp án: C**

<!-- chunk:20 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 19: Cho diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = {x^2} – x$, $y = x + 3$ và hai đường thẳng $x = 0$, $x = m$ $(m > 3)$ bằng $\frac{{{m^3}}}{3} – {m^2}.$ Khẳng định nào sau đây đúng?

A. $m > 5.$

B. $m \ge 8.$

C. $m \le 5.$

D. $7 < m \le 8.$

Lời giải:

Xét phương trình: ${x^2} – x – x – 3 = 0$ $\Leftrightarrow {x^2} – 2x – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3}
\end{array}} \right..
$$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-6.png" alt="">

Ta có: $S = \int_0^m {\left| {{x^2} – 2x – 3} \right|dx}$ $= – \int_0^3 {\left( {{x^2} – 2x – 3} \right)dx}$ $+ \int_3^m {\left( {{x^2} – 2x – 3} \right)dx} .$

$= – \left. {\left( {\frac{{{x^3}}}{3} – {x^2} – 3x} \right)} \right|_0^3$ $+ \left. {\left( {\frac{{{x^3}}}{3} – {x^2} – 3x} \right)} \right|_3^m$ $= \frac{{{m^3}}}{3} – {m^2} – 3m + 18.$

$S = \frac{{{m^3}}}{3} – {m^2}$ $\Rightarrow – 3m + 18 = 0$ $\Leftrightarrow m = 6$ $\Rightarrow m > 5.$

> **Đáp án: A**

<!-- chunk:21 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 20: Diện tích hình elip $(E):{x^2} + 16{y^2} = 16$ bằng:

A. ${\pi .}$

B. ${2\pi .}$

C. ${3\pi .}$

D. ${4\pi .}$

Lời giải:

Vẽ $(E):{x^2} + 16{y^2} = 16$ như hình bên, ta suy ra:

$S = 4\int_0^4 {\frac{{\sqrt {16 – {x^2}} dx}}{4}}$ $= \int_0^4 {\sqrt {16 – {x^2}} } dx.$

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-7.png" alt="">

Đặt $x = 4\sin t$, $t \in \left[ { – \frac{\pi }{2};\frac{\pi }{2}} \right]$ $\Rightarrow dx = 4\cos tdt.$

Đổi cận: $x = 0$ $\Rightarrow t = 0$, $x = 4$ $\Rightarrow t = \frac{\pi }{2}.$

$S = \int_0^{\frac{\pi }{2}} {\sqrt {16 – 16{{\sin }^2}t} } .4\cos tdt$ $= – 16\int_0^{\frac{\pi }{2}} {{{\cos }^2}} tdt$ $= 8\int_0^{\frac{\pi }{2}} {(1 + \cos 2t)dt} .$

$= \left. {(8t + 4\sin 2t)} \right|_0^{\frac{\pi }{2}} = 4\pi .$

> **Đáp án: D**

<!-- chunk:22 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 21: Trong mặt phẳng tọa độ $Oxy$ cho $(E)$ có phương trình $\frac{{{x^2}}}{{{a^2}}} + \frac{{{y^2}}}{{{b^2}}} = 1$ $(0 < b < a)$ và đường tròn $(C):{x^2} + {y^2} = 7.$ Biết diện tích hình elip $(E)$ gấp $7$ lần diện tích hình tròn $(C).$ Khẳng định nào sau đây là đúng?

A. $ab=7.$

B. $ab = 7\sqrt 7 .$

C. $ab = \sqrt 7 .$

D. $ab = 49.$

Lời giải:

Diện tích hình tròn $(C)$ là: ${S_1} = \pi {R^2} = 7\pi .$

Diện tích hình elip $(E)$ là: ${S_2} = 4\int_0^a {\frac{{b\sqrt {{a^2} – {x^2}} dx}}{a}}$ $= 4\frac{b}{a}\int_0^a {\sqrt {{a^2} – {x^2}} } dx.$

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-8.png" alt="">

Đặt $x = a\sin t$, $t \in \left[ { – \frac{\pi }{2};\frac{\pi }{2}} \right]$ $\Rightarrow dx = a\cos tdt.$

Đổi cận: $x = 0$ $\Rightarrow t = 0$, $x = a$ $\Rightarrow t = \frac{\pi }{2}.$

${S_2} = 4\frac{b}{a}\int_0^{\frac{\pi }{2}} {{a^2}} {\cos ^2}tdt$ $= 2ab\int_0^{\frac{\pi }{2}} {(1 + \cos 2t)dt}$ $= \left. {2ab\left( {t + \frac{1}{2}\sin 2t} \right)} \right|_0^{\frac{\pi }{2}}$ $= \pi ab.$

Theo giả thiết ta có ${S_2} = 7{S_1}$ $\Leftrightarrow \pi ab = 49\pi$ $\Leftrightarrow ab = 49.$

> **Đáp án: D**

Ghi chú: Sau này ta dùng kết quả này cho nhanh các em nhé: “Elip có độ dài trục lớn và trục nhỏ lần lượt là $2a$, $2b$ thì có diện tích $S = \pi ab$”.

<!-- chunk:23 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## Ví dụ 22: Parabol $y = {x^2}$ chia đường tròn tâm là gốc tọa độ, bán kính bằng $\sqrt 2$ thành hai phần. Gọi ${S_1}$ là diện tích phần nằm hoàn toàn trên trục hoành và ${S_2}$ là diện tích phần còn lại. Giá trị ${S_2} – 3{S_1}$ bằng?

A. $\frac{\pi }{2} – 1.$

B. $1 – \frac{\pi }{2}.$

C. $\frac{4}{3}.$

D. $– \frac{4}{3}.$

Lời giải:

Đường tròn tâm $O$, bán kính bằng $2$ có phương trình:

${x^2} + {y^2} = 2.$

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-9.png" alt="">

Tìm các hoành độ giao điểm:

${x^2} + {x^2} = 2$ $\Leftrightarrow x = \pm 1.$

Tính các diện tích:

Diện tích hình tròn $S = \pi {(\sqrt 2 )^2} = 2\pi .$

${S_1} = 2\int_0^1 {\left( {\sqrt {2 – {x^2}} – {x^2}} \right)dx}$ $= 2\int_0^1 {\sqrt {2 – {x^2}} } dx – \left. {\frac{{2{x^3}}}{3}} \right|_0^1.$

Đặt $x = \sqrt 2 \sin t$, $t \in \left[ { – \frac{\pi }{2};\frac{\pi }{2}} \right]$ $\Rightarrow dx = \sqrt 2 \cos tdt.$

Đổi cận: $x = 0$ $\Rightarrow t = 0$, $x = 1$ $\Rightarrow t = \frac{\pi }{4}.$

$\int_0^1 {\sqrt {2 – {x^2}} } dx$ $= \int_0^{\frac{\pi }{4}} {\sqrt {2 – 2{{\sin }^2}t} } .\sqrt 2 \cos tdt.$

$= \int_0^{\frac{\pi }{4}} {(1 + \cos 2t)dt}$ $= \left. {\left( {t + \frac{{\sin 2t}}{2}} \right)} \right|_0^{\frac{\pi }{4}}$ $= \frac{\pi }{4} + \frac{1}{2}.$

$\Rightarrow {S_1} = \frac{\pi }{2} + \frac{1}{3}$ $\Rightarrow {S_2} = S – {S_1}$ $= \frac{{3\pi }}{2} – \frac{1}{3}$ $\Rightarrow {S_2} – 3{S_1} = – \frac{4}{3}.$

> **Đáp án: D**

<!-- chunk:24 level:1 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong.html -->
## III. LUYỆN TẬP
1. ĐỀ BÀI

## Câu 1: Viết công thức tính diện tích $S$ của hình phẳng giới hạn bởi đồ thị hai hàm số $y = {f_1}(x)$, $y = {f_2}(x)$ liên tục trên đoạn $[a;b]$ và các đường thẳng $x = a$, $x=b.$

A. $S = \int_a^b {\left| {{f_1}(x) + {f_2}(x)} \right|dx} .$

B. $S = \int_a^b {\left| {{f_1}(x) – {f_2}(x)} \right|dx} .$

C. $S = \left| {\int_a^b {\left( {{f_1}(x) – {f_2}(x)} \right)dx} } \right|.$

D. $S = \int_a^b {\left[ {{f_2}(x) – {f_1}(x)} \right]dx} .$

## Câu 2: Cho diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = {x^3}$, $y = {x^5}$ bằng $\frac{a}{b}$ với $a$, $b$ là các số nguyên dương và $\frac{a}{b}$ là phân số tối giản. Tính $T = a + b.$

A. ${T = 5.}$

B. ${T = 6.}$

C. $T = 7.$

D. $T = 8.$

## Câu 3: Cho diện tích hình phẳng giới hạn bởi các đường $y = {x^2} + 5$, $y = 6x$, $x = 0$, $x = 1$ bằng $\frac{a}{b}$ với $a$, $b$ là các số nguyên dương và $\frac{a}{b}$ là phân số tối giản. Tính $T = {\log _2}(a + b – 2).$

A. $T = 2.$

B. $T=3.$

C. $T=4.$

D. $T=8.$

## Câu 4: Gọi ${S_1}$ là diện tích của hình phẳng giới hạn bởi elip $\frac{{{x^2}}}{{25}} + \frac{{{y^2}}}{9} = 1$ và ${S_2}$ là diện tích của hình thoi có các đỉnh là các đỉnh của elip đó. Tính tỉ số giữa ${S_1}$ và ${S_2}.$

A. $\frac{{{S_1}}}{{{S_2}}} = \frac{2}{\pi }.$

B. $\frac{{{S_1}}}{{{S_2}}} = \frac{3}{\pi }.$

C. $\frac{{{S_1}}}{{{S_2}}} = \frac{\pi }{3}.$

D. $\frac{{{S_1}}}{{{S_2}}} = \frac{\pi }{2}.$

## Câu 5: Cho diện tích hình phẳng được giới hạn bởi các đường $y = {x^3}$, $y = 2 – {x^2}$, $x = 0$ bằng $\frac{a}{b}$ với $a$, $b$ là các số nguyên dương và $\frac{a}{b}$ là phân số tối giản. Khẳng định nào sau đây là đúng?

A. $a > 2b.$

B. $a > b.$

C. $a = b + 2.$

D. $b = a + 2.$

## Câu 6: Cho diện tích của hình phẳng giới hạn bởi các đường $y = \frac{{\ln x}}{{2\sqrt x }}$, $y = 0$, $x = 1$, $x = e$ bằng $a + b\sqrt e$ với $a$, $b$ là các số nguyên. Giá trị $a+b$ thuộc khoảng nào sau đây?

A. $(0;2).$

B. $(2;4).$

C. $(4;6).$

D. $(6;8).$

## Câu 7: Cho diện tích hình phẳng giới hạn bởi các đường thẳng $y = 2 – x$, $y = 0$, $x = m$, $x = 3$ $(m < 2)$ bằng $13.$ Giá trị $m$ thuộc khoảng nào sau đây?

A. $(-4;-2).$

B. $(-2;0).$

C. $(0;2).$

D. $(-6;-4).$

## Câu 8: Cho diện tích hình phẳng giới hạn bởi các đường $y = (e + 1)x$ và $y = \left( {{e^x} + 1} \right)x$ bằng $\frac{e}{a} + b$ với $a$, $b$ là các số nguyên. Tính $T = a + 2b.$

A. $3.$

B. $2.$

C. $1.$

D. $0.$

## Câu 9: Diện tích hình phẳng giới hạn bởi các đường parabol: $(P):y = {x^2} – 2x + 2$, tiếp tuyến của $(P)$ tại $M(3;5)$ và trục $Oy$ có giá trị thuộc khoảng nào sau đây?

A. $(2;4).$

B. $(4;6).$

C. $(6;8).$

D. $(8;10).$

## Câu 10: Parabol $y = \frac{{{x^2}}}{2}$ chia hình tròn có tâm tại gốc tọa độ, bán kính $2\sqrt 2$ thành $2$ phần. Gọi ${S_1}$, ${S_2}$ lần lượt là diện tích phần gạch chéo và phần không gạch chéo như hình vẽ.

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-hai-duong-cong-10.png" alt="">

Tính tỉ số $\frac{{{S_1}}}{{{S_2}}}$ lấy giá trị gần đúng hàng phần trăm.

A. $0,43.$

B. $0,53.$

C. $0,63.$

D. $0,73.$

**2. BẢNG ĐÁP ÁN**

**Câu** | 
1 | 
2 | 
3 | 
4 | 
5 | 

**Đáp án** | 
B | 
C | 
B | 
D | 
B | 

**Câu** | 
6 | 
7 | 
8 | 
9 | 
10 | 

**Đáp án** | 
A | 
A | 
D | 
D | 
A |