# Chứng minh tính chất của cấp số cộng, cấp số nhân

<!-- chunk:0 level:0 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
Bài viết hướng dẫn phương pháp giải bài toán chứng minh tính chất của cấp số cộng, cấp số nhân trong chương trình Đại số và Giải tích 11.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## I. PHƯƠNG PHÁP

Sử dụng công thức tổng quát của cấp số, chuyển các đại lượng qua số hạng đầu và công sai, công bội.

Sử dụng tính chất của cấp số:

+ $a$, $b$, $c$ theo thứ tự đó lập thành CSC $\Leftrightarrow a + c = 2b.$

+ $a$, $b$, $c$ theo thứ tự đó lập thành CSN $\Leftrightarrow ac = {b^2}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## Ví dụ 1. Chứng minh rằng các số:

1. $1$, $\sqrt 3$, $3$ không thể cùng thuộc một cấp số cộng.

2. $2$, $3$, $5$ không thể cùng thuộc một cấp số nhân.

Lời giải:

1. Giả sử $1$, $\sqrt 3$, $3$ là số hạng thứ $m$, $n$, $p$ của một CSC $\left( {{u_n}} \right).$ Ta có:

$\sqrt 3 = \frac{{3 – \sqrt 3 }}{{\sqrt 3 – 1}}$ $= \frac{{{u_p} – {u_n}}}{{{u_n} – {u_m}}}$ $= \frac{{{u_1}(p – n)}}{{{u_1}(n – m)}}$ $= \frac{{p – n}}{{n – m}}$ vô lí vì $\sqrt 3$ là số vô tỉ, còn $\frac{{p – n}}{{n – m}}$ là số hữu tỉ.

2. Giả sử $2$, $3$, $5$ là ba số hạng thứ $m$, $n$, $p$ của CSN $\left( {{v_n}} \right)$ có công bội $q.$

Ta có: $\frac{2}{3} = \frac{{{u_m}}}{{{u_n}}} = {q^{m – n}}$; $\frac{5}{3} = {q^{p – n}}$, suy ra ${\left( {\frac{2}{3}} \right)^{p – n}} = {\left( {\frac{5}{3}} \right)^{m – n}}$ $= {p^{(p – n)(m – n)}}.$

$\Rightarrow {2^{p – n}}{.3^{m – p}}{.5^{n – m}} = 1$ vô lí.

<!-- chunk:3 level:3 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## Ví dụ 2. Chứng minh rằng dãy số $\left( {{u_n}} \right)$ là:

1. Cấp số cộng khi và chỉ khi ${u_n} = an + b.$

2. Cấp số nhân khi và chỉ khi ${u_n} = a.{q^n}.$

Lời giải:

1. Giả sử $\left( {{u_n}} \right)$ là một cấp số cộng công sai $d$, khi đó:

${u_n} = {u_1} + (n – 1)d$ $= dn + {u_1} – d = an + b.$

Giả sử: ${u_n} = an + b$ $\Rightarrow {u_{n + 1}} – {u_n} = a$ $\Rightarrow {u_{n + 1}} = {u_n} + a$, $\forall n.$

Suy ra $\left( {{u_n}} \right)$ là một cấp số cộng với công sai $a.$

2. Giả sử $\left( {{u_n}} \right)$ là cấp số nhân với công bội $q$, khi đó: ${u_n} = {u_1}.{q^n}.$

Giả sử ${u_n} = a.{q^n}$, suy ra $\frac{{{u_{n + 1}}}}{{{u_n}}} = q$ $\Rightarrow {u_{n + 1}} = q.{u_n}$, $\forall n.$

Suy ra dãy $\left( {{u_n}} \right)$ là cấp số nhân với công bội $q.$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## Ví dụ 3. Chứng minh rằng:

1. Nếu phương trình ${x^3} – a{x^2} + bx – c = 0$ có ba nghiệm lập thành cấp số cộng thì $9ab = 2{a^3} + 27c.$

2. Nếu phương trình ${x^3} – a{x^2} + bx – c = 0$ có ba nghiệm lập thành cấp số nhân thì $c\left( {c{a^3} – {b^3}} \right) = 0.$

Lời giải:

1. Giả sử phương trình có ba nghiệm ${x_1}$, ${x_2}$, ${x_3}$ lập thành cấp số cộng.

Suy ra: ${x_1} + {x_3} = 2{x_2}$ $(1).$

Mặt khác: ${x^3} – a{x^2} + bx – c$ $= \left( {x – {x_1}} \right)\left( {x – {x_2}} \right)\left( {x – {x_3}} \right).$

$= {x^3} – \left( {{x_1} + {x_2} + {x_3}} \right){x^2}$ $+ \left( {{x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1}} \right)x$ $– {x_1}{x_2}{x_3}.$

Suy ra ${x_1} + {x_2} + {x_3} = a$ $(2).$

Từ $(1)$ và $(2)$, ta suy ra $3{x_2} = a$ hay ${x_2} = \frac{a}{3}.$

Dẫn tới phương trình đã cho có nghiệm ${x_2} = \frac{a}{3}$, tức là:

${\left( {\frac{a}{3}} \right)^3} – a{\left( {\frac{a}{3}} \right)^2} + b\left( {\frac{a}{3}} \right) – c = 0$ $\Leftrightarrow – \frac{{2{a^3}}}{{27}} + \frac{{ba}}{3} – c = 0$ $\Leftrightarrow 9ab = 2{a^3} + 27c.$

Ta có điều phải chứng minh.

2. Giả sử ba nghiệm ${x_1}$, ${x_2}$, ${x_3}$ lập thành CSN, suy ra ${x_1}{x_3} = x_2^2.$

Theo phân tích bài trên, ta có: ${x_1}{x_2}{x_3} = c$ $\Rightarrow x_2^3 = c$ $\Rightarrow {x_2} = \sqrt[3]{c}.$

Hay phương trình đã cho có nghiệm ${x_2} = \sqrt[3]{c}$, tức là:

${(\sqrt[3]{c})^3} – a{(\sqrt[3]{c})^2} + b\sqrt[3]{c} – c = 0$ $\Leftrightarrow b\sqrt[3]{c} = a\sqrt[3]{{{c^2}}}$ $\Leftrightarrow c\left( {c{a^3} – {b^3}} \right) = 0.$

Bài toán được chứng minh.

<!-- chunk:5 level:3 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## Ví dụ 4. Chứng minh rằng với mọi cách chia tập $x = \{ 1,2,3, \ldots ,9\}$ thành hai tập con rời nhau luôn có một tập chứa ba số lập thành cấp số cộng.

Lời giải:

Ta chứng minh bài toán bằng phương pháp phản chứng.

Giả sử $X$ được chia thành hai tập con $A$ và $B$ đồng thời trong $A$ và $B$ không có ba số nào lập thành cấp số cộng.

Xét ba cấp số cộng $(1;3;5)$, $(3;4;5)$, $(3;5;7).$

Ta thấy số $3$, $5$ không thể cùng nằm trong một tập hợp, vì nếu hai số này thuộc $A$ thì $1$, $4$, $7$ phải thuộc $B$, tuy nhiên các số $1$, $4$, $7$ lại lập thành cấp số cộng.

Tương tự bằng cách xét CSC $(3;5;7)$, $(5;6;7)$, $(5;7;9)$ thì ta có hai số $5$, $7$ không thể cùng nằm trong một tập.

Vì cặp $(3;5)$ và $(5;7)$ không cùng thuộc một tập nên ta suy ra $(3;7)$ thuộc $A$, $5$ thuộc $B.$ Khi đó ta xét các trường hợp sau:

+ $4 \in A$, vì $3,4 \in A$ $\Rightarrow 2 \notin A$ $\Rightarrow 2 \in B$, do $1$, $4$, $7$ lập thành cấp số cộng nên $1 \in B$; $2$, $5$, $8$ lập thành cấp số cộng nên $8 \in A$ $\Rightarrow 9 \in B.$

Do đó $1,5,9 \in B$ lập thành cấp số cộng, vô lí.

+ $4 \in B$, do $4,5 \in B$ $\Rightarrow 6 \in A$ mà $6,7 \in A$ $\Rightarrow 8 \in B.$

$5,8 \in B$ $\Rightarrow 2 \in A$, vì $2,3 \in A$ $\Rightarrow 1 \in B$, vì $1,5 \in B$ $\Rightarrow 9 \in A.$

Do đó: $3,6,9 \in B$ vô lí. Vậy bài toán được chứng minh.

<!-- chunk:6 level:3 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## Ví dụ 5. Dãy số $({x_n})$ thỏa mãn điều kiện: $\left| {{x_{n + m}} – {x_m} – {x_n}} \right| < \frac{1}{{m + n}}$, $\forall m,n \in {N^*}.$ Chứng minh rằng: $({x_n})$ là một cấp số cộng.

Lời giải:

Đặt ${a_n} = {x_n} – n{x_1}$, khi đó ta có ${a_1} = 0$ và $|{a_{m + n}} – {a_m} – {a_n}| < \frac{1}{{m + n}}$, $\forall m,n \in N.$

Ở đây ta sẽ chứng minh ${a_n} = 0$, $\forall n \in N.$

Thật vậy, ta có:

$\left| {{a_{n + 1}} – {a_n}} \right| < \frac{1}{{n + 1}}$, $\forall n \in N$ nên $\lim \left| {{a_{n + 1}} – {a_n}} \right| = 0$ hay $\lim \left| {{a_{n + k}} – {a_n}} \right| = 0$, $\forall k \in N.$

Mà $\left| {{a_{n + k}} – {a_n} – {a_k}} \right| < \frac{1}{{n + k}}$ nên $\mathop {\lim }\limits_n \left| {{a_{n + k}} – {a_n} – {a_k}} \right| = 0.$

Từ đây suy ra ${a_k} = 0$, $\forall k \in N.$ Vậy ta có điều phải chứng minh.

<!-- chunk:7 level:1 source:https://toanmath.com/2020/05/chung-minh-tinh-chat-cua-cap-so-cong-cap-so-nhan.html -->
## III. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1.

## Bài tập 1. Cho ba số $a$, $b$, $c$ lập thành cấp số cộng. Chứng minh rằng: ${a^2} + 2bc = {c^2} + 2ab.$

## Bài tập 2. Cho $a,b,c > 0$ lập thành cấp số cộng. Chứng minh rằng:

$\frac{1}{{\sqrt a + \sqrt b }} + \frac{1}{{\sqrt b + \sqrt c }} = \frac{2}{{\sqrt c + \sqrt a }}.$

## Bài tập 3. Cho $\left( {{u_n}} \right)$ là cấp số cộng. Chứng minh rằng: ${u_n} = \frac{1}{2}\left( {{u_{n – k}} + {u_{n + k}}} \right)$, $1 \le k \le n – 1.$

Lời giải:

## Bài tập 1. Vì $a$, $b$, $c$ lập thành cấp số cộng nên $a + c = 2b.$

Do đó: ${a^2} + 2bc – {c^2} – 2ab$ $= (a – c)(a + c) – 2b(a – c).$

$= (a – c)(a + c – 2b) = 0.$

Suy ra ${a^2} + 2bc = {c^2} + 2ab.$

## Bài tập 2. Gọi $d$ là công sai của cấp số, suy ra $b – a = c – b = d$, $c – a = 2d.$

Do đó:  $\frac{1}{{\sqrt a + \sqrt b }} + \frac{1}{{\sqrt b + \sqrt c }}$ $= \frac{{\sqrt b – \sqrt a }}{d} + \frac{{\sqrt c – \sqrt b }}{d}$ $= \frac{{\sqrt c – \sqrt a }}{d}.$

$= \frac{{c – a}}{{d(\sqrt c + \sqrt a )}}$ $= \frac{2}{{\sqrt c + \sqrt a }}.$

## Bài tập 3. Gọi $d$ là công sai của cấp số. Ta có:

$$
\left\{ {\begin{array}{l}
{{u_{n – k}} = {u_1} + (n – k – 1)d}\\
{{u_{n + k}} = {u_1} + (n + k – 1)d}
\end{array}} \right..
$$

$\Rightarrow {u_{n – k}} + {u_{n + k}}$ $= 2{u_1} + (2n – 2)d = 2{u_n}$ $\Rightarrow {u_n} = \frac{{{u_{n – k}} + {u_{n + k}}}}{2}.$

## Bài 2.

## Bài tập 1. Cho tam giác $ABC.$ Chứng minh rằng $\tan \frac{A}{2}$; $\tan \frac{B}{2}$; $\tan \frac{C}{2}$ lập thành cấp số cộng $\Leftrightarrow \cos A$; $\cos B$; $\cos C$ lập thành cấp số cộng.

## Bài tập 2. Cho tam giác $ABC.$ Chứng minh rằng $\cot \frac{A}{2}$; $\cot \frac{B}{2}$; $\cot \frac{C}{2}$ lập thành cấp số cộng $\Leftrightarrow \sin A$; $\sin B$; $\sin C$ lập thành cấp số cộng.

Lời giải:

1. Ta có: $\tan \frac{A}{2}$; $\tan \frac{B}{2}$; $\tan \frac{C}{2}$ lập thành cấp số cộng.

$\Leftrightarrow \tan \frac{A}{2} + \tan \frac{C}{2} = 2\tan \frac{B}{2}$ $\Leftrightarrow \frac{{\sin \left( {\frac{A}{2} + \frac{C}{2}} \right)}}{{\cos \frac{A}{2}\cos \frac{C}{2}}} = 2\frac{{\sin \frac{B}{2}}}{{\cos \frac{B}{2}}}.$

$\Leftrightarrow {\cos ^2}\frac{B}{2}$ $= \sin \frac{B}{2}\left[ {\cos \left( {\frac{A}{2} + \frac{C}{2}} \right) + \cos \left( {\frac{A}{2} – \frac{C}{2}} \right)} \right].$

$\Leftrightarrow \frac{{1 + \cos B}}{2}$ $= \frac{{1 – \cos B}}{2} + \frac{1}{2}[\cos A + \cos C].$

$\Leftrightarrow \cos B = \frac{{\cos A + \cos C}}{2}$ $\Leftrightarrow \cos A$, $\cos B$, $\cos C$ lập thành cấp số cộng.

2. Ta có: $\cot \frac{A}{2} – \cot \frac{B}{2} = \cot \frac{B}{2} – \cot \frac{C}{2}.$

$\Leftrightarrow \frac{{\cos \frac{A}{2}\sin \frac{B}{2} – \cos \frac{B}{2}\sin \frac{A}{2}}}{{\sin \frac{A}{2}\sin \frac{B}{2}}}$ $= \frac{{\cos \frac{B}{2}\sin \frac{C}{2} – \cos \frac{C}{2}\sin \frac{B}{2}}}{{\sin \frac{C}{2}\sin \frac{B}{2}}}.$

$\Leftrightarrow \sin \frac{{B – A}}{2}\cos \frac{{B + A}}{2}$ $= \sin \frac{{C – B}}{2}\cos \frac{{C + B}}{2}.$

$\Leftrightarrow \sin B – \sin A = \sin C – \sin B$ $\Leftrightarrow \sin A + \sin C = 2\sin B.$

## Bài 3. Cho $a,b,c$ lập thành cấp số nhân. Chứng minh rằng:

## Bài tập 1. $(a + b + c)(a – b + c)$ $= {a^2} + {b^2} + {c^2}.$

## Bài tập 2. $\left( {{a^2} + {b^2}} \right)\left( {{b^2} + {c^2}} \right)$ $= {(ab + bc)^2}.$

## Bài tập 3. $\left( {{a^n} + {b^n} + {c^n}} \right)\left( {{a^n} – {b^n} + {c^n}} \right)$ $= {a^{2n}} + {b^{2n}} + {c^{2n}}$, $n \in {N^*}.$

Lời giải:

Vì $a,b,c$ lập thành cấp số nhân nên ta có ${b^2} = ac.$

1. Ta có: $(a + b + c)(a – b + c)$ $= {(a + c)^2} – {b^2}$ $= {a^2} + 2ac + {c^2} – {b^2}.$

2. Ta có: $\left( {{a^2} + {b^2}} \right)\left( {{b^2} + {c^2}} \right)$ $= \left( {{a^2} + ac} \right)\left( {ac + {c^2}} \right)$ $= ac{(a + c)^2}.$

$= {b^2}{(a + c)^2}$ $= {(ab + bc)^2}.$

3. Ta có: $VT = {\left( {{a^n} + {c^n}} \right)^2} – {b^{2n}}$ $= {a^{2n}} + {c^{2n}} + {b^{2n}} + 2\left( {{a^n}{c^n} – {b^{2n}}} \right)$ $= {a^{2n}} + {b^{2n}} + {c^{2n}}.$

## Bài 4. Cho $\left( {{u_n}} \right)$ là cấp số nhân. Chứng minh rằng:

## Bài tập 1. ${a_1}{a_n} = {a_k}.{a_{n – k + 1}}$, $k = \overline {1;n} .$

## Bài tập 2. ${S_n}\left( {{S_{3n}} – {S_{2n}}} \right)$ $= {\left( {{S_{2n}} – {S_n}} \right)^2}.$

Lời giải:

Gọi $q$ là công bội của cấp số.

1. Ta có: ${a_1}{a_n} = {a_1}.{a_1}{q^{n – 1}} = a_1^2{q^{n – 1}}$; ${a_k}{a_{n – k + 1}} = {a_1}{q^{k – 1}}{a_1}{q^{n – k}} = a_1^2{q^{n – 1}}.$

Suy ra: ${a_1}{a_n} = {a_k}.{a_{n – k + 1}}.$

2. Ta có: ${S_n}\left( {{S_{3n}} – {S_{2n}}} \right)$ $= {u_1}\frac{{{q^n} – 1}}{{q – 1}}.{u_1}\left( {\frac{{{q^{3n}} – 1}}{{q – 1}} – \frac{{{q^{2n}} – 1}}{{q – 1}}} \right)$ $= u_1^2\frac{{{q^{2n}}{{\left( {{q^n} – 1} \right)}^2}}}{{{{(q – 1)}^2}}}.$

${\left( {{S_{2n}} – {S_n}} \right)^2}$ $= {\left( {{u_1}\frac{{{q^{2n}} – 1}}{{q – 1}} – {u_1}\frac{{{q^n} – 1}}{{q – 1}}} \right)^2}$ $= u_1^2\frac{{{q^{2n}}{{\left( {{q^n} – 1} \right)}^2}}}{{{{(q – 1)}^2}}}.$

Suy ra ${S_n}\left( {{S_{3n}} – {S_{2n}}} \right) = {\left( {{S_{2n}} – {S_n}} \right)^2}.$

## Bài 5.

## Bài tập 1. Điều cần và đủ để ba số khác không $a,b,c$ là ba số hạng của một cấp số nhân là tồn tại ba số nguyên khác không $p,t,r$ sao cho:
$$
\left\{ {\begin{array}{l}
{p + t + r = 0}\\
{{a^p}.{b^t}.{c^r} = 1}
\end{array}} \right..
$$

## Bài tập 2. Cho bốn số thực ${a_1}$; ${a_2}$; ${a_3}$; ${a_4}.$ Biết rằng:
$$
\left\{ {\begin{array}{l}
{\frac{1}{{{a_1}{a_2}}} + \frac{1}{{{a_2}{a_3}}} = \frac{2}{{{a_1}{a_3}}}}\\
{\frac{1}{{{a_1}{a_2}}} + \frac{1}{{{a_2}{a_3}}} + \frac{1}{{{a_3}{a_4}}} = \frac{3}{{{a_1}{a_4}}}}
\end{array}} \right..
$$
 Chứng minh rằng: ${a_1};{a_2};{a_3};{a_4}$ lập thành cấp số cộng.

## Bài tập 3. Chứng minh rằng điều kiện cần và đủ để ba số $a,b,c$ là ba số hạng của một cấp số cộng là tồn tại ba số nguyên khác không $p,q,r$ thỏa mãn:
$$
\left\{ {\begin{array}{l}
{pa + qb + rc = 0}\\
{p + q + r = 0}
\end{array}} \right..
$$

## Bài tập 4. Chứng minh rằng nếu ba cạnh của tam giác lập thành cấp số nhân thì công bội của cấp số nhân đó nằm trong khoảng $\left( {\frac{{\sqrt 5 – 1}}{2};\frac{{1 + \sqrt 5 }}{2}} \right).$

Lời giải:

## Bài tập 1. Giả sử $a,b,c$ là ba số hạng thứ $k + 1$; $l + 1$; $m + 1$ của cấp số nhân có công bội $q$, khi đó ta có:

$a = {u_1}.{q^k}$; $b = {u_1}.{q^l}$; $c = {u_1}.{q^m}$ $\Rightarrow \frac{a}{b} = {q^{k – l}}$; $\frac{b}{c} = {q^{l – m}}$ $\Rightarrow {\left( {\frac{a}{b}} \right)^{l – m}} = {\left( {\frac{b}{c}} \right)^{k – l}}.$

$\Rightarrow {a^{l – m}}.{b^{m – l – k + l}}.{c^{k – l}} = 1.$

Đặt $p = l – m$; $t = m – l – k + l$; $r = k – l.$

Khi đó ta có ba số $p$, $t$, $r$ thỏa mãn yêu cầu bài toán.

Giả sử ta có 
$$
\left\{ {\begin{array}{l}
{p + t + r = 0}\\
{{a^p}.{b^t}.{c^r} = 1}
\end{array}} \right.
$$
 suy ra ${a^p}.{c^r} = {b^{p + r}}$ $\Rightarrow {\left( {\frac{a}{b}} \right)^p} = {\left( {\frac{b}{c}} \right)^r}$ $(*).$

Do $p+t+r=0$ nên tồn tại ít nhất một số dương và một số âm.

Giả sử $r > 0$, $t < 0.$ Đặt $\frac{b}{a} = {q^r}$ $\Rightarrow b = a.{q^r}$ kết hợp với $(*)$ ta có:

${\left( {\frac{a}{{a.{q^r}}}} \right)^p} = {\left( {\frac{{a.{q^r}}}{c}} \right)^r}$ $\Rightarrow c = a.{q^{r + p}}.$

Vậy ba số $a$, $b$, $c$ là ba số hạng của cấp số nhân với $a$ là số hạng đầu, $b$ là số hạng thứ $r+1$ và $c$ là số hạng thứ $r+p+1.$

2. Ta có: $\frac{1}{{{a_1}{a_2}}} + \frac{1}{{{a_2}{a_3}}} = \frac{2}{{{a_1}{a_3}}}$ $\Leftrightarrow {a_3} + {a_1} = 2{a_2}$ $\Rightarrow {a_1} – {a_2} = {a_2} – {a_3} = d.$

$\frac{1}{{{a_1}{a_2}}} + \frac{1}{{{a_2}{a_3}}} + \frac{1}{{{a_3}{a_4}}} = \frac{3}{{{a_1}{a_4}}}$ $\Leftrightarrow \frac{2}{{{a_1}{a_3}}} + \frac{1}{{{a_3}{a_4}}} = \frac{3}{{{a_1}{a_4}}}.$

$\Leftrightarrow 2{a_4} + {a_1} = 3{a_3}$ $\Leftrightarrow 2{a_4} = 3\left( {{a_1} + 2d} \right) – {a_1}$ $\Rightarrow {a_4} = {a_1} + 3d.$

## Bài tập 3. Giả sử $a$, $b$, $c$ là ba số hạng thứ $m +1$, $n +1$, $k+1$ của một cấp số cộng $\left( {{u_n}} \right).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{a = {u_1} + md}\\
{b = {u_1} + nd}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{d = \frac{{a – b}}{{m – n}}}\\
{{u_1} = a – \frac{{m(a – b)}}{{m – n}} = \frac{{mb – an}}{{m – n}}}
\end{array}} \right..
$$

Mặt khác: $c = {u_1} + kd$ $\Rightarrow (m – n)c = mb – na + k(a – b).$

$\Rightarrow (k – n)a + (m – k)b + (n – m)c = 0.$

Đặt $p = k – n$, $q = m – k$, $r = n – m$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{pa + qb + rc = 0}\\
{p + q + r = 0}
\end{array}} \right..
$$

Giả sử tồn tại ba số nguyên khác không $p$, $q$, $r$ sao cho: 
$$
\left\{ {\begin{array}{l}
{pa + qb + rc = 0}\\
{p + q + r = 0}
\end{array}} \right..
$$

Không mất tính tổng quát ta giả sử $a \ge b \ge c$ và $p,q,r > 0.$

Ta có: $p = – q – r$ nên $( – q – r)a + qb + rc = 0$ $\Leftrightarrow (a – b)p = (c – a)r.$

Đặt $d = \frac{{a – b}}{r}$ $\Rightarrow a = b + rd$, $c = a + pd = b + (p + r)d.$

Vậy $b$, $a$, $c$ là ba số hạng của một cấp số cộng.

## Bài tập 4. Giả sử $a$, $b$, $c$ là ba cạnh tam giác theo thứ tự đó lập thành CSN với công bội $q.$

Ta có: 
$$
\left\{ {\begin{array}{l}
{a + aq > a{q^2}}\\
{a{q^2} + aq > a}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{q^2} – q – 1 < 0}\\
{{q^2} + q – 1 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{q \in \left( {\frac{{1 – \sqrt 5 }}{2};\frac{{1 + \sqrt 5 }}{2}} \right)}\\
{q \in \left( { – \infty ;\frac{{ – 1 – \sqrt 5 }}{2}} \right) \cup \left( {\frac{{ – 1 + \sqrt 5 }}{2}; + \infty } \right)}
\end{array}} \right..
$$

$\Leftrightarrow q \in \left( {\frac{{\sqrt 5 – 1}}{2};\frac{{\sqrt 5 + 1}}{2}} \right).$

## Bài 6. Cho hai số tự nhiên $n$, $k$ thỏa mãn: $k + 3 \le n.$

## Bài tập 1. Chứng minh rằng tồn tại không quá hai giá trị của $k$ sao cho $C_n^k$, $C_n^{k + 1}$ và $C_n^{k + 2}$ là ba số hạng liên tiếp của một cấp số cộng.

## Bài tập 2. Chứng minh rằng không tồn tại $k$ để $C_n^k$, $C_n^{k + 1}$, $C_n^{k + 2}$ và $C_n^{k + 3}$ là bốn số hạng liên tiếp của một cấp số cộng.

Lời giải:

1. Ta có: $C_n^k + C_n^{k + 2} = 2C_n^{k + 1}$ $\Leftrightarrow \frac{{n!}}{{k!(n – k)!}} + \frac{{n!}}{{(k + 2)!(n – k – 2)!}}$ $= 2\frac{{n!}}{{(k + 1)!(n – k – 1)!}}.$

$\Leftrightarrow (k + 1)(k + 2) + (n – k)(n – k – 1)$ $= 2(k + 2)(n – k).$

Đây là phương trình bậc hai ẩn $k$ nên có nhiều nhất hai nghiệm.

## Bài tập 2. Giả sử tồn tại $k$ để $C_n^k$, $C_n^{k + 1}$, $C_n^{k + 2}$ và $C_n^{k + 3}$ là bốn số hạng liên tiếp của một cấp số cộng.

Do $C_n^k = C_n^{n – k}$ nên suy ra: $C_n^{n – k}$, $C_n^{n – k – 1}$, $C_n^{n – k – 2}$, $C_n^{n – k – 3}$ cũng tạo thành bốn số hạng liên tiếp của một cấp số cộng.

Vậy ta có các bộ sau là ba số hạng liên tiếp của một cấp số cộng:

$C_n^k$, $C_n^{k + 1}$, $C_n^{k + 2}.$

$C_n^k$, $C_n^{k + 1}$, $C_n^{k + 2}$, $C_n^{k + 3}.$

$C_n^{n – k – 3}$, $C_n^{n – k – 2}$, $C_n^{n – k – 1}.$

$C_n^{n – k – 2}$, $C_n^{n – k – 1}$, $C_n^{n – k}.$

Ta chứng minh tập $\{ k,k + 1,n – k – 3,n – k – 2\}$ chứa không quá hai số khác nhau. Thật vậy, giả sử $k$, $k + 1$, $n – k – 3$ là ba số khác nhau. Khi đó, tồn tại ba cấp số cộng:

$C_n^k$, $C_n^{k + 1}$, $C_n^{k + 2}.$

$C_n^{k + 1}$, $C_n^{k + 2}$, $C_n^{k + 3}.$

$C_n^{n – k – 3}$, $C_n^{n – k – 2}$, $C_n^{n – k – 1}.$

Điều này trái với kết quả câu 1.

Do $k$, $k+1$ và $n-k – 3$, $n-k – 2$ là các số tự nhiên liên tiếp nên ta có:

$$
\left\{ {\begin{array}{l}
{k = n – k – 3}\\
{k + 1 = n – k – 2}
\end{array}} \right.
$$
 $\Rightarrow C_n^{k + 1} = C_n^{n – k – 2} = C_n^{k + 2}.$ Suy ra $C_n^k = C_n^{k + 1} = C_n^{k + 2}$ $(1).$

Xét phương trình: $C_n^k = C_n^{k + 1}$ $(2)$ $\Leftrightarrow \frac{{n!}}{{k!(n – k)!}} = \frac{{n!}}{{(k + 1)!(n – k – 1)!}}.$

$\Leftrightarrow k + 1 = n – k$ $\Rightarrow k = \frac{{n – 1}}{2}.$

Suy ra phương trình $(2)$ có không quá một nghiệm $k$, điều này dẫn tới $(1)$ mâu thuẫn.

Vậy không tồn tại $k$ để $C_n^k$, $C_n^{k + 1}$, $C_n^{k + 2}$ và $C_n^{k + 3}$ là bốn số hạng liên tiếp của một cấp số cộng.