# Tìm tập xác định của hàm số mũ và hàm số logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
Bài viết trình bày phương pháp tìm tập xác định của hàm số mũ và hàm số logarit, đây là dạng toán cơ bản trong chương trình Giải tích 12 chương 2.

1. Phương pháp tìm tập xác định của hàm số mũ và hàm số logarit
Tập xác định của hàm số $y = f(x)$ là tập các giá trị $x \in R$ sao cho tồn tại $f(x) \in R.$

• Hàm số mũ $y = {a^{\varphi (x)}}$ xác định khi:

+ Nếu $a > 0$ và $\varphi (x)$ xác định.

+ Nếu $a = 0$ thì $\varphi (x) \ne 0.$

+ Nếu $a < 0$ thì $\varphi (x) \in Z.$

• Hàm số logarit $y = {\log _a}\varphi (x)$ xác định khi $a > 0$, $a \ne 1$ và $\varphi (x)$ xác định, $\varphi (x) > 0.$

Trong trường hợp có mẫu số thì phải có điều kiện mẫu số xác định và khác $0$, nếu có biểu thức chứa ẩn số trong dấu căn bậc chẵn, biểu thức phải xác định và không âm.

2. Một số ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 1: Tìm tập xác định của hàm số $y = \sqrt {{{\log }_2}(3x + 4)} .$

Hàm số xác định khi 
$$
\left\{ {\begin{array}{l}
{3x + 4 > 0}\\
{{{\log }_2}(3x + 4) \ge 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{3x + 4 > 0}\\
{3x + 4 \ge 1}
\end{array}} \right.
$$
 $\Leftrightarrow 3x + 3 \ge 0$ $\Leftrightarrow x \ge – 1.$

Vậy tập xác định $D = [ – 1, + \infty ).$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 2: Tìm tập xác định của hàm số:

a) $y = \sqrt {16 – {x^2}} {\log _2}\left( {{x^2} – 5x + 6} \right).$

b) $y = \sqrt {{x^2} – 25} + \log \left( {42 + x – {x^2}} \right).$

a) Hàm số xác định khi 
$$
\left\{ {\begin{array}{l}
{16 – {x^2} \ge 0}\\
{{x^2} – 5x + 6 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 4 \le x \le 4}\\
{x < 2\:{\rm{hoặc}}\:x > 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 4 \le x < 2}\\
{3 < x \le 4}
\end{array}} \right.
$$

Vậy $D = [ – 4,2) \cup (3,4].$

b) Tương tự, ta có: 
$$
\left\{ {\begin{array}{l}
{{x^2} – 25 \ge 0}\\
{42 + x – {x^2} > 0}
\end{array}} \right.
$$

Vậy $D = ( – 6, – 5| \cup [5,7).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 3: Tìm tập xác định của hàm số:

a) $y = \sqrt {{x^2} + x – 2} .{\log _3}\left( {9 – {x^2}} \right).$

b) $y = \sqrt {12 – x – {x^2}} .\log \left( {{x^2} – 4} \right).$

Đáp án:

a) $D = ( – 3, – 2| \cup [1,3).$

b) $D = [ – 4, – 2) \cup (2,3].$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 4: Tìm tập xác định và tập giá trị của hàm số: $y = \sqrt {{{\log }_2}\left( {7 – 2x – {x^2}} \right)} .$

Hàm số xác định khi: 
$$
\left\{ {\begin{array}{l}
{7 – 2x – {x^2} > 0}\\
{{{\log }_2}\left( {7 – 2x – {x^2}} \right) \ge 0}
\end{array}} \right.
$$
 $\Leftrightarrow 7 – 2x – {x^2} \ge 1$ ${x^2} + 2x – 6 \le 0$ $\Leftrightarrow – 1 – \sqrt 7 \le x \le – 1 + \sqrt 7 .$

Vậy tập xác định là $D = \left[ { – 1 – \sqrt 7 , – 1 + \sqrt 7 } \right].$

Ta có $\forall x \in D$: ${\log _2}\left( {7 – 2x – {x^2}} \right) \ge 0$ $\Rightarrow y \ge 0.$

Vậy tập giá trị của hàm số là $[0, + \infty ).$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 5: Tìm tập xác định của các hàm số:

a) $y = \sqrt {{{\log }_{\frac{1}{3}}}(x – 3) – 1} .$

b) $y = \sqrt {{{\log }_{\frac{1}{2}}}\frac{{x – 1}}{{x + 5}}} .$

c) $y = \sqrt {{{\log }_{\frac{1}{5}}}\left( {{{\log }_5}\frac{{{x^2} + 1}}{{x + 3}}} \right)} .$

a) Hàm số xác định khi 
$$
\left\{ {\begin{array}{l}
{x – 3 > 0}\\
{{{\log }_{\frac{1}{3}}}(x – 3) – 1 \ge 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 3}\\
{x – 3 \le \frac{1}{3} \Leftrightarrow 3 < x \le \frac{{10}}{3}}
\end{array}} \right.
$$

Vậy $D = \left( {3,\frac{{10}}{3}} \right].$

b) Lập điều kiện: 
$$
\left\{ {\begin{array}{l}
{\frac{{x – 1}}{{x + 5}} > 0}\\
{{{\log }_{\frac{1}{2}}}\frac{{x – 1}}{{x + 5}} \ge 0}
\end{array}} \right.
$$

Giải hệ ta có $x > 1.$

Vậy $D = (1, + \infty ).$

c) Hàm số xác định khi 
$$
\left\{ {\begin{array}{l}
{{{\log }_{\frac{1}{5}}}\left( {{{\log }_5}\frac{{{x^2} + 1}}{{x + 3}}} \right) \ge 0}\\
{{{\log }_5}\frac{{{x^2} + 1}}{{x + 3}} > 0}\\
{\frac{{{x^2} + 1}}{{x + 3}} > 0}
\end{array}} \right.
$$
 $\Leftrightarrow 1 < \frac{{{x^2} + 1}}{{x + 3}} \le 5$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{{x^2} – 5x – 14}}{{x + 3}} \le 0}\\
{\frac{{{x^2} – x – 2}}{{x + 3}} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x < – 3\:{\rm{ hoặc}}\: – 2 \le x \le 7}\\
{ – 3 < x < – 1\:{\rm{ hoặc }}\:x > 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{ – 2 \le x < – 1}\\
{2 < x \le 7}
\end{array}} \right.
$$

Vậy tập xác định là $D = [ – 2, – 1) \cup (2,7].$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 6: Tìm tập xác định của các hàm số:

a) $y = {\log _2}\sqrt {\frac{{x – 3}}{{x + 1}}} .$

b) $y = \sqrt {{{\log }_{\frac{1}{2}}}\frac{{x – 1}}{{x + 5}}} – {\log _2}\sqrt {{x^2} – x – 6} .$

c) $y = {\log _3}\frac{{{x^2} + 4x + 3}}{{x – 2}}.$

a) Lập điều kiện 
$$
\left\{ {\begin{array}{l}
{x \ne – 1}\\
{\frac{{x – 3}}{{x + 1}} > 0}
\end{array}} \right.
$$

Suy ra $D = ( – \infty , – 1) \cup (3, + \infty ).$

b) 
$$
\left\{ {\begin{array}{l}
{{{\log }_{\frac{1}{2}}}\frac{{x – 1}}{{x + 5}} \ge 0}\\
{{x^2} – x – 6 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{0 < \frac{{x – 1}}{{x + 5}} \le 1}\\
{x < – 2\: {\rm{hoặc}}\:x > 3}
\end{array}} \right.
$$

Suy ra $D = (3, + \infty ).$

c) $\frac{{{x^2} + 4x + 3}}{{x – 2}} > 0.$

Suy ra $D = ( – 3, – 1) \cup (2, + \infty ).$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 7: Tìm tập xác định của hàm số: $y = \log \left( { – {x^2} + 3x + 4} \right)$ $+ \frac{1}{{\sqrt {{x^2} – x – 6} }}.$

Hàm số xác định khi: 
$$
\left\{ {\begin{array}{l}
{ – {x^2} + 3x + 4 > 0}\\
{{x^2} – x – 6 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 < x < 4}\\
{x < – 2\:{\rm{hoặc}}\:x > 3}
\end{array}} \right.
$$
 $\Leftrightarrow 3 < x < 4.$

Tập xác định của hàm số là $D = (3;4).$

[ads]

<!-- chunk:8 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 8: Tìm miền xác định của hàm số: $y = \sqrt {{{\log }_3}\left( {\sqrt {{x^2} – 3x + 2} + 4 – x} \right)} .$

Hàm số xác định khi: 
$$
\left\{ {\begin{array}{l}
{{x^2} – 3x + 2 \ge 0}\\
{\sqrt {{x^2} – 3x + 2} + 4 – x \ge 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 1\:{\rm{hoặc}}\:x \ge 2}\\
{\sqrt {{x^2} – 3x + 2} \ge x – 3}
\end{array}} \right.
$$

Giải ${\sqrt {{x^2} – 3x + 2} \ge x – 3}$, ta có: 
$$
\left\{ {\begin{array}{l}
{{x^2} – 3x + 2 \ge 0}\\
{x \le 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \le 1}\\
{2 \le x \le 3}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{x \ge 3}\\
{{x^2} – 3x + 2 \ge {{(x – 3)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 3}\\
{3x \ge 7}
\end{array}} \right.
$$
 $\Leftrightarrow x \ge 3.$ Suy ra 
$$
\left[ {\begin{array}{l}
{x \le 1}\\
{x \ge 2}
\end{array}} \right.
$$

Vậy $D = ( – \infty ,1] \cup [2, + \infty ).$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 9: Tìm tập xác định của hàm số: $y = \sqrt {{{\log }_2}\left( {\frac{1}{{1 – x}} – \frac{1}{{1 + x}}} \right)} .$

Hàm số xác định khi:

$$
\left\{ {\begin{array}{l}
{x \ne \pm 1}\\
{\frac{1}{{1 – x}} – \frac{1}{{1 + x}} > 0}\\
{{{\log }_2}\left( {\frac{1}{{1 – x}} – \frac{1}{{1 + x}}} \right) \ge 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \pm 1}\\
{\frac{{2x}}{{1 \cdot {x^2}}} > 0}\\
{\frac{{2x}}{{1 – {x^2}}} \ge 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \pm 1}\\
{\frac{{{x^2} + 2x – 1}}{{1 – {x^2}}} \ge 0}
\end{array}} \right.
$$

Xét dấu của $P = \frac{{{x^2} + 2x – 1}}{{1 – {x^2}}}$ bằng phương pháp khoảng:

<img link="data_for_rag/toan11/images/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit-1.png" alt="tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit-1">

Vậy tập xác định của hàm số là $D = [ – 1 – \sqrt 2 , – 1) \cup [ – 1 + \sqrt 2 ,1).$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 10: Tìm tập xác định của hàm số: $y = {2^{\sqrt {\left| {x – 3} \right| – |8 – x|} }}$ $+ \sqrt {\frac{{ – {{\log }_{0,3}}(x – 1)}}{{\sqrt {{x^2} – 2x – 8} }}} .$

Hàm số xác định khi:

$$
\left\{ {\begin{array}{l}
{|x – 3| – |8 – x| \ge 0}\\
{x – 1 > 0}\\
{{{\log }_{0,3}}(x – 1) \le 0}\\
{{x^2} – 2x – 8 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{{(x – 3)}^2} \ge {{(8 – x)}^2}}\\
{x > 1}\\
{x – 1 \ge 1}\\
{x < – 2\:{\rm{hoặc}}\:x > 4}
\end{array}} \right.
$$
 $\Leftrightarrow x \ge \frac{{11}}{2}.$

Vậy $D = \left[ {\frac{{11}}{2}, + \infty } \right).$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 11: Với các giá trị nào của $m$ thì hàm số sau đây xác định với mọi $x ∈ R$: $y = \log \sqrt {\cos 2x + m\cos x + 4} .$

Đặt $t = \cos x$, $– 1 \le t \le 1$, ta có: $\cos 2x + m\cos x + 4$ $= 2{\cos ^2}x – 1 + m\cos x + 4$ $= 2{t^2} + mt + 3.$

Hàm số đã cho xác định với mọi $x$ thuộc $R$ khi và chỉ khi $2{t^2} + mt + 3 > 0$ $\forall t \in \left[ { – 1,1} \right].$

Đặt $f(t) = 2{t^2} + mt + 3$, ta có:

$f(t) > 0$ $\forall t \in \left[ { – 1,1} \right]$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\Delta < 0\:\left( 1 \right)\\
\left\{ {\begin{array}{l}
{\Delta \ge 0}\\
{\left[ {\begin{array}{c}
{ – 1 < 1 < {t_1} \le {t_2}}\\
{{t_1} \le {t_2} < – 1 < 1}
\end{array}} \right.}
\end{array}} \right.
\end{array} \right.\:\left( 2 \right)
$$

Ta có: $\Delta = {m^2} – 24$, $f(1) = m + 5$, $f( – 1) = – m + 5.$

Dấu $Δ$:

<img link="data_for_rag/toan11/images/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit-2.png" alt="tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit-2">

$(1) \Leftrightarrow – 2\sqrt 6 < m < 2\sqrt 6$ $(3).$

$$
\left( 2 \right) \Leftrightarrow \left\{ \begin{array}{l}
m \le – 2\sqrt 6 \:{\rm{hoặc}}\:m \ge 2\sqrt 6 \\
\left\{ {\begin{array}{l}
{f(1) > 0}\\
{\frac{s}{2} – 1 > 0}
\end{array}} \right.\:{\rm{hoặc}}\:\left\{ {\begin{array}{l}
{f( – 1) > 0}\\
{\frac{s}{2} + 1 < 0}
\end{array}} \right.
\end{array} \right.
$$

$$
\left\{ {\begin{array}{l}
{f(1) > 0}\\
{\frac{s}{2} – 1 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m + 5 > 0}\\
{ – \frac{m}{4} – 1 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow – 5 < m < – 4.$

$$
\left\{ {\begin{array}{l}
{f( – 1) > 0}\\
{\frac{s}{2} + 1 < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{ – m + 5 > 0}\\
{ – \frac{m}{4} + 1 < 0}
\end{array}} \right.
$$
 $\Leftrightarrow 4 < m < 5.$

Suy ra 
$$
(2) \Leftrightarrow \left[ {\begin{array}{l}
{ – 5 < m \le – 2\sqrt 6 }\\
{2\sqrt 6 \le m < 5}
\end{array}} \right.
$$

Hợp các tập nghiệm ở $(3)$ và $(4)$ ta có $– 5 < m < 5.$

Vậy $D = ( – 5;5).$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 12: Tìm tập xác định của hàm số: $y = \sqrt {{{\log }_3}\left( {\frac{{1 + \log _a^2x}}{{1 + {{\log }_a}x}}} \right)} .$

Hàm số xác định khi:

${\log _3}\left( {\frac{{1 + \log _a^2x}}{{1 + {{\log }_a}x}}} \right) \ge 0$ $\Leftrightarrow \frac{{1 + \log _a^2x}}{{1 + {{\log }_a}x}} \ge 1$ $\Leftrightarrow \frac{{\log _a^2x – {{\log }_a}x}}{{1 + {{\log }_a}x}} \ge 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{{\log }_a}x \ge 1}\\
{ – 1 < {{\log }_a}x \le 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
\left\{ \begin{array}{l}
x \ge a\\
\frac{1}{a} < x \le 1
\end{array} \right.\:{\rm{nếu}}\:a > 1\\
\left\{ \begin{array}{l}
0 < x \le a\\
1 \le x < \frac{1}{a}
\end{array} \right.\:{\rm{nếu}}\:0 < a < 1
\end{array} \right.
$$

Vậy:

+ Với $a>1$: $D = \left( {\frac{1}{a},1} \right] \cup [a, + \infty ).$

+ Với $0<a<1$: $D = \left( {0,{\rm{ }}a} \right] \cup \left[ {1,\frac{1}{a}} \right).$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 13: Tìm các giá trị của m để hàm số $y = \frac{1}{{\sqrt {{{\log }_3}\left( {{x^2} – 2x + 3m} \right)} }}$ xác định $\forall x \in R.$

Hàm số xác định $\forall x \in R$ khi ${\log _3}\left( {{x^2} – 2x + 3m} \right) > 0$ $\Leftrightarrow {x^2} – 2x + 3m > 1$ $\Leftrightarrow \quad {x^2} – 2x + 3m – 1 > 0$ $\forall x \in R.$

Vì $a = 1 > 0$ nên $\Delta ‘ < 0$ $\Leftrightarrow 1 – (3m – 1) < 0$ $\Leftrightarrow m > \frac{2}{3}.$

Với $m > \frac{2}{3}$, hàm số đã cho xác định $\forall x \in R.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/10/tim-tap-xac-dinh-cua-ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 14: Cho hàm số $y = \frac{{\sqrt {mx – m + 1} }}{{\log \left[ {(m – 1)x – m + 3} \right]}}.$

a) Tìm tập xác định của hàm số khi $m = 2.$

b) Tìm các giá trị của $m$ sao cho hàm số xác định $\forall x \ge 1.$

a) Với $m = 2$ ta có $y = \frac{{\sqrt {2x – 1} }}{{\log (x + 1)}}$ xác định khi 
$$
\left\{ {\begin{array}{l}
{x \ge \frac{1}{2}}\\
{x + 1 > 0}\\
{x + 1 \ne 1}
\end{array}} \right.
$$
 $\Leftrightarrow x \ge \frac{1}{2}.$

Vậy $D = \left[ {\frac{1}{2}, + \infty } \right).$

b) Hàm số xác định với mọi $x \ge 1$ khi và chỉ khi 
$$
\left\{ {\begin{array}{l}
{ mx – m + 1 \ge 0\:(1)}\\
{(m – 1)x – m + 3 > 0\:(2)}\\
{(m – 1)x – m + 3 \ne 1\:(3)}
\end{array}} \right.
$$
 $\forall x \ge 1.$

Giải bất phương trình, ta có:

$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{m = 0}\\
{x \in R}
\end{array}} \right.}\\
{m > 0}\\
{x \ge \frac{{m – 1}}{m} = 1 – \frac{1}{m}}
\end{array}} \right.
$$

$(1)$ có tập nghiệm là:

+ Nếu $m = 0$ thì ${s_1} = R.$

+ Nếu $m > 0$ thì ${s_1} = \left[ {\frac{{m – 1}}{m}, + \infty } \right).$

Nếu $m = 1$ thì $(2)$ và $(3)$ đều thỏa mãn điều kiện.

Nếu $m < 1$ thì $(2)$ không thỏa $\forall x \ge 1.$

Nếu $m > 1$ thì $(2) \Leftrightarrow x > \frac{{m – 3}}{{m – 1}}.$

Vì $\frac{{m – 3}}{{m – 1}} < 1$, $\forall m > 1$ nên $(2)$ thỏa $\forall x \ge 1.$

Với $m > 1$ thì $(3) \Leftrightarrow x \ne \frac{{m – 2}}{{m – 1}}$ thỏa $\forall x \ge 1.$

Đáp số: $m \ge 1.$