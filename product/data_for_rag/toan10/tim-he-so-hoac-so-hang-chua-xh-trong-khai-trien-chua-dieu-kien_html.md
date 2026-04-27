# Tìm hệ số hoặc số hạng chứa ${x^h}$ trong khai triển chứa điều kiện

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tim-he-so-hoac-so-hang-chua-xh-trong-khai-trien-chua-dieu-kien.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm hệ số hoặc số hạng chứa ${x^h}$ trong khai triển chứa điều kiện, đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11: Tổ hợp và xác suất.

1. PHƯƠNG PHÁP GIẢI TOÁN

Các bài toán loại này thường chưa biết $n$ trong khai triển, do đó ta thực hiện các bước:

+ Từ điều kiện bài toán tìm $n$ (hoặc các ẩn liên quan).

+ Sau đó thực hiện tương tự bài toán tìm hệ số của số hạng chứa ${x^h}$ trong khai triển biết $n$ đã được đề cập trước đó trên TOANMATH.com.

## Bài tập

## Bài 1: Cho $n$ là số nguyên dương thỏa mãn: $5C_n^{n – 1} = C_n^3.$ Tìm số hạng chứa ${x^5}$ trong khai triển nhị thức Niu-tơn của ${\left( {\frac{{n{x^2}}}{{14}} – \frac{1}{x}} \right)^n}$ với $x \ne 0.$

Lời giải:

Xét phương trình $5C_n^{n – 1} = C_n^3.$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{n \ge 3}\\
{n \in Z}
\end{array}} \right..
$$

Phương trình $\Leftrightarrow 5.\frac{{n!}}{{(n – 1)!}} = \frac{{n!}}{{3!(n – 3)!}}$ $\Leftrightarrow 5n = \frac{{n(n – 1)(n – 2)}}{6}.$

$\Leftrightarrow 30 = {n^2} – 3n + 2$ $\Leftrightarrow {n^2} – 3n – 28 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 7}\\
{n = – 4\,\,{\rm{(loại)}}}
\end{array}} \right..
$$

Khi đó: ${\left( {\frac{{n{x^2}}}{{14}} – \frac{1}{x}} \right)^n}$ $= {\left( {\frac{{{x^2}}}{2} – \frac{1}{x}} \right)^7}$ $= \sum\limits_{k = 0}^7 {C_7^k} {\left( {\frac{{{x^2}}}{2}} \right)^{7 – k}}.{\left( { – \frac{1}{x}} \right)^k}.$

Số hạng tổng quát trong khai triển là:

${T_{k + 1}}$ $= C_7^k{\left( {\frac{{{x^2}}}{2}} \right)^{7 – k}}.{\left( { – \frac{1}{x}} \right)^k}$ $= C_7^k.\frac{{{x^{14 – 2k}}}}{{{2^{7 – k}}}}.\frac{{{{( – 1)}^k}}}{{{x^k}}}$ $= C_7^k.\frac{{{{( – 1)}^k}}}{{{2^{7 – k}}}}.{x^{14 – 3k}}.$

Nếu hạng tử ${T_{k + 1}}$ chứa ${x^5}$ thì: $14 – 3k = 5$ $\Leftrightarrow k = 3.$

Vậy số hạng chứa ${x^5}$ là số hạng thứ $4$ trong khai triển là:

${T_6} = C_7^3.\frac{{{{( – 1)}^3}}}{{{2^4}}}.{x^5} = – \frac{{35}}{{16}}{x^5}.$

## Bài 2: Tìm hệ số của số hạng chứa ${x^{10}}$ trong khai triển nhị thức Niutơn của ${(2 + x)^n}$, biết ${3^n}C_n^0 – {3^{n – 1}}C_n^1$ $+ {3^{n – 2}}C_n^2 – {3^{n – 3}}C_n^3$ $+ … + {( – 1)^n}C_n^n = 2048.$

Lời giải:

Ta có: ${(3 + x)^n}$ $= C_n^0{3^n} + C_n^1{3^{n – 1}}x$ $+ C_n^2{3^{n – 2}}{x^2} + \ldots + C_n^n{x^n}.$

Chọn $x = – 1$, ta được:

${3^n}C_n^0 – {3^{n – 1}}C_n^1$ $+ {3^{n – 2}}C_n^2 – {3^{n – 3}}C_n^3$ $+ … + {( – 1)^n}C_n^n$ $= {(3 – 1)^n} = {2^n}.$

Từ giả thiết suy ra: ${2^n} = 2048 = {2^{11}}$ $\Leftrightarrow n = 11.$

Suy ra: ${(2 + x)^n}$ $= {(2 + x)^{11}}$ $= \sum\limits_{k = 0}^{11} {C_{11}^k} {2^{11 – k}}{x^k}.$

Số hạng tổng quát trong khai triển là: $C_{11}^k{2^{11 – k}}{x^k}.$

Cho $k =10$, ta được hệ số của ${x^{10}}$ trong khai triển là: $C_{11}^{10}.2 = 22.$

## Bài 3: Trong khai triển nhị thức ${\left( {x + \frac{1}{x}} \right)^n}$, hệ số của số hạng thứ ba lớn hơn hệ số của số hạng thứ hai là $35.$ Tìm số hạng không chứa $x$ trong khai triển nói trên (với $n \in {N^*}$).

Lời giải:

Ta có: ${\left( {x + \frac{1}{x}} \right)^n}$ $= \sum\limits_{k = 0}^n {C_n^k} {x^{n – k}}{\left( {\frac{1}{x}} \right)^k}$ $= \sum\limits_{k = 0}^n {C_n^k} {x^{n – 2k}}.$

Hệ số của số hạng thứ $k + 1$ trong khai triển là: ${T_{k + 1}} = C_n^k.$

Theo giả thiết ta có: $C_n^2 – C_n^1 = 35$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{n \ge 2,n \in N}\\
{\frac{{n!}}{{2!(n – 2)!}} – n = 35}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{n \ge 2,n \in N}\\
{\frac{{n(n – 1)}}{2} – n = 35}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{n \ge 2,n \in N}\\
{{n^2} – 3n – 70 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow n = 10.$

Do đó: ${\left( {x + \frac{1}{x}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{10 – 2k}}.$

Số hạng không chứa $x$ trong khai triển là: $C_{10}^k$ với $10 – 2k = 0$ $\Leftrightarrow k = 5.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{10}^5 = 252.$

## Bài 4: Tìm số hạng không chứa $x$ trong khai triển nhị thức ${\left( {{x^2} + \frac{1}{{{x^3}}}} \right)^n}$, biết rằng $C_n^1 + C_n^3 = 13n$ ($n$ là số tự nhiên lớn hơn $2$ và $x$ là số thực khác $0$).

Lời giải:

Ta có: $C_n^1 + C_n^3 = 13n$ $\Leftrightarrow \frac{{n!}}{{(n – 1)!}} + \frac{{n!}}{{3!(n – 3)!}} = 13n$ $\Leftrightarrow n + \frac{{n(n – 1)(n – 2)}}{6} = 13n.$

$\Leftrightarrow 1 + \frac{{(n – 1)(n – 2)}}{6} = 13$ $\Leftrightarrow {n^2} – 3n – 70 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 10}\\
{n = – 7\,\,{\rm{(loại)}}}
\end{array}} \right..
$$

Do đó: ${\left( {{x^2} + \frac{1}{{{x^3}}}} \right)^n}$ $= {\left( {{x^2} + \frac{1}{{{x^3}}}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {{x^2}} \right)^{10 – k}}{\left( {{x^{ – 3}}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{20 – 5k}}.$

Số hạng tổng quát trong khai triển $C_{10}^k{x^{20 – 5k}}.$

Hệ số không chứa $x$ trong khai triển là: $C_{10}^k$ với $k$ thỏa mãn $20 – 5k = 0$ $\Leftrightarrow k = 4.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{10}^4 = 210.$

## Bài 5: Khai triển biểu thức ${(1 – 2x)^n}$ ta được đa thức có dạng ${a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_n}{x^n}.$ Tìm hệ số của ${x^5}$ biết rằng: ${a_0} + {a_1} + {a_2} = 71.$

Lời giải:

Ta có: ${(1 – 2x)^n}$ $= \sum\limits_{k = 0}^n {C_n^k} .{( – 2x)^k}$ $= \sum\limits_{k = 0}^n {C_n^k} .{( – 2)^k}{x^k}.$

Do đó: ${a_k} = C_n^k.{( – 2)^k}$, $\forall k = \overline {0..n} .$

Khi đó ${a_0} + {a_1} + {a_2} = 71$ $\Leftrightarrow C_n^0 – 2C_n^1 + 4C_n^2 = 71.$

$\Leftrightarrow 1 – 2n + 4\frac{{n(n – 1)}}{2} = 71$ $\Leftrightarrow {n^2} + 2n – 35 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 5}\\
{n = – 7\,\,{\rm{(loại)}}}
\end{array}} \right..
$$

Suy ra: ${(1 – 2x)^7}$ $= \sum\limits_{k = 0}^7 {C_7^k.} {( – 2)^k}.{x^k}.$

Vậy hệ số của ${x^5}$ trong khai triển là: $C_7^5{( – 2)^5} = – 672.$

## Bài 6: Tìm hệ số của ${x^{26}}$ trong khai triển nhị thức Newton của ${\left( {\frac{1}{{{x^4}}} + {x^7}} \right)^n}$, biết rằng $C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n$ $= {2^{20}} – 1.$

Lời giải:

Xét khai triển ${(1 + x)^{2n + 1}}$ $= C_{2n + 1}^0 + C_{2n + 1}^1x$ $+ C_{2n + 1}^2{x^2} + C_{2n + 1}^3{x^3}$ $+ \ldots + C_{2n + 1}^{2n + 1}{x^{2n + 1}}.$

Chọn $x = 1$, ta được: $C_{2n + 1}^0 + C_{2n + 1}^1$ $+ C_{2n + 1}^2 + C_{2n + 1}^3$ $+ \ldots + C_{2n + 1}^{2n + 1} = {2^{2n + 1}}$ $(*).$

Áp dụng công thức $C_{2n + 1}^k = C_{2n + 1}^{2n + 1 – k}$, ta có:

$(*) \Leftrightarrow C_{2n + 1}^0 + C_{2n + 1}^1$ $+ C_{2n + 1}^2 + \ldots + C_{2n + 1}^n$ $+ C_{2n + 1}^n + C_{2n + 1}^{n – 1}$ $+ \ldots + C_{2n + 1}^0 = {2^{2n + 1}}.$

$\Leftrightarrow 2\left( {C_{2n + 1}^0 + C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n} \right) = {2^{2n + 1}}.$

$\Leftrightarrow C_{2n + 1}^0 + C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n = {2^{2n}}.$

$\Leftrightarrow C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n$ $= {2^{2n}} – 1.$

Từ giả thiết ta có: ${2^{2n}} – 1 = {2^{20}} – 1$ $\Leftrightarrow n = 10.$

Khi đó: ${\left( {\frac{1}{{{x^4}}} + {x^7}} \right)^n}$ $= {\left( {\frac{1}{{{x^4}}} + {x^7}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {{x^{ – 4}}} \right)^{10 – k}}{\left( {{x^7}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{11k – 40}}.$

Số hạng tổng quát trong khai triển là: $C_{10}^k{x^{11k – 40}}.$

Hệ số của ${x^{26}}$ trong khai triển là $C_{10}^k$ với $k$ thỏa mãn $11k – 40 = 26$ $\Leftrightarrow k = 6.$

Vậy hệ số của ${x^{26}}$ trong khai triển là $C_{10}^6 = 210.$

## Bài 7: Tìm hệ số chứa ${x^7}$ trong khai triển thành đa thức của ${(2 – 3x)^{2n}}$, trong đó $n$ là số nguyên dương thỏa mãn: $C_{2n + 1}^1 + C_{2n + 1}^3$ $+ C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1} = 1024.$

Lời giải:

Ta có: ${(1 + x)^{2n + 1}}$ $= C_{2n + 1}^0 + C_{2n + 1}^1x$ $+ C_{2n + 1}^2{x^2} + C_{2n + 1}^3{x^3}$ $+ \ldots + C_{2n + 1}^{2n + 1}{x^{2n + 1}}.$

Chọn $x = 1$, ta được: $C_{2n + 1}^0 + C_{2n + 1}^1$ $+ C_{2n + 1}^2 + C_{2n + 1}^3$ $+ \ldots + C_{2n + 1}^{2n + 1} = {2^{2n + 1}}$ $(*).$

Chọn $x = -1$, ta được: $C_{2n + 1}^0 – C_{2n + 1}^1$ $+ C_{2n + 1}^2 – C_{2n + 1}^3$ $+ \ldots – C_{2n + 1}^{2n + 1} = 0.$

$\Leftrightarrow C_{2n + 1}^0 + C_{2n + 1}^2$ $+ C_{2n + 1}^4 + \ldots + C_{2n + 1}^{2n}$ $= C_{2n + 1}^1 + C_{2n + 1}^3$ $+ C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1}.$

Từ $(*)$ suy ra: $2\left( {C_{2n + 1}^1 + C_{2n + 1}^3 + C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1}} \right)$ $= {2^{2n + 1}}.$

$\Leftrightarrow C_{2n + 1}^1 + C_{2n + 1}^3$ $+ C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1} = {2^{2n}}.$

Theo giả thiết ta có: ${2^{2n}} = 1024 = {2^{10}}$ $\Leftrightarrow n = 5.$

Từ đó suy ra: ${(2 – 3x)^{2n}}$ $= {(2 – 3x)^{10}}$ $= \sum\limits_{k = 0}^{10} {{{( – 1)}^k}} C_{10}^k{2^{10 – k}}{(3x)^k}$ $= \sum\limits_{k = 0}^{10} {{{( – 1)}^k}} {.3^k}.C_{10}^k{2^{10 – k}}{x^k}.$

Số hạng tổng quát trong khai triển là: ${( – 1)^k}{.3^k}.C_{10}^k{2^{10 – k}}.{x^k}.$

Để có hệ số chứa ${x^7}$ tương ứng với giá trị của $k$ thỏa mãn $k =7.$

Vậy hệ số chứa ${x^7}$ trong khai triển là: ${( – 1)^7}{.3^7}.C_{10}^7{.2^3}$ $= – C_{10}^7{3^7}{2^3} = 2099520.$

## Bài 8: Tìm hệ số chứa ${x^8}$ trong khai triển nhị thức Newton ${\left( {\frac{1}{{{x^3}}} + \sqrt {{x^5}} } \right)^n}$, biết rằng $C_{n + 4}^{n + 1} – C_{n + 3}^n$ $= 7(n + 3)$ ($n$ nguyên dương, $x>0$).

Lời giải:

Ta có: $C_{n + 4}^{n + 1} – C_{n + 3}^n$ $= 7(n + 3)$ $\Leftrightarrow \frac{{(n + 4)!}}{{3!(n + 1)!}} + \frac{{(n + 3)!}}{{3!n!}}$ $= 7(n + 3).$

$\Leftrightarrow \frac{{(n + 4)(n + 3)(n + 2)}}{6}$ $– \frac{{(n + 3)(n + 2)(n + 1)}}{6}$ $= 7(n + 3).$

$\Leftrightarrow \frac{{(n + 4)(n + 2)}}{6}$ $– \frac{{(n + 2)(n + 1)}}{6} = 7$ $\Leftrightarrow (n + 4)(n + 2) – (n + 2)(n + 1) = 42.$

$\Leftrightarrow 3n + 6 = 42$ $\Leftrightarrow n = 12.$

Khi đó: ${\left( {\frac{1}{{{x^3}}} + \sqrt {{x^5}} } \right)^n}$ $= {\left( {{x^{ – 3}} + {x^{\frac{5}{2}}}} \right)^{12}}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {\left( {{x^{ – 3}}} \right)^k}{\left( {{x^{\frac{5}{2}}}} \right)^{12 – k}}.$

Số hạng tổng quát trong khai triển là: $C_{12}^k{\left( {{x^{ – 3}}} \right)^k}{\left( {{x^{\frac{5}{2}}}} \right)^{12 – k}}$ $= C_{12}^k{x^{\frac{{60 – 11k}}{2}}}.$

Để có hệ số chứa ${x^8}$ thì $\frac{{60 – 11k}}{2} = 8$ $\Leftrightarrow 60 – 11k = 16$ $\Leftrightarrow k = 4.$

Vậy hệ số chứa ${x^8}$ trong khai triển là $C_{12}^4 = \frac{{12!}}{{4!(12 – 4)!}} = 495.$

## Bài 9: Cho khai triển ${\left( {{2^{\frac{{x – 1}}{2}}} + {2^{\frac{{ – x}}{3}}}} \right)^n}$ $= C_n^0{\left( {{2^{\frac{{x – 1}}{2}}}} \right)^n}$ $+ C_n^1{\left( {{2^{\frac{{x – 1}}{2}}}} \right)^{n – 1}}\left( {{2^{\frac{{ – x}}{3}}}} \right)$ $+ \ldots + C_n^{n – 1}\left( {{2^{\frac{{x – 1}}{2}}}} \right){\left( {{2^{\frac{{ – x}}{3}}}} \right)^{n – 1}}$ $+ C_n^n{\left( {{2^{\frac{{ – x}}{3}}}} \right)^n}$ ($n$ là số nguyên dương). Biết rằng trong khai triển đó có $C_n^3 = 5C_n^1$ và số hạng thứ tư bằng $140.$ Tìm $n$ và $x.$

Lời giải:

Xét phương trình ${C_n^3 = 5C_n^1}$ (điều kiện ${n \ge 3}$).

Ta có: $C_n^3 = 5C_n^1$ $\Leftrightarrow \frac{{n!}}{{3!(n – 3)!}} = 5\frac{{n!}}{{(n – 1)!}}$ $\Leftrightarrow \frac{{n(n – 1)(n – 2)}}{6} = 5n.$

$\Leftrightarrow \frac{{(n – 1)(n – 2)}}{6} = 5$ $\Leftrightarrow {n^2} – 3n – 28 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 7}\\
{n = – 4\,\,({\rm{loại}})}
\end{array}} \right..
$$

Số hạng thứ tư trong khai triển là: $C_n^3{\left( {{2^{\frac{{x – 1}}{2}}}} \right)^{n – 3}}{\left( {{2^{\frac{{ – x}}{3}}}} \right)^3}$ $= C_7^3{\left( {{2^{\frac{{x – 1}}{2}}}} \right)^4}{\left( {{2^{\frac{{ – x}}{3}}}} \right)^3}.$

Theo đề bài ta có: $C_7^3{\left( {{2^{\frac{{x – 1}}{2}}}} \right)^4}{\left( {{2^{\frac{{ – x}}{3}}}} \right)^3} = 140$ $\Leftrightarrow {35.2^{2x – 2}}{.2^{ – x}} = 140$ $\Leftrightarrow {2^{x – 2}} = 4$ $\Leftrightarrow x – 2 = 2$ $\Leftrightarrow x = 4.$

Vậy $n = 7$ và $x = 4.$

## Bài 10: Với $n$ là số nguyên dương, gọi ${a_{3n – 3}}$ là hệ số của ${x^{3n – 3}}$ trong khai triển thành đa thức của ${\left( {{x^2} + 1} \right)^n}{(x + 2)^n}.$ Tìm $n$ để ${a_{3n – 3}} = 26n.$

Lời giải:

Ta có: ${\left( {{x^2} + 1} \right)^n}$ $= C_n^0{x^{2n}} + C_n^1{x^{2n – 2}}$ $+ C_n^2{x^{2n – 4}} + \ldots + C_n^n$ $(1).$

Và ${(x + 2)^n}$ $= C_n^0{x^n} + 2C_n^1{x^{n – 1}}$ $+ {2^2}C_n^2{x^{n – 2}} + {2^3}C_n^3{x^{n – 3}}$ $+ \ldots + {2^n}C_n^n$ $(2).$

Với $n = 1$, ta có: ${\left( {{x^2} + 1} \right)^n}{(x + 2)^n}$ $= \left( {{x^2} + 1} \right)(x + 2)$ $= {x^3} + 2{x^2} + x + 2$ không thỏa mãn hệ thức ${a_{3n – 3}} = 26n.$

Tương tự với $n = 2$, cũng không thỏa mãn.

Với $n \ge 3$, ta có: ${x^{3n – 3}} = {x^{2n}}.{x^{n – 3}}$ $= {x^{2n – 2}}.{x^{n – 1}}.$

Suy ra hệ số chứa ${x^{3n – 3}}$ bằng tổng của tích hệ số chứa ${x^{2n}}$ trong $(1)$ với hệ số chứa ${x^{n – 3}}$ trong $(2)$ và tích hệ số chứa ${x^{2n – 2}}$ trong $(1)$ với hệ số chứa ${x^{n – 1}}$ trong $(2).$

Hay ta có: ${a_{3n – 3}} = {2^3}.C_n^0.C_n^3 + 2.C_n^1.C_n^1$ $\Leftrightarrow {2^3}.1.\frac{{n!}}{{3!(n – 3)!}} + 2{n^2} = 26n.$

$\Leftrightarrow \frac{{4n(n – 1)(n – 2)}}{3} + 2{n^2} = 26n$ $\Leftrightarrow \frac{{2(n – 1)(n – 2)}}{3} + n = 13.$

$\Leftrightarrow 2{n^2} – 3n – 35 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 5}\\
{n = – \frac{7}{2}\,\,{\rm{(loại)}}}
\end{array}} \right..
$$

Vậy $n = 5.$