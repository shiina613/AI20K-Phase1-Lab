# Giải phương trình vô tỉ bằng phương pháp đặt ẩn phụ hoàn toàn

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
Bài viết hướng dẫn giải phương trình vô tỉ bằng phương pháp đặt ẩn phụ hoàn toàn, đây là dạng toán thường gặp trong chương trình Đại số 10: phương trình và hệ phương trình.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN
Đặt $t = u(x)$, đưa về phương trình theo $t.$

Tuy nhiên trong một số bài toán, ta phải thêm bớt, nhóm, hoặc chia hai vế của phương trình cho một biểu thức nào đó, khi đó mới xuất hiện ẩn phụ $t = u(x).$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 1. Giải phương trình ${x^2} + 4x – 7 + \sqrt {{x^2} + 4x – 1} = 0.$

Điều kiện: ${x^2} + 4x – 1 \ge 0.$

Đặt $t = \sqrt {{x^2} + 4x – 1}$, điều kiện: $t \ge 0.$

Suy ra ${t^2} = {x^2} + 4x – 1.$

Phương trình đã cho trở thành: ${t^2} + t – 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 2}\\
{t = – 3}
\end{array}} \right.
$$
 $\Rightarrow t = 2.$

Với $t = 2$ $\Rightarrow \sqrt {{x^2} + 4x – 1} = 2$ $\Leftrightarrow {x^2} + 4x – 1 = 4$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – 5}
\end{array}} \right..
$$

Thử vào điều kiện, ta được nghiệm của phương trình là: $x=1$, $x=-5.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 2. Giải phương trình $\sqrt {{x^2} – 4x + 5} + 3 = 4x – {x^2}.$

Đặt $t = \sqrt {{x^2} – 4x + 5} .$ Do ${x^2} – 4x + 5$ $= {(x – 2)^2} + 1 \ge 1$, $\forall x \in R$ nên điều kiện là: $t \ge 1.$

Suy ra ${t^2} = {x^2} – 4x + 5.$

Phương trình đã cho trở thành: $t – 2 = – {t^2}.$

$\Leftrightarrow {t^2} + t – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = – 2}
\end{array}} \right.
$$
 $\Rightarrow t = 1.$

Với $t = 1$ $\Rightarrow \sqrt {{x^2} – 4x + 5} = 1$ $\Leftrightarrow {x^2} – 4x + 5 = 1$ $\Leftrightarrow x = 2.$

Kết luận: phương trình có một nghiệm là $x = 2.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 3. Giải phương trình ${x^2} + 2x – 2 + 3\sqrt { – {x^2} – 2x} = 0.$

Điều kiện: $– {x^2} – 2x \ge 0.$

Đặt $t = \sqrt { – {x^2} – 2x} .$ Do $– {x^2} – 2x = – {(x + 1)^2} + 1 \le 1$ nên điều kiện là: $0 \le t \le 1.$

Suy ra ${t^2} = – {x^2} – 2x.$

Phương trình đã cho trở thành: $– {t^2} – 2 + 3t = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 2}\\
{t = 1}
\end{array}} \right.
$$
 $\Rightarrow t = 1.$

Với $t = 1$ $\Rightarrow \sqrt { – {x^2} – 2x} = 1$ $\Leftrightarrow x = – 1.$

Thử vào điều kiện, ta được nghiệm của phương trình là $x = -1.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 4. Giải phương trình $4\sqrt {{x^2} – 6x + 6} = {x^2} – 6x + 9.$

Điều kiện: ${x^2} – 6x + 6 \ge 0.$

Đặt $t = \sqrt {{x^2} – 6x + 6} .$ Điều kiện: $t \ge 0.$ Suy ra ${t^2} = {x^2} – 6x + 6.$

Phương trình đã cho trở thành: $4t = {t^2} + 3$ $\Leftrightarrow {t^2} – 4t + 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 3}\\
{t = 1}
\end{array}} \right..
$$

Từ đó ta được: 
$$
\left[ {\begin{array}{l}
{\sqrt {{x^2} – 6x + 6} = 3}\\
{\sqrt {{x^2} – 6x + 6} = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} – 6x + 6 = 9}\\
{{x^2} – 6x + 6 = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 3 \pm 2\sqrt 3 }\\
{x = 5}\\
{x = 1}
\end{array}} \right..
$$

Thử vào điều kiện, ta được nghiệm của phương trình là:

$x = 3 \pm 2\sqrt 3$, $x = 5$, $x = 1.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 5. Giải phương trình $\sqrt {{x^2} – 3x + 3} + \sqrt {{x^2} – 3x + 6} = 3.$

Đặt $t = {x^2} – 3x + 3$ $= {\left( {x – \frac{3}{2}} \right)^2} + \frac{3}{4}$ $\Rightarrow t \ge \frac{3}{4}.$

Phương trình đã cho trở thành: $\sqrt t + \sqrt {t + 3} = 3$ $\Leftrightarrow 2t + 3 + 2\sqrt {t(t + 3)} = 9.$

$\Leftrightarrow \sqrt {{t^2} + 3t} = 3 – t$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{3 – t \ge 0}\\
{{t^2} + 3t = {{(3 – t)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{t \le 3}\\
{9t – 9 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow t = 1.$

Với $t = 1$ $\Rightarrow {x^2} – 3x + 3 = 1$ $\Leftrightarrow {x^2} – 3x + 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 2}
\end{array}} \right..
$$

Kết luận: phương trình có nghiệm là $x = 1$, $x = 2.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 6. Giải phương trình $\sqrt[3]{{2 – x}} = 1 – \sqrt {x – 1} .$

Điều kiện: $x \ge 1.$

Đặt $t = \sqrt[3]{{2 – x}}$ $\Rightarrow x = 2 – {t^3}.$

Phương trình đã cho trở thành:

$t = 1 – \sqrt {1 – {t^3}}$ $\Leftrightarrow \sqrt {1 – {t^3}} = 1 – t$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{t \le 1}\\
{1 – {t^3} = {{(1 – t)}^2}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{t \le 1}\\
{t\left( {{t^2} + t – 2} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
t \le 1\\
\left[ {\begin{array}{l}
{t = 0}\\
{t = 1}\\
{t = – 2}
\end{array}} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = 1}\\
{t = – 2}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{x = 2}\\
{x = 1}\\
{x = 10}
\end{array}} \right..
$$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = 1$, $x = 2$, $x = 10.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 7. Giải phương trình $\sqrt {3x – 2} + \sqrt {x – 1}$ $= 4x – 9$ $+ 2\sqrt {3{x^2} – 5x + 2} .$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{3x – 2 \ge 0}\\
{x – 1 \ge 0}
\end{array}} \right.
$$
 $\Leftrightarrow x \ge 1.$

Đặt $t = \sqrt {3x – 2} + \sqrt {x – 1}$, điều kiện: $t \ge 1.$

Suy ra ${t^2} = 3x – 2 + x – 1$ $+ 2\sqrt {(3x – 2)(x – 1)} .$

$\Rightarrow 4x + 2\sqrt {3{x^2} – 5x + 2} = {t^2} + 3.$

Khi đó phương trình đã cho trở thành:

$t = {t^2} – 6$ $\Leftrightarrow {t^2} – t – 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 3}\\
{t = – 2}
\end{array}} \right.
$$
 $\Rightarrow t = 3.$

Với $t = 3$ $\Rightarrow \sqrt {3x – 2} + \sqrt {x – 1} = 3$ $\Leftrightarrow \sqrt {3{x^2} – 5x + 2} = 6 – 2x.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{6 – 2x \ge 0}\\
{3{x^2} – 5x + 2 = {{(6 – 2x)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 3}\\
{{x^2} – 19x + 34 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 3}\\
{\left[ {\begin{array}{l}
{x = 17}\\
{x = 2}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow x = 2.$

So sánh với điều kiện, ta được nghiệm của phương trình là $x = 2.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 8. Giải phương trình $3\sqrt {2 + x}$ $– 6\sqrt {2 – x}$ $+ 4\sqrt {4 – {x^2}}$ $= 10 – 3x.$

Điều kiện: $– 2 \le x \le 2.$

Đặt: $t = \sqrt {2 + x} – 2\sqrt {2 – x} .$ Điều kiện: $– 4 \le t \le 2.$

Suy ra ${t^2} = 2 + x$ $+ 4(2 – x)$ $– 4\sqrt {4 – {x^2}}$ $= 10 – 3x$ $– 4\sqrt {4 – {x^2}} .$

Phương trình đã cho trở thành:

$3t = {t^2}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = 3\:\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Rightarrow t = 0$ $\Rightarrow \sqrt {2 + x} – 2\sqrt {2 – x} = 0$ $\Leftrightarrow x = \frac{6}{5}.$

So sánh với điều kiện, ta được nghiệm của phương trình là $x = \frac{6}{5}.$

Tổng quát: Khi gặp phương trình dạng: $\alpha \left[ {P(x) + Q(x)} \right]$ $+ \beta \left[ {\sqrt {P(x)} \pm \sqrt {Q(x)} } \right]$ $\pm 2\alpha \sqrt {P(x)Q(x)}$ $+ \delta = 0$ với điều kiện ${\alpha ^2} + {\beta ^2} > 0.$ Ta giải như sau:

Đặt $t = \sqrt {P(x)} \pm \sqrt {Q(x)}$ $\Rightarrow {t^2} = P(x) + Q(x) \pm 2\sqrt {P(x)Q(x)} .$

Khi đó phương trình đã cho trở thành: $\alpha {t^2} + \beta t + \delta = 0.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 9. Giải phương trình ${x^2} + 2x$ $+ \sqrt {x + 3}$ $+ 2x\sqrt {x + 3}$ $= 9.$

Điều kiện: $x + 3 \ge 0.$

Đặt $t = x + \sqrt {x + 3}$ $\Rightarrow {t^2} = {x^2} + x + 3$ $+ 2x\sqrt {x + 3} .$

Khi đó phương trình đã cho trở thành: ${t^2} + t – 12 = 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{t = 3}\\
{t = – 4}
\end{array}} \right..
$$

+ Với $t = 3$ $\Rightarrow x + \sqrt {x + 3} = 3$ $\Leftrightarrow \sqrt {x + 3} = 3 – x.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{3 – x \ge 0}\\
{x + 3 = {x^2} – 6x + 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 3}\\
{{x^2} – 7x + 6 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

+ Với $t = – 4$ $\Rightarrow x + \sqrt {x + 3} = – 4$ $\Leftrightarrow \sqrt {x + 3} = – (x + 4)$ (vô nghiệm do điều kiện).

Kết luận: phương trình có nghiệm duy nhất $x =1.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 10. Giải phương trình ${x^2} + 2x\sqrt {x – \frac{1}{x}} = 3x + 1.$

Điều kiện $x – \frac{1}{x} \ge 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ge 1}\\
{ – 1 \le x < 0}
\end{array}} \right..
$$

Chia cả hai vế cho $x$ ta được phương trình: $x + 2\sqrt {x – \frac{1}{x}} = 3 + \frac{1}{x}.$

Đặt $t = \sqrt {x – \frac{1}{x}}$ $(t \ge 0).$

Phương trình trên trở thành: ${t^2} + 2t – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = – 3\:\:{\rm{(loại)}}}
\end{array}.} \right.
$$

Với $t = 1$ $\Rightarrow \sqrt {x – \frac{1}{x}} = 1$ $\Leftrightarrow {x^2} – x – 1 = 0$ $\Leftrightarrow x = \frac{{1 + \sqrt 5 }}{2}$ hoặc $x = \frac{{1 – \sqrt 5 }}{2}.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = \frac{{1 \pm \sqrt 5 }}{2}.$

Nhận xét:

+ Trong các bài toán đặt ẩn phụ, ta có thể đặt điều kiện hoặc không cần đặt điều kiện cho ẩn phụ. Nếu ta đặt $t = f(x)$, mà việc tìm điều kiện cho $t$ là đơn giản thì chúng ta nên đặt điều kiện cho ẩn phụ $t$, khi đó ta sẽ tiết kiệm được thời gian giải phương trình: $t = f(x)$ nếu phương trình này vô nghiệm. Còn nếu việc tìm điều kiện cho ẩn phụ $t$ là khá phức tạp thì ta có thể bỏ qua việc đặt điều kiện cho ẩn phụ $t$, bởi nếu ta không đặt điều kiện cho ẩn phụ $t$, mà trong trường hợp ẩn phụ $t$ không thoả mãn điều kiện thì phương trình: $t = f(x)$ giải ra sẽ vô nghiệm.

+ Tuy nhiên trong các bài toán chứa tham số, việc đặt điều kiện cho ẩn phụ là bắt buộc. Nếu đặt điều kiện cho ẩn phụ sai thì bài toán chứa tham số sẽ chấm hết tại đó.

<!-- chunk:12 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 11. Giải phương trình ${x^2} + \sqrt[3]{{{x^4} – {x^2}}} = 2x + 1.$

Ta có $x = 0$ không là nghiệm của phương trình.

Chia cả hai vế cho $x \ne 0$, ta được phương trình: $\left( {x – \frac{1}{x}} \right) + \sqrt[3]{{x – \frac{1}{x}}} = 2.$

Đặt $t = \sqrt[3]{{x – \frac{1}{x}}}.$ Phương trình trên trở thành:

${t^3} + t – 2 = 0$ $\Leftrightarrow (t – 1)\left( {{t^2} + t + 2} \right) = 0$ $\Leftrightarrow t = 1.$

Với $t = 1$ $\Rightarrow \sqrt[3]{{x – \frac{1}{x}}} = 1$ $\Leftrightarrow x – \frac{1}{x} = 1$ $\Leftrightarrow x = \frac{{1 \pm \sqrt 5 }}{2}.$

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = \frac{{1 \pm \sqrt 5 }}{2}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 12. Giải phương trình $\sqrt {{x^3} – 1} = {x^2} + 3x – 1.$

Điều kiện: $x \ge 1.$

Phương trình đã cho tương đương:

$\sqrt {(x – 1)\left( {{x^2} + x + 1} \right)}$ $= 2(x – 1) + {x^2} + x + 1.$

$\Leftrightarrow \sqrt {\frac{{x – 1}}{{{x^2} + x + 1}}}$ $= 2\frac{{x – 1}}{{{x^2} + x + 1}} + 1$ (với ${x^2} + x + 1 > 0$).

Đặt: $u = \sqrt {\frac{{x – 1}}{{{x^2} + x + 1}}}$, $u \ge 0.$

Phương trình trên trở thành: $2{u^2} – u + 1 = 0$ (vô nghiệm).

Kết luận: phương trình vô nghiệm.

<!-- chunk:14 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 13. Giải phương trình $\sqrt {4{x^2} + x + 6}$ $= 4x – 2 + 7\sqrt {x + 1} .$

Điều kiện: $x \ge – 1.$

Phương trình tương đương:

$\sqrt {{{(2x – 1)}^2} + 5(x + 1)}$ $= 2(2x – 1) + 7\sqrt {x + 1} .$

+ Với $x = -1$: không thỏa mãn phương trình.

Với $x > -1$: phương trình tương đương $\sqrt {{{\left( {\frac{{2x – 1}}{{\sqrt {x + 1} }}} \right)}^2} + 5}$ $= 2\frac{{2x – 1}}{{\sqrt {x + 1} }} + 7.$

Đặt $t = \frac{{2x – 1}}{{\sqrt {x + 1} }}$, phương trình trên trở thành:

$\sqrt {{t^2} + 5} = 2t + 7$ 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{t \ge – \frac{7}{2}}\\
{3{t^2} + 28t + 44 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow t = – 2.$

Với $t = – 2$ $\Rightarrow \frac{{2x – 1}}{{\sqrt {x + 1} }} = – 2$ $\Leftrightarrow 2\sqrt {x + 1} = 1 – 2x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{x \le \frac{1}{2}}\\
{x = \frac{{2 \pm \sqrt 7 }}{2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{{2 – \sqrt 7 }}{2}.$

Kết luận: phương trình đã cho có một nghiệm là $x = \frac{{2 – \sqrt 7 }}{2}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 14. Giải phương trình $10\sqrt {{x^3} + 8} = 3\left( {{x^2} – x + 6} \right).$

Điều kiện: $x \ge – 2.$

+ Với $x = – 2:$ không thỏa mãn phương trình.

+ Với $x > – 2:$ phương trình tương đương:

$10\sqrt {(x + 2)\left( {{x^2} – 2x + 4} \right)}$ $= 3(x + 2) + 3\left( {{x^2} – 2x + 4} \right).$

$\Leftrightarrow 10\sqrt {\frac{{{x^2} – 2x + 4}}{{x + 2}}}$ $= 3 + 3\frac{{{x^2} – 2x + 4}}{{x + 2}}.$

Đặt $u = \sqrt {\frac{{{x^2} – 2x + 4}}{{x + 2}}}$, $u \ge 0.$

Phương trình trên trở thành: $3{u^2} – 10u + 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = 3}\\
{u = \frac{1}{3}}
\end{array}} \right..
$$

+ Với $u = 3$ ta được: $\sqrt {\frac{{{x^2} – 2x + 4}}{{x + 2}}} = 3$ $\Leftrightarrow {x^2} – 11x – 14 = 0$ $\Leftrightarrow x = \frac{{11 \pm \sqrt {177} }}{2}.$

+ Với $u = \frac{1}{3}$ ta được: $\sqrt {\frac{{{x^2} – 2x + 4}}{{x + 2}}} = \frac{1}{3}$ $\Leftrightarrow 9{x^2} – 19x + 34 = 0$ (vô nghiệm).

So sánh với điều kiện, ta được nghiệm của phương trình là: $x = \frac{{11 \pm \sqrt {177} }}{2}.$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 15. Giải phương trình ${x^2} – 3x + 1$ $= – \frac{{\sqrt 3 }}{3}\sqrt {{x^4} + {x^2} + 1} .$

Phương trình đã cho tương đương:

$2\left( {{x^2} – x + 1} \right)$ $– \left( {{x^2} + x + 1} \right)$ $+ \frac{{\sqrt 3 }}{3}\sqrt {\left( {{x^2} – x + 1} \right)\left( {{x^2} + x + 1} \right)}$ $= 0.$

$\Leftrightarrow 2\frac{{{x^2} – x + 1}}{{{x^2} + x + 1}} – 1$ $+ \frac{{\sqrt 3 }}{3}\sqrt {\frac{{{x^2} – x + 1}}{{{x^2} + x + 1}}} = 0.$

Đặt $t = \sqrt {\frac{{{x^2} – x + 1}}{{{x^2} + x + 1}}}$, $t \ge 0.$ Phương trình trên trở thành:

$2{t^2} + \frac{{\sqrt 3 }}{3}t – 1 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – \frac{3}{{2\sqrt 3 }}\:\:{\rm{(loại)}}}\\
{t = \frac{1}{{\sqrt 3 }}}
\end{array}} \right..
$$

Với $t = \frac{1}{{\sqrt 3 }}$ $\Rightarrow \sqrt {\frac{{{x^2} – x + 1}}{{{x^2} + x + 1}}} = \frac{1}{{\sqrt 3 }}$ $\Leftrightarrow x = 1.$

Kết luận: phương trình có một nghiệm $x = 1.$

<!-- chunk:17 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 16. Giải phương trình $\sqrt {{x^2} + x – 6}$ $+ 3\sqrt {x – 1}$ $– \sqrt {3{x^2} – 6x + 19}$ $= 0.$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{{x^2} + x – 6 \ge 0}\\
{x – 1 \ge 0}\\
{3{x^2} – 6x + 19 \ge 0}
\end{array}} \right.
$$
 $\Leftrightarrow x \ge 2.$

Phương trình tương đương:

$\sqrt {{x^2} + x – 6} + 3\sqrt {x – 1}$ $= \sqrt {3{x^2} – 6x + 19} .$

$\Leftrightarrow {x^2} + x – 6$ $+ 6\sqrt {\left( {{x^2} + x – 6} \right)(x – 1)}$ $+ 9x – 9$ $= 3{x^2} – 6x + 19.$

$\Leftrightarrow 3\sqrt {(x – 2)(x + 3)(x – 1)}$ $= {x^2} – 8x + 17.$

$\Leftrightarrow 3\sqrt {\left( {{x^2} + 2x – 3} \right)(x – 2)}$ $= \left( {{x^2} + 2x – 3} \right)$ $– 10(x – 2)$ $(1).$

$\Leftrightarrow 3\sqrt {\frac{{{x^2} + 2x – 3}}{{x – 2}}}$ $= \frac{{{x^2} + 2x – 3}}{{x – 2}} – 10$ $(2)$ (do $x = 2$ không là nghiệm của phương trình $(1)$).

Đặt $t = \sqrt {\frac{{{x^2} + 2x – 3}}{{x – 2}}} \ge 0.$ Phương trình $(2)$ trở thành:

$3t = {t^2} – 10$ $\Leftrightarrow {t^2} – 3t – 10 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 2\:\:{\rm{(loại)}}}\\
{t = 5}
\end{array}} \right..
$$

Với $t = 5$ $\Rightarrow \sqrt {\frac{{{x^2} + 2x – 3}}{{x – 2}}} = 5$ $\Leftrightarrow {x^2} – 23x + 47 = 0$ $\Leftrightarrow x = \frac{{23 \pm \sqrt {341} }}{2}.$

Kết hợp điều kiện ta thấy phương trình đã cho có hai nghiệm $x = \frac{{23 \pm \sqrt {341} }}{2}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 17. Giải phương trình $\sqrt {5{x^2} + 14x + 9}$ $– \sqrt {{x^2} – x – 20}$ $= 5\sqrt {x + 1} .$

Điều kiện: $x \ge 5.$

Phương trình tương đương:

$\sqrt {5{x^2} + 14x + 9}$ $= \sqrt {{x^2} – x – 20}$ $+ 5\sqrt {x + 1} .$

$\Leftrightarrow 5{x^2} + 14x + 9$ $= {x^2} – x – 20$ $+ 10\sqrt {{x^2} – x – 20} \sqrt {x + 1}$ $+ 25x + 25.$

$\Leftrightarrow 2{x^2} – 5x + 2$ $= 5\sqrt {(x + 4)(x – 5)(x + 1)} .$

$\Leftrightarrow 2\left( {{x^2} – 4x – 5} \right)$ $+ 3(x + 4)$ $= 5\sqrt {{x^2} – 4x – 5} \sqrt {x + 4} .$

$\Leftrightarrow 2\left( {\frac{{{x^2} – 4x – 5}}{{x + 4}}} \right) + 3$ $= 5\sqrt {\frac{{{x^2} – 4x – 5}}{{x + 4}}} .$

Đặt: $u = \sqrt {\frac{{{x^2} – 4x – 5}}{{x + 4}}}$ $(u \ge 0).$

Khi đó phương trình trên trở thành: $2{u^2} – 5u + 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = 1}\\
{u = \frac{3}{2}}
\end{array}} \right..
$$

+ Với $u = 1$ ta được: $\sqrt {\frac{{{x^2} – 4x – 5}}{{x + 4}}} = 1.$

$\Leftrightarrow {x^2} – 4x – 5 = x + 4$ $\Leftrightarrow {x^2} – 5x – 9 = 0$ $\Leftrightarrow x = \frac{{5 \pm \sqrt {61} }}{2}.$

+ Với $u = \frac{3}{2}$ ta được: $\sqrt {\frac{{{x^2} – 4x – 5}}{{x + 4}}} = \frac{3}{2}.$

$\Leftrightarrow 4{x^2} – 16x – 20 = 9x + 36$ $\Leftrightarrow 4{x^2} – 25x – 56 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 8}\\
{x = – \frac{7}{4}}
\end{array}} \right..
$$

Do điều kiện $x \ge 5$ nên phương trình chỉ có hai nghiệm: $x = 8$, $x = \frac{{5 + \sqrt {61} }}{2}.$

Tổng quát: Khi gặp phương trình dạng: $\alpha P(x) + \beta Q(x)$ $+ \delta \sqrt {P(x)Q(x)} = 0$ $(1).$

Ta giải như sau:

+ Nếu $Q(x) = 0$ $\Rightarrow P(x) = 0.$

+ Nếu $Q(x) \ne 0.$ Phương trình trên tương đương: $\alpha \frac{{P(x)}}{{Q(x)}} + \beta + \delta \sqrt {\frac{{P(x)}}{{Q(x)}}} = 0.$

+ Đặt $t = \sqrt {\frac{{P(x)}}{{Q(x)}}}$, $t \ge 0$. Ta được phương trình $\alpha {t^2} + \delta t + \beta = 0.$

Tuy nhiên, hầu hết các phương trình đều không cho tường minh như phương trình (1), mà yêu cầu người giải phải biến đổi khéo léo phương trình đã cho để đưa được về phương trình (1).

<!-- chunk:19 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 18. Giải phương trình $\sqrt {2 – {x^2}} + \sqrt {2 – \frac{1}{{{x^2}}}}$ $= 4 – x – \frac{1}{x}.$

Bình phương hai vế của phương trình đã cho, ta được:

$4 – \left( {{x^2} + \frac{1}{{{x^2}}}} \right)$ $+ 2\sqrt {5 – 2\left( {{x^2} + \frac{1}{{{x^2}}}} \right)}$ $= 16 – 8\left( {x + \frac{1}{x}} \right)$ $+ {\left( {x + \frac{1}{x}} \right)^2}.$

Đặt $t = x + \frac{1}{x}$, $|t| \ge 2$ $\Rightarrow {x^2} + \frac{1}{{{x^2}}} = {t^2} – 2.$

Phương trình trên trở thành:

$4 – \left( {{t^2} – 2} \right)$ $+ 2\sqrt {5 – 2\left( {{t^2} – 2} \right)}$ $= 16 – 8t + {t^2}.$

$\Leftrightarrow 2\sqrt {9 – 2{t^2}} = 2{t^2} – 8t + 10$ $\Leftrightarrow \sqrt {9 – 2{t^2}} = {t^2} – 4t + 5.$

$\Leftrightarrow {\left( {9 – 2{t^2}} \right)^2} = {\left( {{t^2} – 4t + 5} \right)^2}$ $\Leftrightarrow {t^4} – 8{t^3} + 28{t^2} – 40t + 16 = 0.$

$\Leftrightarrow {(t – 2)^4} = 0$ $\Leftrightarrow t = 2.$

Khi đó $x + \frac{1}{x} = 2$ $\Leftrightarrow x = 1.$

Thử lại ta được nghiệm của phương trình là $x = 1.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 19. Giải phương trình $\sqrt[4]{{x – \sqrt {{x^2} – 1} }}$ $+ \sqrt {x + \sqrt {{x^2} – 1} } = 2.$

Điều kiện: $x \ge 1.$

Phương trình đã cho tương đương:

$\frac{{\sqrt[4]{{(x + \sqrt {{x^2} – 1} )(x – \sqrt {{x^2} – 1} )}}}}{{\sqrt[4]{{x + \sqrt {{x^2} – 1} }}}}$ $+ \sqrt {x + \sqrt {{x^2} – 1} } = 2.$

$\Leftrightarrow \frac{1}{{\sqrt[4]{{x + \sqrt {{x^2} – 1} }}}}$ $+ \sqrt {x + \sqrt {{x^2} – 1} } = 2.$

Đặt $u = \sqrt[4]{{x + \sqrt {{x^2} – 1} }}$, do $x \ge 1$ nên $u \ge 1.$

Phương trình trên trở thành: ${u^2} + \frac{1}{u} = 2.$

$\Leftrightarrow {u^3} – 2u + 1 = 0$ $\Leftrightarrow (u – 1)\left( {{u^2} + u – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = 1}\\
{u = \frac{{ – 1 \pm \sqrt 5 }}{2}}
\end{array}} \right.
$$
 $\Rightarrow u = 1.$

Với $u = 1$ $\Rightarrow \sqrt[4]{{x + \sqrt {{x^2} – 1} }} = 1$ $\Leftrightarrow x + \sqrt {{x^2} – 1} = 1.$

$\Leftrightarrow \sqrt {x – 1} (\sqrt {x – 1} + \sqrt {x + 1} ) = 0$ $\Leftrightarrow x = 1.$

Kết luận: nghiệm của phương trình là $x = 1.$

<!-- chunk:21 level:3 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## Ví dụ 20. Giải phương trình $729{x^4} + 8\sqrt {1 – {x^2}} = 36.$

Điều kiện: $– 1 \le x \le 1.$

Đặt $t = \sqrt {1 – {x^2}}$, $0 \le t \le 1.$

Phương trình đã cho trở thành:

$729{\left( {1 – {t^2}} \right)^2} + 8t = 36.$

$\Leftrightarrow \left[ {{{27}^2}{{\left( {1 – {t^2}} \right)}^2} – 36\left( {1 – {t^2}} \right) + \frac{4}{9}} \right]$ $– \left( {36{t^2} – 8t + \frac{4}{9}} \right) = 0.$

$\Leftrightarrow {\left[ {27\left( {1 – {t^2}} \right) – \frac{2}{3}} \right]^2}$ $– {\left( {6t – \frac{2}{3}} \right)^2} = 0.$

$\Leftrightarrow \left[ {27\left( {1 – {t^2}} \right) – 6t} \right]\left[ {27\left( {1 – {t^2}} \right) + 6t – \frac{4}{3}} \right] = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{27\left( {1 – {t^2}} \right) – 6t = 0}\\
{27\left( {1 – {t^2}} \right) + 6t – \frac{4}{3} = 0}
\end{array}} \right..
$$

Ta có: $27\left( {1 – {t^2}} \right) – 6t = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{{ – 1 – \sqrt {82} }}{9}\:\:{\rm{(loại)}}}\\
{t = \frac{{ – 1 + \sqrt {82} }}{9}}
\end{array}} \right.
$$
 $\Rightarrow t = \frac{{ – 1 + \sqrt {82} }}{9}.$

Với $t = \frac{{ – 1 + \sqrt {82} }}{9}$ $\Rightarrow \sqrt {1 – {x^2}} = \frac{{ – 1 + \sqrt {82} }}{9}$ $\Leftrightarrow x = \pm \frac{1}{9}\sqrt { – 2 + 2\sqrt {82} } .$

Ta có: $27\left( {1 – {t^2}} \right) + 6t – \frac{4}{3} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{{1 – \sqrt {78} }}{9}\:\:{\rm{(loại)}}}\\
{t = \frac{{1 + \sqrt {78} }}{9}\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Kết luận: nghiệm của phương trình là $x = \pm \frac{1}{9}\sqrt { – 2 + 2\sqrt {82} } .$

<!-- chunk:22 level:1 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## I. BÀI TẬP
1. Giải phương trình $1 + \frac{2}{3}\sqrt {x – {x^2}} = \sqrt x + \sqrt {1 – x} .$

2. Giải phương trình $\sqrt {1 – x} + \sqrt {1 + x} + 2\sqrt {1 – {x^2}} = 4.$

3. Giải phương trình $2x + \sqrt {x + 1} + \sqrt x + 2\sqrt {{x^2} + x} = 1.$

4. Giải phương trình $2x + 1 + \sqrt {x + 3} – \sqrt x$ $= 2\sqrt {{x^2} + 3x} .$

5. Giải phương trình $2\sqrt {2x – {x^2}} + 4$ $= 3(\sqrt x + \sqrt {2 – x} ).$

6. Giải phương trình $2x + 6 + 2\sqrt {{x^2} + 3x}$ $= 4(\sqrt x + \sqrt {x + 3} ).$

7. Giải phương trình $\sqrt {1 + \sqrt {1 – {x^2}} }$ $= x(1 + 2\sqrt {1 – {x^2}} ).$

8. Giải phương trình $\frac{2}{{\sqrt {x + 1} + \sqrt {3 – x} }}$ $= 1 + \sqrt {3 + 2x – {x^2}} .$

9. Giải phương trình ${x^2} + 4x + 1$ $– 2x\sqrt {3x + 1}$ $= \sqrt {3x + 1} .$

10. Giải phương trình $2{x^2} + x$ $– \sqrt {{x^2} + 5}$ $– 2x\sqrt {{x^2} + 5}$ $= 7.$

11. Giải phương trình $1 + 4{x^2} + (4x – 3)\sqrt {x – 1} = 5x.$

12. Giải phương trình $10{x^2} + 3x + 1$ $= (1 + 6x)\sqrt {{x^2} + 3} .$

13. Giải phương trình $4{x^2} – x + 4$ $= 3x\sqrt {x + \frac{1}{x}} .$

14. Giải phương trình $\frac{{2x}}{{2{x^2} – 5x + 3}} + \frac{{13x}}{{2{x^2} + x + 3}} = 6.$

15. Giải phương trình $x\sqrt[3]{{35 – {x^3}}}(x + \sqrt[3]{{35 – {x^3}}}) = 30.$

16. Giải phương trình $4{x^2} – 3x – 4 = \sqrt[3]{{{x^4} – {x^2}}}.$

17. Giải phương trình $\sqrt {{x^2} – x + 1} + \sqrt {{x^2} + 7x + 1} = 4\sqrt x .$

18. Giải phương trình $\sqrt[4]{{{x^2} + x + 1}} + \sqrt[4]{{{x^2} – x + 1}} = 2\sqrt[4]{x}.$

19. Giải phương trình $\sqrt {{x^2} – 2x + 5} + \sqrt {x – 1} = 2.$

20. Giải phương trình $2\left( {{x^2} + 2} \right) = 5\sqrt {{x^3} + 1} .$

21. Giải phương trình $2{x^2} + 5x – 1 = 7\sqrt {{x^3} – 1} .$

22. Giải phương trình $2\left( {{x^2} – 3x + 2} \right) = 3\sqrt {{x^3} + 8} .$

23. Giải phương trình $3{x^2} – 2x – 2$ $= \frac{6}{{\sqrt {30} }}\sqrt {{x^3} + 3{x^2} + 4x + 2} .$

24. Giải phương trình $7{x^2} – 10x + 14 = 5\sqrt {{x^4} + 4} .$

25. Giải phương trình $– 3{x^2} + 5x + 10$ $= 5\sqrt {\left( {{x^2} – 3x + 2} \right)(x + 3)} .$

26. Giải phương trình $– 2{x^2} + 15x + 23$ $= 7\sqrt {\left( {{x^2} + 2x – 3} \right)(x – 2)} .$

27. Giải phương trình $\sqrt {\frac{9}{5}{x^2} – \frac{{12}}{5}x – 5}$ $– \sqrt {x – 3}$ $= \sqrt {{x^2} + x – 2} .$

28. Giải phương trình $\sqrt {9{x^2} + 9x + 4}$ $= 9x + 3 – \sqrt {x + 1} .$

29. Giải phương trình ${x^4} + 2{x^3} + 2{x^2} – 2x + 1$ $= \left( {{x^3} + x} \right)\sqrt {\frac{{1 – {x^2}}}{x}} .$

30. Giải phương trình $(x – 2)\sqrt {x – 1} – \sqrt 2 x + 2 = 0.$

31. Giải phương trình $2{x^2} – 11x + 21 – 3\sqrt[3]{{4x – 4}} = 0.$

32. Giải phương trình ${(\sqrt {x – 1} + 1)^3} + 2\sqrt {x – 1} = 2 – x.$

33. Giải phương trình ${\left( {{x^2} + 2} \right)^2}$ $+ 4{(x + 1)^3}$ $+ \sqrt {{x^2} + 2x + 5}$ $= {(2x – 1)^2} + 2.$

34. Giải phương trình ${x^3} + \sqrt {{{\left( {1 – {x^2}} \right)}^3}}$ $= x\sqrt {2\left( {1 – {x^2}} \right)} .$

35. Giải phương trình $(13 – 4x)\sqrt {2x – 3}$ $+ (4x – 3)\sqrt {5 – 2x}$ $= 2 + 8\sqrt {16x – 4{x^2} – 15} .$

36. Giải phương trình $4\sqrt {{x^2} + x + 1}$ $= 1 + 5x + 4{x^2} – 2{x^3} – {x^4}.$

37. Giải phương trình $\sqrt {{{\left( {{x^2} + 1} \right)}^3}}$ $– \sqrt {{x^4} – {x^3} + {x^2}}$ $= \sqrt {x\left( {{x^4} + {x^2} + 1} \right)} .$

<!-- chunk:23 level:1 source:https://toanmath.com/2019/11/giai-phuong-trinh-vo-ti-bang-phuong-phap-dat-an-phu-hoan-toan.html -->
## II. ĐÁP SỐ
1. $x = 0$, $x = 1.$

2. $x = 0.$

3. $x = 0.$

4. $x = 1$, $x = \frac{1}{{16}}.$

5. $x = 1.$

6. $x = 1.$

7. $x = 1$, $x = \frac{1}{2}.$

8. $x = – 1$, $x = 3.$

9. $x = 0$, $x = 1$, $x = \frac{{3 + \sqrt {13} }}{2}.$

10. $x = – \frac{{11}}{8}.$

11. $x = 1.$

12. $x = 1$, $x = \frac{{ – 3 + \sqrt 7 }}{4}.$

13. Vô nghiệm.

14. $x = 2$, $x = \frac{3}{4}.$

15. $x = 2$, $x = 3.$

16. $x = \frac{{1 \pm \sqrt 5 }}{2}.$

17. $x = 1.$

18. $x = \frac{{65 \pm \sqrt {3201} }}{{32}}.$

19. $x = 1.$

20. $x = \frac{{5 \pm \sqrt {37} }}{2}.$

21. $x = 4 \pm \sqrt 6 .$

22. $x = 3 \pm \sqrt 5 .$

23. $x = 2$, $x = – \frac{2}{3}.$

24. $x = \frac{{5 \pm \sqrt 7 }}{3}.$

25. $x = \sqrt 5 .$

26. $x = 2 \pm \sqrt 5 .$

27. $\frac{{13 + \sqrt {229} }}{2}.$

28. $x = 0.$

29. $x = – 1 + \sqrt 2 .$

30. $x = {\left( {\frac{{1 + \sqrt {1 + 4\sqrt 2 } }}{2}} \right)^2} + 1.$

31. $x = 3.$

32. $x = 1.$

33. $x = – 1.$

34. $x = \frac{{\sqrt 2 }}{2}$, $x = \frac{{1 – \sqrt 2 – \sqrt {2\sqrt 2 – 1} }}{2}.$

35. $x = 2.$

36.

37. Vô nghiệm.