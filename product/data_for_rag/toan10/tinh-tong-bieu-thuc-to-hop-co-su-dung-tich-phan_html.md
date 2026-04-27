# Tính tổng biểu thức tổ hợp có sử dụng tích phân

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tinh-tong-bieu-thuc-to-hop-co-su-dung-tich-phan.html -->
Ngoài những ứng dụng của tích phân để tính diện tích và thể tích mà chúng ta đã được tìm hiểu trong chương trình Giải tích 12, thì tích phân còn có nhiều ứng dụng quan trọng khác trong giải toán; bài viết dưới đây trình bày ứng dụng của tích phân để tính tổng biểu thức tổ hợp.

1. PHƯƠNG PHÁP VÀ DẤU HIỆU

Phương pháp chung:

+ Xét khai triển $f(x) = {(a \pm bx)^n}.$

+ Tính tích phân hai vế của khai triển với các cận được chọn thích hợp.

+ Chọn $a$, $b$, $x$ thích hợp.

Dấu hiệu nhận biết:

+ Xuất hiện số hạng tổng quát dạng: $\frac{{C_n^k}}{{k + 1}}$ hoặc $\frac{{C_n^k}}{{(n – k + 1)}}$ thì tích phân thường có dạng: $\int_0^1 f (x)dx.$

+ Xuất hiện số hạng tổng quát dạng: $\frac{{C_n^k\left( {{\alpha ^k} – {\beta ^k}} \right)}}{{k + 1}}$ hoặc $\frac{{C_n^k\left( {{\alpha ^k} – {\beta ^k}} \right)}}{{(n – k + 1)}}$ thì tích phân thường có dạng: $\int_\beta ^\alpha f (x)dx.$

Lưu ý: Ngoài việc tính tích phân của khai triển $f(x) = {(a \pm bx)^n}$ thì một số bài toán còn nhân thêm $2$ vế của khai triển với một đại lượng $g(x)$ nào đó. Trong trường hợp này ta nên xem xét sự chênh lệch giữa $k$ ở $C_n^k$ và mẫu $h$ ở $\frac{{C_n^k}}{h}$ mà nhân thêm hoặc chia bớt đi thích hợp.

## Bài tập

## Bài 1: Chứng minh rằng: $\frac{1}{2}C_{2n}^1 + \frac{1}{4}C_{2n}^3$ $+ \frac{1}{6}C_{2n}^5 + … + \frac{1}{{2n}}C_{2n}^{2n – 1}$ $= \frac{{{2^{2n}} – 1}}{{2n + 1}}$ (với $n \in Z_ + ^*$).

Lời giải:

Ta có: ${(1 + x)^{2n}}$ $= C_{2n}^0 + C_{2n}^1x$ $+ C_{2n}^2{x^2} + C_{2n}^3{x^3}$ $+ \ldots + C_{2n}^{2n}{x^{2n}}$ $(1).$

${(1 – x)^{2n}}$ $= C_{2n}^0 – C_{2n}^1x$ $+ C_{2n}^2{x^2} – C_{2n}^3{x^3}$ $+ \ldots + C_{2n}^{2n}{x^{2n}}$ $(2).$

Xét hàm số: $f(x) = \frac{{{{(1 + x)}^{2n}} – {{(1 – x)}^{2n}}}}{2}$ $(3).$

Từ $(1)$, $(2)$ và $(3)$ suy ra: $f(x) = C_{2n}^1x + C_{2n}^3{x^3}$ $+ C_{2n}^5{x^5} + \ldots + C_{2n}^{2n – 1}{x^{2n – 1}}$ $(4).$

Từ $(3)$ ta có: $\int_0^1 f (x)dx$ $= \int_0^1 {\left( {\frac{{{{(1 + x)}^{2n}} – {{(1 – x)}^{2n}}}}{2}} \right)dx}$ $= \left. {\left( {\frac{{{{(1 + x)}^{2n + 1}} + {{(1 – x)}^{2n + 1}}}}{{2(2n + 1)}}} \right)} \right|_0^1$ $= \frac{{{2^{2n + 1}} – 2}}{{2(2n + 1)}}$ $= \frac{{{2^{2n}} – 1}}{{2n + 1}}$ $(5).$

Từ $(4)$ ta có: $\int_0^1 f (x)dx$ $= \int_0^1 {\left( {C_{2n}^1x + C_{2n}^3{x^3} + C_{2n}^5{x^5} + \ldots + C_{2n}^{2n – 1}{x^{2n – 1}}} \right)dx} .$

$= \left. {\left( {C_{2n}^1\frac{{{x^2}}}{2} + C_{2n}^3\frac{{{x^4}}}{4} + C_{2n}^5\frac{{{x^6}}}{6} + \ldots + C_{2n}^{2n – 1}\frac{{{x^{2n}}}}{{2n}}} \right)} \right|_0^1.$

$= \frac{1}{2}C_{2n}^1 + \frac{1}{4}C_{2n}^3 + \frac{1}{6}C_{2n}^5 + \ldots + \frac{1}{{2n}}C_{2n}^{2n – 1}$ $(6).$

Từ $(5)$ và $(6)$ suy ra $\frac{1}{2}C_{2n}^1 + \frac{1}{4}C_{2n}^3$ $+ \frac{1}{6}C_{2n}^5 + … + \frac{1}{{2n}}C_{2n}^{2n – 1}$ $= \frac{{{2^{2n}} – 1}}{{2n + 1}}.$

## Bài 2:

1) Tính tổng $S = C_n^1 – 2C_n^2$ $+ 3C_n^3 – 4C_n^4$ $+ \ldots + {( – 1)^{n – 1}}nC_n^n$ $(n > 2).$

2) Tính tổng $T = C_n^0 + \frac{1}{2}C_n^1$ $+ \frac{1}{3}C_n^2 + \ldots + \frac{1}{{n + 1}}C_n^n.$ Biết rằng $n$ là số nguyên dương thỏa mãn điều kiện: $C_n^n + C_n^{n – 1} + C_n^{n – 2} = 79.$

Lời giải:

1) Xét khai triển ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2}$ $+ \ldots + C_n^n{x^n}.$

Đạo hàm $2$ vế ta được: $n{(1 + x)^{n – 1}}$ $= C_n^1 + 2C_n^2x + 3C_n^3{x^2}$ $+ \ldots + nC_n^n{x^{n – 1}}.$

Chọn $x= -1$ ta được: $0 = C_n^1 – 2C_n^2 + 3C_n^3 – 4C_n^4$ $+ \ldots + {( – 1)^{n – 1}}nC_n^n.$

Vậy $S = 0.$

2) Ta có: ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Suy ra $\int_0^1 {{{(1 + x)}^n}} dx$ $= \int_0^1 {\left( {C_n^0 + C_n^1x + C_n^2{x^2} + C_n^3{x^3} + \ldots + C_n^n{x^n}} \right)dx} .$

$\left. { \Leftrightarrow \frac{{{{(1 + x)}^{n + 1}}}}{{n + 1}}} \right|_0^1$ $= \left. {\left( {C_n^0x + \frac{1}{2}C_n^1{x^2} + \frac{1}{3}C_n^2{x^3} + \ldots + \frac{1}{{n + 1}}C_n^n{x^{n + 1}}} \right)} \right|_0^1.$

$\Leftrightarrow \frac{{{2^{n + 1}} – 1}}{{n + 1}}$ $= C_n^0 + \frac{1}{2}C_n^1 + \frac{1}{3}C_n^2 + \ldots + \frac{1}{{n + 1}}C_n^n.$

Suy ra: $T = \frac{{{2^{n + 1}} – 1}}{{n + 1}}.$

Mặt khác ta có: $C_n^n + C_n^{n – 1} + C_n^{n – 2} = 79.$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{n \ge 2}\\
{n \in N}
\end{array}} \right..
$$

$C_n^n + C_n^{n – 1} + C_n^{n – 2} = 79$ $\Leftrightarrow 1 + \frac{{n!}}{{(n – 1)!}} + \frac{{n!}}{{2!(n – 2)!}} = 79.$

$\Leftrightarrow 1 + n + \frac{{n(n – 1)}}{2} = 79$ $\Leftrightarrow {n^2} + n – 156 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 12}\\
{n = – 13\,\,{\rm{(loại)}}}
\end{array}} \right..
$$

Vậy $T = \frac{{{2^{n + 1}} – 1}}{{n + 1}}$ $= \frac{{{2^{13}} – 1}}{{13}} = \frac{{8191}}{{13}}.$

## Bài 3: Cho $n$ là số nguyên dương. Tính tổng $C_n^0 + \frac{{{2^2} – 1}}{2}C_n^1$ $+ \frac{{{2^3} – 1}}{3}C_n^2 + \ldots + \frac{{{2^{n + 1}} – 1}}{{n + 1}}C_n^n.$

Lời giải:

Xét khai triển ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Suy ra: $\int_1^2 {{{(1 + x)}^n}} dx$ $= \int_1^2 {\left( {C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}} \right)dx.}$

$\left. { \Leftrightarrow \frac{1}{{n + 1}}{{(1 + x)}^{n + 1}}} \right|_1^2$ $= \left. {\left( {C_n^0x + C_n^1\frac{{{x^2}}}{2} + C_n^2\frac{{{x^3}}}{3} + \ldots + C_n^n\frac{{{x^{n + 1}}}}{{n + 1}}} \right)} \right|_1^2.$

$\Leftrightarrow C_n^0 + \frac{{{2^2} – 1}}{2}C_n^1 + \frac{{{2^3} – 1}}{3}C_n^2 + \ldots + \frac{{{2^{n + 1}} – 1}}{{n + 1}}C_n^n$ $= \frac{{{3^{n + 1}} – {2^{n + 1}}}}{{n + 1}}.$

## Bài 4: Với mỗi số tự nhiên $n$, hãy tính tổng $S = C_n^0 + \frac{1}{2}C_n^1.2$ $+ \frac{1}{3}C_n^2{.2^2} + \frac{1}{4}C_n^3{.2^3}$ $+ \ldots + \frac{1}{{n + 1}}C_n^n{.2^n}.$

Lời giải:

Xét khai triển ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Suy ra: $\int_0^2 {{{(1 + x)}^n}} dx$ $= \int_0^2 {\left( {C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}} \right)} .$

$\left. { \Leftrightarrow \frac{{{{(1 + x)}^{n + 1}}}}{{n + 1}}} \right|_0^2$ $= \left. {\left[ {C_n^0x + \frac{{C_n^1{x^2}}}{2} + \frac{{C_n^2{x^3}}}{3} + \ldots + \frac{{C_n^n{x^{n + 1}}}}{{n + 1}}} \right]} \right|_0^2.$

$\Leftrightarrow \frac{{{3^{n + 1}} – 1}}{{n + 1}}$ $= C_n^0.2 + \frac{{C_n^1{{.2}^2}}}{2}$ $+ \frac{{C_n^2{{.2}^3}}}{3} + \ldots + \frac{{C_n^n{{.2}^{n + 1}}}}{{n + 1}}.$

$\Leftrightarrow \frac{{{3^{n + 1}} – 1}}{{n + 1}}$ $= 2.\left( {C_n^0 + \frac{1}{2}C_n^1.2 + \frac{1}{3}C_n^2{{.2}^2} + \frac{1}{4}C_n^3{{.2}^3} + \ldots + \frac{1}{{n + 1}}C_n^n{{.2}^n}} \right).$

$\Leftrightarrow C_n^0 + \frac{1}{2}C_n^1.2$ $+ \frac{1}{3}C_n^2{.2^2} + \frac{1}{4}C_n^3{.2^3}$ $+ \ldots + \frac{1}{{n + 1}}C_n^n{.2^n}$ $= \frac{{{3^{n + 1}} – 1}}{{2(n + 1)}}.$

Vậy $S = \frac{{{3^{n + 1}} – 1}}{{2(n + 1)}}.$

## Bài 5:

1) Tính tích phân: $I = \int_0^1 {{{(x + 2)}^6}} dx.$

2) Tính tổng $S = \frac{{{2^6}}}{1}C_6^0 + \frac{{{2^5}}}{2}C_6^1$ $+ \frac{{{2^4}}}{3}C_6^2 + \frac{{{2^3}}}{4}C_6^3$ $+ \frac{{{2^2}}}{5}C_6^4 + \frac{2}{6}C_6^5 + \frac{1}{7}C_6^6.$

Lời giải:

1) Ta có: $I = \int_0^1 {{{(x + 2)}^6}} dx$ $= \left. {\frac{{{{(x + 2)}^7}}}{7}} \right|_0^1$ $= \frac{{{3^7} – {2^7}}}{7}$ $= \frac{{2059}}{7}$ $(1).$

2) Mặt khác ta có: $I = \int_0^1 {{{(x + 2)}^6}} dx$ $= \int_0^1 {{{(2 + x)}^6}} dx.$

$= \int_0^1 {\left( {C_6^0{2^6} + C_6^1{2^5}x + C_6^2{2^4}{x^2} + C_6^3{2^3}{x^3} + C_6^4{2^2}{x^4} + C_6^52{x^5} + C_6^6{x^6}} \right)dx.}$

$= \left[ {\frac{{{2^6}}}{1}C_6^0x + \frac{{{2^5}}}{2}C_6^1{x^2} + \frac{{{2^4}}}{3}C_6^2{x^3} + \frac{{{2^3}}}{4}C_6^3{x^4} + \frac{{{2^2}}}{5}C_6^4{x^5} + \frac{2}{6}C_6^5{x^6} + \frac{1}{7}C_6^6{x^7}} \right]_0^1.$

$= \frac{{{2^6}}}{1}C_6^0 + \frac{{{2^5}}}{2}C_6^1$ $+ \frac{{{2^4}}}{3}C_6^2 + \frac{{{2^3}}}{4}C_6^3$ $+ \frac{{{2^2}}}{5}C_6^4 + \frac{2}{6}C_6^5 + \frac{1}{7}C_6^6$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $S = \frac{{2059}}{7}.$

## Bài 6: Tính tích phân $I = \int_0^1 x {\left( {1 – {x^2}} \right)^n}dx$ $\left( {n \in {N^*}} \right).$ Từ đó chứng minh rằng: $\frac{1}{2}C_n^0 – \frac{1}{4}C_n^1$ $+ \frac{1}{6}C_n^2 – \frac{1}{8}C_n^3$ $+ \ldots + \frac{{{{( – 1)}^n}}}{{2(n + 1)}}C_n^n$ $= \frac{1}{{2(n + 1)}}.$

Lời giải:

Đặt $t = 1 – {x^2}$ $\Rightarrow dt = – 2xdx$ $\Rightarrow xdx = – \frac{{dt}}{2}.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 1}\\
{x = 1 \Rightarrow t = 0}
\end{array}} \right..
$$

Suy ra: $I = \int_1^0 {\left( { – \frac{1}{2}{t^n}} \right)dt}$ $= \frac{1}{2}\int_0^1 {{t^n}} dt$ $= \left. {\frac{1}{{2(n + 1)}}{t^{n + 1}}} \right|_0^1$ $= \frac{1}{{2(n + 1)}}$ $(1).$

Mặt khác ta có:

$I = \int_0^1 x {\left( {1 – {x^2}} \right)^n}dx$ $= \int_0^1 x \left( {C_n^0 – C_n^1{x^2} + C_n^2{x^4} – C_n^3{x^6} + \ldots + {{( – 1)}^n}C_n^n{x^{2n}}} \right)dx.$

$= \left. {\left( {C_n^0.\frac{{{x^2}}}{2} – C_n^1.\frac{{{x^4}}}{4} + C_n^2.\frac{{{x^6}}}{6} – C_n^3.\frac{{{x^8}}}{8} + \ldots + {{( – 1)}^n}C_n^n.\frac{{{x^{2n + 2}}}}{{2n + 2}}} \right)} \right|_0^1.$

$= \frac{1}{2}C_n^0 – \frac{1}{4}C_n^1$ $+ \frac{1}{6}C_n^2 – \frac{1}{8}C_n^3$ $+ \ldots + \frac{{{{( – 1)}^n}}}{{2(n + 1)}}C_n^n$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\frac{1}{2}C_n^0 – \frac{1}{4}C_n^1$ $+ \frac{1}{6}C_n^2 – \frac{1}{8}C_n^3$ $+ \ldots + \frac{{{{( – 1)}^n}}}{{2(n + 1)}}C_n^n$ $= \frac{1}{{2(n + 1)}}.$

## Bài 7: Tính tổng $S = C_n^0 + \frac{1}{2}C_n^1 + \frac{1}{3}C_n^2 + \ldots + \frac{1}{{n + 1}}C_n^n.$

Lời giải:

Xét khai triển ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Lấy tích phân từ $0$ đến $1$ hai vế ta được:

$\int_0^1 {{{(1 + x)}^n}} dx$ $= \int_0^1 {\left( {C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}} \right)dx.}$

$\left. { \Leftrightarrow \frac{{{{(1 + x)}^{n + 1}}}}{{n + 1}}} \right|_0^1$ $= \left. {\left( {C_n^0x + C_n^1.\frac{{{x^2}}}{2} + C_n^2.\frac{{{x^3}}}{3} + \ldots + C_n^n.\frac{{{x^n}}}{2}} \right)} \right|_0^1.$

$\Leftrightarrow \frac{{{2^{n + 1}} – 1}}{{n + 1}}$ $= C_n^0 + \frac{1}{2}C_n^1 + \frac{1}{3}C_n^2$ $+ \ldots + \frac{1}{{n + 1}}C_n^n.$

Vậy $S = \frac{{{2^{n + 1}} – 1}}{{n + 1}}.$

## Bài 8: Chứng minh đẳng thức sau: $\frac{{{2^6}}}{1}.C_6^0 + \frac{{{2^5}}}{2}.C_6^1$ $+ \frac{{{2^4}}}{3}.C_6^2 + \ldots + \frac{1}{7}.C_6^6$ $= \frac{{{3^7} – {2^7}}}{7}.$

Lời giải:

Xét khai triển: ${(2 + x)^6}$ $= {2^6}C_6^0 + {2^5}xC_6^1$ $+ {2^4}{x^2}C_6^2 + \ldots + {x^6}C_6^6.$

$\Rightarrow \int_0^1 {{{(2 + x)}^6}} dx$ $= \int_0^1 {\left( {{2^6}C_6^0 + {2^5}xC_6^1 + {2^4}{x^2}C_6^2 + \ldots + {x^6}C_6^6} \right)dx.}$

$\left. { \Leftrightarrow \frac{1}{7}{{(2 + x)}^7}} \right|_0^1$ $= \left. {\left( {{2^6}C_6^0x + {2^5}\frac{{{x^2}}}{2}C_6^1 + {2^4}\frac{{{x^3}}}{3}C_6^2 + \ldots + \frac{{{x^7}}}{7}C_6^6} \right)} \right|_0^1.$

$\Leftrightarrow \frac{{{3^7} – {2^7}}}{7}$ $= \frac{{{2^6}}}{1}.C_6^0 + \frac{{{2^5}}}{2}.C_6^1$ $+ \frac{{{2^4}}}{3}.C_6^2 + \ldots + \frac{1}{7}.C_6^6.$

Vậy $\frac{{{2^6}}}{1}.C_6^0 + \frac{{{2^5}}}{2}.C_6^1$ $+ \frac{{{2^4}}}{3}.C_6^2 + \ldots + \frac{1}{7}.C_6^6$ $= \frac{{{3^7} – {2^7}}}{7}.$

## Bài 9:

1) Tính $\int_0^1 {{x^2}} {\left( {1 + {x^3}} \right)^n}dx.$

2) Chứng minh: $\frac{1}{3}C_n^0 + \frac{1}{6}C_n^1 + \frac{1}{9}C_n^2 + \ldots + \frac{1}{{3n + 3}}C_n^n$ $= \frac{{{2^{n + 1}} – 1}}{{3n + 3}}.$

Lời giải:

1) Ta có: $I = \int_0^1 {{x^2}} {\left( {1 + {x^3}} \right)^n}dx$ $= \frac{1}{3}\int_0^1 {{{\left( {1 + {x^3}} \right)}^n}} d\left( {1 + {x^3}} \right)$ $= \left. {\frac{{{{\left( {1 + {x^3}} \right)}^{n + 1}}}}{{3(n + 1)}}} \right|_0^1$ $= \frac{{{2^{n + 1}} – 1}}{{3n + 3}}$ $(1).$

2) Mặt khác ta có: ${x^2}{\left( {1 + {x^3}} \right)^n}$ $= {x^2}\left( {C_n^0 + C_n^1{x^3} + C_n^2{x^6} + \ldots + C_n^n{x^{3n}}} \right)$ $= C_n^0{x^2} + C_n^1{x^5} + C_n^2{x^8} + \ldots + C_n^n{x^{3n + 2}}.$

Suy ra: $I = \int_0^1 {{x^2}} {\left( {1 + {x^3}} \right)^n}dx$ $= \int_0^1 {\left( {C_n^0{x^2} + C_n^1{x^5} + C_n^2{x^8} + \ldots + C_n^n{x^{3n + 2}}} \right)dx} .$

$= \left. {\left( {C_n^0\frac{{{x^3}}}{3} + C_n^1\frac{{{x^6}}}{6} + C_n^2\frac{{{x^9}}}{9} + \ldots + C_n^n\frac{{{x^{3n + 3}}}}{{3n + 3}}} \right)} \right|_0^1.$

$= \frac{1}{3}C_n^0 + \frac{1}{6}C_n^1 + \frac{1}{9}C_n^2$ $+ \ldots + \frac{1}{{3n + 3}}C_n^n$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\frac{1}{3}C_n^0 + \frac{1}{6}C_n^1 + \frac{1}{9}C_n^2$ $+ \ldots + \frac{1}{{3n + 3}}C_n^n$ $= \frac{{{2^{n + 1}} – 1}}{{3n + 3}}.$

## Bài 10: Cho $n$ là số nguyên dương. Chứng minh: $1 + \frac{1}{2}C_n^1 + \frac{1}{3}C_n^2$ $+ \ldots + \frac{1}{{n + 1}}C_n^n$ $= \frac{{{2^{n + 1}} – 1}}{{n + 1}}.$

Lời giải:

Ta có: ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2}$ $+ \ldots + C_n^n{x^n}.$

Suy ra $\int_0^1 {{{(1 + x)}^n}} dx$ $= \int_0^1 {\left( {C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}} \right)dx} .$

$\left. { \Leftrightarrow \frac{{{{(1 + x)}^{n + 1}}}}{{n + 1}}} \right|_0^1$ $= \left. {\left( {C_n^0x + C_n^1\frac{{{x^2}}}{2} + C_n^2\frac{{{x^3}}}{3} + \ldots + C_n^n\frac{{{x^{n + 1}}}}{{n + 1}}} \right)} \right|_0^1.$

$\Leftrightarrow 1 + \frac{1}{2}C_n^1 + \frac{1}{3}C_n^2$ $+ \ldots + \frac{1}{{n + 1}}C_n^n$ $= \frac{{{2^{n + 1}} – 1}}{{n + 1}}.$

## Bài 11: Chứng minh rằng: $2C_n^0 + \frac{{{2^2}}}{2}C_n^1 + \frac{{{2^3}}}{3}C_n^2$ $+ \ldots + \frac{{{2^{n + 1}}}}{{n + 1}}C_n^n$ $= \frac{{{3^{n + 1}} – 1}}{{n + 1}}.$

Lời giải:

Xét khai triển: ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Suy ra: $\int_0^2 {{{(1 + x)}^n}} dx$ $= \int_0^2 {\left( {C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}} \right)dx} .$

$\left. { \Leftrightarrow \frac{{{{(1 + x)}^{n + 1}}}}{{n + 1}}} \right|_0^2$ $= \left. {\left( {C_n^0x + C_n^1\frac{{{x^2}}}{2} + C_n^2\frac{{{x^3}}}{3} + \ldots + C_n^n\frac{{{x^{n + 1}}}}{{n + 1}}} \right)} \right|_0^2.$

$\Leftrightarrow \frac{{{3^{n + 1}} – 1}}{{n + 1}}$ $= 2C_n^0 + \frac{{{2^2}}}{2}C_n^1 + \frac{{{2^3}}}{3}C_n^2 + \ldots + \frac{{{2^{n + 1}}}}{{n + 1}}C_n^n.$

Vậy $2C_n^0 + \frac{{{2^2}}}{2}C_n^1 + \frac{{{2^3}}}{3}C_n^2$ $+ \ldots + \frac{{{2^{n + 1}}}}{{n + 1}}C_n^n$ $= \frac{{{3^{n + 1}} – 1}}{{n + 1}}.$

## Bài 12:

1) Tính tích phân: $\int_0^1 x {(1 – x)^n}dx.$

2) Chứng minh: $\frac{1}{2}C_n^0 – \frac{1}{3}C_n^1 + \frac{1}{4}C_n^2$ $+ \ldots + {( – 1)^n}\frac{1}{{n + 2}}C_n^n$ $= \frac{1}{{(n + 1)(n + 2)}}.$

Lời giải:

1) Đặt $t = 1 – x$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x = 1 – t}\\
{dt = – dx}
\end{array}} \right..
$$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 1}\\
{x = 1 \Rightarrow t = 0}
\end{array}} \right..
$$

Suy ra: $I = \int_0^1 x {(1 – x)^n}dx$ $= \int_1^0 {(1 – t)} {t^n}( – dt)$ $= \int_0^1 {\left( {{t^n} – {t^{n + 1}}} \right)dt}$ $= \left. {\left( {\frac{{{t^{n + 1}}}}{{n + 1}} – \frac{{{t^{n + 2}}}}{{n + 2}}} \right)} \right|_0^1.$

$= \frac{1}{{n + 1}} – \frac{1}{{n + 2}}$ $= \frac{1}{{(n + 1)(n + 2)}}$ $(1).$

2) Mặt khác ta có: ${(1 – x)^n}$ $= C_n^0 – C_n^1x + C_n^2{x^2}$ $+ \ldots + {( – 1)^n}C_n^n{x^n}.$

$\Leftrightarrow x{(1 – x)^n}$ $= C_n^0x – C_n^1{x^2} + C_n^2{x^3}$ $+ \ldots + {( – 1)^n}C_n^n{x^{n + 1}}.$

$\Rightarrow \int_0^1 x {(1 – x)^n}dx$ $= \int_0^1 {\left( {C_n^0x – C_n^1{x^2} + C_n^2{x^3} + \ldots + {{( – 1)}^n}C_n^n{x^{n + 1}}} \right)dx.}$

$= \left. {\left( {C_n^0\frac{{{x^2}}}{2} – C_n^1\frac{{{x^3}}}{3} + C_n^2\frac{{{x^4}}}{4} + \ldots + {{( – 1)}^n}C_n^n\frac{{{x^{n + 2}}}}{{n + 2}}} \right)} \right|_0^1.$

$= \frac{1}{2}C_n^0 – \frac{1}{3}C_n^1 + \frac{1}{4}C_n^2$ $+ \ldots + {( – 1)^n}\frac{1}{{n + 2}}C_n^n$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\frac{1}{2}C_n^0 – \frac{1}{3}C_n^1 + \frac{1}{4}C_n^2$ $+ \ldots + {( – 1)^n}\frac{1}{{n + 2}}C_n^n$ $= \frac{1}{{(n + 1)(n + 2)}}.$

## Bài 13: Chứng minh rằng: $2C_n^0 – \frac{1}{2}{.2^2}C_n^1 + \frac{1}{3}{.2^3}C_n^2$ $– \ldots + {( – 1)^n}{2^{n + 1}}C_n^n$ $= \frac{1}{{n + 1}}\left[ {1 + {{( – 1)}^n}} \right].$

Lời giải:

Xét khai triển: ${(1 – x)^n}$ $= C_n^0 – C_n^1x + C_n^2{x^2}$ $+ \ldots + {( – 1)^n}C_n^n{x^n}.$

Suy ra: $\int_0^2 {{{(1 – x)}^n}} dx$ $= \int_0^2 {\left( {C_n^0 – C_n^1x + C_n^2{x^2} + \ldots + {{( – 1)}^n}C_n^n{x^n}} \right)dx.}$

$\left. { \Leftrightarrow \frac{{{{(1 – x)}^{n + 1}}}}{{ – (n + 1)}}} \right|_0^2$ $= \left. {\left( {C_n^0x – C_n^1\frac{{{x^2}}}{2} + C_n^2\frac{{{x^3}}}{3} + \ldots + {{( – 1)}^n}C_n^n\frac{{{x^{n + 1}}}}{{n + 1}}} \right)} \right|_0^2.$

$\Leftrightarrow \frac{{ – {{( – 1)}^{n + 1}} + {1^{n + 1}}}}{{n + 1}}$ $= 2C_n^0 – \frac{1}{2}{.2^2}C_n^1 + \frac{1}{3}{.2^3}C_n^2$ $– \ldots + {( – 1)^n}{2^{n + 1}}C_n^n.$

$\Leftrightarrow 2C_n^0 – \frac{1}{2}{.2^2}C_n^1 + \frac{1}{3}{.2^3}C_n^2$ $– \ldots + {( – 1)^n}{2^{n + 1}}C_n^n$ $= \frac{1}{{n + 1}}\left[ {1 + {{( – 1)}^n}} \right].$