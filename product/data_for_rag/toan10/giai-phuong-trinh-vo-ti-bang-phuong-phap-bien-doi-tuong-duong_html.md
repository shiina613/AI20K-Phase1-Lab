# Giải phương trình vô tỉ bằng phương pháp biến đổi tương đương

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
Bài viết hướng dẫn giải phương trình vô tỉ bằng phương pháp biến đổi tương đương, đây là bài toán thường gặp trong chương trình Đại số 10: phương trình và hệ phương trình.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN

Chuyển vế đổi dấu để hai vế đều không âm, sau đó bình phương hai vế (ta được phương trình tương đương) để khử căn thức, đưa về phương trình đại số, trong đó:

+ Phương trình có dạng $\sqrt A = B$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{B \ge 0}\\
{A = {B^2}}
\end{array}} \right..
$$

+ Ta có thể bình phương mà không cần quan tâm tới điều kiện hai vế phải dương (ta được phương trình hệ quả) để khử căn thức, tuy nhiên sau khi giải ra nghiệm ta phải thử lại nghiệm.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 1. Giải phương trình $\sqrt {2x – 3} = x – 3.$

Phương trình đã cho tương đương:

$$
\left\{ {\begin{array}{l}
{x – 3 \ge 0}\\
{2x – 3 = {{(x – 3)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 3}\\
{{x^2} – 8x + 12 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 3}\\
{\left[ {\begin{array}{l}
{x = 6}\\
{x = 2}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow x = 6.$

Kết luận: phương trình có một nghiệm là $x = 6.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 2. Giải phương trình $x – \sqrt {2x – 5} = 4.$

Phương trình đã cho tương đương $\sqrt {2x – 5} = x – 4.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – 4 \ge 0}\\
{2x – 5 = {{(x – 4)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 4}\\
{{x^2} – 10x + 21 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 4}\\
{\left[ {\begin{array}{l}
{x = 7}\\
{x = 3}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow x = 7.$

Kết luận: phương trình có một nghiệm là $x = 7.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 3. Giải phương trình $\sqrt { – {x^2} + 4x} + 2 = 2x.$

Phương trình đã cho tương đương $\sqrt { – {x^2} + 4x} = 2(x – 1).$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2(x – 1) \ge 0}\\
{ – {x^2} + 4x = {{[2(x – 1)]}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 1}\\
{ – {x^2} + 4x = 4{x^2} – 8x + 4}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 1}\\
{5{x^2} – 12x + 4 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 1}\\
{\left[ {\begin{array}{l}
{x = 2}\\
{x = \frac{2}{5}}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow x = 2.$

Kết luận: phương trình có một nghiệm là $x = 2.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 4. Giải phương trình $\sqrt {x + 4} – \sqrt {1 – x} = \sqrt {1 – 2x} .$

Điều kiện: $– 4 \le x \le \frac{1}{2}.$

Với điều kiện trên phương trình tương đương:

$\sqrt {1 – x} + \sqrt {1 – 2x} = \sqrt {x + 4} .$

$\Leftrightarrow 1 – x + 1 – 2x$ $+ 2\sqrt {(1 – x)(1 – 2x)}$ $= x + 4.$

$\Leftrightarrow \sqrt {(1 – x)(1 – 2x)} = 2x + 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2x + 1 \ge 0}\\
{(1 – x)(1 – 2x) = {{(2x + 1)}^2}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – \frac{1}{2}}\\
{2{x^2} + 7x = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 0.$

So sánh với điều kiện ta được nghiệm của phương trình là $x= 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 5. Giải phương trình $\sqrt {3x + 4} – \sqrt {2x + 1} = \sqrt {x + 3} .$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{3x + 4 \ge 0}\\
{2x + 1 \ge 0}\\
{x + 3 \ge 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – \frac{4}{3}}\\
{x \ge – \frac{1}{2}}\\
{x \ge – 3}
\end{array}} \right.
$$
 $\Leftrightarrow x \ge – \frac{1}{2}.$

Với điều kiện trên phương trình tương đương:

$\sqrt {3x + 4} = \sqrt {2x + 1} + \sqrt {x + 3} .$

$\Leftrightarrow {(\sqrt {3x + 4} )^2} = {(\sqrt {2x + 1} + \sqrt {x + 3} )^2}.$

$\Leftrightarrow 3x + 4$ $= {(\sqrt {2x + 1} )^2}$ $+ 2\sqrt {2x + 1} \sqrt {x + 3}$ $+ {(\sqrt {x + 3} )^2}.$

$\Leftrightarrow 3x + 4$ $= 3x + 4$ $+ 2\sqrt {(2x + 1)(x + 3)} .$

$\Leftrightarrow \sqrt {(2x + 1)(x + 3)} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 3}\\
{x = – \frac{1}{2}}
\end{array}} \right..
$$

So sánh với điều kiện ta được nghiệm của phương trình là $x = – \frac{1}{2}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 6. Giải phương trình $\sqrt {3x + 8} – \sqrt {3x + 5}$ $= \sqrt {5x – 4} – \sqrt {5x – 7} .$

Điều kiện: $x \ge \frac{7}{5}.$

Với điều kiện trên phương trình tương đương:

$\sqrt {3x + 8} + \sqrt {5x – 7}$ $= \sqrt {5x – 4} + \sqrt {3x + 5} .$

$\Leftrightarrow {(\sqrt {3x + 8} + \sqrt {5x – 7} )^2}$ $= {(\sqrt {5x – 4} + \sqrt {3x + 5} )^2}.$

$\Leftrightarrow \sqrt {15{x^2} + 19x – 56}$ $= \sqrt {15{x^2} + 13x – 20} .$

$\Leftrightarrow 15{x^2} + 19x – 56$ $= 15{x^2} + 13x – 20.$

$\Leftrightarrow 6x = 36$ $\Leftrightarrow x = 6.$

So sánh với điều kiện ta được nghiệm của phương trình là $x = 6.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 7. Giải phương trình ${x^2} + \sqrt {x + 1} = 1.$

Phương trình đã cho tương đương:

$\sqrt {x + 1} = 1 – {x^2}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{1 – {x^2} \ge 0}\\
{x + 1 = {{\left( {1 – {x^2}} \right)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 \le x \le 1}\\
{{x^4} – 2{x^2} – x = 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 \le x \le 1}\\
{x\left( {{x^3} – 2x – 1} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 \le x \le 1}\\
{x(x + 1)\left( {{x^2} – x – 1} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = – 1}\\
{x = \frac{{1 – \sqrt 5 }}{2}}
\end{array}} \right..
$$

Kết luận: phương trình có ba nghiệm là $x =0$, $x =-1$, $x = \frac{{1 – \sqrt 5 }}{2}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 8. Giải phương trình ${x^2} + \sqrt {{x^2} – 6} = 12.$

Phương trình đã cho tương đương:

$\sqrt {{x^2} – 6} = 12 – {x^2}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{12 – {x^2} \ge 0}\\
{{x^2} – 6 = 144 – 24{x^2} + {x^4}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{12 \ge {x^2}}\\
{{x^4} – 25{x^2} + 150 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{12 \ge {x^2}}\\
{\left[ {\begin{array}{l}
{{x^2} = 15}\\
{{x^2} = 10}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow {x^2} = 10$ $\Leftrightarrow x = \pm \sqrt {10} .$

Kết luận: phương trình có hai nghiệm là $x = \pm \sqrt {10} .$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 9. Giải phương trình $\sqrt {x + 3} + \sqrt {3x + 1}$ $= 2\sqrt x + \sqrt {2x + 2} .$

Điều kiện: $x \ge 0.$

Với điều kiện trên phương trình tương đương:

$2\sqrt x – \sqrt {x + 3}$ $= \sqrt {3x + 1} – \sqrt {2x + 2} .$

$\Rightarrow 5x + 3 – 2\sqrt {4{x^2} + 12x}$ $= 5x + 3 – 2\sqrt {6{x^2} + 8x + 2} .$

$\Leftrightarrow 4{x^2} + 12x = 6{x^2} + 8x + 2$ $\Leftrightarrow x = 1.$

Thử lại thấy nghiệm $x=1$ thỏa mãn.

Vậy phương trình có nghiệm duy nhất $x=1.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 10. Giải phương trình $\sqrt {{x^2} – x – 6} + 3\sqrt x$ $= \sqrt {2\left( {{x^2} + 5x – 3} \right)} .$

Điều kiện: $x \ge 3.$

Với điều kiện trên phương trình tương đương:

${x^2} + 8x – 6 + 6\sqrt {x\left( {{x^2} – x – 6} \right)}$ $= 2\left( {{x^2} + 5x – 3} \right).$

$\Leftrightarrow 6\sqrt {x\left( {{x^2} – x – 6} \right)} = x(x + 2)$ $\Leftrightarrow 6\sqrt {{x^2} – x – 6} = \sqrt x (x + 2).$

$\Leftrightarrow 36\left( {{x^2} – x – 6} \right) = x{(x + 2)^2}$ $\Leftrightarrow (x + 2)\left( {{x^2} – 34x + 108} \right) = 0.$

$\Leftrightarrow {x^2} – 34x + 108 = 0$ $\Leftrightarrow x = 17 \pm \sqrt {181} .$

Kết luận: phương trình có hai nghiệm là $x = 17 \pm \sqrt {181} .$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 11. Giải phương trình $\frac{{{x^2}}}{{\sqrt {3x – 2} }} – \sqrt {3x – 2} = 1 – x.$

Điều kiện: $x > \frac{2}{3}.$

Với điều kiện trên phương trình tương đương:

${x^2} – 3x + 2 = (1 – x)\sqrt {3x – 2}$ $\Leftrightarrow {x^2} – 3x + 2$ $+ (x – 1)\sqrt {3x – 2} = 0.$

$\Leftrightarrow (x – 1)(x – 2)$ $+ (x – 1)\sqrt {3x – 2} = 0$ $\Leftrightarrow (x – 1)(x – 2 + \sqrt {3x – 2} ) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x – 2 + \sqrt {3x – 2} = 0}
\end{array}} \right..
$$

Ta có: $x – 2 + \sqrt {3x – 2} = 0$ $\Leftrightarrow 2 – x = \sqrt {3x – 2}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2 – x \ge 0}\\
{{{(2 – x)}^2} = 3x – 2}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 2}\\
{{x^2} – 7x + 6 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 2}\\
{\left[ {\begin{array}{l}
{x = 1}\\
{x = 6}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

Kết luận: phương trình có nghiệm là $x=1.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 12. Giải phương trình $2(\sqrt {2(2 + x)} + 2\sqrt {2 – x} )$ $= \sqrt {9{x^2} + 16} .$

Điều kiện: $– 2 \le x \le 2.$

Với điều kiện trên phương trình tương đương:

$8(x + 2)$ $+ 16\sqrt {2\left( {4 – {x^2}} \right)}$ $+ 16(2 – x)$ $= 9{x^2} + 16.$

$\Leftrightarrow 9{x^2} + 8x – 32$ $= 16\sqrt {2\left( {4 – {x^2}} \right)} .$

$\Rightarrow {\left( {9{x^2} + 8x – 32} \right)^2}$ $= 512\left( {4 – {x^2}} \right).$

$\Leftrightarrow 81{x^4} + 144{x^3} – 512x – 1024 = 0.$

$\Leftrightarrow \left( {9{x^2} – 32} \right)\left( {9{x^2} + 16x + 32} \right) = 0$ $\Leftrightarrow x = \pm \frac{{\sqrt {32} }}{3}.$

Thử lại ta được nghiệm của phương trình là $x = \frac{{\sqrt {32} }}{3}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 13. Giải phương trình $2\sqrt {x + 2 + 2\sqrt {x + 1} } – \sqrt {x + 1} = 4.$

Điều kiện: $x \ge – 1.$

Với điều kiện trên phương trình tương đương:

$2\sqrt {{{(\sqrt {x + 1} + 1)}^2}} – \sqrt {x + 1} = 4$ $\Leftrightarrow 2(\sqrt {x + 1} + 1) – \sqrt {x + 1} = 4.$

$\Leftrightarrow \sqrt {x + 1} = 2$ $\Leftrightarrow x + 1 = 4$ $\Leftrightarrow x = 3.$

Kết luận: phương trình có nghiệm là $x = 3.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 14. Giải phương trình $\sqrt {x – 1 + 2\sqrt {x – 2} }$ $– \sqrt {x – 1 – 2\sqrt {x – 2} } = 1.$

Điều kiện: $x \ge 2.$

Đặt $t = \sqrt {x – 2}$, $t \ge 0$ $\Rightarrow {t^2} = x – 2$ $\Leftrightarrow {t^2} + 2 = x.$

Khi đó phương trình đã cho trở thành:

$\sqrt {{t^2} + 1 + 2t} – \sqrt {{t^2} + 1 – 2t} = 1.$

$\Leftrightarrow \sqrt {{{(t + 1)}^2}} – \sqrt {{{(t – 1)}^2}} = 1$ $\Leftrightarrow (t + 1) – |t – 1| = 1.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t + 1 – (t – 1) = 1\:\:{\rm{với}}\:\:t \ge 1}\\
{t + 1 – (1 – t) = 1\:\:{\rm{với}}\:\:t < 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t + 1 – t + 1 = 1\:\:{\rm{với}}\:\:t \ge 1{\rm{(vô\:nghiệm)}}}\\
{t + 1 – 1 + t = 1\:\:{\rm{với}}\:\:t < 1}
\end{array}} \right..
$$

$\Leftrightarrow t = \frac{1}{2}$ $\Rightarrow \sqrt {x – 2} = \frac{1}{2}$ $\Leftrightarrow x = \frac{9}{4}.$

Kết luận: phương trình có một nghiệm là $x = \frac{9}{4}.$

Tổng quát: Khi gặp phương trình dạng:

$\sqrt {x + {a^2} – b + 2a\sqrt {x – b} }$ $+ \sqrt {x + {a^2} – b + 2a\sqrt {x – b} }$ $= cx + m$ $(a \ne 0).$

Ta thường giải như sau:

+ Điều kiện: $x \ge b.$

+ Đặt $t = \sqrt {x – b}$, $t \ge 0$ ta có $x = {t^2} + b.$ Thay vào $x + {a^2} – b \pm 2a\sqrt {x – b}$ ta được:

${t^2} + {a^2} \pm 2at = {(t \pm a)^2}.$

+ Khi đó phương trình đã cho trở thành: $|t + a| + |t – a|$ $= c\left( {{t^2} + b} \right) + m$ $(*).$

Nếu $t \ge a$ thì phương trình $(*)$ trở thành: $2t = c{t^2} + bc + m$ $\Leftrightarrow c{t^2} – 2t + bc + m = 0.$

Nếu $0 \le t \le a$ thì phương trình $(*)$ trở thành: $2a = c{t^2} + bc + m$ $\Leftrightarrow c{t^2} – 2a + bc + m = 0.$

+ Giải hai phương trình trên ta tìm được $t$, khi đó $x = {t^2} + b$ (thoả mãn điều kiện).

<!-- chunk:16 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 15. Giải phương trình $\frac{x}{2} – 2 = \frac{{{x^2}}}{{2{{(1 + \sqrt {1 + x} )}^2}}}.$

Điều kiện: $x \ge – 1.$

Vì $x = 0$ không là nghiệm của phương trình, nên phương trình đã cho tương đương:

$\frac{x}{2} – 2 = \frac{{{x^2}{{(1 – \sqrt {1 + x} )}^2}}}{{2{x^2}}}$ $\Leftrightarrow x – 4 = 1 – 2\sqrt {1 + x} + 1 + x$ $\Leftrightarrow \sqrt {1 + x} = 3.$

$\Leftrightarrow x = 8.$

So với điều kiện ta được nghiệm của phương trình là $x=8.$

<!-- chunk:17 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 16. Giải phương trình $3(2 + \sqrt {x – 2} ) = 2x + \sqrt {x + 6} .$

Điều kiện: $x \ge 2.$

Với điều kiện trên phương trình tương đương:

$3\sqrt {x – 2} – \sqrt {x + 6} = 2(x – 3).$

$\Leftrightarrow 9(x – 2) – (x + 6)$ $= 2(x – 3)(3\sqrt {x – 2} + \sqrt {x + 6} ).$

$\Leftrightarrow 4(x – 3)$ $= (x – 3)(3\sqrt {x – 2} + \sqrt {x + 6} ).$

$\Leftrightarrow (x – 3)(3\sqrt {x – 2} + \sqrt {x + 6} – 4) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 3}\\
{3\sqrt {x – 2} + \sqrt {x + 6} – 4 = 0}
\end{array}} \right..
$$

Ta có $3\sqrt {x – 2} + \sqrt {x + 6} – 4 = 0$ $\Leftrightarrow 3\sqrt {x – 2} + \sqrt {x + 6} = 4.$

$\Leftrightarrow 9(x – 2) + x + 6$ $+ 6\sqrt {(x – 2)(x + 6)} = 16.$

$\Leftrightarrow 3\sqrt {(x – 2)(x + 6)} = 14 – 5x.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{14 – 5x \ge 0}\\
{9(x – 2)(x + 6) = {{(14 – 5x)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le \frac{{14}}{5}}\\
{{x^2} – 11x + 19 = 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ \begin{array}{l}
x \le \frac{{14}}{5}\\
\left[ {\begin{array}{l}
{x = \frac{{11 + 3\sqrt 5 }}{2}}\\
{x = \frac{{11 – 3\sqrt 5 }}{2}}
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow x = \frac{{11 – 3\sqrt 5 }}{2}.$

Kết luận: phương trình có nghiệm là $x = 3$, $x = \frac{{11 – 3\sqrt 5 }}{2}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 17. Giải phương trình $\sqrt[3]{{x – 1}} + \sqrt[3]{{x – 2}} = \sqrt[3]{{2x – 3}}.$

Phương trình đã cho tương đương:

${(\sqrt[3]{{x – 1}} + \sqrt[3]{{x – 2}})^3} = {(\sqrt[3]{{2x – 3}})^3}.$

$\Leftrightarrow x – 1 + x – 2$ $+ 3\sqrt[3]{{x – 1}}\sqrt[3]{{x – 2}}(\sqrt[3]{{x – 1}} + \sqrt[3]{{x – 2}})$ $= 2x – 3$ $(1).$

$\Rightarrow \sqrt[3]{{x – 1}}\sqrt[3]{{x – 2}}\sqrt[3]{{2x – 3}} = 0$ $(2)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 2}\\
{x = \frac{3}{2}}
\end{array}} \right..
$$

Thử lại, ta thấy nghiệm của phương trình là: $x =1$, $x = 2$, $x = \frac{3}{2}.$

Nhận xét: Từ phương trình $(1)$ biến đổi sang phương trình $(2)$ ta đã thay $\sqrt[3]{{x – 1}} + \sqrt[3]{{x – 2}}$ bằng $\sqrt[3]{{2x – 3}}$ và ta phải sử dụng dấu “$\Rightarrow$”, bởi nếu phương trình $\sqrt[3]{{x – 1}} + \sqrt[3]{{x – 2}} = \sqrt[3]{{2x – 3}}$ vô nghiệm thì không tồn tại $x$ để $\sqrt[3]{{x – 1}} + \sqrt[3]{{x – 2}} = \sqrt[3]{{2x – 3}}.$

Tổng quát: Khi gặp phương trình dạng:

$\sqrt[3]{{A(x)}} \pm \sqrt[3]{{B(x)}} = \sqrt[3]{{C(x)}}$ $(1).$

Ta thường giải như sau:

+ Lập phương hai vế ta được phương trình:

$A(x) \pm B(x)$ $\pm 3\sqrt[3]{{A(x)}}\sqrt[3]{{B(x)}}(\sqrt[3]{{A(x)}} \pm \sqrt[3]{{B(x)}})$ $= C(x)$ $(2)$

+ Thay $(1)$ vào $(2)$ ta được phương trình hệ quả:

$A(x) \pm B(x)$ $\pm 3\sqrt[3]{{A(x)}}\sqrt[3]{{B(x)}}\sqrt[3]{{C(x)}}$ $= C(x).$

$\Leftrightarrow A(x) \pm B(x) – C(x)$ $= \mp 3\sqrt[3]{{A(x)}}\sqrt[3]{{B(x)}}\sqrt[3]{{C(x)}}.$

$\Leftrightarrow {[A(x) \pm B(x) – C(x)]^3}$ $= \mp 27A(x)B(x)C(x)$ $(3).$

Việc giải phương trình $(1)$ chứa căn thức được đưa về giải phương trình $(3)$ là phương trình đa thức.

<!-- chunk:19 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 18. Giải phương trình $\sqrt {2{x^2} + x + 6}$ $+ \sqrt {{x^2} + x + 2}$ $= x + \frac{4}{x}$ $(1).$

Điều kiện: $x \ne 0.$

Để $x$ là nghiệm của phương trình thì $x>0.$

Phương trình đã cho tương đương:

$\frac{{{x^2} + 4}}{{\sqrt {2{x^2} + x + 6} – \sqrt {{x^2} + x + 2} }}$ $= \frac{{{x^2} + 4}}{x}.$

$\Leftrightarrow \sqrt {2{x^2} + x + 6}$ $– \sqrt {{x^2} + x + 2}$ $= x$ $(2).$

Kết hợp giữa phương trình $(1)$ và phương trình $(2)$ ta được phương trình: $2\sqrt {{x^2} + x + 2} = \frac{4}{x}.$

$\Leftrightarrow 4 = 2x\sqrt {{x^2} + x + 2}$ $\Leftrightarrow 4 = {x^2}\left( {{x^2} + x + 2} \right)$ $\Leftrightarrow {x^4} + {x^3} + 2{x^2} – 4 = 0.$

$\Leftrightarrow (x – 1)\left( {{x^3} + 2{x^2} + 4x + 4} \right) = 0$ $\Leftrightarrow x = 1$ (do ${{x^3} + 2{x^2} + 4x + 4 > 0}$, ${\forall x > 0}$).

Kết luận: phương trình có nghiệm là $x=1.$

<!-- chunk:20 level:1 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## I. BÀI TẬP

1. Giải phương trình $\sqrt { – {x^2} + 4x – 3} = 2x – 5.$

2. Giải phương trình $x + \sqrt {{x^2} + x + 2} = 3.$

3. Giải phương trình $\sqrt {7 – {x^2} + x\sqrt {x + 5} } = \sqrt {3 – 2x – {x^2}} .$

4. Giải phương trình $\sqrt {3x – 2} – \sqrt {x + 7} = 1.$

5. Giải phương trình $\sqrt {x + 8} – \sqrt x = \sqrt {x + 3} .$

6. Giải phương trình $\sqrt {x(x – 1)} + \sqrt {x(x + 2)} = 2x.$

7. Giải phương trình $\sqrt {x + 3} + \sqrt {3x + 1} = 2\sqrt x + \sqrt {2x + 2} .$

8. Giải phương trình $\sqrt {4x + 5} + \sqrt {3x + 1}$ $= \sqrt {2x + 7} + \sqrt {x + 3} .$

9. Giải phương trình $\sqrt {x + 2\sqrt {x – 1} }$ $– \sqrt {x – 2\sqrt {x – 1} } = 2.$

10. Giải phương trình $\sqrt {x + 2\sqrt {x – 1} }$ $+ \sqrt {x – 2\sqrt {x – 1} } = \frac{{x + 3}}{2}.$

11. Giải phương trình $4{(x + 1)^2}$ $= (2x + 10){(1 – \sqrt {3 + 2x} )^2}.$

12. Giải phương trình $\sqrt {\frac{1}{2} – x\sqrt {1 – {x^2}} } = 1 – 2{x^2}.$

13. Giải phương trình $\sqrt[3]{{2{x^3} – 1}} + \sqrt[3]{{1 – {x^3}}} = x.$

14. Giải phương trình $\sqrt[3]{{{x^3} + 1}} + \sqrt[3]{{{x^3} – 1}} = x\sqrt[3]{2}.$

15. Giải phương trình $\sqrt[3]{{x + 1}} + \sqrt[3]{{x + 3}} = \sqrt[3]{{x + 2}}.$

16. Giải phương trình $\sqrt[3]{{2x – 1}} = x\sqrt[3]{{16}} – \sqrt[3]{{2x + 1}}.$

17. Giải phương trình $\sqrt[3]{{x + 1}} + \sqrt[3]{{x – 1}} = \sqrt[3]{{5x}}.$

18. Giải phương trình $\sqrt[3]{{15x – 1}} = 4\sqrt[3]{x} – \sqrt[3]{{13x + 1}}.$

19. Giải phương trình $\sqrt[3]{{2x – 1}} = \sqrt[3]{{3x + 1}} – \sqrt[3]{{x – 1}}.$

<!-- chunk:21 level:1 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-bien-doi-tuong-duong.html -->
## II. ĐÁP SỐ
1. $x = \frac{{14}}{5}.$

2. $x = 1.$

3. $x = – 1.$

4. $x = 9.$

5. $x = 1.$

6. $x = 0$, $x = \frac{9}{8}.$

7. $x = 1.$

8. $x = 1.$

9. $x \ge 2.$

10. $x = 1$, $x = 5.$

11. $x = 3$, $x = – 1.$

12. $x = \frac{{\sqrt 2 }}{2}$, $x = \frac{1}{4}(\sqrt 2 + \sqrt 6 ).$

13. $x = 0$, $x = 1$, $x = \frac{1}{{\sqrt[3]{2}}}.$

14. $x = 0$, $x = \pm 1.$

15. $x = – 2$, $x = \frac{{ – 28 \pm \sqrt {189} }}{{14}}.$

16. $x = 0$, $x = \pm \frac{1}{2}$, $x = \pm \sqrt {\frac{{2 + 3\sqrt 3 }}{8}} .$

17. $x = 0$, $x = \pm \frac{{\sqrt 5 }}{2}.$

18. $x = – \frac{1}{{12}}$, $x = 0$, $x = \frac{1}{{14}}.$

19. $x = \frac{7}{6}.$