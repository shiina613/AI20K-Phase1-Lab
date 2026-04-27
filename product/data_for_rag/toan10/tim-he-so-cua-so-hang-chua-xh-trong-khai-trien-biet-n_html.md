# Tìm hệ số của số hạng chứa ${x^h}$ trong khai triển biết $n$

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tim-he-so-cua-so-hang-chua-xh-trong-khai-trien-biet-n.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm hệ số của số hạng chứa ${x^h}$ trong khai triển nhị thức Newton khi biết số mũ $n$, đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11.

1. PHƯƠNG PHÁP GIẢI TOÁN

Phương pháp:

+ Áp dụng khai triển ${(a + b)^n} = \sum\limits_{k = 0}^n {C_n^k} {a^{n – k}}{b^k}.$

+ Xác định số hạng tổng quát $C_n^k{a^{n – k}}{b^k}.$

+ Dùng các công thức lũy thừa chuyển số hạng tổng quát dưới dạng $A.{x^{f(k)}}$ (với $x$ là ẩn).

+ Đối chiếu với giả thiết giải phương trình $f(k) = h$, tìm $k$ tương ứng.

+ Suy ra hệ số cần tìm.

Lưu ý: Một số tính chất của lũy thừa:

${a^m}.{a^n} = {a^{m + n}}.$

$\frac{{{a^m}}}{{{a^n}}} = {a^{m – n}}.$

${\left( {{a^m}} \right)^n} = {a^{m.n}}.$

${(ab)^m} = {a^m}.{b^m}.$

${\left( {\frac{a}{b}} \right)^m} = \frac{{{a^m}}}{{{b^m}}}.$

$\frac{1}{{{a^n}}} = {a^{ – n}}.$

$\sqrt[m]{{{a^n}}} = {a^{\frac{n}{m}}}.$

$\sqrt[m]{{\sqrt[n]{a}}} = \sqrt[{mn}]{a}.$

## Bài tập

## Bài 1: Tìm hệ số của ${x^{31}}$ trong khai triển ${\left( {x + \frac{1}{{{x^2}}}} \right)^{40}}.$

Lời giải:

Ta có: ${\left( {x + \frac{1}{{{x^2}}}} \right)^{40}}$ $= \sum\limits_{k = 0}^{40} {C_{40}^k} {x^k}{\left( {\frac{1}{{{x^2}}}} \right)^{40 – k}}$ $= \sum\limits_{k = 0}^{40} {C_{40}^k} {x^{3k – 80}}.$

Số hạng tổng quát trong khai triển là: $C_{40}^k{x^{3k – 80}}.$

Để có hệ số của ${x^{31}}$ thì $3k – 80 = 31$ $\Leftrightarrow k = 37.$

Vậy hệ số của ${x^{31}}$ là: $C_{40}^{37} = 9880.$

## Bài 2: Tìm hệ số không chứa $x$ của khai triển nhị thức Newton của ${\left( {\sqrt[3]{x} + \frac{1}{{\sqrt[4]{x}}}} \right)^7}$ với $x > 0.$

Lời giải:

Ta có: ${\left( {\sqrt[3]{x} + \frac{1}{{\sqrt[4]{x}}}} \right)^7}$ $= \sum\limits_{k = 0}^7 {C_7^k} {(\sqrt[3]{x})^{7 – k}}{\left( {\frac{1}{{\sqrt[4]{x}}}} \right)^k}$ $= \sum\limits_{k = 0}^7 {C_7^k} {x^{\frac{{7 – k}}{3}}}.\frac{1}{{{x^{\frac{k}{4}}}}}$ $= \sum\limits_{k = 0}^7 {C_7^k} {x^{\frac{{28 – 7k}}{{12}}}}.$

Số hạng tổng quát trong khai triển là: $C_7^k{x^{\frac{{28 – 7k}}{{12}}}}.$

Để có số hạng không chứa $x$ thì $\frac{{28 – 7k}}{{12}} = 0$ $\Leftrightarrow k = 4.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_7^4 = 35.$

## Bài 3: Tìm hệ số của ${x^{29}}{y^8}$ trong khai triển ${\left( {{x^3} – xy} \right)^{15}}.$

Lời giải:

Ta có: ${\left( {{x^3} – xy} \right)^{15}}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {\left( {{x^3}} \right)^{15 – k}}.{( – xy)^k}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} .{( – 1)^k}.{x^{45 – 2k}}.{y^k}.$

Số hạng tổng quát trong khai triển là: $C_{15}^k.{( – 1)^k}.{x^{45 – 2k}}.{y^k}.$

Hệ số của ${x^{29}}{y^8}$ là: $C_{15}^k.{( – 1)^k}$ với $k$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{45 – 2k = 29}\\
{k = 8}
\end{array}} \right.
$$
 $\Leftrightarrow k = 8.$

Vậy hệ số của ${x^{29}}{y^8}$ trong khai triển là: $C_{15}^8.{( – 1)^8} = 6435.$

## Bài 4: Tìm hệ số không chứa $x$ trong khai triển: ${\left( {2x + \frac{1}{{\sqrt[5]{x}}}} \right)^{18}}$ $(x > 0).$

Lời giải:

Ta có: ${\left( {2x + \frac{1}{{\sqrt[5]{x}}}} \right)^{18}}$ $= {\left( {2x + {x^{ – \frac{1}{5}}}} \right)^{18}}$ $= \sum\limits_{k = 0}^{18} {C_{18}^k} {(2x)^{18 – k}}{\left( {{x^{ – \frac{1}{5}}}} \right)^k}$ $= \sum\limits_{k = 0}^{18} {C_{18}^k} {.2^{18 – k}}.{x^{\frac{{90 – 6k}}{5}}}.$

Số hạng tổng quát trong khai triển là: $C_{18}^k{.2^{18 – k}}.{x^{\frac{{90 – 6k}}{5}}}.$

Hệ số của số hạng không chứa $x$ trong khai triển là: $C_{18}^k{.2^{18 – k}}$ với $k$ thỏa mãn: $\frac{{90 – 6k}}{5} = 0$ $\Leftrightarrow k = 15.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{18}^{15}{.2^3} = 6528.$

## Bài 5: Tìm hệ số không chứa $x$ trong khai triển: ${\left( {\frac{1}{{\sqrt[3]{{{x^2}}}}} + \sqrt[4]{{{x^3}}}} \right)^{17}}$ với $x \ne 0.$

Lời giải:

Số hạng tổng quát trong khai triển là: $C_{17}^k{\left( {{x^{ – \frac{2}{3}}}} \right)^{17 – k}}{\left( {{x^{\frac{3}{4}}}} \right)^k}$ $= C_{17}^k{x^{\frac{{17}}{{16}}k – \frac{{17}}{2}}}$ với 
$$
\left\{ {\begin{array}{l}
{k \in N}\\
{k \le 17}
\end{array}} \right..
$$

Để có số hạng không chứa $x$ thì: $\frac{{17}}{{16}}k – \frac{{17}}{2} = 0$ $\Leftrightarrow k = 8.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{17}^8 = 24310.$

## Bài 6: Tìm hệ số của số hạng chứa ${x^8}$ trong khai triển ${\left( {\frac{1}{{{x^3}}} + \sqrt {{x^5}} } \right)^{12}}.$

Lời giải:

Ta có: ${\left( {\frac{1}{{{x^3}}} + \sqrt {{x^5}} } \right)^{12}}$ $= {\left( {{x^{ – 3}} + {x^{\frac{5}{2}}}} \right)^{12}}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {\left( {{x^{ – 3}}} \right)^{12 – k}}{\left( {{x^{\frac{5}{2}}}} \right)^k}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {x^{\frac{{ – 72 + 11k}}{2}}}.$

Số hạng tổng quát trong khai triển là: $C_{12}^k{x^{\frac{{ – 72 + 11k}}{2}}}.$

Hệ số của số hạng chứa ${x^8}$ là $C_{12}^k$ với $k$ thỏa mãn $\frac{{ – 72 + 11k}}{2} = 8$ $\Leftrightarrow k = 8.$

Vậy hệ số của số hạng chứa ${x^8}$ trong khai triển là: $C_{12}^8 = 495.$

## Bài 7: Tìm số hạng không chứa $x$ trong khai triển: ${\left( {2{x^3} + \frac{1}{{{x^2}}}} \right)^{10}}.$

Lời giải:

Ta có: ${\left( {2{x^3} + \frac{1}{{{x^2}}}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {2{x^3}} \right)^{10 – k}}{\left( {\frac{1}{{{x^2}}}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {2^{10 – k}}{x^{30 – 5k}}.$

Số hạng tổng quát trong khai triển là: $C_{10}^k{2^{10 – k}}{x^{30 – 5k}}.$

Số hạng không chứa $x$ trong khai triển là $C_{10}^k{2^{10 – k}}$ với $k$ thỏa mãn $30 – 5k = 0$ $\Leftrightarrow k = 6.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{10}^6{2^4} = 3360.$

## Bài 8: Tìm hệ số của số hạng chứa ${x^7}$ trong khai triển ${\left( {x + \frac{1}{x}} \right)^{15}}.$

Lời giải:

Ta có: ${\left( {x + \frac{1}{x}} \right)^{15}}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {x^{15 – k}}{\left( {\frac{1}{x}} \right)^k}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {x^{15 – 2k}}.$

Số hạng tổng quát trong khai triển là: $C_{15}^k{x^{15 – 2k}}.$

Hệ số của số hạng chứa ${x^7}$ là $C_{15}^k$ với $k$ thỏa mãn $15 – 2k = 7$ $\Leftrightarrow k = 4.$

Vậy hệ số của số hạng chứa ${x^7}$ trong khai triển là: $C_{15}^4 = 1365.$

## Bài 9: Tìm số hạng không chứa $x$ trong khai triển: ${\left( {2x – \frac{1}{x}} \right)^{10}}.$

Lời giải:

Ta có: $= {\left( {2x – \frac{1}{x}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {(2x)^{10 – k}}{\left( { – \frac{1}{x}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {(2)^{10 – k}}{( – 1)^k}{x^{10 – 2k}}.$

Số hạng tổng quát trong khai triển là: $C_{10}^k{(2)^{10 – k}}{( – 1)^k}{x^{10 – 2k}}.$

Để có số hạng không chứa $x$ thì $10 – 2k = 0$ $\Leftrightarrow k = 5.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{10}^5{(2)^5}{( – 1)^5} = – 8064.$

## Bài 10: Tìm hệ số của ${x^{16}}$ trong khai triển: ${\left( {{x^2} – 2x} \right)^{10}}.$

Lời giải:

Ta có: ${\left( {{x^2} – 2x} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {{x^2}} \right)^{10 – k}}{( – 2x)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {( – 2)^k}{x^{20 – k}}.$

Số hạng tổng quát trong khai triển là: $C_{10}^k{( – 2)^k}{x^{20 – k}}.$

Hệ số của ${x^{16}}$ là $C_{10}^k{( – 2)^k}$ với $k$ thỏa mãn $20 – k = 16$ $\Leftrightarrow k = 4.$

Vậy hệ số của ${x^{16}}$ trong khai triển: $C_{10}^4{( – 2)^4} = 3360.$

## Bài 11: Tìm hệ số của ${x^{25}}{y^{10}}$ trong khai triển: ${\left( {{x^3} + xy} \right)^{15}}.$

Lời giải:

Ta có: ${\left( {{x^3} + xy} \right)^{15}}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {\left( {{x^3}} \right)^{15 – k}}{(xy)^k}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {x^{45 – 2k}}{y^k}.$

Số hạng tổng quát trong khai triển là: $C_{15}^k{x^{45 – 2k}}{y^k}.$

Hệ số của ${x^{25}}{y^{10}}$ là $C_{15}^k$ với $k$ thỏa mãn 
$$
\left\{ {\begin{array}{l}
{45 – 2k = 25}\\
{k = 10}
\end{array}} \right.
$$
 $\Leftrightarrow k = 10.$

Vậy hệ số của ${x^{25}}{y^{10}}$ trong khai triển là: $C_{15}^{10} = 3003.$

## Bài 12: Tìm hệ số của số hạng chứa ${x^8}$ trong khai triển của nhị thức Newton: ${\left( {x – \frac{2}{{{x^2}}}} \right)^{20}}.$

Lời giải:

Ta có: ${\left( {x – \frac{2}{{{x^2}}}} \right)^{20}}$ $= \sum\limits_{k = 0}^{20} {C_{20}^k} {x^{20 – k}}{\left( { – \frac{2}{x}} \right)^k}$ $= \sum\limits_{k = 0}^{20} {C_{20}^k} {( – 2)^k}{x^{20 – 2k}}.$

Số hạng tổng quát trong khai triển là: $C_{20}^k{( – 2)^k}{x^{20 – 2k}}.$

Hệ số của số hạng chứa ${x^8}$ trong khai triển là: $C_{20}^k{( – 2)^k}$ với $k$ thỏa mãn: $20 – 2k = 8$ $\Leftrightarrow k = 6.$

Vậy hệ số của số hạng chứa ${x^8}$ là: $C_{20}^6{( – 2)^6} = 2480640.$

## Bài 13: Tìm hệ số của ${x^8}$ trong khai triển thành đa thức của ${\left[ {1 + {x^2}(1 – x)} \right]^8}.$

Lời giải:

Ta có: ${\left[ {1 + {x^2}(1 – x)} \right]^8}$ $= C_8^0 + C_8^1{x^2}(1 – x)$ $+ C_8^2{x^4}{(1 – x)^2} + C_8^3{x^6}{(1 – x)^3}$ $+ C_8^4{x^8}{(1 – x)^4} + C_8^5{x^{10}}{(1 – x)^5}$ $+ C_8^6{x^{12}}{(1 – x)^6} + C_8^7{x^{14}}{(1 – x)^7}$ $+ C_8^8{x^{16}}{(1 – x)^8}.$

Nhận xét:

Bậc của $x$ trong $3$ số hạng đầu luôn nhỏ hơn $8.$

Bậc của $x$ trong $4$ số hạng cuối luôn lớn hơn $8.$

Do đó ${x^8}$ chỉ có trong số hạng thứ tư và thứ năm.

Xét trong khai triển $C_8^3{x^6}{(1 – x)^3}$ thì hệ số của ${x^8}$ là: $C_8^3.C_3^2.$

Xét trong khai triển $C_8^4{x^8}{(1 – x)^4}$ thì hệ số của ${x^8}$ là: $C_8^4.C_4^0.$

Vậy hệ số của ${x^8}$ trong khai triển ${\left[ {1 + {x^2}(1 – x)} \right]^8}$ là: $C_8^3.C_3^2 + C_8^4.C_4^0 = 238.$

## Bài 14: Tìm hệ số của ${x^5}$ trong khai triển ${(x + 1)^4} + {(x + 1)^5} + {(x + 1)^6} + {(x + 1)^7}.$

Lời giải:

Hệ số của ${x^5}$ trong khai triển là tổng hệ số của ${x^5}$ trong từng khai triển ${(x + 1)^i}$, $i = \overline {4…7} .$

Nhận xét rằng trong khai triển ${(x + 1)^4}$ không chứa ${x^5}.$ Ta có:

${(x + 1)^5} + {(x + 1)^6} + {(x + 1)^7}$ $= \sum\limits_{{k_1} = 0}^5 {C_5^{{k_1}}} {x^{{k_1}}}$ $+ \sum\limits_{{k_2} = 0}^6 {C_6^{{k_2}}} {x^{{k_2}}}$ $+ \sum\limits_{{k_3} = 0}^7 {C_7^{{k_3}}} {x^{{k_3}}}.$

Chọn ${k_1} = {k_2} = {k_3} = 5$ ta được hệ số của ${x^5}$ trong khai triển là: $C_5^5 + C_6^5 + C_7^5 = 28.$

## Bài 15: Cho đa thức $P(x) = {(1 + x)^9} + {(1 + x)^{10}}$ $+ {(1 + x)^{11}} + \ldots + {(1 + x)^{14}}$ có dạng khai triển là: $P(x) = {a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_{14}}{x^{14}}.$ Hãy tính hệ số ${a_9}.$

Lời giải:

Để tính hệ số ${a_9}$ là hệ số của ${x^9}$ ta tính hệ số ${a_9}$ trong từng nhị thức của $P(x)$ rồi tính tổng của chúng.

Xét khai triển ${(1 + x)^9} = \sum\limits_{k = 0}^9 {C_9^k} {x^k}.$

Hệ số của ${x^9}$ trong khai triển trên tương ứng $k = 9$ là $C_9^9.$

Xét khai triển ${(1 + x)^{10}} = \sum\limits_{k = 0}^{10} {C_{10}^k} {x^k}.$

Hệ số của ${x^9}$ trong khai triển trên tương ứng $k = 9$ là $C_{10}^9.$

Thực hiện tương tự cho các nhị thức còn lại trong $P(x)$ ta được:

${a_9} = C_9^9 + C_{10}^9 + C_{11}^9 + C_{12}^9 + C_{13}^9 + C_{14}^9 = 3003.$

## Bài 16: Cho $A = {\left( {x – \frac{1}{{{x^2}}}} \right)^{20}} + {\left( {{x^3} – \frac{1}{x}} \right)^{10}}.$ Sau khi khai triển và rút gọn thì biểu thức $A$ gồm bao nhiêu số hạng?

Lời giải:

Ta có: $A = {\left( {x – \frac{1}{{{x^2}}}} \right)^{20}} + {\left( {{x^3} – \frac{1}{x}} \right)^{10}}$ $= \sum\limits_{k = 0}^{20} {{{( – 1)}^k}} C_{20}^k{x^{20 – k}}{\left( {{x^{ – 2}}} \right)^k}$ $+ \sum\limits_{h = 0}^{10} {{{( – 1)}^h}} C_{10}^h{\left( {{x^3}} \right)^{10 – h}}{\left( {{x^{ – 1}}} \right)^h}.$

$= \sum\limits_{k = 0}^{20} {{{( – 1)}^k}} C_{20}^k{x^{20 – 3k}}$ $+ \sum\limits_{h = 0}^{10} {{{( – 1)}^h}} C_{10}^h{x^{30 – 4h}}.$

Trong khai triển ${\left( {x – \frac{1}{{{x^2}}}} \right)^{20}}$ có $21$ số hạng và khai triển ${\left( {{x^3} – \frac{1}{x}} \right)^{10}}$ có $11$ số hạng.

Xét trường hợp $20 – 3k = 30 – 4h$ $\Leftrightarrow 4h – 10 = 3k.$

Vì 
$$
\left\{ {\begin{array}{l}
{k \in N}\\
{h \in N}
\end{array}} \right.
$$
 suy ra: $4h – 10$ phải chia hết cho $3.$

Mặt khác $0 \le h \le 10$, suy ra: $h = 4$, $h = 7$, $h = 10.$

Suy ra trong hai khai triển của ${\left( {x – \frac{1}{{{x^2}}}} \right)^{20}}$ và ${\left( {{x^3} – \frac{1}{x}} \right)^{10}}$ có $3$ số hạng có lũy thừa của $x$ giống nhau.

Vì vậy sau khi khai triển và rút gọn thì biểu thức $A$ gồm có: $21 + 11 – 3 = 29$ số hạng.

## Bài 17: Tìm hệ số của ${x^5}$ trong khai triển thành đa thức của: $x{(1 – 2x)^5} + {x^2}{(1 + 3x)^{10}}.$

Lời giải:

Hệ số của ${x^5}$ trong khai triển $x{(1 – 2x)^5} + {x^2}{(1 + 3x)^{10}}$ bằng tổng hệ số chứa ${x^5}$ trong khai triển $x{(1 – 2x)^5}$ và ${x^2}{(1 + 3x)^{10}}.$

Xét khai triển: $x{(1 – 2x)^5}$ $= x.\sum\limits_{k = 0}^5 {C_5^k} {( – 2x)^k}$ $= \sum\limits_{k = 0}^5 {C_5^k} {( – 2)^k}{x^{k + 1}}.$

Số hạng tổng quát trong khai triển là: $C_5^k{( – 2)^k}{x^{k + 1}}.$

Chọn $k = 4$ ta được hệ số của ${x^5}$ là: $C_5^4{( – 2)^4} = 80.$

Xét khai triển ${x^2}{(1 + 3x)^{10}}$ $= {x^2}\sum\limits_{h = 0}^{10} {C_{10}^h} {(3x)^h}$ $= \sum\limits_{h = 0}^{10} {C_{10}^h} {3^h}{x^{h + 2}}.$

Số hạng tổng quát trong khai triển là: $C_{10}^h{3^h}{x^{h + 2}}.$

Chọn $h=3$, ta được hệ số của ${x^5}$ là: $C_{10}^3{3^3} = 3240.$

Vậy hệ số của ${x^5}$ trong khai triển $x{(1 – 2x)^5} + {x^2}{(1 + 3x)^{10}}$ là: $80 + 3240 = 3320.$

## Bài 18: Tìm số hạng không chứa $x$ trong khai triển nhị thức: ${\left( {\frac{x}{{\sqrt[5]{x}}} + {x^{\frac{{ – 28}}{{25}}}}} \right)^{12}}.$

Lời giải:

Ta có: ${\left( {\frac{x}{{\sqrt[5]{x}}} + {x^{\frac{{ – 28}}{{25}}}}} \right)^{12}}$ $= {\left( {{x^{\frac{4}{5}}} + {x^{\frac{{ – 28}}{{25}}}}} \right)^{12}}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {\left( {{x^{\frac{4}{5}}}} \right)^{12 – k}}{\left( {{x^{\frac{{ – 28}}{{25}}}}} \right)^k}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {x^{\frac{{240 – 48k}}{{25}}}}.$

Số hạng tổng quát trong khai triển là: $C_{12}^k{x^{\frac{{240 – 48k}}{{25}}}}.$

Số hạng không chứa $x$ trong khai triển là $C_{12}^k$ với $k$ thỏa mãn:

$\frac{{240 – 48k}}{{25}} = 0$ $\Leftrightarrow k = 5.$

Vậy số hạng không chứa $x$ trong khai triển là: $C_{12}^k = 729.$

## Bài 19: Gọi ${a_0}$, ${a_1}$, ${a_2}$, …, ${a_{11}}$ là hệ số trong khai triển: ${(x + 1)^{10}}(x + 2)$ $= {x^{11}} + {a_1}{x^{10}} + {a_2}{x^9} + \ldots . + {a_{10}}x + {a_{11}}.$ Tìm hệ số của ${a_5}.$

Lời giải:

Ta có: ${(x + 1)^{10}}(x + 2)$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{10 – k}}(x + 2)$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{11 – k}} + \sum\limits_{k = 0}^{10} 2 C_{10}^k{x^{10 – k}}.$

Ta có hệ số ${a_5}$ chính là hệ số của ${x^6}$ trong khai triển.

Xét tổng: $\sum\limits_{k = 0}^{10} {C_{10}^k} {x^{11 – k}}$ có số hạng tổng quát là: $C_{10}^k{x^{11 – k}}.$

Chọn $k = 5$, ta được hệ số của số hạng chứa ${x^6}$ là: $C_{10}^5.$

Xét tổng: $\sum\limits_{k = 0}^{10} 2 C_{10}^k{x^{10 – k}}$ có số hạng tổng quát là: $2C_{10}^k{x^{10 – k}}.$

Chọn $k = 4$, ta được hệ số của số hạng chứa ${x^6}$ là: $2C_{10}^4.$

Vậy ${a_5} = C_{10}^5 + 2C_{10}^4 = 672.$

## Bài 20: Tìm hệ số của số hạng thứ tư trong khai triển ${\left( {x + \frac{1}{x}} \right)^{10}}.$

Lời giải:

Ta có: ${\left( {x + \frac{1}{x}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{10 – k}}{\left( {\frac{1}{x}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{10 – 2k}}.$

Số hạng thứ $k +1$ trong khai triển là: ${T_{k + 1}} = C_{10}^k{x^{10 – 2k}}.$

Chọn $k = 3$, ta được hệ số của số hạng thứ tư trong khai triển đó là: $C_{10}^3 = 120.$

## Bài 21: Tìm hệ số của số hạng thứ $31$ trong khai triển ${\left( {x + \frac{1}{{{x^2}}}} \right)^{40}}.$

Lời giải:

Ta có: ${\left( {x + \frac{1}{{{x^2}}}} \right)^{40}}$ $= \sum\limits_{k = 0}^{40} {C_{40}^k} {x^{40 – k}}{\left( {\frac{1}{{{x^2}}}} \right)^k}$ $= \sum\limits_{k = 0}^{40} {C_{40}^k} {x^{40 – 3k}}.$

Số hạng thứ $k +1$ trong khai triển là: ${T_{k + 1}} = C_{40}^k{x^{40 – 3k}}.$

Chọn $k = 30$, ta được hệ số của số hạng thứ $31$ trong khai triển là:

$C_{40}^{30} = 847660528.$

## Bài 22: Tìm hạng tử chứa ${x^2}$ trong khai triển ${\left( {\sqrt[3]{{{x^{ – 2}}}} + x} \right)^7}.$

Lời giải:

Ta có: ${\left( {\sqrt[3]{{{x^{ – 2}}}} + x} \right)^7}$ $= {\left( {{x^{ – \frac{2}{3}}} + x} \right)^7}$ $= \sum\limits_{k = 0}^7 {C_7^k} {\left( {{x^{ – \frac{2}{3}}}} \right)^{7 – k}}{x^k}$ $= \sum\limits_{k = 0}^7 {C_7^k} {x^{\frac{{ – 14 + 5k}}{3}}}.$

Số hạng tổng quát trong khai triển là: $C_7^k{x^{\frac{{ – 14 + 5k}}{3}}}.$

Hạng tử chứa ${x^2}$ trong khai triển là $C_7^k{x^{\frac{{ – 14 + 5k}}{3}}}$ với $k$ thỏa mãn:

$\frac{{ – 14 + 5k}}{3} = 2$ $\Leftrightarrow k = 4.$

Vậy hạng tử chứa ${x^2}$ trong khai triển là $C_7^4{x^2} = 35{x^2}.$

## Bài 23: Cho đa thức $P(x) = (1 + x) + 2{(1 + x)^2}$ $+ 3{(1 + x)^3} + \ldots + 20{(1 + x)^{20}}$ được viết dưới dạng: $P(x) = {a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_{20}}{x^{20}}.$ Tìm hệ số ${a_{15}}$?.

Lời giải:

Hệ số ${a_{15}}$ là hệ số của ${x^{15}}$ trong khai triển $P(x).$

Ta nhận thấy ${x^{15}}$ chỉ xuất hiện trong số hạng khai triển thứ $15$ trở đi, tức là trong tổng $15{(1 + x)^{15}}$ $+ 16{(1 + x)^{16}}$ $+ 17{(1 + x)^{17}}$ $+ \ldots + 20{(1 + x)^{20}}.$

Mà $15{(1 + x)^{15}}$ $+ 16{(1 + x)^{16}}$ $+ \ldots + 20{(1 + x)^{20}}$ $= 15\sum\limits_{{k_1} = 0}^{15} {C_{15}^{{k_1}}} {x^{{k_1}}}$ $+ 16\sum\limits_{{k_2} = 0}^{16} {C_{16}^{{k_2}}} {x^{{k_2}}}$ $+ \ldots + 20\sum\limits_{{k_6} = 0}^{20} {C_{20}^{{k_6}}} {x^{{k_6}}}.$

Chọn ${k_1} = {k_2} = {k_3} = \ldots = {k_6}$ ta được hệ số của $x^{15}$ trong khai triển $P(x)$ là:

$15C_{15}^{15} + 16C_{16}^{15}$ $+ 17C_{17}^{15} + \ldots + 20C_{20}^{15}$ $= 400995.$

## Bài 24: Khai triển $P(x) = {(3 + x)^{50}}$ $= {a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_{50}}{x^{50}}.$

a/ Tính hệ số ${a_{46}}.$

b/ Tính tổng $S = {a_0} + {a_1} + {a_2} + \ldots + {a_{50}}.$

Lời giải:

a) Ta có: ${(3 + x)^{50}}$ $= \sum\limits_{k = 0}^{50} {C_{50}^k} {3^{50 – k}}{x^k}$ $(*).$

Ta có: ${a_k} = C_{50}^k{3^{50 – k}}$, $\forall k = \overline {0..50} .$

Suy ra: ${a_{46}} = C_{50}^{46}{3^4} = 18654300.$

b) Nhận thấy $S = {a_0} + {a_1} + {a_2} + \ldots + {a_{50}}$ $= \sum\limits_{k = 0}^{50} {C_{50}^k} {3^{50 – k}}.$

Từ $(*)$ chọn $x= 1$, ta được: ${(3 + 1)^{50}}$ $= \sum\limits_{k = 0}^{50} {C_{50}^k} {3^{50 – k}}$ $\Leftrightarrow \sum\limits_{k = 0}^{50} {C_{50}^k} {3^{50 – k}} = {4^{50}}.$

Vậy $S = {a_0} + {a_1} + {a_2} + \ldots + {a_{50}} = {4^{50}}.$

## Bài 25:

a/ Tìm số hạng của khai triển ${\left( {\sqrt 3 + \sqrt[3]{2}} \right)^9}$ là một số nguyên.

b/ Tìm số hạng hữu tỉ của khai triển ${\left( {\sqrt 3 – \sqrt {15} } \right)^6}.$

c/ Xác định các số hạng hữu tỉ của khai triển ${\left( {\sqrt[5]{3} + \sqrt[3]{7}} \right)^{36}}.$

d/ Có bao nhiêu hạng tử nguyên của khai triển ${\left( {\sqrt 3 + \sqrt[4]{5}} \right)^{124}}.$

Lời giải:

a) Ta có: ${\left( {\sqrt 3 + \sqrt[3]{2}} \right)^9}$ $= {\left( {{3^{\frac{1}{2}}} + {2^{\frac{1}{3}}}} \right)^9}$ $= \sum\limits_{k = 0}^9 {C_9^k} {\left( {{3^{\frac{1}{2}}}} \right)^{9 – k}}{\left( {{2^{\frac{1}{3}}}} \right)^k}$ $= \sum\limits_{k = 0}^9 {C_9^k} {(3)^{\frac{{9 – k}}{2}}}{(2)^{\frac{k}{3}}}.$

Số hạng tổng quát trong khai triển là: $C_9^k{(3)^{\frac{{9 – k}}{2}}}{(2)^{\frac{k}{3}}}.$

Số hạng nguyên trong khai triển là số hạng có $k$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{9 – k \vdots 2}\\
{k \vdots 3}\\
{k = \overline {0..9} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k = 3}\\
{k = 9}
\end{array}} \right..
$$

Vậy các số hạng nguyên trong khai triển là: ${T_4} = C_9^3{.3^3}.2 = 4536$, ${T_{10}} = C_9^9{2^3} = 8.$

b) Ta có: ${\left( {\sqrt 3 – \sqrt {15} } \right)^6}$ $= {3^3}{\left( {1 – \sqrt 5 } \right)^6}$ $= \sum\limits_{k = 0}^6 2 7C_6^k{( – 1)^k}{.5^{\frac{k}{2}}}.$

Số hạng tổng quát trong khai triển là: $27C_6^k{( – 1)^k}{.5^{\frac{k}{2}}}.$

Để có số hạng hữu tỷ thì ${5^{\frac{k}{2}}}$ là số hữu tỷ, suy ra: 
$$
\left\{ {\begin{array}{l}
{k \vdots 2}\\
{k = \overline {0..6} }
\end{array}} \right.
$$
 $\Leftrightarrow k \in \{ 0;2;4;6\} .$

Vậy các số hạng hữu tỷ là: ${T_1} = 27C_6^0 = 27$, ${T_3} = 27C_6^2.{( – 1)^2}.5 = 810$, ${T_5} = 27C_6^4{( – 1)^4}{.5^2} = 10125$, ${T_7} = 27C_6^6{( – 1)^6}{.5^3} = 3375.$

c) Ta có: ${\left( {\sqrt[5]{3} + \sqrt[3]{7}} \right)^{36}}$ $= {\left( {{3^{\frac{1}{5}}} + {7^{\frac{1}{3}}}} \right)^{36}}$ $= \sum\limits_{k = 0}^{36} {C_{36}^k} {3^{\frac{{36 – k}}{5}}}{.7^{\frac{k}{3}}}.$

Số hạng tổng quát trong khai triển là: $C_{36}^k{3^{\frac{{36 – k}}{5}}}{.7^{\frac{k}{3}}}.$

Số hạng hữu tỷ trong khai triển là số hạng chứa $k$ thỏa mãn điều kiện: 
$$
\left\{ {\begin{array}{l}
{36 – k \vdots 5}\\
{k \vdots 3}\\
{k = \overline {0..36} }
\end{array}} \right.
$$
 $\Leftrightarrow k \in \{ 6;21;36\} .$

Vậy các số hạng hữu tỷ trong khai triển là: ${T_7} = C_{36}^6{3^6}{7^2}$, ${T_{22}} = C_{36}^{21}{3^3}{7^7}$, ${T_{37}} = C_{36}^{36}{7^{12}}.$

d) Ta có: ${\left( {\sqrt 3 + \sqrt[4]{5}} \right)^{124}}$ $= {\left( {{3^{\frac{1}{2}}} + {5^{\frac{1}{4}}}} \right)^{124}}$ $= \sum\limits_{k = 0}^{124} {C_{124}^k} {.3^{\frac{{124 – k}}{2}}}{.5^{\frac{k}{4}}}.$

Số hạng tổng quát trong khai triển là: $C_{124}^k{.3^{\frac{{124 – k}}{2}}}{.5^{\frac{k}{4}}}.$

Số hạng nguyên trong khai triển thỏa mãn điều kiện:

$$
\left\{ {\begin{array}{l}
{124 – k \vdots 2}\\
{k \vdots 4}\\
{k = \overline {0..124} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{k = 4h}\\
{k = \overline {0..124} }\\
{h \in N}
\end{array}} \right.
$$
 $\Leftrightarrow 0 \le 4h \le 124$ $\Leftrightarrow 0 \le h \le 31.$

Vậy có $32$ số hạng nguyên trong khai triển.