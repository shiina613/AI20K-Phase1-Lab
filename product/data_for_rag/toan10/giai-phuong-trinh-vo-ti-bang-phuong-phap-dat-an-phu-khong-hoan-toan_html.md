# Giải phương trình vô tỉ bằng phương pháp đặt ẩn phụ không hoàn toàn

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
Bài viết hướng dẫn cách giải phương trình vô tỉ bằng phương pháp đặt ẩn phụ không hoàn toàn, đây là dạng toán thường gặp trong chương trình Đại số 10: phương trình và hệ phương trình.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN
+ Đặt $t = u(x)$, đưa về phương trình theo ẩn $t$ (thông thường là phương trình bậc hai), nhưng hệ số vẫn còn chứa $x.$ Tính $\Delta$ theo $x$ (ta sẽ được $\Delta$ là bình phương của một đa thức theo $x$).

+ Nếu ta tính $\Delta$ không là bình phương của một đa thức theo $x$, khi đó ta phải điều chỉnh hệ số của ${t^2}$ hoặc của ${x^2}$ sao cho tính được $\Delta$ là bình phương của một đa thức theo $x.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 1. Giải phương trình ${x^2} – 2x – 1$ $– 2(1 – x)\sqrt {{x^2} + 2x – 1} = 0.$

Điều kiện: ${x^2} + 2x – 1 \ge 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \le – 1 – \sqrt 2 }\\
{x \ge – 1 + \sqrt 2 }
\end{array}} \right..
$$

Phương trình đã cho tương đương ${x^2} + 2x – 1$ $– 2(1 – x)\sqrt {{x^2} + 2x – 1}$ $– 4x = 0.$

Đặt $t = \sqrt {{x^2} + 2x – 1}$, $t \ge 0$ $\Rightarrow {t^2} = {x^2} + 2x – 1.$

Khi đó phương trình đã cho trở thành ${t^2} – 2(1 – x)t – 4x = 0$ $(1).$

Ta xem phương trình $(1)$ là phương trình bậc hai theo ẩn $t$, xem $x$ là tham số.

Ta có: $\Delta ‘ = {(1 – x)^2} – ( – 4x)$ $= {x^2} – 2x + 1 + 4x$ $= {(x + 1)^2}.$

Từ đó ta tìm được nghiệm của phương trình $(1)$ là:

$$
\left[ {\begin{array}{l}
{t = 1 – x + 1 + x = 2}\\
{t = 1 – x – 1 – x = – 2x}
\end{array}} \right..
$$

+ Với $t = 2$, ta có: $\sqrt {{x^2} + 2x – 1} = 2$ $\Leftrightarrow {x^2} + 2x – 5 = 0$ $\Leftrightarrow x = – 1 \pm \sqrt 6 .$

+ Với $t = – 2x$, ta có:

$\sqrt {{x^2} + 2x – 1} = – 2x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 2x \ge 0}\\
{{x^2} + 2x – 1 = 4{x^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 0}\\
{3{x^2} – 2x + 1 = 0}
\end{array}} \right.
$$
 (vô nghiệm).

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = – 1 \pm \sqrt 6 .$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 2. Giải phương trình ${x^2} + 3x + 1$ $= (x + 3)\sqrt {{x^2} + 1} .$

Đặt $t = \sqrt {{x^2} + 1}$, $t \ge 1.$ Phương trình đã cho trở thành: ${t^2} – (x + 3)t + 3x = 0$ $(1).$

Phương trình $(1)$ có $\Delta = {(x + 3)^2} – 12x$ $= {(x – 3)^2}.$ Nên phương trình $(1)$ có nghiệm 
$$
\left[ {\begin{array}{l}
{t = 3}\\
{t = x}
\end{array}} \right..
$$

+ Với $t = x$ $\Rightarrow \sqrt {{x^2} + 1} = x$ (phương trình vô nghiệm).

+ Với $t = 3$ $\Rightarrow \sqrt {{x^2} + 1} = 3$ $\Leftrightarrow x = \pm 2\sqrt 2 .$

Kết luận: nghiệm của phương trình là $x = \pm 2\sqrt 2 .$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 3. Giải phương trình $(4x – 1)\sqrt {{x^2} + 1}$ $= 2{x^2} + 2x + 1.$

Ta có phương trình đã cho tương đương $(4x – 1)\sqrt {{x^2} + 1}$ $= 2\left( {{x^2} + 1} \right) + 2x – 1$ $(1).$

Đặt $u = \sqrt {{x^2} + 1} \ge 1.$ Phương trình $(1)$ trở thành:

$(4x – 1)u = 2{u^2} + 2x – 1.$

$\Leftrightarrow 2{u^2} – (4x – 1)u + 2x – 1 = 0$ $(2).$

Ta xem phương trình $(2)$ là phương trình ẩn $u$ (mà hệ số vẫn chứa $x$).

Phương trình $(2)$ có $\Delta = {(4x – 1)^2} – 8(2x – 1)$ $= {(4x – 3)^2}.$

Phương trình $(2)$ có nghiệm là: 
$$
\left[ {\begin{array}{l}
{u = \frac{{4x – 1 + (4x – 3)}}{4} = 2x – 1}\\
{u = \frac{{4x – 1 – (4x – 3)}}{4} = \frac{1}{2} < 1\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Với $u = 2x – 1$ $\Rightarrow \sqrt {{x^2} + 1} = 2x – 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2x – 1 \ge 0}\\
{{x^2} + 1 = {{(2x – 1)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge \frac{1}{2}}\\
{3{x^2} – 4x = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{4}{3}.$

Kết luận: nghiệm của phương trình là: $x = \frac{4}{3}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 4. Giải phương trình $(3x + 2)\sqrt {2x – 3}$ $= 2{x^2} + 3x – 6.$

Điều kiện: $x \ge \frac{3}{2}.$

Phương trình đã cho tương đương $2x – 3$ $– (3x + 2)\sqrt {2x – 3}$ $+ 2{x^2} + x – 3 = 0$ $(1).$

Đặt $t = \sqrt {2x – 3}$, $t \ge 0.$ Phương trình $(1)$ trở thành ${t^2} – (3x + 2)t + 2{x^2} + x – 3 = 0.$

Phương trình $(1)$ có $\Delta = 9{x^2} + 12x + 4$ $– 4\left( {2{x^2} + x – 3} \right)$ $= {(x + 4)^2}.$

Nên phương trình $(1)$ có nghiệm 
$$
\left[ {\begin{array}{l}
{t = 2x + 3}\\
{t = x – 1}
\end{array}} \right..
$$

+ Với $t = 2x + 3$ $\Rightarrow \sqrt {2x – 3} = 2x + 3.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2x + 3 \ge 0}\\
{2x – 3 = 4{x^2} + 12x + 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2x + 3 \ge 0}\\
{4{x^2} + 10x + 12 = 0}
\end{array}} \right.
$$
 (vô nghiệm).

+ Với $t = x – 1$ $\Rightarrow \sqrt {2x – 3} = x – 1$ $\Leftrightarrow x = 2.$

Kết luận: phương trình có nghiệm duy nhất là $x = 2.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 5. Giải phương trình $\sqrt {x + 8} = \frac{{3{x^2} + 7x + 8}}{{4x + 2}}.$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x + 8 \ge 0}\\
{4x + 2 \ne 0}
\end{array}} \right..
$$

Phương trình tương đương $(x + 8)$ $– (4x + 2)\sqrt {x + 8}$ $+ 3{x^2} + 6x = 0$ $(1).$

Đặt $t = \sqrt {x + 8} \ge 0.$ Phương trình $(1)$ trở thành ${t^2} – (4x + 2)t + 3{x^2} + 6x = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 3x}\\
{t = x + 2}
\end{array}} \right..
$$

+ Với $t = 3x$ $\Rightarrow \sqrt {x + 8} = 3x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{9{x^2} – x – 8 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

+ Với $t = x + 2$ $\Rightarrow \sqrt {x + 8} = x + 2$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – 2}\\
{{x^2} + 3x – 4 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x=1.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 6. Giải phương trình $\sqrt {{x^2} + x + 2}$ $= \frac{{3{x^2} + 3x + 2}}{{3x + 1}}.$

Điều kiện: $3x + 1 \ne 0.$

Phương trình đã cho tương đương:

$\left( {{x^2} + x + 2} \right)$ $– (3x + 1)\sqrt {{x^2} + x + 2}$ $+ 2{x^2} + 2x = 0.$

Đặt $t = \sqrt {{x^2} + x + 2}$, $t \ge \frac{{\sqrt 7 }}{2}.$

Phương trình trên trở thành:

${t^2} – (3x + 1)t + 2{x^2} + 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 2x}\\
{t = x + 1}
\end{array}} \right..
$$

$$
\Rightarrow \left[ {\begin{array}{l}
{\sqrt {{x^2} + x + 2} = 2x}\\
{\sqrt {{x^2} + x + 2} = x + 1}
\end{array}} \right..
$$

+ Với $\sqrt {{x^2} + x + 2} = 2x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{3{x^2} – x – 2 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

+ Với $\sqrt {{x^2} + x + 2} = x + 1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – 1}\\
{x + 2 = 2x + 1}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x=1.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 7. Giải phương trình ${x^2} + x + 12\sqrt {x + 1} = 36$ $(1).$

Điều kiện: $x \ge – 1.$

Khi đó phương trình $(1)$ $\Leftrightarrow x(x + 1) + 12\sqrt {x + 1} = 36$ $(2).$

Nhận xét: $x=0$ không phải là nghiệm của phương trình $(1).$

Ta xét $– 1 \le x \ne 0.$ Đặt $u = \sqrt {x + 1} \ge 0.$ Phương trình $(2)$ trở thành:

$x{u^2} + 12u – 36 = 0$ $(3).$

Ta xem phương trình $(3)$ là phương trình bậc hai đối với ẩn $u$ (mà hệ số vẫn chứa $x$).

Phương trình $(3)$ có $\Delta ‘ = 36 + 36x$ $= 36(1 + x)$ $= 36{u^2}.$

Khi đó, phương trình $(3)$ có các nghiệm: $u = \frac{{ – 6 \pm 6u}}{x}.$

+ Với $u = \frac{{ – 6 – 6u}}{x}$ $\Leftrightarrow xu + 6u = – 6$ $\Leftrightarrow (x + 6)u = – 6$ (vô nghiệm) (do $x + 6 > 0$ $\Rightarrow (x + 6)u > 0$).

+ Với $u = \frac{{ – 6 + 6u}}{x}$ $\Leftrightarrow xu = 6u – 6$ $\Leftrightarrow 6 = (6 – x)u$ $\Leftrightarrow 6 = (6 – x)\sqrt {x + 1} .$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{(x + 1)\left( {{x^2} – 12x + 36} \right) = 36}\\
{ – 1 \le x < 6}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x\left( {{x^2} – 11x + 24} \right) = 0}\\
{ – 1 \le x < 6}
\end{array}} \right.
$$
 $\Leftrightarrow x = 3.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = 3.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 8. Giải phương trình $(3x + 1)\sqrt {2{x^2} – 1}$ $= 5{x^2} + \frac{3}{2}x – 3.$

Điều kiện: $x \le – \frac{{\sqrt 2 }}{2}$ hoặc $x \ge \frac{{\sqrt 2 }}{2}.$

Phương trình đã cho tương đương:

$2(3x + 1)\sqrt {2{x^2} – 1}$ $= 10{x^2} + 3x – 6.$

$\Leftrightarrow 2(3x + 1)\sqrt {2{x^2} – 1}$ $= 4\left( {2{x^2} – 1} \right)$ $+ 2{x^2} + 3x – 2.$

Đặt $t = \sqrt {2{x^2} – 1}$, $t \ge 0.$ Phương trình trên trở thành $4{t^2} – 2(3x + 1)t$ $+ 2{x^2} + 3x – 2 = 0.$

Ta có: $\Delta ‘ = {(3x + 1)^2} – 4\left( {2{x^2} + 3x – 2} \right)$ $= {(x – 3)^2}.$

Từ đó ta có phương trình có nghiệm: 
$$
\left[ {\begin{array}{l}
{t = \frac{{2x – 1}}{2}}\\
{t = \frac{{x + 2}}{2}}
\end{array}} \right..
$$

Thay vào cách đặt, giải ra ta được phương trình có các nghiệm:

$x = \frac{{ – 1 + \sqrt 6 }}{2}$, $x = \frac{{2 \pm \sqrt {60} }}{7}.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 9. Giải phương trình $2x + \frac{{x – 1}}{x}$ $– \frac{{\sqrt {x – 1} }}{{\sqrt x }}$ $– 3\sqrt {x – \frac{1}{x}} = 0$ $(1).$

Điều kiện: $x \ge 1.$

Khi đó phương trình $(1)$ $\Leftrightarrow 2x + \frac{{x – 1}}{x}$ $– \sqrt {1 – \frac{1}{x}}$ $– 3\sqrt {\frac{{x – 1}}{x}(x + 1)} = 0$ $(2).$

Đặt: $u = \sqrt {\frac{{x – 1}}{x}} .$ Phương trình $(2)$ trở thành:

${u^2} – u – 3u\sqrt {x + 1} + 2x = 0.$

$\Leftrightarrow {u^2} – (1 + 3\sqrt {x + 1} )u + 2x = 0.$

Ta có: $\Delta = {(1 + 3\sqrt {x + 1} )^2} – 8x$ $= {(\sqrt {x + 1} + 3)^2}.$

Nên phương trình có nghiệm 
$$
\left[ {\begin{array}{l}
{u = 2(\sqrt {x + 1} + 1)}\\
{u = \sqrt {x + 1} – 1}
\end{array}} \right..
$$

Do $u = \sqrt {\frac{{x – 1}}{x}}$ $= \sqrt {1 – \frac{1}{x}} < 1$ (khi $x \ge 1$) vì vậy nghiệm $u = 2(\sqrt {x + 1} + 1)$ bị loại.

Với $u = \sqrt {x + 1} – 1$ $\Rightarrow \sqrt {\frac{{x – 1}}{x}} = \sqrt {x + 1} – 1$ $\Leftrightarrow {(x – \sqrt {x + 1} )^2} = 0.$

$\Leftrightarrow x = \sqrt {x + 1}$ $\Leftrightarrow {x^2} – x + 1 = 0$ $\Rightarrow x = \frac{{1 + \sqrt 5 }}{2}.$

Kết luận: phương trình có nghiệm duy nhất $x = \frac{{1 + \sqrt 5 }}{2}.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 10. Giải phương trình $4\sqrt {1 + x} – 1$ $= 3x + 2\sqrt {1 – x} + \sqrt {1 – {x^2}}$ $(1).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{1 + x \ge 0}\\
{1 – x \ge 0}\\
{1 – {x^2} \ge 0}
\end{array}} \right.
$$
 $\Leftrightarrow – 1 \le x \le 1.$

Khi đó phương trình $(1)$ $\Leftrightarrow 4\sqrt {1 + x} – 2 – 2x + (1 – x)$ $= 2\sqrt {1 – x} + \sqrt {1 + x} \sqrt {1 – x}$ $(2).$

Đặt: $u = \sqrt {1 – x}$ $(0 \le u \le \sqrt 2 )$ $\Rightarrow {u^2} = 1 – x.$ Phương trình $(2)$ trở thành:

${u^2} – (2 + \sqrt {1 + x} )u$ $– 2(1 + x – 2\sqrt {1 + x} ) = 0.$

Ta có $\Delta = {(2 + \sqrt {1 + x} )^2}$ $+ 8(1 + x – 2\sqrt {1 – x} ).$

$= 4 + 9(1 + x) – 12\sqrt {1 + x}$ $= {(3\sqrt {1 + x} – 2)^2}.$

Nên phương trình có nghiệm 
$$
\left[ {\begin{array}{l}
{u = \frac{{2 + \sqrt {1 + x} + (3\sqrt {1 + x} – 2)}}{2}}\\
{u = \frac{{2 + \sqrt {1 + x} – (3\sqrt {1 + x} – 2)}}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = 2\sqrt {x + 1} }\\
{u = 2 – \sqrt {1 + x} }
\end{array}} \right..
$$

+ Với $u = 2\sqrt {x + 1}$ $\Rightarrow \sqrt {1 – x} = 2\sqrt {x + 1}$ $\Leftrightarrow x = \frac{{ – 3}}{5}.$

+ Với $u = 2 – \sqrt {1 + x}$ $\Rightarrow \sqrt {1 – x} = 2 – \sqrt {1 + x}$ $\Leftrightarrow \sqrt {1 – x} + \sqrt {1 + x} = 2.$

$\Leftrightarrow 2 + 2\sqrt {1 – {x^2}} = 4$ $\Leftrightarrow \sqrt {1 – {x^2}} = 1$ $\Leftrightarrow x = 0.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = – \frac{3}{5}$, $x = 0.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 11. Giải phương trình $3(\sqrt {2{x^2} + 1} – 1)$ $= x(1 + 3x + 8\sqrt {2{x^2} + 1} )$ $(1).$

Ta có phương trình $(1)$ $\Leftrightarrow 3{x^2} + x + 3$ $+ (8x – 3)\sqrt {2{x^2} + 1} = 0.$

$\Leftrightarrow 3\left( {{x^2} + 3} \right)$ $+ (8x – 3)\sqrt {2{x^2} + 1}$ $– 3{x^2} + x = 0$ $(2).$

Đặt $t = \sqrt {2{x^2} + 1}$, $t \ge 1.$ Phương trình $(2)$ trở thành $3{t^2} + (8x – 3)t – 3{x^2} + x = 0.$

Ta có $\Delta = {(10x – 3)^2}.$

Nên phương trình có nghiệm 
$$
\left[ {\begin{array}{l}
{t = \frac{x}{3}}\\
{t = 1 – 3x}
\end{array}} \right..
$$

+ Với $t = \frac{x}{3}$ $\Rightarrow \sqrt {2{x^2} + 1} = \frac{x}{3}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{2{x^2} + 1 = \frac{{{x^2}}}{9}}
\end{array}} \right.
$$
 (vô nghiệm).

+ Với $t = 1 – 3x$ $\Rightarrow \sqrt {2{x^2} + 1} = 1 – 3x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le \frac{1}{3}}\\
{7{x^2} – 6x = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 0.$

Kết luận: phương trình có một nghiệm là $x = 0.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 12. Giải phương trình $2\sqrt {2x + 4} + 4\sqrt {2 – x}$ $= \sqrt {9{x^2} + 16} .$

Điều kiện: $|x| \le 2.$

Với điều kiện trên phương trình tương đương:

$4(2x + 4)$ $+ 16(2 – x)$ $+ 16\sqrt {2\left( {4 – {x^2}} \right)}$ $= 9{x^2} + 16.$

$\Leftrightarrow 8\left( {4 – {x^2}} \right)$ $+ 16\sqrt {2\left( {4 – {x^2}} \right)}$ $= {x^2} + 8x$ $(1).$

Đặt $t = \sqrt {2\left( {4 – {x^2}} \right)} \ge 0.$ Phương trình $(1)$ trở thành $4{t^2} + 16t – {x^2} – 8x = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{x}{2}}\\
{t = – \frac{x}{2} – 4 < 0}
\end{array}} \right.
$$
 $\Rightarrow t = \frac{x}{2}$ $\Rightarrow \sqrt {2\left( {4 – {x^2}} \right)} = \frac{x}{2}.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ge 0}\\
{8\left( {4 – {x^2}} \right) = {x^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{{4\sqrt 2 }}{3}.$

Kết luận: phương trình có nghiệm duy nhất $x = \frac{{4\sqrt 2 }}{3}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 13. Giải phương trình $\left( {{x^2} + 2} \right)\sqrt {{x^2} – x + 1}$ $= {x^3} + 2{x^2} – 3x + 1$ $(1).$

Ta có phương trình $(1)$ $\Leftrightarrow \left( {{x^2} – x + 1} \right)$ $– \left( {{x^2} + 2} \right)\sqrt {{x^2} – x + 1}$ $+ {x^3} + {x^2} – 2x = 0$ $(2).$

Đặt $t = \sqrt {{x^2} – x + 1} .$ Phương trình $(2)$ trở thành ${t^2} – \left( {{x^2} + 2} \right)t$ $+ {x^3} + {x^2} – 2x = 0.$

Ta có $\Delta = {\left( {{x^2} – 2x – 2} \right)^2}$, suy ra 
$$
\left[ {\begin{array}{l}
{t = {x^2} – x}\\
{t = x + 2}
\end{array}} \right..
$$

+ Với $t = x + 2$ ta được $\sqrt {{x^2} – x + 1} = x + 2$ $\Leftrightarrow x = – \frac{3}{5}.$

+ Với $t = {x^2} – x$ ta được $\sqrt {{x^2} – x + 1} = {x^2} – x$ $\Leftrightarrow x = \frac{{1 \pm \sqrt {3 + 2\sqrt 5 } }}{2}.$

Kết luận: phương trình có ba nghiệm là: $x = – \frac{3}{5}$, $x = \frac{{1 \pm \sqrt {3 + 2\sqrt 5 } }}{2}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## Ví dụ 14. Giải phương trình $\frac{{3\sqrt {19} }}{{{x^3}}} – 2{x^3} + \frac{{25}}{x} + \sqrt {19} x = 0$ $(1).$

Điều kiện: $x \ne 0.$

Ta có phương trình $(1)$ $\Leftrightarrow \frac{{3\sqrt {19} }}{{{x^3}}} – 2{x^3}$ $+ \frac{{19 + 6}}{x} + \sqrt {19} x = 0$ $(2).$

Đặt $u = \sqrt {19} .$ Phương trình $(2)$ trở thành $\frac{{3u}}{{{x^3}}} – 2{x^3} + \frac{{{u^2} + 6}}{x} + ux = 0.$

$\Leftrightarrow {x^2}{u^2} + \left( {{x^4} + 3} \right)u – 2{x^6} + 6{x^2} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = – 2{x^2}}\\
{u = \frac{{{x^4} – 3}}{{{x^2}}}}
\end{array}} \right..
$$

+ Với $u = – 2{x^2}$ $\Rightarrow \sqrt {19} = – 2{x^2}$ (vô nghiệm).

+ Với $u = \frac{{{x^4} – 3}}{{{x^2}}}$ $\Rightarrow \sqrt {19} = \frac{{{x^4} – 3}}{{{x^2}}}$ $\Leftrightarrow {x^2} = \frac{{\sqrt {19} + \sqrt {31} }}{2}$ $\Leftrightarrow x = \pm \sqrt {\frac{{\sqrt {19} + \sqrt {31} }}{2}} .$

Kết luận: phương trình có nghiệm hai nghiệm là $x = \pm \sqrt {\frac{{\sqrt {19} + \sqrt {31} }}{2}} .$

Nhận xét: Ta thấy rằng đây là một bài toán có cách giải tương đối lạ. Việc nghĩ ra cách đặt $u = \sqrt {19}$ là không hề tự nhiên. Tuy nhiên việc đặt như vậy để được phương trình ${x^2}{u^2} + \left( {{x^4} + 3} \right)u – 2{x^6} + 6{x^2} = 0$ sau đó xem phương trình trên là phương trình ẩn $u$ là một ý tưởng hết sức táo bạo. Đến đây ta sẽ đặt câu hỏi liệu còn cách giải nào khác tự nhiên hơn không, hay chỉ có một cách duy nhất do tác giả bài toán nghĩ ra, và ta có thể xây dựng được một lớp các bài toán tương tự hay không?

<!-- chunk:16 level:1 source:https://toanmath.com/2019/12/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-khong-hoan-toan.html -->
## III. BÀI TẬP TỰ LUYỆN
## Bài tập
## Bài tập 1. Giải phương trình $2{x^2} + x + 3 = 3x\sqrt {x + 3} .$

## Bài tập 2. Giải phương trình $(1 – 2x)\sqrt {{x^2} + 1}$ $– 2{x^2} – 7x – 1 = 0.$

## Bài tập 3. Giải phương trình $3{x^2} + 2x + 3$ $= (3x + 1)\sqrt {{x^2} + 3} .$

## Bài tập 4. Giải phương trình $(x + 1)\sqrt {{x^2} – 2x + 3} = {x^2} + 1.$

## Bài tập 5. Giải phương trình ${x^2} + 3x + 4$ $= (x + 3)\sqrt {{x^2} + x + 2} .$

## Bài tập 6. Giải phương trình $(1 – 2x)\sqrt {2{x^2} + x + 1}$ $– {x^2} – 6x – 1 = 0.$

## Bài tập 7. Giải phương trình $\frac{{x + 2 + x\sqrt {2x + 1} }}{{x + \sqrt {2x + 1} }} = \sqrt {x + 2} .$

## Bài tập 8. Giải phương trình ${x^2} + (3 – \sqrt {{x^2} + 2} )x$ $= 1 + 2\sqrt {{x^2} + 2} .$

## Bài tập 9. Giải phương trình $15{x^2} + 2(x + 1)\sqrt {x + 2} = 2 – 5x.$

## Bài tập 10. Giải phương trình $(4x – 1)\sqrt {{x^3} + 1}$ $= 2{x^3} + 2x + 1.$

## Bài tập 11. Giải phương trình $(1 – 2x)\sqrt {{x^2} + 1}$ $+ \frac{{{x^2}}}{2} – \frac{7}{2}x + 1 = 0.$

## Bài tập 12. Giải phương trình $\sqrt {{x^2} – x + 1}$ $= \frac{{{x^3} + 3{x^2} – 4x + 1}}{{{x^2} + 3}}.$

## Bài tập 13. Giải phương trình $\left( {{x^3} – 3x + 1} \right)\sqrt {{x^2} + 21}$ $+ {x^4} – 3{x^2} + x = 21.$

## Bài tập 14. Giải phương trình $3x + 2\sqrt {3 – x} + \sqrt {4x – {x^2} – 3}$ $= 4\sqrt {x – 1} + 5.$

2. Đáp số
## Bài tập 1. $x = 1$, $x = \frac{{1 + \sqrt {13} }}{2}.$

2. $x = 0.$

3. $x = 1.$

## Bài tập 4. $x = 1 \pm \sqrt 2 .$

## Bài tập 5. $x = – 2$, $x = 1.$

6. $x = 0.$

## Bài tập 7. $x = 1$, $x = 2.$

## Bài tập 8. $x = \pm \sqrt 7 .$

## Bài tập 9. $x = \frac{{ – 19 + \sqrt {161} }}{{50}}$, $x = \frac{{1 – \sqrt {73} }}{{18}}.$

## Bài tập 10. $x = – \sqrt[3]{{\frac{3}{4}}}$, $x = 2.$

## Bài tập 11. $x = \frac{{ – 3 + 2\sqrt 6 }}{5}.$

## Bài tập 12. $x = – \frac{8}{7}$, $x = \frac{{1 \pm \sqrt {3 + 2\sqrt 5 } }}{2}.$

13. $x = 2.$

## Bài tập 14. $x = 2$, $x = \frac{7}{5}.$