# Giải phương trình vô tỉ bằng phương pháp đặt ẩn phụ đưa về hệ phương trình

<!-- chunk:0 level:0 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
Bài viết hướng dẫn cách giải phương trình vô tỉ (phương trình có chứa dấu căn thức) bằng phương pháp đặt ẩn phụ đưa về hệ phương trình, đây là dạng toán thường gặp trong chương trình Đại số 10.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN

Đặt $u = t(x)$, ta được một hệ theo biến $u$ và biến $x.$

Hoặc $u = t(x)$, $v = k(x)$ ta được hệ mới theo biến $u$ và biến $v.$

Thông thường cả hai cách đặt đều dẫn đến hệ phương trình đối xứng loại $2$.

<!-- chunk:2 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 1. Giải phương trình ${x^2} + \sqrt {1 + x} = 1.$

Lời giải:

Điều kiện: $– 1 \le x \le 1.$

Đặt $u = \sqrt {x + 1} .$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{x^2} = 1 – u}\\
{{u^2} = 1 + x}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^2} = 1 – u}\\
{{x^2} – {u^2} = – (x + u)}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^2} = 1 – u}\\
{(x + u)(x – u + 1) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^2} = 1 – u}\\
{\left[ {\begin{array}{l}
{x + u = 0}\\
{x – u + 1 = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{x + u = 0}\\
{{x^2} = 1 – u}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{x – u + 1 = 0}\\
{{x^2} = 1 – u}
\end{array}} \right.}
\end{array}} \right..
$$

+ Với 
$$
\left\{ {\begin{array}{l}
{x + u = 0}\\
{{x^2} = 1 – u}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – u}\\
{{x^2} – x – 1 = 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{x = \frac{{1 – \sqrt 5 }}{2}}\\
{x = \frac{{1 + \sqrt 5 }}{2}}
\end{array}} \right.
$$
 $\Rightarrow x = \frac{{1 – \sqrt 5 }}{2}$ (do $x=\frac{1+\sqrt{5}}{2}>1$).

+ Với 
$$
\left\{ {\begin{array}{l}
{x – u + 1 = 0}\\
{{x^2} = 1 – u}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = x + 1}\\
{{x^2} + x = 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = – 1}
\end{array}} \right..
$$

Kết luận: phương trình có ba nghiệm là $x = – 1$, $x = 0$, $x = \frac{{1 – \sqrt 5 }}{2}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 2. Giải phương trình ${x^3} + 1 = 2\sqrt[3]{{2x – 1}}.$

Lời giải:

Đặt $y = \sqrt[3]{{2x – 1}}$ $\Leftrightarrow {y^3} = 2x – 1$ $\Leftrightarrow {y^3} + 1 = 2x.$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{x^3} + 1 = 2y\:\:(1)}\\
{{y^3} + 1 = 2x\:\:(2)}
\end{array}} \right..
$$

Lấy phương trình $(1)$ trừ phương trình $(2)$ vế theo vế ta được phương trình: ${x^3} – {y^3} = 2(y – x).$

$\Leftrightarrow (x – y)\left( {{x^2} + xy + {y^2} + 2} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = y}\\
{{x^2} + xy + {y^2} + 2 = 0\:\:(3)}
\end{array}} \right..
$$

Ta có ${x^2} + xy + {y^2} + 2$ $= {\left( {x + \frac{1}{2}y} \right)^2} + \frac{3}{4}{y^2} + 2 > 0$, $\forall x$, $y$ nên phương trình $(3)$ vô nghiệm.

Thay $y = x$ vào phương trình ${x^3} + 1 = 2y$ ta được phương trình: ${x^3} + 1 = 2x$ $\Leftrightarrow {x^3} – 2x + 1 = 0.$

$\Leftrightarrow (x – 1)\left( {{x^2} + x – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = \frac{{ – 1 \pm \sqrt 5 }}{2}}
\end{array}} \right..
$$

Kết luận: nghiệm của phương trình là: $x = 1$, $x = \frac{{ – 1 \pm \sqrt 5 }}{2}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 3. Giải phương trình $\sqrt[3]{{x – 9}} = {(x – 3)^3} + 6.$

Lời giải:

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[3]{{x – 9}}}\\
{v = x – 3}
\end{array}} \right.
$$
 $\Rightarrow {u^3} + 6 = v.$

Kết hợp với đề bài ta được hệ phương trình: 
$$
\left\{ {\begin{array}{l}
{u = {v^3} + 6}\\
{v = {u^3} + 6}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = {v^3} + 6}\\
{u – v = {v^3} – {u^3}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = {v^3} + 6}\\
{(u – v)\left( {{u^2} + {v^2} + uv + 1} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = {v^3} + 6}\\
{u = v}
\end{array}} \right.
$$
 (do ${u^2} + {v^2} + uv + 1$ $= {\left( {u + \frac{v}{2}} \right)^2} + \frac{3}{4}{v^2} + 1 > 0$, $\forall u$, $v$).

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = v}\\
{{u^3} – u + 6 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = v}\\
{(u + 2)\left( {{u^2} – 2u + 3} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = – 2}\\
{v = – 2}
\end{array}} \right.
$$
 $\Rightarrow x = 1.$

Kết luận: nghiệm của phương trình là: $x =1.$

<!-- chunk:5 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 4. Giải phương trình $\sqrt[3]{{24 + x}} + \sqrt {12 – x} = 6.$

Lời giải:

Điều kiện: $x \le 12.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[3]{{24 + x}}}\\
{v = \sqrt {12 – x} \ge 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{{u^3} = 24 + x}\\
{{v^2} = 12 – x}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{u + v = 6}\\
{{u^3} + {v^2} = 36}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{v = 6 – u}\\
{{u^3} + {{(6 – u)}^2} = 36}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{v = 6 – u}\\
{{u^3} + {u^2} – 12u = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{v = 6 – u}\\
{u(u – 3)(u + 4) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{v = 6 – u}\\
{\left[ {\begin{array}{l}
{u = 0}\\
{u = 3}\\
{u = – 4}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 0}\\
{v = 6}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 3}\\
{v = 3}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = – 4}\\
{v = 10}
\end{array}} \right.}
\end{array}} \right..
$$

+ Với 
$$
\left\{ {\begin{array}{l}
{u = 0}\\
{v = 6}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{24 + x = 0}\\
{12 – x = 36}
\end{array}} \right.
$$
 $\Leftrightarrow x = – 24.$

+ Với 
$$
\left\{ {\begin{array}{l}
{u = 3}\\
{v = 3}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{24 + x = 27}\\
{12 – x = 9}
\end{array}} \right.
$$
 $\Leftrightarrow x = 3.$

+ Với 
$$
\left\{ {\begin{array}{l}
{u = – 4}\\
{v = 10}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{24 + x = – 64}\\
{12 – x = 100}
\end{array}} \right.
$$
 $\Leftrightarrow x = – 88.$

Kết luận: nghiệm của phương trình là: $x = – 88$, $x = – 24$, $x = 3.$

<!-- chunk:6 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 5. Giải phương trình $\sqrt[3]{{x + 34}} – \sqrt[3]{{x – 3}} = 1.$

Lời giải:

Đặt 
$$
\left\{ {\begin{array}{l}
{a = \sqrt[3]{{x + 34}}}\\
{b = \sqrt[3]{{x – 3}}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{a^3} = x + 34}\\
{{b^3} = x – 3}
\end{array}} \right.
$$
 $\Rightarrow {a^3} – {b^3} = 37.$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{a – b = 1}\\
{{a^3} – {b^3} = 37}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 1 + b}\\
{{{(1 + b)}^3} – {b^3} = 37}
\end{array}.} \right.
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 1 + b}\\
{1 + 3b + 3{b^2} + {b^3} – {b^3} = 37}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{b = 3}\\
{a = 4}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{b = – 4}\\
{a = – 3}
\end{array}} \right.}
\end{array}} \right..
$$

+ Với $b = 3$, ta được ${b^3} = x – 3$ $\Leftrightarrow {3^3} = x – 3$ $\Leftrightarrow x = 30.$

+ Với $b =–4$, ta được ${b^3} = x – 3$ $\Leftrightarrow {( – 4)^3} = x – 3$ $\Leftrightarrow x = – 61.$

Kết luận: phương trình có nghiệm là $x = 30$, $x=-61.$

<!-- chunk:7 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 6. Giải phương trình $\sqrt {x – 1} + x – 3$ $= \sqrt {2{{(x – 3)}^2} + 2(x – 1)} .$

Lời giải:

Điều kiện: $x \ge 1.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt {x – 1} ,u \ge 0}\\
{v = x – 3}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x = {u^2} + 1}\\
{x = v + 3}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình:

$$
\left\{ {\begin{array}{l}
{u \ge 0}\\
{u + v = \sqrt {2{u^2} + 2{v^2}} }\\
{{u^2} + 1 = v + 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u \ge 0}\\
{u + v \ge 0}\\
{u = v}\\
{{u^2} – u – 2 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = 2}\\
{v = 2}
\end{array}} \right.
$$
 $\Rightarrow x = 5.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x=5.$

<!-- chunk:8 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 7. Giải phương trình $\sqrt[4]{{56 – x}} + \sqrt[4]{{x + 41}} = 5.$

Lời giải:

Điều kiện: $– 41 \le x \le 56.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[4]{{56 – x}} \ge 0}\\
{v = \sqrt[4]{{x + 41}} \ge 0}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình:

$$
\left\{ {\begin{array}{l}
{u + v = 5}\\
{{u^4} + {v^4} = 97}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 5}\\
{{{\left( {{u^2} + {v^2}} \right)}^2} – 2{u^2}{v^2} = 97}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 5}\\
{{u^2}{v^2} – 50uv + 264 = 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u + v = 5}\\
{uv = 6}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u + v = 5}\\
{uv = 44}
\end{array}\:\:{\rm{(vô\:nghiệm)}}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 5}\\
{uv = 6}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 2}\\
{v = 3}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 3}\\
{v = 2}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{\sqrt[4]{{56 – x}} = 2}\\
{\sqrt[4]{{x + 41}} = 3}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{\sqrt[4]{{56 – x}} = 3}\\
{\sqrt[4]{{x + 41}} = 2}
\end{array}} \right.}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{56 – x = 16}\\
{x + 41 = 81}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{56 – x = 81}\\
{x + 41 = 16}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 40}\\
{x = – 25}
\end{array}} \right..
$$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x=40$, $x=-25.$

<!-- chunk:9 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 8. Giải phương trình $\sqrt[3]{{{{(2 – x)}^2}}} + \sqrt[3]{{{{(7 + x)}^2}}}$ $– \sqrt[3]{{(2 – x)(7 + x)}} = 3.$

Lời giải:

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[3]{{2 – x}}}\\
{v = \sqrt[3]{{7 + x}}}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình:

$$
\left\{ {\begin{array}{l}
{{u^2} + {v^2} – uv = 3}\\
{{u^3} + {v^3} = 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u^2} + {v^2} – uv = 3}\\
{(u + v)\left( {{u^2} + {v^2} – uv} \right) = 9}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 3}\\
{{{(u + v)}^2} – 3uv = 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 3}\\
{uv = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 2}\\
{v = 1}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 1}\\
{v = 2}
\end{array}} \right.}
\end{array}} \right..
$$

+ Với $u = 2$ $\Rightarrow \sqrt[3]{{2 – x}} = 2$ $\Leftrightarrow x = – 6.$

+ Với $u = 1$ $\Rightarrow \sqrt[3]{{2 – x}} = 1$ $\Leftrightarrow x = 1.$

<!-- chunk:10 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 9. Giải phương trình $\sqrt {4x + 1} – \sqrt {3x – 2}$ $= \frac{{x + 3}}{5}.$

Lời giải:

Điều kiện: $x \ge \frac{2}{3}.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt {4x + 1} }\\
{v = \sqrt {3x – 2} }
\end{array}} \right..
$$
 Kết hợp với đề bài ta được hệ phương trình:

$$
\left\{ {\begin{array}{l}
{{u^2} – {v^2} = x + 3}\\
{u – v = \frac{{x + 3}}{5}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u – v = \frac{{x + 3}}{5}}\\
{u + v = 5}
\end{array}} \right..
$$

Suy ra $2u = \frac{{25 + x + 3}}{5}$ $\Leftrightarrow u = \frac{{28 + x}}{{10}}.$

Suy ra $\sqrt {4x + 1} = \frac{{28 + x}}{{10}}$ $\Leftrightarrow 4x + 1 = {\left( {\frac{{28 + x}}{{10}}} \right)^2}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2}\\
{x = 342}
\end{array}} \right..
$$

Thử lại ta được nghiệm của phương trình là $x = 2.$

<!-- chunk:11 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 10. Giải phương trình $1 + \frac{2}{3}\sqrt {x – {x^2}} = \sqrt x + \sqrt {1 – x} .$

Lời giải:

Điều kiện: $0 \le x \le 1.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt x }\\
{v = \sqrt {1 – x} }
\end{array}} \right..
$$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{u \ge 0}\\
{v \ge 0}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{1 + \frac{2}{3}uv = u + v}\\
{{u^2} + {v^2} = 1}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{3 + 2uv = 3(u + v)}\\
{{{(u + v)}^2} – 2uv = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2uv = 3(u + v) – 3}\\
{{{(u + v)}^2} + 3 = 3(u + v) + 1}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u + v = 1}\\
{uv = 0}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u + v = 2}\\
{uv = \frac{3}{2}}
\end{array}\:\:{\rm{(vô\:nghiệm)}}} \right.}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 1}\\
{uv = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 1}\\
{v = 0}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 0}\\
{v = 1}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 0}
\end{array}} \right..
$$

Kết luận: phương trình đã cho có hai nghiệm là $x= 0$, $x=1.$

<!-- chunk:12 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 11. Giải phương trình ${x^2} – 2x = 2\sqrt {2x – 1} .$

Lời giải:

Điều kiện: $x \ge \frac{1}{2}.$

Phương trình đã cho tương đương ${(x – 1)^2} – 1 = 2\sqrt {2x – 1} .$

Đặt $y – 1 = \sqrt {2x – 1} .$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{x^2} – 2x = 2(y – 1)}\\
{{y^2} – 2y = 2(x – 1)}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình: $(x – y)(x + y) = 0.$

+ Với $x = y$ $\Rightarrow x – 1 = \sqrt {2x – 1}$ $\Rightarrow x = 2 + \sqrt 2 .$

+ Với $x = – y$ $\Rightarrow – x – 1 = \sqrt {2x – 1}$ (vô nghiệm).

Kết luận: phương trình đã cho có một nghiệm là $x = 2 + \sqrt 2 .$

<!-- chunk:13 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 12. Giải phương trình $2{x^2} – 6x – 1 = \sqrt {4x + 5} .$

Lời giải:

Điều kiện: $x \ge – \frac{5}{4}.$

Phương trình đã cho tương đương ${(2x – 3)^2} – 11 = 2\sqrt {4x + 5} .$

Đặt $2y – 3 = \sqrt {4x + 5} .$

Kết hợp với đề bài ta được hệ phương trình: 
$$
\left\{ {\begin{array}{l}
{{{(2x – 3)}^2} = 4y + 5}\\
{{{(2y – 3)}^2} = 4x + 5}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

$(x – y)(x + y – 2) = 0.$

+ Với $x = y$ $\Rightarrow 2x – 3 = \sqrt {4x + 5}$ $\Rightarrow x = 2 + \sqrt 3 .$

+ Với $x + y – 2 = 0$ $\Rightarrow y = 2 – x$ $\Rightarrow x = 1 – \sqrt 2 .$

Kết luận: phương trình đã cho có hai nghiệm là $x = 1 – \sqrt 2$, $x = 2 + \sqrt 3 .$

<!-- chunk:14 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 13. Giải phương trình $3{x^2} + x – \frac{{29}}{6}$ $= \sqrt {\frac{{12x + 61}}{{36}}} .$

Lời giải:

Điều kiện: $x \ge – \frac{{61}}{{12}}.$

Đặt $\sqrt {\frac{{12x + 61}}{{36}}} = y + \frac{1}{6}$, $y \ge – \frac{1}{6}$ $\Rightarrow \frac{{12x + 61}}{{36}} = {y^2} + \frac{1}{3}y + \frac{1}{{36}}.$

$\Leftrightarrow 12x + 61 = 36{y^2} + 12y + 1$ $\Leftrightarrow 3{y^2} + y = x + 5$ $(1).$

Mặt khác từ phương trình đã cho ta có $3{x^2} + x – \frac{{29}}{6} = y + \frac{1}{6}$ $\Leftrightarrow 3{x^2} + x = y + 5$ $(2).$

Từ $(1)$ và $(2)$ ta có hệ phương trình 
$$
\left\{ {\begin{array}{l}
{3{x^2} + x = y + 5}\\
{3{y^2} + y = x + 5}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

$(x – y)(3x + 3y + 2) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = y}\\
{y = – \frac{{3x + 2}}{3}}
\end{array}} \right..
$$

+ Với $x = y$ $\Rightarrow 3{x^2} = 5$ $\Rightarrow x = \sqrt {\frac{5}{3}} .$

+ Với $y = – \frac{{3x + 2}}{3}$ $\Rightarrow 3{x^2} + x = – \frac{{3x + 2}}{3} + 5$ $\Leftrightarrow 9{x^2} + 6x – 13 = 0.$

$\Rightarrow x = \frac{{ – 3 \pm \sqrt {126} }}{9}.$

Kết luận: nghiệm của phương trình là $x = \sqrt {\frac{5}{3}}$, $x = \frac{{ – 1 – \sqrt {14} }}{3}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 14. Giải phương trình ${x^3} + 3{x^2} – 3\sqrt[3]{{3x + 5}}$ $= 1 – 3x.$

Lời giải:

Phương trình đã cho tương đương ${(x + 1)^3} = 3\sqrt[3]{{3x + 5}} + 2.$

Đặt $\sqrt[3]{{3x + 5}} = y + 1$ $\Rightarrow 3x + 5 = {(y + 1)^3}.$

Khi đó phương trình đã cho trở thành ${(x + 1)^3} = 3y + 5.$

Từ đó ta có hệ: 
$$
\left\{ {\begin{array}{l}
{{{(x + 1)}^3} = 3y + 5}\\
{{{(y + 1)}^3} = 3x + 5}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

${(x + 1)^3} – {(y + 1)^3}$ $= – 3(x – y).$

$\Leftrightarrow (x – y)\left[ {{{(x + 1)}^2} + (x + 1)(y + 1) + {{(y + 1)}^2} + 3} \right] = 0.$

$\Leftrightarrow x = y$ (Vì ${(x + 1)^2} + (x + 1)(y + 1)$ $+ {(y + 1)^2} + 3 > 0$).

Với $x = y$ $\Rightarrow {(x + 1)^3} = 3x + 5$ $\Leftrightarrow {x^3} + 3{x^2} – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – 2}
\end{array}} \right..
$$

Kết luận: phương trình có hai nghiệm là $x=1$, $x= -2.$

<!-- chunk:16 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 15. Giải phương trình $\sqrt[3]{{2x + 3}} + 1 = {x^3} + 3{x^2} + 2x.$

Lời giải:

Phương trình đã cho tương đương $\sqrt[3]{{2x + 3}} = {(x + 1)^3} – x – 2.$

Đặt $y + 1 = \sqrt[3]{{2x + 3}}$ $\Rightarrow {(y + 1)^3} = 2x + 3.$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{{(x + 1)}^3} = x + y + 3}\\
{{{(y + 1)}^3} = 2x + 3}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình ${(x + 1)^3} – {(y + 1)^3} = y – x.$

$\Leftrightarrow (x – y)\left[ {{{(x + 1)}^2} + (x + 1)(y + 1) + {{(y + 1)}^2} + 1} \right] = 0.$

$\Leftrightarrow x = y$ (do ${(x + 1)^2} + (x + 1)(y + 1)$ $+ {(y + 1)^2} + 1 > 0$).

Với $x = y$ $\Rightarrow {(x + 1)^3} = 2x + 3$ $\Leftrightarrow (x + 2)\left( {{x^2} + x – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 2}\\
{x = \frac{{ – 1 \pm \sqrt 5 }}{2}}
\end{array}} \right..
$$

Kết luận: phương trình có ba nghiệm là $x = – 2$, $x = \frac{{ – 1 \pm \sqrt 5 }}{2}.$

Lưu ý:

+ Từ các ví dụ 11, 12, 13, 14 và 15, các bạn hãy tự rút ra quy tắc về cách đặt ẩn phụ trong các ví dụ này. Nguyên tắc là đặt để sau đó có được hệ đối xứng, vậy quy tắc ở đây là gì?

+ Các bài toán dạng này còn có thể giải được bằng phương pháp hàm số.

<!-- chunk:17 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 16. Giải phương trình $x + \sqrt {5 + \sqrt {x – 1} } = 6.$

Lời giải:

Điều kiện: $x \ge 1.$

Đặt 
$$
\left\{ {\begin{array}{l}
{a = \sqrt {x – 1} \ge 0}\\
{b = \sqrt {5 + \sqrt {x – 1} } \ge 0}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{a^2} + b = 5}\\
{{b^2} – a = 5}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

$(a + b)(a – b + 1) = 0$ $\Rightarrow a – b + 1 = 0$ $\Rightarrow a + 1 = b.$

Suy ra $\sqrt {x – 1} + 1 = \sqrt {5 + \sqrt {x – 1} }$ $\Leftrightarrow \sqrt {x – 1} = 5 – x$ $\Rightarrow x = \frac{{11 – \sqrt {17} }}{2}.$

Kết luận: phương trình đã cho có một nghiệm là $x = \frac{{11 – \sqrt {17} }}{2}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 17. Giải phương trình $4x = \sqrt {30 + \frac{1}{4}\sqrt {30 + \frac{1}{4}\sqrt {30 + \frac{1}{4}\sqrt {x + 30} } } } .$

Lời giải:

Để $x$ là nghiệm thì $x > 0.$

Đặt $u = \frac{1}{4}\sqrt {30 + \frac{1}{4}\sqrt {x + 30} } .$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{4u = \sqrt {30 + \frac{1}{4}\sqrt {x + 30} } }\\
{4x = \sqrt {30 + \frac{1}{4}\sqrt {u + 30} } }
\end{array}} \right.
$$
 $(1).$

+ Giả sử $x \ge u$, khi đó ta có:

$4u = \sqrt {30 + \frac{1}{4}\sqrt {x + 30} }$ $\ge \sqrt {30 + \frac{1}{4}\sqrt {u + 30} } = 4x$ $\Rightarrow u \ge x.$

Suy ra ta có $x = u$, hay $4x = \sqrt {30 + \frac{1}{4}\sqrt {x + 30} }$ $(2).$

Đặt $v = \frac{1}{4}\sqrt {x + 30} .$ Kết hợp với phương trình $(2)$ ta có hệ phương trình 
$$
\left\{ {\begin{array}{l}
{4x = \sqrt {30 + v} }\\
{4v = \sqrt {x + 30} }
\end{array}} \right.
$$
 $(3).$

+ Giả sử $x \ge v$, khi đó $4v = \sqrt {x + 30}$ $\ge \sqrt {v + 30} = 4x$ $\Rightarrow v \ge x$ $\Rightarrow x = v.$

Vậy $x = v$ hay $4x = \sqrt {x + 30}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{16{x^2} = x + 30}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{{1 + \sqrt {1921} }}{{32}}.$

Kết luận: Phương trình đã cho có nghiệm duy nhất $x = \frac{{1 + \sqrt {1921} }}{{32}}.$

<!-- chunk:19 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 18. Giải phương trình $\sqrt x + \sqrt {1 – x}$ $– 2\sqrt {x(1 – x)}$ $– 2\sqrt[4]{{x(1 – x)}} = – 1.$

Lời giải:

Điều kiện: $0 \le x \le 1.$

Đặt: 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[4]{x}}\\
{v = \sqrt[4]{{1 – x}}}
\end{array}} \right.
$$
 $\Rightarrow {u^4} + {v^4} = 1$ $(1).$

Khi đó phương trình đã cho trở thành ${u^2} + {v^2} – 2{u^2}{v^2} – 2uv = – 1$ $(2).$

Kết hợp phương trình $(1)$ và phương trình $(2)$ ta có hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{u^4} + {v^4} = 1}\\
{{u^2} + {v^2} – 2uv + 1 – 2{u^2}{v^2} = 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u^4} + {v^4} = 1}\\
{{u^2} + {v^2} – 2uv + {u^4} + {v^4} – 2{u^2}{v^2} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u^4} + {v^4} = 1}\\
{{{(u – v)}^2} + {{\left( {{u^2} – {v^2}} \right)}^2} = 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u^4} + {v^4} = 1}\\
{u – v = 0}\\
{{u^2} – {v^2} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = v}\\
{{u^4} = {v^4} = \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x = \frac{1}{2}}\\
{1 – x = \frac{1}{2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{1}{2}.$

Kết luận: phương trình đã cho có một nghiệm là $x = \frac{1}{2}.$

<!-- chunk:20 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 19. Giải phương trình $\sqrt x + \sqrt[4]{{x{{(1 – x)}^2}}} + \sqrt[4]{{{{(1 – x)}^3}}}$ $= \sqrt {1 – x} + \sqrt[4]{{{x^3}}} + \sqrt[4]{{{x^2}(1 – x)}}.$

Lời giải:

Điều kiện: $0 \le x \le 1.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[4]{x}}\\
{v = \sqrt[4]{{1 – x}}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{u \ge 0}\\
{v \ge 0}\\
{{u^4} + {v^4} = 1}
\end{array}} \right..
$$

Khi đó phương trình đã cho trở thành ${u^2} + u{v^2} + {v^3}$ $= {v^2} + {u^3} + {u^2}v.$

$\Leftrightarrow {u^2} – {v^2}$ $– \left( {{u^3} – {v^3}} \right)$ $– uv(u – v) = 0.$

$\Leftrightarrow (u – v)\left[ {u + v – \left( {{u^2} + uv + {v^2}} \right) – uv} \right] = 0.$

$\Leftrightarrow (u – v)\left[ {u + v – {{(u + v)}^2}} \right] = 0.$

$\Leftrightarrow (u – v)(u + v)[1 – (u + v)] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u – v = 0}\\
{u + v = 1}
\end{array}} \right.
$$
 (do $u$ và $v$ không đồng thời bằng không nên $u + v > 0$).

+ Với 
$$
\left\{ {\begin{array}{l}
{u – v = 0}\\
{{u^4} + {v^4} = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u^4} = \frac{1}{2}}\\
{{v^4} = \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x = \frac{1}{2}}\\
{1 – x = \frac{1}{2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{1}{2}.$

+ Với 
$$
\left\{ {\begin{array}{l}
{u + v = 1}\\
{{u^4} + {v^4} = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 1}\\
{{{\left[ {{{(u + v)}^2} – 2uv} \right]}^2} – 2{u^2}{v^2} = 1}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 1}\\
{1 – 4uv + 4{u^2}{v^2} – 2{u^2}{v^2} = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 1}\\
{uv(uv – 2) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u + v = 1}\\
{uv = 0}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u + v = 1}\\
{uv = 2}
\end{array}{\rm{(vô\:nghiệm)}}} \right.}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 0}\\
{v = 1}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 1}\\
{v = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{x = 0}\\
{1 – x = 1}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{x = 1}\\
{1 – x = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 1}
\end{array}} \right..
$$

Kết luận: phương trình đã cho có ba nghiệm là $x = 0$, $x = \frac{1}{2}$, $x = 1.$

<!-- chunk:21 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 20. Giải phương trình $\frac{{(34 – x)\sqrt[3]{{x + 1}} – (x + 1)\sqrt[3]{{34 – x}}}}{{\sqrt[3]{{34 – x}} – \sqrt[3]{{x + 1}}}} = 30.$

Lời giải:

Điều kiện: $\sqrt[3]{{34 – x}} \ne \sqrt[3]{{x + 1}}$ $\Leftrightarrow x \ne \frac{{33}}{2}.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[3]{{x + 1}}}\\
{v = \sqrt[3]{{34 – x}}}
\end{array}} \right.
$$
 $(u \ne v).$

Kết hợp với đề bài ta được hệ phương trình:

$$
\left\{ {\begin{array}{l}
{\frac{{{v^3}u – {u^3}v}}{{v – u}} = 30}\\
{{u^3} + {v^3} = 35}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{uv(u + v) = 30}\\
{{{(u + v)}^3} – 3uv(u + v) = 35}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 5}\\
{uv = 6}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 2}\\
{v = 3}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 3}\\
{v = 2}
\end{array}} \right.}
\end{array}} \right..
$$

+ Khi $u =2$, ta được $\sqrt[3]{{x + 1}} = 2$ $\Leftrightarrow x + 1 = 8$ $\Leftrightarrow x = 7.$

+ Khi $u =3$, ta được $\sqrt[3]{{x + 1}} = 3$ $\Leftrightarrow x + 1 = 27$ $\Leftrightarrow x = 26.$

Kết luận: Phương trình đã cho có hai nghiệm là $x = 7$, $x = 26.$

<!-- chunk:22 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 21. Giải phương trình $\frac{{\sqrt[3]{{7 – x}} – \sqrt[3]{{x – 5}}}}{{\sqrt[3]{{7 – x}} + \sqrt[3]{{x – 5}}}} = 6 – x.$

Lời giải:

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[3]{{7 – x}}}\\
{v = \sqrt[3]{{x – 5}}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{{u^3} + {v^3} = 2}\\
{\frac{{{u^3} – {v^3}}}{2} = 6 – x}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{u^3} + {v^3} = 2}\\
{\frac{{u – v}}{{u + v}} = \frac{1}{2}\left( {{u^3} – {v^3}} \right)}
\end{array}} \right..
$$

+ Với 
$$
\left\{ {\begin{array}{l}
{{u^3} + {v^3} = 2}\\
{u – v = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u^3} = 1}\\
{{v^3} = 1}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{7 – x = 1}\\
{x – 5 = 1}
\end{array}} \right.
$$
 $\Leftrightarrow x = 6.$

+ Với 
$$
\left\{ {\begin{array}{l}
{{u^3} + {v^3} = 2}\\
{\left( {{u^2} + {v^2} + uv} \right)(u + v) = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\left( {{u^2} + {v^2} – uv} \right)(u + v) = 2}\\
{\left( {{u^2} + {v^2} + uv} \right)(u + v) = 2}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{uv = 0}\\
{{u^3} + {v^3} = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 0}\\
{{v^3} = 2}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{{u^3} = 2}\\
{v = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{x = 7}\\
{x = 5}
\end{array}} \right..
$$

Kết luận: phương trình đã cho có ba nghiệm là $x = 5$, $x = 6$, $x = 7.$

<!-- chunk:23 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 22. Giải phương trình $\sqrt[4]{x} + \sqrt[4]{{x + 1}} = \sqrt[4]{{2x + 1}}.$

Lời giải:

Điều kiện: $x \ge 0.$

Phương trình đã cho tương đương: $\sqrt[4]{{\frac{x}{{2x + 1}}}} + \sqrt[4]{{\frac{{x + 1}}{{2x + 1}}}} = 1.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt[4]{{\frac{x}{{2x + 1}}}}}\\
{v = \sqrt[4]{{\frac{{x + 1}}{{2x + 1}}}}}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{u + v = 1}\\
{{u^4} + {v^4} = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u + v = 1}\\
{\left[ {\begin{array}{l}
{uv = 2}\\
{uv = 0}
\end{array}} \right.}
\end{array}} \right..
$$

+ Với 
$$
\left\{ {\begin{array}{l}
{uv = 0}\\
{u + v = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{u = 0}\\
{v = 1}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{u = 1}\\
{v = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Rightarrow x = 0.$

+ Với 
$$
\left\{ {\begin{array}{l}
{uv = 2}\\
{u + v = 1}
\end{array}} \right.
$$
 (vô nghiệm).

Kết luận: phương trình đã cho có một nghiệm là $x=0.$

<!-- chunk:24 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 23. Giải phương trình $\sqrt {{x^2} – x + 1} + \sqrt {{x^2} + x + 1} = 2.$

Lời giải:

Vì $x=0$ không phải là nghiệm của phương trình, nên phương trình đã cho tương đương:

$\frac{{2x}}{{\sqrt {{x^2} + x + 1} – \sqrt {{x^2} – x + 1} }} = 2$ $\Leftrightarrow \sqrt {{x^2} + x + 1} – \sqrt {{x^2} – x + 1} = x.$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{\sqrt {{x^2} + x + 1} + \sqrt {{x^2} – x + 1} = 2}\\
{\sqrt {{x^2} + x + 1} – \sqrt {{x^2} – x + 1} = x}
\end{array}} \right..
$$

Suy ra $2\sqrt {{x^2} + x + 1} = x + 2$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – 2}\\
{4{x^2} + 4x + 4 = {x^2} + 4x + 4}
\end{array}} \right.
$$
 $\Leftrightarrow x = 0.$

Kết luận: phương trình đã cho có một nghiệm là $x= 0.$

<!-- chunk:25 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 24. Giải phương trình $4{x^2} – 11x + 10$ $= (x – 1)\sqrt {2{x^2} – 6x + 2} .$

Lời giải:

Điều kiện: $2{x^2} – 6x + 2 \ge 0.$

Phương trình đã cho tương đương:

${(2x – 3)^2} + x + 1$ $= (x – 1)\sqrt {(x – 1)(2x – 3) – x – 1} .$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = 2x – 3}\\
{v = \sqrt {(x – 1)(2x – 3) – x – 1} }
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{u^2} + x + 1 = (x – 1)v}\\
{{v^2} + x + 1 = (x – 1)u}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

${u^2} – {v^2} = (x – 1)(v – u)$ $\Leftrightarrow (u – v)(u + v + x – 1) = 0.$

+ Với $u = v$ $\Rightarrow {u^2} + x + 1 = (x – 1)u.$

$\Leftrightarrow {(2x – 3)^2} + x + 1$ $= (x – 1)(2x – 3)$ $\Leftrightarrow 2{x^2} – 6x + 7 = 0$ (vô nghiệm).

+ Với $u + v + x – 1 = 0$ $\Rightarrow 2x – 3$ $+ \sqrt {2{x^2} – 6x + 2}$ $+ x – 1 = 0.$

$\Leftrightarrow \sqrt {2{x^2} – 6x + 2} = 4 – 3x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le \frac{4}{3}}\\
{7{x^2} – 18x + 14 = 0}
\end{array}} \right.
$$
 (vô nghiệm).

Kết luận: phương trình đã cho vô nghiệm.

<!-- chunk:26 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 25. Giải phương trình ${x^3} – 5{x^2} + 4x – 5$ $= (1 – 2x)\sqrt[3]{{6{x^2} – 2x + 7}}.$

Lời giải:

Phương trình đã cho tương đương:

${(x + 1)^3} – 8{x^2} + x – 6$ $= (1 – 2x)\sqrt[3]{{(1 – 2x)(x + 1) + 8{x^2} – x + 6}}.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = x + 1}\\
{v = \sqrt[3]{{(1 – 2x)(x + 1) + 8{x^2} – x + 6}}}
\end{array}} \right..
$$

Kết hợp với đề bài ta được hệ phương trình:

$$
\left\{ {\begin{array}{l}
{{u^3} – \left( {8{x^2} – x + 6} \right) = (1 – 2x)v}\\
{{v^3} – \left( {8{x^2} – x + 6} \right) = (1 – 2x)u}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

$(u – v)\left( {{u^2} + uv + {v^2} + 1 – 2x} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = v}\\
{{u^2} + uv + {v^2} + 1 – 2x = 0\:\:(1)}
\end{array}} \right..
$$

+ Với $u = v$, ta được: $\sqrt[3]{{6{x^2} – 2x + 7}} = x + 1$ $\Leftrightarrow x = 2.$

+ Ta có ${u^2} + uv + {v^2} + 1 – 2x$ $= {\left( {\frac{u}{2} + v} \right)^2}$ $+ \frac{{3{u^2} – 8x + 4}}{4}$ $\ge \frac{{3{u^2} – 8x + 4}}{4}$ $= \frac{{3{{(x + 1)}^2} – 8x + 4}}{4}$ $= \frac{{3{x^2} – 2x + 7}}{4} > 0.$

Nên phương trình $(1)$ vô nghiệm.

Kết luận: phương trình đã cho có một nghiệm $x = 2.$

<!-- chunk:27 level:3 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## Ví dụ 26. Giải phương trình ${x^3} + 1 = 3\sqrt[3]{{3x – 1}}.$

Lời giải:

Đặt $u = \sqrt[3]{{3x – 1}}$ $\Rightarrow {u^3} + 1 = 3x.$

Kết hợp với đề bài ta được hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{x^3} + 1 = 3u}\\
{{u^3} + 1 = 3x}
\end{array}} \right..
$$

Lấy phương trình trên trừ phương trình dưới ta được phương trình:

$(x – u)\left( {{x^2} + xu + {u^2} + 3} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = u}\\
{{x^2} + xu + {u^2} + 3 = 0\:\:{\rm{(vô\:nghiệm)}}}
\end{array}} \right..
$$

Với $x = u$, ta được phương trình: ${x^3} – 3x + 1 = 0$ $(1).$

Xét $x \in [ – 2;2].$ Đặt $x = 2\cos t$, $x \in [0;\pi ].$

Phương trình $(1)$ trở thành: $8{\cos ^3}t – 6\cos t = – 1.$

$\Leftrightarrow \cos 3t = – \frac{1}{2}$ $\Leftrightarrow t = \pm \frac{{2\pi }}{9} + k\frac{{2\pi }}{3}.$

Do $x \in [0;\pi ]$ $\Rightarrow t = \frac{{2\pi }}{9}$, $t = \frac{{4\pi }}{9}$, $t = \frac{{8\pi }}{9}.$

Suy ra $x = 2\cos \frac{{2\pi }}{9}$, $x = 2\cos \frac{{4\pi }}{9}$, $x = 2\cos \frac{{8\pi }}{9}.$

Vì phương trình bậc ba có tối đa ba nghiệm nên phương trình trên có ba nghiệm: $x = 2\cos \frac{{2\pi }}{9}$, $x = 2\cos \frac{{4\pi }}{9}$, $x = 2\cos \frac{{8\pi }}{9}$ và không còn nghiệm nào khác nằm ngoài đoạn $x \in [ – 2;2].$

<!-- chunk:28 level:1 source:https://toanmath.com/2020/01/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-dua-ve-he-phuong-trinh.html -->
## C. BÀI TẬP TỰ LUYỆN
1. ĐỀ BÀI
1. Giải phương trình: $2{x^3} = 1 + \sqrt[3]{{\frac{{x + 1}}{2}}}.$

2. Giải phương trình: ${x^3} – 3\sqrt[3]{{3x + 2}} = 2.$

3. Giải phương trình: $2\sqrt[3]{{3x – 2}} + 3\sqrt {6 – 5x} – 8 = 0.$

4. Giải phương trình: $3 + \sqrt {3 + \sqrt x } = x.$

5. Giải phương trình: $2x = \sqrt[3]{{7 + \sqrt[3]{{\frac{{x + 7}}{8}}}}}.$

6. Giải phương trình: $x = 2007 + \sqrt {2007 + \sqrt x } .$

7. Giải phương trình: $2x = \sqrt {1 + \frac{3}{2}\sqrt {1 + 3x} } .$

8. Giải phương trình: $2x = \sqrt {3 + \frac{1}{2}\sqrt {3 + \frac{1}{2}\sqrt {3 + \frac{1}{2}\sqrt {x + 3} } } } .$

9. Giải phương trình: ${x^2} – 4x – 3 = \sqrt {x + 5} .$

10. Giải phương trình: ${x^2} – 2x – 3 = \sqrt {x + 3} .$

11. Giải phương trình: $3{x^2} + 6x – 3 = \sqrt {\frac{{x + 7}}{3}} .$

12. Giải phương trình: $7{x^2} + 7x = \sqrt {\frac{{4x + 9}}{{28}}} .$

13. Giải phương trình: $\sqrt {2x + 15} = 32{x^2} + 32x – 20.$

14. Giải phương trình: $\sqrt[3]{{3x – 5}} = 8{x^3} – 36{x^2} + 53x – 25.$

15. Giải phương trình: $\sqrt[3]{{81x – 8}} = {x^3} – 2{x^2} + \frac{4}{3}x – 2.$

16. Giải phương trình: $\sqrt {2{x^2} + 1} – \sqrt {{x^2} + 1} = {x^2}.$

17. Giải phương trình: $\sqrt {x + 3} + \sqrt[3]{x} = 3.$

18. Giải phương trình: $(x + 3)\sqrt { – {x^2} – 8x + 48} = x – 24.$

19. Giải phương trình: $\sqrt {2 – {x^2}} = {(2 – \sqrt x )^2}.$

20. Giải phương trình: $\sqrt {1 + \sqrt {1 – {x^2}} } \left[ {\sqrt {{{(1 – x)}^3}} – \sqrt {{{(1 + x)}^3}} } \right]$ $= 2 + \sqrt {1 – {x^2}} .$

21. Giải phương trình: $\sqrt {x + 3} – \sqrt {1 – x} = x + 1.$

22. Giải phương trình: $\sqrt {{x^2} + x + 1}$ $= 2x + \sqrt {{x^2} – x + 1} .$

23. Giải phương trình: $\sqrt {2{x^2} + x + 9}$ $+ \sqrt {2{x^2} – x + 1}$ $= x + 4.$

24. Giải phương trình: $\sqrt {{x^2} – 9x + 24}$ $– \sqrt {6{x^2} – 59x + 149}$ $= 5 – x.$

25. Giải phương trình: $\sqrt {2{x^2} + x + 1} + \sqrt {{x^2} – x + 1} = 3x.$

26. Giải phương trình: $\sqrt[3]{{{{(x + 1)}^2}}} + \sqrt[3]{{{x^2}}}$ $+ \sqrt[3]{{x(x + 1)}} = 1.$

27. Giải phương trình: $(x + 5)\sqrt {x + 1} + 1 = \sqrt[3]{{3x + 4}}.$

28. Giải phương trình: $8{x^2} – 13x + 7$ $= \left( {1 + \frac{1}{x}} \right)\sqrt[3]{{3{x^2} – 2}}.$

29. Giải phương trình: $2x + 1 + x\sqrt {{x^2} + 2}$ $+ (x + 1)\sqrt {{x^2} + 2x + 3} = 0.$

30. Giải phương trình: ${x^2} – 2x – 4$ $= \left( {\frac{1}{x} – 2} \right)\sqrt[3]{{3{x^2} + 6x + 2}}.$

31. Giải phương trình: $\sqrt {2 – \sqrt 2 (1 + x)} + \sqrt[4]{{2x}} = 1.$

32. Giải phương trình: ${x^2}\sqrt x + {(x – 5)^2}\sqrt {5 – x}$ $= 11(\sqrt x + \sqrt {5 – x} ).$

2. ĐÁP SỐ
1. $x = 1.$

2. $x = – 1$, $x = 2.$

3. $x = – 2.$

4. $x = \frac{{7 + \sqrt {13} }}{2}.$

5. $x = 1.$

6. $x = \frac{{8030 + 2\sqrt {8029} }}{4}.$

7. $x = 1.$

8. $x = 1.$

9. $x = – 1$, $x = \frac{{5 + \sqrt {29} }}{2}.$

10. $x = \frac{{3 + \sqrt {17} }}{2}$, $x = \frac{{1 – \sqrt {13} }}{2}.$

11. $x = \frac{{\sqrt {73} – 5}}{6}$, $x = \frac{{ – \sqrt {69} – 7}}{6}.$

12. $\frac{{ – 6 + 5\sqrt 2 }}{{14}}$, $\frac{{ – 8 – \sqrt {46} }}{{14}}.$

13. $x = \frac{1}{2}$, $x = \frac{{ – 9 – \sqrt {221} }}{{16}}.$

14. $x = 2$, $x = \frac{{5 \pm \sqrt 3 }}{4}.$

15. $x = 0$, $x = \frac{{3 \pm 2\sqrt 6 }}{3}.$

16. $x = 0.$

17. $x = 1.$

18. $x = – 2 – 2\sqrt 7$, $x = – 5 – \sqrt {31} .$

19. $x = 1.$

20. $x = – \frac{{\sqrt 2 }}{2}.$

21. $x = \pm 1$, $x = – 3.$

22. $x = 0.$

23. $x = 0$, $x = \frac{8}{7}.$

24. $x = 5$, $x = \frac{{19}}{3}.$

25. $x = 1$, $x = – \frac{8}{7}.$

26. $x = – 1$, $x = 0.$

27. $x = – 1.$

28. $x = 1$, $x = – \frac{1}{8}.$

29. $x = – \frac{1}{2}.$

30. $x = 2\cos \frac{\pi }{9}$, $x = 2\cos \frac{{5\pi }}{9}$, $x = 2\cos \frac{{7\pi }}{9}.$

31. $x = {\left( {\frac{{1 \pm \sqrt {\frac{{4 – 3\sqrt[4]{2}}}{{\sqrt[4]{2}}}} }}{2}} \right)^4}.$

32. $x = 1$, $x = 4.$