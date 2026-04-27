# Tìm hệ số của số hạng chứa ${x^h}$ trong khai triển nhiều hạng tử

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tim-he-so-cua-so-hang-chua-xh-trong-khai-trien-nhieu-hang-tu.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm hệ số của số hạng chứa ${x^h}$ trong khai triển nhiều hạng tử (ba hạng tử, bốn hạng tử …), đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11: Tổ hợp và Xác suất.

## Bài 1: Tìm hệ số của ${x^6}$ trong khai triển ${\left[ {1 + {x^2}(1 + x)} \right]^7}.$

Lời giải:

Ta có: ${\left[ {1 + {x^2}(1 + x)} \right]^7}$ $= \sum\limits_{k = 0}^7 {C_7^k} {x^{2k}}{(1 + x)^k}$ $= \sum\limits_{k = 0}^7 {C_7^k} {\left( {{x^2} + {x^3}} \right)^k}$ $= \sum\limits_{k = 0}^7 {\sum\limits_{h = 0}^k {C_7^k} } C_k^h{x^{2k + h}}.$

Số hạng tổng quát trong khai triển là: $C_7^kC_k^h{x^{2k + h}}.$

Để có hệ số của số hạng chứa ${x^6}$ chọn $k$, $h$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{2k + h = 6}\\
{h \le k}\\
{k = \overline {0..7} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{h = 0}\\
{k = 3}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{h = 2}\\
{k = 2}
\end{array}} \right.}
\end{array}} \right..
$$

Vậy hệ số của số hạng chứa ${x^6}$ là: $C_7^3C_3^0 + C_7^2C_2^2 = 56.$

## Bài 2: Tìm hệ số của ${x^4}$ trong khai triển ${\left( {1 + 2x + 3{x^2}} \right)^{10}}.$

Lời giải:

Ta có: ${\left( {1 + 2x + 3{x^2}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {2x + 3{x^2}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} \sum\limits_{h = 0}^k {C_k^h} {(2x)^{k – h}}{\left( {3{x^2}} \right)^h}.$

$= \sum\limits_{k = 0}^{10} {\sum\limits_{h = 0}^k {C_{10}^k} } C_k^h{2^{k – h}}{3^h}{x^{k + h}}.$

Số hạng tổng quát trong khai triển là $C_{10}^kC_k^h{2^{k – h}}{3^h}{x^{k + h}}.$

Để có hệ số của số hạng chứa ${x^4}$ chọn $k$, $h$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{k + h = 4}\\
{h \le k}\\
{k = \overline {0..10} }
\end{array}} \right.
$$
 $\Leftrightarrow (k;h) \in \{ (4;0);(3;1);(2;2)\} .$

Vậy hệ số của số hạng chứa ${x^4}$ trong khai triển là:

$C_{10}^4C_4^0{2^4} + C_{10}^3C_3^1{2^2}.3 + C_{10}^2C_2^2{3^2} = 8085.$

Cách khác:

Ta có: ${\left( {1 + 2x + 3{x^2}} \right)^{10}}$ $= {[1 + x(2 + 3x)]^{10}}$ $= C_{10}^0$ $+ C_{10}^1x(2 + 3x)$ $+ C_{10}^2{x^2}{(2 + 3x)^2}$ $+ C_{10}^3{x^3}{(2 + 3x)^3}$ $+ C_{10}^4{x^4}{(2 + 3x)^4}$ $+ C_{10}^5{x^5}{(2 + 3x)^5}$ $+ \ldots + C_{10}^{10}{x^{10}}{(2 + 3x)^{10}}.$

Ta nhận thấy rằng số mũ của $x$ trong khai triển tăng dần, và ${x^4}$ chỉ chứa trong số hạng thứ $2$, thứ $3$, thứ $4$ trong khai triển trên.

Từ đó ta phân tích các khai triển: $C_{10}^2{x^2}{(2 + 3x)^2}$ $= C_{10}^2C_2^0{2^2}{x^2}$ $+ C_{10}^2C_2^12.3{x^3}$ $+ C_{10}^2C_2^2{3^2}{x^4}.$

$C_{10}^3{x^3}{(2 + 3x)^3}$ $= C_{10}^3C_3^0{2^3}{x^3}$ $+ C_{10}^3C_3^1{2^2}.3{x^4}$ $+ C_{10}^3C_3^2{2.3^2}{x^5}$ $+ C_{10}^3C_3^3{3^3}{x^6}.$

$C_{10}^4{x^4}{(2 + 3x)^4}$ $= C_{10}^4C_4^0{2^4}{x^4}$ $+ C_{10}^4C_4^1{2^3}.3{x^5}$ $+ \ldots + C_{10}^4C_4^4{3^4}{x^8}.$

Vậy hệ số của số hạng chứa ${x^4}$ trong khai triển là:

$C_{10}^4C_4^0{2^4}$ $+ C_{10}^3C_3^1{2^2}.3$ $+ C_{10}^2C_2^2{3^2}$ $= 8085.$

## Bài 3: Tìm số hạng không chứa $x$ trong khai triển: ${\left( {1 + 2x – \frac{1}{{{x^2}}}} \right)^9}.$

Lời giải:

Ta có: ${\left( {1 + 2x – \frac{1}{{{x^2}}}} \right)^9}$ $= \sum\limits_{k = 0}^9 {C_9^k} {\left( {2x – \frac{1}{{{x^2}}}} \right)^k}$ $= \sum\limits_{k = 0}^9 {C_9^k} \sum\limits_{h = 0}^k {C_k^h} {(2x)^{k – h}}{\left( { – \frac{1}{{{x^2}}}} \right)^h}.$

$= \sum\limits_{k = 0}^9 {\sum\limits_{h = 0}^k {C_9^k} } C_k^h{(2)^{k – h}}{( – 1)^h}{x^{k – 3h}}.$

Số hạng tổng quát trong khai triển là: $C_9^kC_k^h{(2)^{k – h}}{( – 1)^h}{x^{k – 3h}}.$

Để có số hạng không chứa $x$, ta chọn $k$, $h$ thỏa mãn:

$$
\left\{ {\begin{array}{l}
{k – 3h = 0}\\
{h \le k}\\
{k = \overline {0..9} }
\end{array}} \right.
$$
 $\Leftrightarrow (k;h) \in \{ (3;1);(6;2);(9;3)\} .$

Vậy số hạng không chứa $x$ trong khai triển là: $C_9^3C_3^1{(2)^2}{( – 1)^1}$ $+ C_9^6C_6^2{(2)^4}{( – 1)^2}$ $+ C_9^9C_9^3{(2)^6}{( – 1)^3}$ $= 14122.$

## Bài 4: Tìm số hạng chứa $\frac{1}{{\sqrt[3]{x}}}$ trong khai triển ${\left( {1 – 2\sqrt x + \frac{1}{{\sqrt[3]{{{x^2}}}}}} \right)^7}.$

Lời giải:

Ta có: ${\left( {1 – 2\sqrt x + \frac{1}{{\sqrt[3]{{{x^2}}}}}} \right)^7}$ $= \sum\limits_{k = 0}^7 {C_7^k} {\left( { – 2\sqrt x + \frac{1}{{\sqrt[3]{{{x^2}}}}}} \right)^k}.$

$= \sum\limits_{k = 0}^7 {C_7^k} \sum\limits_{h = 0}^k {C_k^h} {\left( { – 2{x^{\frac{1}{2}}}} \right)^{k – h}}{\left( {{x^{ – \frac{2}{3}}}} \right)^h}$ $= \sum\limits_{k = 0}^7 {\sum\limits_{h = 0}^k {C_7^k} } C_k^h{( – 2)^{k – h}}{x^{\frac{{3k – 7h}}{6}}}.$

Số hạng tổng quát trong khai triển là: $C_7^kC_k^h{( – 2)^{k – h}}{x^{\frac{{3k – 7h}}{6}}}.$

Để có số hạng chứa $\frac{1}{{\sqrt[3]{x}}} = {x^{ – \frac{1}{3}}}$, ta chọn $k$, $h$ thỏa mãn:

$$
\left\{ {\begin{array}{l}
{\frac{{3k – 7h}}{6} = – \frac{1}{3}}\\
{h \le k}\\
{k = \overline {0..7} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{3k – 7h = – 2}\\
{h \le k}\\
{k = \overline {0..7} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k = 4}\\
{h = 2}
\end{array}} \right..
$$

Vậy số hạng chứa $\frac{1}{{\sqrt[3]{x}}}$ trong khai triển là: $C_7^4C_4^2{( – 2)^2}{x^{\frac{{ – 1}}{3}}} = \frac{{840}}{{\sqrt[3]{x}}}.$

## Bài 5: Khai triển $f(x) = {\left( {1 + x + {x^2} + {x^3}} \right)^5}$ và viết lại dưới dạng: $f(x) = {a_0} + {a_1}x + \ldots + {a_{15}}{x^{15}}.$ Tính ${a_9}.$

Lời giải:

Ta có: $f(x) = {\left( {1 + x + {x^2} + {x^3}} \right)^5}$ $= {(1 + x)^5}{\left( {1 + {x^3}} \right)^5}.$

$= \sum\limits_{k = 0}^5 {C_5^k} {x^k}.\sum\limits_{l = 0}^5 {C_5^l} {\left( {{x^3}} \right)^l}$ $= \sum\limits_{k = 0}^5 {\sum\limits_{l = 0}^5 {C_5^k} } C_5^l{x^{k + 3l}}.$

Số hạng tổng quát trong khai triển là: $C_5^kC_5^l{x^{k + 3l}}.$

Nhận thấy ${a_9}$ chính là hệ số của số hạng chứa ${x^9}$ trong khai triển, vì vậy chọn $k$, $l$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{k + 3l = 9}\\
{k,l = \overline {0..5} }
\end{array}} \right..
$$

Suy ra: 
$$
\left\{ {\begin{array}{l}
{l = \frac{{9 – k}}{3}}\\
{k,l = \overline {0..5} }
\end{array}} \right.
$$
, do đó: $k \vdots 3$ 
$$
\Rightarrow \left[ {\begin{array}{l}
{k = 0 \Rightarrow l = 3}\\
{k = 3 \Rightarrow l = 2}
\end{array}} \right..
$$

Vậy có hai cặp số $(k,l)$ thỏa mãn.

Suy ra hệ số của số hạng chứa ${x^9}$ trong khai triển là: $C_5^3C_5^2 + C_5^0C_5^3 = 110.$

## Bài 6: Giả sử ${\left( {1 + x + {x^2} + {x^3}} \right)^5}$ có khai triển thành đa thức: ${a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_{15}}{x^{15}}.$ Tính ${a_0} – {a_1} + {a_2} – {a_3} + \ldots – {a_{15}}.$

Lời giải:

Ta có: ${\left( {1 + x + {x^2} + {x^3}} \right)^5}$ $= {\left[ {(1 + x)\left( {1 + {x^2}} \right)} \right]^5}$ $= {(1 + x)^5}{\left( {1 + {x^2}} \right)^5}.$

$= \sum\limits_{k = 0}^5 {C_5^k} {x^k}\sum\limits_{h = 0}^5 {C_5^h} {x^{2h}}$ $= \sum\limits_{k = 0}^5 {\sum\limits_{h = 0}^5 {C_5^k} } C_5^h{x^{k + 2h}}.$

Chọn $x = -1$, ta được:

${a_0} – {a_1} + {a_2} – {a_3} + \ldots – {a_{15}}$ $= \sum\limits_{k = 0}^5 {\sum\limits_{h = 0}^5 {C_5^k} } C_5^h{( – 1)^{k + 2h}}$ $= \left( {1 – 1 + {1^2} + {{( – 1)}^3}} \right) = 0.$

Vậy ${a_0} – {a_1} + {a_2} – {a_3} + \ldots – {a_{15}} = 0.$

## Bài 7: Trong khai triển ${(x + y + z)^n}$, tìm số hạng chứa ${x^k}{y^m}{z^{n – k – m}}$ $(k,m < n).$

Lời giải:

Ta có: ${(x + y + z)^n}$ $= {[(y + z) + x]^n}$ $= C_n^0{(y + z)^n}$ $+ C_n^1x{(y + z)^{n – 1}}$ $+ C_n^2{x^2}{(y + z)^{n – 2}}$ $+ \ldots + C_n^k{x^k}{(y + z)^{n – k}}$ $+ \ldots + C_n^n{x^n}.$

Do đó số hạng chứa ${x^k}{y^m}{z^{n – k – m}}$ nằm trong khai triển $C_n^k{x^k}{(y + z)^{n – k}}.$

Mặt khác ta có: ${(y + z)^{n – k}}$ $= C_{n – k}^0{z^{n – k}}$ $+ C_{n – k}^1y{z^{n – k – 1}}$ $+ C_{n – k}^2{y^2}{z^{n – k – 2}}$ $+ \ldots + C_{n – k}^m{y^m}{z^{n – k – m}}$ $+ \ldots + C_{n – k}^{n – k}{y^{n – k}}.$

Do đó số hạng chứa ${x^k}{y^m}{z^{n – k – m}}$ trong khai triển là: $C_n^kC_{n – k}^m{x^k}{y^m}{z^{n – k – m}}.$

## Bài 8: Trong khai triển ${\left( {2{x^3} + 2{x^2} + x + 1} \right)^{10}}$, tìm số hạng chứa ${x^5}.$

Lời giải:

Ta có: ${\left( {2{x^3} + 2{x^2} + x + 1} \right)^{10}}$ $= {\left[ {(1 + x)\left( {1 + 2{x^2}} \right)} \right]^{10}}$ $= {(1 + x)^{10}}{\left( {1 + 2{x^2}} \right)^{10}}.$

$= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^k}\sum\limits_{h = 0}^{10} {C_{10}^h} {2^{2h}}{x^{2h}}$ $= \sum\limits_{k = 0}^{10} {\sum\limits_{h = 0}^{10} {C_{10}^k} } C_{10}^h{2^{2h}}{x^{k + 2h}}.$

Số hạng tổng quát trong khai triển là: $C_{10}^kC_{10}^h{2^{2h}}{x^{k + 2h}}.$

Để có số hạng chứa ${x^5}$, ta chọn $k$, $h$ sao cho:

$$
\left\{ {\begin{array}{l}
{k + 2h = 5}\\
{h,k = \overline {0..10} }
\end{array}} \right.
$$
 $\Leftrightarrow (k;h) \in \{ (1;2);(3;1)\} .$

Vậy số hạng chứa ${x^5}$ trong khai triển là: $C_{10}^1C_{10}^2{2^4}{x^5} + C_{10}^3C_{10}^1{2^2}{x^5}$ $= 12000{x^5}.$