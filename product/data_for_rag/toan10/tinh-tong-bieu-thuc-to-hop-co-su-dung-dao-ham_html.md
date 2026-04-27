# Tính tổng biểu thức tổ hợp có sử dụng đạo hàm

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tinh-tong-bieu-thuc-to-hop-co-su-dung-dao-ham.html -->
Bài viết hướng dẫn sử dụng đạo hàm để tính tổng biểu thức tổ hợp, đây là dạng toán nâng cao trong chương trình Đại số và Giải tích 11.

1. PHƯƠNG PHÁP VÀ DẤU HIỆU

• Phương pháp chung:

+ Khai triển nhị thức ${(a \pm bx)^n}.$

+ Lấy đạo hàm cấp $1$ hoặc cấp $2$ ….

+ Chọn $a$, $b$, $x$ thích hợp.

• Dấu hiệu nhận biết đạo hàm cấp $1$ (một lần hoặc nhiều lần):

+ Trong mỗi số hạng xuất hiện số hạng tổng quát: $kC_n^k$, không có mặt số hạng $C_n^0$ hoặc $C_n^n.$

+ Nếu xuất hiện ${k^2}C_n^k$ thì sau khi đạo hàm lần $1$ ta nhân $2$ vế với $x$ rồi đạo hàm lần $2$ ….

Nói chung việc nhận thêm đại lượng vào khai triển tùy thuộc vào đại lượng tổng quát mà từ đó có thể suy trực tiếp ra đại lượng cần nhân thêm.

• Dấu hiệu nhận biết đạo hàm cấp $2$:

+ Trong mỗi số hạng xuất hiện số hạng dạng tổng quát $k(k – 1)C_n^k.$

+ Trong tổng không xuất hiện $C_n^0$, $C_n^1$ hoặc $C_n^n$, $C_n^{n – 1}.$

## Bài tập

## Bài 1: Chứng minh rằng: $C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n = n{.2^{n – 1}}$ (với $n$ nguyên dương).

Lời giải:

Xét khai triển nhị thức: ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Đạo hàm hai vế ta được: $n{(1 + x)^{n – 1}}$ $= C_n^1 + 2C_n^2x + 3C_n^3{x^2} + \ldots + nC_n^n{x^{n – 1}}.$

Chọn $x = 1$, ta được: $n{(1 + 1)^{n – 1}}$ $= C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n.$

$\Leftrightarrow C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n$ $= n{.2^{n – 1}}.$

## Bài 2: Tìm số nguyên dương $n$ sao cho:

$C_{2n + 1}^1 – 2.2C_{2n + 1}^2$ $+ {3.2^2}C_{2n + 1}^3 – {4.2^3}C_{2n + 1}^4$ $+ \ldots + (2n + 1){.2^{2n}}C_{2n + 1}^{2n + 1}$ $= 2005.$

Lời giải:

Xét khai triển: ${(1 + x)^{2n + 1}}$ $= C_{2n + 1}^0 + C_{2n + 1}^1x$ $+ C_{2n + 1}^2{x^2} + C_{2n + 1}^3{x^3}$ $+ \ldots + C_{2n + 1}^{2n + 1}{x^{2n + 1}}.$

Đạo hàm hai vế ta được:

$(2n + 1){(1 + x)^{2n}}$ $= C_{2n + 1}^1 + 2C_{2n + 1}^2x$ $+ 3C_{2n + 1}^3{x^2} + \ldots + (2n + 1)C_{2n + 1}^{2n + 1}{x^{2n}}.$

Chọn $x= -2$, ta được:

$(2n + 1){(1 – 2)^{2n}}$ $= C_{2n + 1}^1 – 2.2C_{2n + 1}^2$ $+ {3.2^2}C_{2n + 1}^3$ $– \ldots + (2n + 1){2^{2n}}C_{2n + 1}^{2n + 1}.$

$\Leftrightarrow C_{2n + 1}^1 – 2.2C_{2n + 1}^2$ $+ {3.2^2}C_{2n + 1}^3$ $– \ldots + (2n + 1){2^{2n}}C_{2n + 1}^{2n + 1}$ $= 2n + 1.$

Theo đề bài ta có: $2n + 1 = 2005$ $\Leftrightarrow n = 1002.$

Vậy $n = 1002.$

## Bài 3: Hãy khai triển nhị thức Newton ${(1 – x)^{2n}}$ với $n$ là số nguyên dương. Từ đó chứng minh rằng:

$1C_{2n}^1 + 3C_{2n}^3$ $+ \ldots + (2n – 1)C_{2n}^{2n – 1}$ $= 2C_{2n}^2 + 4C_{2n}^4$ $+ \ldots + 2nC_{2n}^{2n}.$

Lời giải:

Ta có: ${(1 – x)^{2n}}$ $= C_{2n}^0 – C_{2n}^1x$ $+ C_{2n}^2{x^2} – C_{2n}^3{x^3}$ $+ C_{2n}^4{x^4} – \ldots – C_{2n}^{2n – 1}{x^{2n – 1}}$ $+ C_{2n}^{2n}{x^{2n}}.$

Đạo hàm hai vế ta được: $– 2n{(1 – x)^{2n – 1}}$ $= – C_{2n}^1 + 2C_{2n}^2x$ $– 3C_{2n}^3{x^2} + 4C_{2n}^4{x^3}$ $– \ldots – (2n – 1)C_{2n}^{2n – 1}{x^{2n – 2}}$ $+ 2nC_{2n}^{2n}{x^{2n – 1}}.$

Chọn $x = 1$ ta được: $0 = – C_{2n}^1 + 2C_{2n}^2$ $– 3C_{2n}^3 + 4C_{2n}^4$ $– \ldots – (2n – 1)C_{2n}^{2n – 1} + 2nC_{2n}^{2n}$ $\Leftrightarrow 1C_{2n}^1 + 3C_{2n}^3$ $+ \ldots + (2n – 1)C_{2n}^{2n – 1}$ $= 2C_{2n}^2 + 4C_{2n}^4 + \ldots + 2nC_{2n}^{2n}.$

## Bài 4: Tính tổng $S = C_{2000}^0 + 2C_{2000}^1$ $+ 3C_{2000}^2 + \ldots + 2001C_{2000}^{2000}.$

Lời giải:

Cách 1:

Ta có: $S = C_{2000}^0 + 2C_{2000}^1$ $+ 3C_{2000}^2 + \ldots + 2001C_{2000}^{2000}$ $= {S_1} + {S_2}.$

Với:

${S_1} = C_{2000}^0 + C_{2000}^1$ $+ C_{2000}^2 + \ldots + C_{2000}^{2000}.$

${S_2} = C_{2000}^1 + 2C_{2000}^2$ $+ 3C_{2000}^3 + \ldots + 2000C_{2000}^{2000}.$

Xét nhị thức ${(1 + x)^{2000}}$ $= C_{2000}^0 + C_{2000}^1x$ $+ C_{2000}^2{x^2} + \ldots + C_{2000}^{2000}{x^{2000}}.$

Chọn $x = 1$ ta được: ${S_1} = C_{2000}^0 + C_{2000}^1$ $+ C_{2000}^2 + \ldots + C_{2000}^{2000}$ $= {2^{2000}}.$

Xét nhị thức: ${(1 + x)^{2000}}$ $= C_{2000}^0 + C_{2000}^1x$ $+ C_{2000}^2{x^2} + \ldots + C_{2000}^{2000}{x^{2000}}.$

Lấy đạo hàm $2$ vế ta được:

$2000{(1 + x)^{1999}}$ $= C_{2000}^1 + 2C_{2000}^2x$ $+ 3C_{2000}^3{x^2} + \ldots + 2000C_{2000}^{2000}{x^{1999}}.$

Chọn $x = 1$ ta được: ${S_2} = C_{2000}^1 + 2C_{2000}^2$ $+ 3C_{2000}^3 + \ldots + 2000C_{2000}^{2000}.$

$= {2000.2^{1999}}$ $= {1000.2.2^{1999}}$ $= {1000.2^{2000}}.$

Vậy $S = {S_1} + {S_2}$ $= {2^{2000}} + {1000.2^{2000}}$ $= {1001.2^{2000}}.$

Cách 2:

Xét nhị thức: ${(1 + x)^{2000}}$ $= C_{2000}^0 + C_{2000}^1x$ $+ C_{2000}^2{x^2} + \ldots + C_{2000}^{2000}{x^{2000}}.$

Nhân $2$ vế với $x$ ta được:

$x.{(1 + x)^{2000}}$ $= C_{2000}^0x + C_{2000}^1{x^2}$ $+ C_{2000}^2{x^3} + \ldots + C_{2000}^{2000}{x^{2001}}.$

Lấy đạo hàm hai vế ta được:

${(1 + x)^{2000}} + 2000x.{(1 + x)^{1999}}$ $= C_{2000}^0 + 2C_{2000}^1x$ $+ 3C_{2000}^2{x^2} + \ldots + 2001C_{2000}^{2000}{x^{2000}}.$

Chọn $x = 1$ ta được:

$S = C_{2000}^0 + 2C_{2000}^1$ $+ 3C_{2000}^2 + \ldots + 2001C_{2000}^{2000}$ $= {2^{2000}} + {2000.2^{1999}}$ $= {1001.2^{2000}}.$

## Bài 5: Tính tổng: $S = C_n^1 – 2C_n^2$ $+ 3C_n^3 – 4C_n^4$ $+ \ldots + {( – 1)^{n – 1}}nC_n^n.$ Trong đó $n$ là số tự nhiên lớn hơn $2.$

Lời giải:

Xét nhị thức: ${(1 – x)^n}$ $= C_n^0 – C_n^1x$ $+ C_n^2{x^2} + \ldots + C_n^n{( – 1)^n}{x^n}.$

Đạo hàm $2$ vế ta được: $– {(1 – x)^{n – 1}}$ $= – C_n^1 + 2C_n^2x$ $+ \ldots + n.C_n^n{( – 1)^n}{x^{n – 1}}.$

Chọn $x = 1$ ta được: $– {(1 – 1)^{n – 1}}$ $= – C_n^1 + 2C_n^2$ $+ \ldots + n.C_n^n{( – 1)^n}.$

$\Leftrightarrow C_n^1 – 2C_n^2$ $+ 3C_n^3 – 4C_n^4$ $+ \ldots + {( – 1)^{n – 1}}nC_n^n = 0.$

Vậy $S =0.$

## Bài 6: Cho $n$ là số tự nhiên, $n \ge 2.$ Chứng minh đẳng thức sau: ${n^2}C_n^0 + {(n – 1)^2}C_n^1$ $+ {(n – 2)^2}C_n^2$ $+ \ldots + {2^2}C_n^{n – 2} + {1^2}C_n^{n – 1}$ $= n(n + 1){2^{n – 2}}.$

Lời giải:

Xét khai triển: ${(x + 1)^n}$ $= C_n^0{x^n} + C_n^1{x^{n – 1}}$ $+ C_n^2{x^{n – 2}} + \ldots + C_n^{n – 1}{x^1} + C_n^n$ $(1).$

Đạo hàm hai vế của $(1)$ ta được:

$n{(x + 1)^{n – 1}}$ $= nC_n^0{x^{n – 1}} + (n – 1)C_n^1{x^{n – 2}}$ $+ (n – 2)C_n^2{x^{n – 3}} + \ldots + 1.C_n^{n – 1}$ $(2).$

Nhân $2$ vế của $(2)$ với $x$ ta được:

$nx{(x + 1)^{n – 1}}$ $= nC_n^0{x^n} + (n – 1)C_n^1{x^{n – 1}}$ $+ (n – 2)C_n^2{x^{n – 2}} + \ldots + 1.C_n^{n – 1}x$ $(3).$

Đạo hàm hai vế của $(3)$ ta được: $\left[ {n{{(x + 1)}^{n – 1}} + n(n – 1)x{{(x + 1)}^{n – 2}}} \right].$

$= {n^2}C_n^0{x^{n – 1}}$ $+ {(n – 1)^2}C_n^1{x^{n – 2}}$ $+ {(n – 2)^2}C_n^2{x^{n – 3}}$ $+ \ldots + {1^2}.C_n^{n – 1}.$

Chọn $x=1$ ta được:

${n^2}C_n^0$ $+ {(n – 1)^2}C_n^1$ $+ {(n – 2)^2}C_n^2$ $+ \ldots + {2^2}C_n^{n – 2} + {1^2}C_n^{n – 1}$ $= n(n + 1){2^{n – 2}}.$

## Bài 7: Chứng minh rằng $\forall n \in {N^*}$ ta có: $C_n^1{3^{n – 1}}$ $+ 2C_n^2{3^{n – 2}}$ $+ 3C_n^3{3^{n – 3}}$ $+ \ldots + nC_n^n$ $= n{.4^{n – 1}}.$

Lời giải:

Xét khai triển: ${(3 + x)^n}$ $= C_n^0{3^n} + C_n^1{3^{n – 1}}x$ $+ C_n^2{3^{n – 2}}{x^2} + \ldots + C_n^n{x^n}.$

Đạo hàm hai vế ta được:

$n{(3 + x)^{n – 1}}$ $= C_n^1{3^{n – 1}} + 2C_n^2{3^{n – 2}}x$ $+ 3C_n^3{3^{n – 3}}{x^2} + \ldots + nC_n^n{x^{n – 1}}.$

Chọn $x = 1$ ta được: $C_n^1{3^{n – 1}} + 2C_n^2{3^{n – 2}}$ $+ 3C_n^3{3^{n – 3}} + \ldots + nC_n^n$ $= n{.4^{n – 1}}.$

## Bài 8: Chứng minh rằng:

$100C_{100}^0{\left( {\frac{1}{2}} \right)^{99}}$ $– 101C_{100}^1{\left( {\frac{1}{2}} \right)^{100}}$ $+ \ldots – 199C_{100}^{99}{\left( {\frac{1}{2}} \right)^{198}}$ $+ 200C_{100}^{100}{\left( {\frac{1}{2}} \right)^{199}} = 0.$

Lời giải:

Xét khai triển: ${\left( {x + {x^2}} \right)^{100}}$ $= C_{100}^0{x^{100}} + C_{100}^1{x^{101}}$ $+ C_{100}^2{x^{102}} + \ldots + C_{100}^{100}{x^{200}}.$

Đạo hàm hai vế ta được:

$100{\left( {x + {x^2}} \right)^{99}}(1 + 2x)$ $= 100C_{100}^0{x^{99}} + 101C_{100}^1{x^{100}}$ $+ 102C_{100}^2{x^{101}} + \ldots + 200C_{100}^{100}{x^{199}}.$

Chọn $x = – \frac{1}{2}$ ta được $0 = – 100C_{100}^0{\left( {\frac{1}{2}} \right)^{99}}$ $+ 101C_{100}^1{\left( {\frac{1}{2}} \right)^{100}}$ $– 102C_{100}^2{\left( {\frac{1}{2}} \right)^{101}}$ $+ \ldots + 199C_{100}^{99}{\left( {\frac{1}{2}} \right)^{198}}$ $– 200C_{100}^{100}{\left( {\frac{1}{2}} \right)^{199}}.$

Hay $100C_{100}^0{\left( {\frac{1}{2}} \right)^{99}}$ $– 101C_{100}^1{\left( {\frac{1}{2}} \right)^{100}}$ $+ \ldots – 199C_{100}^{99}{\left( {\frac{1}{2}} \right)^{198}}$ $+ 200C_{100}^{100}{\left( {\frac{1}{2}} \right)^{199}} = 0.$

## Bài 9: Cho $n$ là số nguyên dương.Chứng minh rằng:

$C_{2n}^0 – 2.C_{2n}^1$ $+ 3C_{2n}^2 – 4C_{2n}^3$ $+ \ldots + (2n + 1)C_{2n}^{2n} = 0.$

Lời giải:

Xét khai triển ${(1 + x)^{2n}}$ $= C_{2n}^0 + C_{2n}^1x$ $+ C_{2n}^2{x^2} + C_{2n}^3{x^3}$ $+ \ldots + C_{2n}^{2n}{x^{2n}}.$

Suy ra: $x{(1 + x)^{2n}}$ $= C_{2n}^0x + C_{2n}^1{x^2}$ $+ C_{2n}^2{x^3} + C_{2n}^3{x^4}$ $+ \ldots + C_{2n}^{2n}{x^{2n + 1}}.$

Đạo hàm $2$ vế ta được:

${(1 + x)^{2n}} + 2n{(1 + x)^{2n – 1}}x$ $= C_{2n}^0 + 2C_{2n}^1x$ $+ 3C_{2n}^2{x^2} + 4C_{2n}^3{x^3}$ $+ \ldots + (2n + 1)C_{2n}^{2n}{x^{2n}}.$

Chọn $x = -1$ ta được: $C_{2n}^0 – 2C_{2n}^1$ $+ 3C_{2n}^2 – 4C_{2n}^3$ $+ \ldots + (2n + 1)C_{2n}^{2n} = 0.$

## Bài 10: Chứng minh rằng: $C_n^0 + 2C_n^1$ $+ 3C_n^2 + \ldots + (n + 1)C_n^n$ $= (n + 2){2^{n – 1}}.$

Lời giải:

Xét khai triển: ${(1 + x)^n}$ $= C_n^0 + C_n^1x$ $+ C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Nhân $2$ vế với $x$ ta được: $x{(1 + x)^n}$ $= C_n^0x + C_n^1{x^2}$ $+ C_n^2{x^3} + \ldots + C_n^n{x^{n + 1}}.$

Đạo hàm hai vế ta được:

${(1 + x)^n} + nx{(1 + x)^{n – 1}}$ $= C_n^0 + 2C_n^1x + 3C_n^2{x^2}$ $+ \ldots + (n + 1)C_n^n{x^n}.$

Chọn $x = 1$ ta được: $C_n^0 + 2C_n^1 + 3C_n^2$ $+ \ldots + (n + 1)C_n^n$ $= {2^n} + n{2^{n – 1}}$ $= (n + 2){2^{n – 1}}.$

## Bài 11: Chứng minh rằng:

$2.1C_n^2 + 3.2C_n^3 + 4.3C_n^4$ $+ \ldots + n(n – 1)C_n^n$ $= n(n – 1){2^{n – 2}}.$

Lời giải:

Xét khai triển: ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2}$ $+ \ldots + C_n^n{x^n}$ $(1).$

Đạo hàm hai vế của $(1)$ ta được:

$n{(1 + x)^{n – 1}}$ $= C_n^1 + 2C_n^2x + 3C_n^3{x^2}$ $+ \ldots + nC_n^n{x^{n – 1}}$ $(2).$

Đạo hàm hai vế của $(2)$ ta được:

$n(n – 1){(1 + x)^{n – 2}}$ $= 2.1C_n^2 + 3.2C_n^3x$ $+ 4.3C_n^4{x^2}$ $+ \ldots + n(n – 1)C_n^n{x^{n – 2}}.$

Chọn $x = 1$ ta được: $2.1C_n^2 + 3.2C_n^3 + 4.3C_n^4$ $+ \ldots + n(n – 1)C_n^n$ $= n(n – 1){2^{n – 2}}.$

## Bài 12: Chứng minh rằng: $n{.2^{n – 1}}C_n^0$ $+ (n – 1){2^{n – 2}}.3C_n^1$ $+ (n – 2){2^{n – 3}}{.3^2}C_n^2$ $+ \ldots + {3^{n – 1}}C_n^{n – 1}$ $= n{.5^{n – 1}}.$

Lời giải:

Xét khai triển: ${(x + 3)^n}$ $= C_n^0{x^n} + C_n^1{x^{n – 1}}.3$ $+ C_n^2{x^{n – 2}}{.3^2}$ $+ \ldots + C_n^{n – 1}x{.3^{n – 1}} + C_n^n{3^n}.$

Đạo hàm hai vế ta được:

$n{(x + 3)^{n – 1}}$ $= nC_n^0{x^{n – 1}}$ $+ (n – 1)C_n^1{x^{n – 2}}.3$ $+ (n – 2)C_n^2{x^{n – 3}}{.3^2}$ $+ \ldots + C_n^{n – 1}{3^{n – 1}}.$

Chọn $x = 1$ ta được:

$n{.2^{n – 1}}C_n^0$ $+ (n – 1){2^{n – 2}}.3C_n^1$ $+ (n – 2){2^{n – 3}}{.3^2}C_n^2$ $+ \ldots + {3^{n – 1}}C_n^{n – 1}$ $= n{.5^{n – 1}}.$

## Bài 13: Tính: $S = 3.2.1C_n^3$ $– 4.3.2C_n^4$ $+ 5.4.3C_n^5{x^2}$ $+ \ldots + n(n – 1)(n – 2){( – 1)^{n – 3}}C_n^n$ với $n \ge 3$, $n \in N.$

Lời giải:

Xét khai triển: ${(1 + x)^n}$ $= C_n^0 + C_n^1x$ $+ C_n^2{x^2} + \ldots + C_n^n{x^n}$ $(1).$

Đạo hàm hai vế của $(1)$ ta được:

$n{(1 + x)^{n – 1}}$ $= C_n^1 + 2C_n^2x$ $+ 3C_n^3{x^2} + \ldots + nC_n^n{x^{n – 1}}$ $(2).$

Đạo hàm hai vế của $(2)$ ta được:

$n(n – 1){(1 + x)^{n – 2}}$ $= 2.1C_n^2 + 3.2C_n^3x + 4.3C_n^4{x^2}$ $+ \ldots + n(n – 1)C_n^n{x^{n – 2}}$ $(3).$

Đạo hàm hai vế của $(3)$ ta được:

$n(n – 1)(n – 2){(1 + x)^{n – 3}}$ $= 3.2.1C_n^3 + 4.3.2C_n^4x$ $+ 5.4.3C_n^5{x^2}$ $+ \ldots + n(n – 1)(n – 2)C_n^n{x^{n – 3}}.$

Chọn $x = -1$ ta được:

$3.2.1C_n^3 – 4.3.2C_n^4$ $+ 5.4.3C_n^5{x^2}$ $+ \ldots + n(n – 1)(n – 2){( – 1)^{n – 3}}C_n^n = 0.$

Vậy $S = 0.$

## Bài 14: Chứng minh rằng: $C_n^2$ $+ 2C_n^3$ $+ 3C_n^4$ $+ \ldots + (n – 1)C_n^n$ $> (n – 2){2^{n – 1}}.$

Lời giải:

Xét khai triển: ${(1 + x)^n}$ $= C_n^0 + C_n^1x + C_n^2{x^2}$ $+ \ldots + C_n^n{x^n}$ $(1).$

Đạo hàm hai vế của $(1)$ ta được: $n{(1 + x)^{n – 1}}$ $= C_n^1 + 2C_n^2x + 3C_n^3{x^2}$ $+ \ldots + nC_n^n{x^{n – 1}}.$

Chọn $x = 1$ ta được: $C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n$ $= n{.2^{n – 1}}$ $(2).$

Từ $(1)$ ta chọn $x =1$, suy ra: $C_n^0 + C_n^1 + C_n^2 + \ldots + C_n^n = {2^n}$ $(3).$

Lấy $(2)$ trừ $(3)$ ta được: $C_n^2 + 2C_n^3 + 3C_n^4$ $+ \ldots + (n – 1)C_n^n – C_n^0$ $= n{.2^{n – 1}} – {2^n}.$

$\Leftrightarrow C_n^2 + 2C_n^3 + 3C_n^4 + \ldots + (n – 1)C_n^n$ $= n{.2^{n – 1}} – {2^n} + C_n^0$ $= (n – 2){2^{n – 1}} + 1$ $> (n – 2){2^{n – 1}}.$

## Bài 15: Cho $f(x) = x{\left( {{x^2} + 1} \right)^{2015}}.$

a) Tính $f'(1).$

b) Tính $S = 4031C_{2015}^0 + 4029C_{2015}^1$ $+ 4027C_{2015}^2 + \ldots + C_{2015}^{2015}.$

Lời giải:

a) Ta có: $f'(x) = {\left( {{x^2} + 1} \right)^{2015}}$ $+ 4030{x^2}{\left( {{x^2} + 1} \right)^{2014}}.$

Suy ra: $f'(1) = {\left( {{1^2} + 1} \right)^{2015}}$ $+ {4030.1^2}{\left( {{1^2} + 1} \right)^{2014}}$ $= {2^{2015}} + {4030.2^{2014}}$ $= {4032.2^{2014}}$ $= {63.2^{2020}}$ $(1).$

b) Mặt khác ta có:

$f(x) = x{\left( {{x^2} + 1} \right)^{2015}}$ $= x\left( {C_{2015}^0{x^{4030}} + C_{2015}^1{x^{4028}} + C_{2015}^2{x^{4026}} + \ldots + C_{2015}^{2015}} \right).$

$= C_{2015}^0{x^{4031}} + C_{2015}^1{x^{4029}}$ $+ C_{2015}^2{x^{4027}} + \ldots + C_{2015}^{2015}x.$

Suy ra: $f'(x) = 4031C_{2015}^0{x^{4030}}$ $+ 4029C_{2015}^1{x^{4028}}$ $+ 4027C_{2015}^2{x^{4026}}$ $+ \ldots + C_{2015}^{2015}.$

$\Rightarrow f'(1) = 4031C_{2015}^0 + 4029C_{2015}^1$ $+ 4027C_{2015}^2 + \ldots + C_{2015}^{2015}$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $4031C_{2015}^0 + 4029C_{2015}^1$ $+ 4027C_{2015}^2 + \ldots + C_{2015}^{2015}$ $= {63.2^{2020}}.$

Vậy $S = {63.2^{2020}}.$

## Bài 16: Tìm số nguyên dương $n$ sao cho:

$C_{2n + 1}^1 – 2.2C_{2n + 1}^2$ $+ {3.2^2}C_{2n + 1}^3 – {4.2^3}C_{2n + 1}^4$ $+ \ldots + (2n + 1){.2^{2n}}C_{2n + 1}^{2n + 1}$ $= 2015.$

Lời giải:

Xét khai triển: ${(1 + x)^{2n + 1}}$ $= C_{2n + 1}^0 + C_{2n + 1}^1x$ $+ C_{2n + 1}^2{x^2} + C_{2n + 1}^3{x^3}$ $+ C_{2n + 1}^4{x^4} + \ldots + C_{2n + 1}^{2n + 1}{x^{2n + 1}}.$

Đạo hàm hai vế ta được:

$(2n + 1){(1 + x)^{2n}}$ $= C_{2n + 1}^1 + 2C_{2n + 1}^2x$ $+ 3C_{2n + 1}^3{x^2} + 4C_{2n + 1}^4{x^3}$ $+ \ldots + (2n + 1)C_{2n + 1}^{2n + 1}{x^{2n}}.$

Chọn $x= -2$ ta được:

$(2n + 1){(1 – 2)^{2n}}$ $= C_{2n + 1}^1 – 2.2C_{2n + 1}^2x$ $+ {3.2^2}C_{2n + 1}^3 – {4.2^3}C_{2n + 1}^4$ $+ \ldots + (2n + 1){.2^{2n}}C_{2n + 1}^{2n + 1}.$

$\Leftrightarrow C_{2n + 1}^1 – 2.2C_{2n + 1}^2x$ $+ {3.2^2}C_{2n + 1}^3 – {4.2^3}C_{2n + 1}^4$ $+ \ldots + (2n + 1){.2^{2n}}C_{2n + 1}^{2n + 1}$ $= 2n + 1.$

Từ giả thiết suy ra: $2n + 1 = 2015$ $\Leftrightarrow n = 1007.$

## Bài 17: Chứng minh rằng: $\frac{{C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n}}{n} < n!$ với mọi $n \in N$, $n \ge 3.$

Lời giải:

Xét khai triển: ${(1 + x)^n}$ $= C_n^0 + C_n^1x$ $+ C_n^2{x^2} + \ldots + C_n^n{x^n}.$

Đạo hàm hai vế của $(1)$ ta được: $n{(1 + x)^{n – 1}}$ $= C_n^1 + 2C_n^2x$ $+ 3C_n^3{x^2} + \ldots + nC_n^n{x^{n – 1}}.$

Chọn $x = 1$ ta được: $C_n^1 + 2C_n^2 + 3C_n^3$ $+ \ldots + nC_n^n = n{.2^{n – 1}}.$

$\Leftrightarrow \frac{{C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n}}{n} = {2^{n – 1}}.$

Suy ra bài toán dẫn đến việc chứng minh: ${2^{n – 1}} < n!$ $(*)$ với mọi $n \in N$, $n \ge 3.$

Ta chứng minh $(*)$ bằng phương pháp quy nạp như sau:

+ Với $n=3$, thay vào $(*)$ thỏa mãn.

+ Giả sử $(*)$ đúng với $n= k$ $(k > 3)$, ta có: ${2^{k – 1}} < k!.$

Ta cần chứng minh $(*)$ đúng với $n=k+1$, tức là chứng minh: ${2^k} < (k + 1)!.$

Thật vậy, ta có: ${2^k} = {2.2^{k – 1}}$ $< 2.k! < (k + 1).k!$ $= (k + 1)!.$

Suy ra $(*)$ đúng với mọi $n \in N$, $n \ge 3.$

Vậy $\frac{{C_n^1 + 2C_n^2 + 3C_n^3 + \ldots + nC_n^n}}{n} < n!.$