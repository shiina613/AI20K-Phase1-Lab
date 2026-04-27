# Tìm giới hạn của dãy số dựa vào các định lý và các giới hạn cơ bản

<!-- chunk:0 level:0 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
Bài viết hướng dẫn phương pháp tìm giới hạn của dãy số dựa vào các định lý và các giới hạn cơ bản, giúp học sinh học tốt chương trình Đại số và Giải tích 11.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
## I. PHƯƠNG PHÁP

Sử dụng các định lí về giới hạn, biến đổi đưa về các giới hạn cơ bản.

+ Khi tìm $\lim \frac{{f(n)}}{{g(n)}}$ ta thường chia cả tử và mẫu cho ${n^k}$, trong đó $k$ là bậc lớn nhất của tử và mẫu.

+ Khi tìm $\lim \left[ {\sqrt[k]{{f(n)}} – \sqrt[m]{{g(n)}}} \right]$ trong đó $\lim f(n) = \lim g(n) = + \infty$ ta thường tách và sử dụng phương pháp nhân lượng liên hợp.

<!-- chunk:2 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
## Ví dụ 1. Tìm các giới hạn sau:

1. $A = \lim \frac{{n\sqrt {1 + 3 + 5 + \ldots + (2n – 1)} }}{{2{n^2} + 1}}.$

2. $B = \lim \frac{{\sqrt {1 + 2 + \ldots + n} – n}}{{\sqrt[3]{{{1^2} + {2^2} + \ldots + {n^2}}} + 2n}}.$

Lời giải:

1. Ta có: $1 + 3 + 5 + \ldots + 2n – 1 = {n^2}.$

Suy ra $A = \lim \frac{{{n^2}}}{{2{n^2} + 1}}$ $= \lim \frac{1}{{2 + \frac{1}{{{n^2}}}}} = \frac{1}{2}.$

2. Ta có: $1 + 2 + \ldots + n = \frac{{n(n + 1)}}{2}.$

${1^2} + {2^2} + \ldots + {n^2} = \frac{{n(n + 1)(2n + 1)}}{6}.$

Suy ra: $B = \lim \frac{{\sqrt {\frac{{n(n + 1)}}{2}} – n}}{{\sqrt[3]{{\frac{{n(n + 1)(2n + 1)}}{6}}} + 2n}}$ $= \lim \frac{{\sqrt {\frac{{{n^2}\left( {1 + \frac{1}{n}} \right)}}{2}} – n}}{{\sqrt[3]{{\frac{{{n^3}\left( {1 + \frac{1}{n}} \right)\left( {2 + \frac{1}{n}} \right)}}{6}}} + 2n}}$ $= \frac{{\sqrt {\frac{1}{2}} – 1}}{{\sqrt[3]{{\frac{1}{3}}} + 2}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
## Ví dụ 2. Tìm các giới hạn sau:

1. $C = \lim \left[ {\left( {1 – \frac{1}{{{2^2}}}} \right)\left( {1 – \frac{1}{{{3^2}}}} \right) \ldots \left( {1 – \frac{1}{{{n^2}}}} \right)} \right].$

2. $D = \lim \left[ {\frac{1}{{1.2}} + \frac{1}{{2.3}} + \frac{1}{{3.4}} + \ldots + \frac{1}{{n(n + 1)}}} \right].$

Lời giải:

1. Ta có: $1 – \frac{1}{{{k^2}}}$ $= \frac{{(k – 1)(k + 1)}}{{{k^2}}}$ nên suy ra:

$\left( {1 – \frac{1}{{{2^2}}}} \right)\left( {1 – \frac{1}{{{3^2}}}} \right) \ldots \left( {1 – \frac{1}{{{n^2}}}} \right)$ $= \frac{{1.3}}{{{2^2}}}.\frac{{2.4}}{{{3^2}}} \ldots \frac{{(n – 1)(n + 1)}}{{{n^2}}}$ $= \frac{{n + 1}}{{2n}}.$

Do vậy $C = \lim \frac{{n + 1}}{{2n}} = \frac{1}{2}.$

2. Ta có: $\frac{1}{{k(k + 1)}} = \frac{1}{k} – \frac{1}{{k + 1}}$ nên suy ra: $\frac{1}{{1.2}} + \frac{1}{{2.3}} + \frac{1}{{3.4}} + \ldots + \frac{1}{{n(n + 1)}}$ $= 1 – \frac{1}{{n + 1}}.$

Vậy $D = \lim \left( {1 – \frac{1}{{n + 1}}} \right) = 1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
## Ví dụ 3. Tìm các giới hạn sau: $A = \lim \frac{{{4^{n + 1}} – {5^{n + 1}}}}{{{4^n} + {5^n}}}.$

Lời giải:

Chia cả tử và mẫu cho ${5^n}$ ta có: $A = \lim \frac{{4{{\left( {\frac{4}{5}} \right)}^n} – 5}}{{{{\left( {\frac{4}{5}} \right)}^n} + 1}} = – 5$ (do $\lim {\left( {\frac{4}{5}} \right)^n} = 0$).

<!-- chunk:5 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
## Ví dụ 4. Tìm giới hạn sau: $C = \lim \left[ {\left( {1 – \frac{1}{{{2^2}}}} \right)\left( {1 – \frac{1}{{{3^2}}}} \right) \ldots \left( {1 – \frac{1}{{{n^2}}}} \right)} \right].$

Lời giải:

Ta có: $1 – \frac{1}{{{k^2}}}$ $= \frac{{(k – 1)(k + 1)}}{{{k^2}}}$ nên suy ra:

$\left( {1 – \frac{1}{{{2^2}}}} \right)\left( {1 – \frac{1}{{{3^2}}}} \right) \ldots \left( {1 – \frac{1}{{{n^2}}}} \right)$ $= \frac{{1.3}}{{{2^2}}}.\frac{{2.4}}{{{3^2}}} \ldots \frac{{(n – 1)(n + 1)}}{{{n^2}}}$ $= \frac{{n + 1}}{{2n}}.$

Do vậy $C = \lim \frac{{n + 1}}{{2n}} = \frac{1}{2}.$

<!-- chunk:6 level:1 source:https://toanmath.com/2020/05/tim-gioi-han-cua-day-so-dua-vao-cac-dinh-ly-va-cac-gioi-han-co-ban.html -->
## III. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1. Tìm các giới hạn sau:

## Bài tập 1. $A = \lim \frac{{{{\left( {2{n^2} + 1} \right)}^4}{{(n + 2)}^9}}}{{{n^{17}} + 1}}.$

## Bài tập 2. $B = \lim \frac{{\sqrt {{n^2} + 1} – \sqrt[3]{{3{n^3} + 2}}}}{{\sqrt[4]{{2{n^4} + n + 2}} – n}}.$

Lời giải:

1. Ta có: $A = \lim \frac{{{n^8}{{\left( {2 + \frac{1}{{{n^2}}}} \right)}^4}.{n^9}{{\left( {1 + \frac{2}{n}} \right)}^9}}}{{{n^{17}}\left( {1 + \frac{1}{{{n^{17}}}}} \right)}}$ $= \lim \frac{{{{\left( {2 + \frac{1}{{{n^2}}}} \right)}^4}.{{\left( {1 + \frac{2}{n}} \right)}^9}}}{{1 + \frac{1}{{{n^{17}}}}}}.$

Suy ra $A = 16.$

2. Ta có: $B = \lim \frac{{n\left( {\sqrt {1 + \frac{1}{{{n^2}}}} – \sqrt[3]{{3 + \frac{2}{{{n^3}}}}}} \right)}}{{n\left( {\sqrt[4]{{2 + \frac{1}{{{n^3}}} + \frac{2}{{{n^4}}}}} – 1} \right)}}$ $= \frac{{1 – \sqrt[3]{3}}}{{\sqrt[4]{2} – 1}}.$

## Bài 2. Tìm các giới hạn sau:

## Bài tập 1. $A = \lim \left( {\sqrt[3]{{{n^3} + 9{n^2}}} – n} \right).$

## Bài tập 2. $B = \lim \left( {\sqrt {{n^2} + 2n} – \sqrt[3]{{{n^3} + 2{n^2}}}} \right).$

Lời giải:

1. Ta có: $A = \lim \left( {\sqrt[3]{{{n^3} + 9{n^2}}} – n} \right)$ $= \lim \frac{{9{n^2}}}{{\sqrt[3]{{{{\left( {{n^3} + 9{n^2}} \right)}^2}}} + n\sqrt[3]{{{n^3} + 9{n^2}}} + {n^2}}}.$

$= \lim \frac{9}{{\sqrt[3]{{{{\left( {1 + \frac{9}{n}} \right)}^2}}} + \sqrt {1 + \frac{9}{n}} + 1}} = 3.$

2. Ta có: $B = \lim \left( {\sqrt {{n^2} + 2n} – n} \right) – \lim \left( {\sqrt[3]{{{n^3} + 2{n^2}}} – n} \right).$

$= \lim \frac{{2n}}{{\sqrt {{n^2} + 2n} + n}}$ $– \lim \frac{{2{n^2}}}{{\sqrt[3]{{{{\left( {{n^3} + 2{n^2}} \right)}^2}}} + n\sqrt[3]{{{n^3} + 2{n^2}}} + {n^2}}}.$

$= \lim \frac{2}{{\sqrt {1 + \frac{2}{n}} + 1}}$ $– \lim \frac{2}{{\sqrt[3]{{{{\left( {1 + \frac{2}{n}} \right)}^2}}} + \sqrt[3]{{1 + \frac{2}{n}}} + 1}}$ $= \frac{1}{3}.$

## Bài 3. Tìm các giới hạn sau:

## Bài tập 1. $C = \lim \frac{{\sqrt[4]{{3{n^3} + 1}} – n}}{{\sqrt {2{n^4} + 3n + 1} + n}}.$

## Bài tập 2. $D = \lim \frac{{{a_k}{n^k} + \ldots + {a_1}n + {a_0}}}{{{b_p}{n^p} + \ldots + {b_1}n + {b_0}}}$ trong đó $k$,$p$ là các số nguyên dương; ${a_k}{b_p} \ne 0.$

## Bài tập 3. $E = \lim \left( {\sqrt {{n^2} + n + 1} – n} \right).$

## Bài tập 4. $F = \lim \left( {\sqrt {4{n^2} + 1} – \sqrt[3]{{8{n^3} + n}}} \right).$

Lời giải:

## Bài tập 1. Chia cả tử và mẫu cho ${n^2}$ ta có được $C = \lim \frac{{\sqrt[4]{{\frac{3}{{{n^5}}} + \frac{1}{{{n^8}}}}} – \frac{1}{n}}}{{\sqrt {2 + \frac{3}{{{n^3}}} + \frac{1}{{{n^4}}}} + \frac{1}{n}}} = 0.$

## Bài tập 2. Ta xét ba trường hợp sau:

+ $k > p.$ Chia cả tử và mẫu cho ${n^k}$ ta có:

$D = \lim \frac{{{a_k} + \frac{{{a_{k – 1}}}}{n} + \ldots + \frac{{{a_0}}}{{{n^k}}}}}{{\frac{{{b_p}}}{{{n^{p – k}}}} + \ldots + \frac{{{b_0}}}{{{n^k}}}}}$ 
$$
= \left\{ {\begin{array}{l}
{ + \infty \,\,{\rm{nếu}}\,\,{a_k}{b_p} > 0}\\
{ – \infty \,\,{\rm{nếu}}\,\,{a_k}{b_p} < 0}
\end{array}} \right..
$$

+ $k = p.$ Chia cả tử và mẫu cho ${n^k}$ ta có: $D = \lim \frac{{{a_k} + \frac{{{a_{k – 1}}}}{n} + \ldots + \frac{{{a_0}}}{{{n^k}}}}}{{{b_k} + \ldots + \frac{{{b_0}}}{{{n^k}}}}} = \frac{{{a_k}}}{{{b_k}}}.$

+ $k < p.$ Chia cả tử và mẫu cho ${n^p}$: $D = \lim \frac{{\frac{{{a_k}}}{{{n^{p – k}}}} + \ldots + \frac{{{a_0}}}{{{n^p}}}}}{{{b_p} + \ldots + \frac{{{b_0}}}{{{n^p}}}}} = 0.$

3. Ta có: $E = \lim \frac{{n + 1}}{{\sqrt {{n^2} + n + 1} + n}}$ $= \lim \frac{{1 + \frac{1}{n}}}{{\sqrt {1 + \frac{1}{n} + \frac{1}{{{n^2}}}} + 1}} = \frac{1}{2}.$

4. Ta có:

$F = \lim \left( {\sqrt {4{n^2} + 1} – 2n} \right)$ $– \lim \left( {\sqrt[3]{{8{n^3} + n}} – 2n} \right).$

Mà: $\lim \left( {\sqrt {4{n^2} + 1} – 2n} \right)$ $= \lim \frac{1}{{\sqrt {4{n^2} + 1} + 2n}} = 0.$

$\lim \left( {\sqrt[3]{{8{n^2} + n}} – 2n} \right)$ $= \lim \frac{n}{{\sqrt[3]{{{{\left( {8{n^2} + n} \right)}^2}}} + 2n\sqrt[3]{{8{n^2} + n}} + 4{n^2}}}$ $= 0.$

## Bài 4. Tìm các giới hạn sau:

## Bài tập 1. $A = \lim \frac{{2{n^3} + \sin 2n – 1}}{{{n^3} + 1}}.$

## Bài tập 2. $B = \lim \frac{{\sqrt[n]{{n!}}}}{{\sqrt {{n^3} + 2n} }}.$

## Bài tập 3. $C = \lim \left( {\sqrt[k]{{{n^2} + 1}} – \sqrt[p]{{{n^2} – 1}}} \right).$

Lời giải:

## Bài tập 1. $A = \lim \frac{{2 + \frac{{\sin 2n – 1}}{{{n^3}}}}}{{1 + \frac{1}{{{n^3}}}}} = 2.$

2. Ta có: $\frac{{\sqrt[n]{{n!}}}}{{\sqrt {{n^3} + 2n} }}$ $< \frac{{\sqrt[n]{{{n^n}}}}}{{\sqrt {{n^3} + 2n} }}$ $= \frac{n}{{\sqrt {{n^3} + 2n} }}$ $\to 0$ $\Rightarrow B = 0.$

## Bài tập 3. Xét các trường hợp:

+ Trường hợp 1: $k > p$ $\Rightarrow C = – \infty .$

+ Trường hợp 2: $k < p$ $\Rightarrow C = + \infty .$

+ Trường hợp 3: $k = p$ $\Rightarrow C = 0.$

## Bài 5. Tìm giới hạn của các dãy số sau:

## Bài tập 1. ${u_n} = \frac{1}{{2\sqrt 1 + \sqrt 2 }}$ $+ \frac{1}{{3\sqrt 2 + 2\sqrt 3 }}$ $+ \ldots + \frac{1}{{(n + 1)\sqrt n + n\sqrt {n + 1} }}.$

## Bài tập 2. ${u_n} = \left( {1 – \frac{1}{{{T_1}}}} \right)\left( {1 – \frac{1}{{{T_2}}}} \right) \ldots \left( {1 – \frac{1}{{{T_n}}}} \right)$ trong đó ${T_n} = \frac{{n(n + 1)}}{2}.$

## Bài tập 3. ${u_n} = \frac{{{2^3} – 1}}{{{2^3} + 1}}.\frac{{{3^3} – 1}}{{{3^3} + 1}} \ldots \frac{{{n^3} – 1}}{{{n^3} + 1}}.$

## Bài tập 4. ${u_n} = \sum\limits_{k = 1}^n {\frac{n}{{{n^2} + k}}} .$

Lời giải:

1. Ta có: $\frac{1}{{(k + 1)\sqrt k + k\sqrt {k + 1} }}$ $= \frac{1}{{\sqrt k }} – \frac{1}{{\sqrt {k + 1} }}.$

Suy ra ${u_n} = 1 – \frac{1}{{\sqrt {n + 1} }}$ $\Rightarrow \lim {u_n} = 1.$

2. Ta có: $1 – \frac{1}{{{T_k}}}$ $= 1 – \frac{2}{{k(k + 1)}}$ $= \frac{{(k – 1)(k + 2)}}{{k(k + 1)}}.$

Suy ra ${u_n} = \frac{1}{3}.\frac{{n + 2}}{n}$ $\Rightarrow \lim {u_n} = \frac{1}{3}.$

3. Ta có $\frac{{{k^3} – 1}}{{{k^3} + 1}}$ $= \frac{{(k – 1)\left( {{k^2} + k + 1} \right)}}{{(k + 1)\left[ {{{(k – 1)}^2} + (k – 1) + 1} \right]}}$ $\Rightarrow {u_n} = \frac{2}{3}.\frac{{{n^2} + n + 1}}{{(n – 1)n}}$ $\Rightarrow \lim {u_n} = \frac{2}{3}.$

4. Ta có: $n\frac{n}{{{n^2} + n}} \le {u_n} \le n\frac{n}{{{n^2} + 1}}$ $\Rightarrow \frac{{ – n}}{{{n^2} + 1}} \le {u_n} – 1 \le \frac{{ – 1}}{{{n^2} + 1}}$ $\Rightarrow \left| {{u_n} – 1} \right| \le \frac{n}{{{n^2} + 1}} \to 0$ $\Rightarrow \lim {u_n} = 1.$

## Bài 6. Tìm các giới hạn sau:

## Bài tập 1. $A = \lim \frac{{{a_k}{n^k} + {a_{k – 1}}{n^{k – 1}} + \ldots + {a_1}n + {a_0}}}{{{b_p}{n^p} + {b_{p – 1}}{n^{p – 1}} + \ldots + {b_1}n + {b_0}}}$ với ${a_k}{b_p} \ne 0.$

## Bài tập 2. $B = \lim \left( {\sqrt {{n^2} + n + 1} – 2\sqrt[3]{{{n^3} + {n^2} – 1}} + n} \right).$

Lời giải:

## Bài tập 1. Ta chia làm các trường hợp sau:

+ Trường hợp 1: $n = k$, chia cả tử và mẫu cho ${n^k}$, ta được:

$A = \lim \frac{{{a_k} + \frac{{{a_{k – 1}}}}{n} + \ldots + \frac{{{a_0}}}{{{n^k}}}}}{{{b_p} + \frac{{{b_{p – 1}}}}{n} + \ldots + \frac{{{b_0}}}{{{n^k}}}}} = \frac{{{a_k}}}{{{b_p}}}.$

+ Trường hợp 2: $k>p$, chia cả tử và mẫu cho ${n^k}$, ta được:

$A = \lim \frac{{{a_k} + \frac{{{a_{k – 1}}}}{n} + \ldots + \frac{{{a_0}}}{{{n^k}}}}}{{\frac{{{b_p}}}{{{n^{k – p}}}} + \frac{{{b_{p – 1}}}}{{{n^{k – p + 1}}}} + \ldots + \frac{{{b_0}}}{{{n^k}}}}}$ 
$$
= \left\{ {\begin{array}{l}
{ + \infty \,\,{\rm{khi}}\,\,{a_k}{b_p} > 0}\\
{ – \infty \,\,{\rm{khi}}\,\,{a_k}{b_p} < 0}
\end{array}} \right..
$$

+ Trường hợp 3: $k<p$, chia cả tử và mẫu cho ${n^p}$, ta được:

$A = \lim \frac{{\frac{{{a_k}}}{{{n^{p – k}}}} + \frac{{{a_{k – 1}}}}{{{n^{p – k + 1}}}} + \ldots + \frac{{{a_0}}}{{{n^p}}}}}{{{b_p} + \frac{{{b_{p – 1}}}}{n} + \ldots + \frac{{{b_0}}}{{{n^p}}}}} = 0.$

2. Ta có: $B = \lim \left( {\sqrt {{n^2} + n + 1} – n} \right)$ $– 2\lim \left( {\sqrt[3]{{{n^3} + {n^2} – 1}} – n} \right).$

Mà: $\lim \left( {\sqrt {{n^2} + n + 1} – n} \right)$ $= \lim \frac{{n + 1}}{{\sqrt {{n^2} + n + 1} + n}}$ $= \lim \frac{{1 + \frac{1}{n}}}{{\sqrt {1 + \frac{1}{n} + \frac{1}{{{n^2}}}} + 1}}$ $= \frac{1}{2}.$

$\lim \left( {\sqrt[3]{{{n^3} + {n^2} – 1}} – n} \right)$ $= \lim \frac{{{n^2} – 1}}{{\sqrt[3]{{{{\left( {{n^3} + {n^2} – 1} \right)}^2}}} + n\sqrt[3]{{{n^3} + {n^2} – 1}} + {n^2}}}.$

$= \lim \frac{{1 – \frac{1}{{{n^2}}}}}{{\sqrt[3]{{{{\left( {1 + \frac{1}{{{n^4}}} – \frac{1}{{{n^6}}}} \right)}^2}}} + \sqrt[3]{{1 + \frac{1}{n} – \frac{1}{{{n^3}}}}} + 1}}$ $= \frac{1}{3}.$

Vậy $B = \frac{1}{2} – \frac{2}{3} = – \frac{1}{6}.$

## Bài 7.

## Bài tập 1. Cho các số thực $a$, $b$ thỏa $|a| < 1$; $|b| < 1.$ Tìm giới hạn $I = \lim \frac{{1 + a + {a^2} + \ldots + {a^n}}}{{1 + b + {b^2} + \ldots + {b^n}}}.$

## Bài tập 2. Cho dãy số $\left( {{x_n}} \right)$ xác định bởi ${x_1} = \frac{1}{2}$, ${x_{n + 1}} = x_n^2 + {x_n}$, $\forall n \ge 1.$

Đặt ${S_n} = \frac{1}{{{x_1} + 1}} + \frac{1}{{{x_2} + 1}} + \ldots + \frac{1}{{{x_n} + 1}}.$ Tính $\lim {S_n}.$

## Bài tập 3. Cho dãy số $\left( {{u_n}} \right)$ được xác định bởi:
$$
\left\{ {\begin{array}{l}
{{u_1} = 3}\\
{{u_{n + 1}} = \frac{{{u_n}{{\left( {{u_n} + 1} \right)}^2} – 8}}{5}}
\end{array}} \right.
$$
, $(n \ge 1,n \in N)$. Xét sự hội tụ và tính giới hạn sau nếu tồn tại: $\mathop {\lim }\limits_{n \to \infty } \sum\limits_{i = 1}^n {\frac{{{u_i} – 2}}{{u_i^2 + 1}}} .$

Lời giải:

1. Ta có $1$, $a$, ${a^2}$ … ${a^n}$ là một cấp số nhân công bội $a.$

$1 + a + {a^2} + \ldots + {a^n}$ $= \frac{{1 – {a^{n + 1}}}}{{1 – a}}.$

Tương tự: $1 + b + {b^2} + \ldots + {b^n}$ $= \frac{{1 – {b^{n + 1}}}}{{1 – b}}.$

Suy ra $\lim I = \lim \frac{{\frac{{1 – {a^{n + 1}}}}{{1 – a}}}}{{\frac{{1 – {b^{n + 1}}}}{{1 – b}}}} = \frac{{1 – b}}{{1 – a}}$ (vì $|a| < 1$, $|b| < 1$ $\Rightarrow \lim {a^{n + 1}} = \lim {b^{n + 1}} = 0$).

## Bài tập 2. Từ công thức truy hồi ta có: ${x_{n + 1}} > {x_n}$, $\forall n = 1,2, \ldots .$

Nên dãy $\left( {{x_n}} \right)$ là dãy số tăng.

Giả sử dãy $\left( {{x_n}} \right)$ là dãy bị chặn trên, khi đó sẽ tồn tại $\lim {x_n} = x.$

Với $x$ là nghiệm của phương trình: $x = {x^2} + x$ $\Leftrightarrow x = 0 < {x_1}$ vô lí.

Do đó dãy $\left( {{x_n}} \right)$ không bị chặn, hay $\lim {x_n} = + \infty .$

Mặt khác $\frac{1}{{{x_{n + 1}}}} = \frac{1}{{{x_n}\left( {{x_n} + 1} \right)}}$ $= \frac{1}{{{x_n}}} – \frac{1}{{{x_n} + 1}}.$

Suy ra: $\frac{1}{{{x_n} + 1}} = \frac{1}{{{x_n}}} – \frac{1}{{{x_{n + 1}}}}.$

Dẫn tới: ${S_n} = \frac{1}{{{x_1}}} – \frac{1}{{{x_{n + 1}}}} = 2 – \frac{1}{{{x_{n + 1}}}}$ $\Rightarrow \lim {S_n} = 2 – \lim \frac{1}{{{x_{n + 1}}}} = 2.$

## Bài tập 3. Ta chứng minh được: ${u_n} \ge 3$; $\forall n \in {N^*}$, do đó ${u_{n + 1}} – {u_n}$ $= \frac{{{{\left( {{u_n} + 2} \right)}^2}\left( {{u_n} – 2} \right)}}{5} > 0.$

Từ đó thấy $\left( {{u_n}} \right)$ tăng.

Giả sử $\left( {{u_n}} \right)$ bị chặn, khi đó tồn tại giới hạn hữu hạn, giả sử $\lim {u_n} = a$ và ta có: $a = \frac{{a{{(a + 1)}^2} – 8}}{5}$ $\Leftrightarrow {a^3} + 2{a^2} – 4a – 8 = 0$ $\Leftrightarrow a = \pm 2$ (loại).

Do đó $\lim {u_n} = + \infty .$

Ta lại thấy rằng: ${u_{n + 1}}$ $= \frac{{{u_n}{{\left( {{u_n} + 1} \right)}^2} – 8}}{5}$ $\Rightarrow \frac{{{u_n} – 2}}{{u_n^2 + 1}}$ $= \frac{1}{{{u_n} + 2}} – \frac{1}{{{u_{n + 1}} + 2}}$, $\forall n \in {N^*}.$

Vì vậy nên: $\mathop {\lim }\limits_{n \to \infty } \sum\limits_{i = 1}^n {\frac{{{u_i} – 2}}{{u_i^2 + 1}}}$ $= \mathop {\lim }\limits_{n \to \infty } \left( {\frac{1}{{{u_1} + 2}} – \frac{1}{{{u_{n + 1}} + 2}}} \right)$ $= \frac{1}{5}.$