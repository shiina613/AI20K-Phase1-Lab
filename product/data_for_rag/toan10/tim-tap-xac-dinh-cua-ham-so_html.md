# Tìm tập xác định của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp tìm tập xác định của hàm số, đây là dạng toán cơ bản trong chương trình Đại số 10 chương 2, nội dung bài viết gồm 3 phần: lý thuyết cần nắm vững, ví dụ minh họa và các bài tập tự luyện.

1. KIẾN THỨC CẦN NẮM VỮNG
Tập xác định của hàm số $y=f\left( x \right)$ là tập hợp tất cả các số thực $x$ sao cho biểu thức $f\left( x \right)$ có nghĩa.

Nếu $P(x)$ là một đa thức thì:

• $\frac{1}{P(x)}$ có nghĩa $\Leftrightarrow P(x)\ne 0.$

• $\sqrt{P(x)}$ có nghĩa $\Leftrightarrow P(x)\ge 0.$

• $\frac{1}{\sqrt{P(x)}}$ có nghĩa $\Leftrightarrow P(x)>0.$

2. VÍ DỤ MINH HỌA

<!-- chunk:1 level:3 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Ví dụ 1. Tìm tập xác định của các hàm số sau:

a) $y=\frac{{{x}^{2}}+1}{{{x}^{2}}+3x-4}.$

b) $y=\frac{x+1}{\left( x+1 \right)\left( {{x}^{2}}+3x+4 \right)}.$

c) $y=\frac{2{{x}^{2}}+x+1}{{{x}^{3}}+{{x}^{2}}-5x-2}.$

d) $y=\frac{x}{{{\left( {{x}^{2}}-1 \right)}^{2}}-2{{x}^{2}}}.$

a) Điều kiện xác định: ${{x}^{2}}+3x-4\ne 0$ 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne 1 \\
x\ne -4 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là $\text{D}=\mathbb{R}\backslash \left\{ 1;-4 \right\}.$

b) Điều kiện xác định: $\left( x+1 \right)\left( {{x}^{2}}+3x+4 \right)\ne 0$ $\Leftrightarrow x\ne -1.$

Suy ra tập xác định của hàm số là $\text{D}=\mathbb{R}\backslash \left\{ -1 \right\}.$

c) Điều kiện xác định: ${{x}^{3}}+{{x}^{2}}-5x-2\ne 0$ 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne 2 \\
x\ne \frac{-3\pm \sqrt{5}}{2} \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là $\text{D}=\mathbb{R}\backslash \left\{ 2;\frac{-3-\sqrt{5}}{2};\frac{-3+\sqrt{5}}{2} \right\}.$

d) Điều kiện xác định: ${{\left( {{x}^{2}}-1 \right)}^{2}}-2{{x}^{2}}\ne 0$ $\Leftrightarrow \left( {{x}^{2}}-\sqrt{2}x-1 \right)\left( {{x}^{2}}+\sqrt{2}x-1 \right)\ne 0$ 
$$
\Leftrightarrow \left\{ \begin{matrix}
{{x}^{2}}-\sqrt{2}x-1\ne 0 \\
{{x}^{2}}+\sqrt{2}x-1\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne \frac{\sqrt{2}\pm \sqrt{7}}{2} \\
x\ne \frac{-\sqrt{2}\pm \sqrt{7}}{2} \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\mathbb{R}\backslash \left\{ \frac{\sqrt{2}-\sqrt{7}}{2};\frac{\sqrt{2}+\sqrt{7}}{2};\frac{-\sqrt{2}-\sqrt{7}}{2};\frac{-\sqrt{2}+\sqrt{7}}{2} \right\}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Ví dụ 2. Tìm tập xác định của các hàm số sau:

a) $y=\frac{x+1}{(x-3)\sqrt{2x-1}}.$

b) $y=\frac{\sqrt{x+2}}{x\sqrt{{{x}^{2}}-4x+4}}.$

c) $y=\frac{\sqrt{5-3\left| x \right|}}{{{x}^{2}}+4x+3}.$

d) $y=\frac{x+4}{\sqrt{{{x}^{2}}-16}}.$

a) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x\ne 3 \\
2x-1>0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne 3 \\
x>\frac{1}{2} \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\left( \frac{1}{2};+\infty \right)\backslash \left\{ 3 \right\}.$

b) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x\ne 0 \\
\begin{align}
& {{x}^{2}}-4x+4>0 \\
& x+2\ge 0 \\
\end{align} \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne 0 \\
\begin{align}
& {{\left( x-2 \right)}^{2}}>0 \\
& x\ge -2 \\
\end{align} \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne 0 \\
\begin{align}
& x\ne 2 \\
& x\ge -2 \\
\end{align} \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ -2;+\infty \right)\backslash \left\{ 0;2 \right\}.$

c) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
5-3\left| x \right|\ge 0 \\
{{x}^{2}}+4x+3\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
\left| x \right|\le \frac{5}{3} \\
\left\{ \begin{matrix}
x\ne -1 \\
x\ne -3 \\
\end{matrix} \right. \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& -\frac{5}{3}\le x\le \frac{5}{3} \\
& x\ne -1 \\
& x\ne -3 \\
\end{align} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& -\frac{5}{3}\le x\le \frac{5}{3} \\
& x\ne -1 \\
\end{align} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ -\frac{5}{3};\frac{5}{3} \right]\backslash \left\{ -1 \right\}.$

d) Điều kiện xác định: ${{x}^{2}}-16>0$ $\Leftrightarrow \left| x \right|>4$ 
$$
\Leftrightarrow \left[ \begin{matrix}
x>4 \\
x<-4 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\left( -\infty ;-4 \right)\cup \left( 4;+\infty \right).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Ví dụ 3. Tìm tập xác định của các hàm số sau:

a) $y=\frac{\sqrt[3]{{{x}^{2}}-1}}{{{x}^{2}}+2x+3}.$

b) $y=\frac{x}{x-\sqrt{x}-6}.$

c) $y=\sqrt{x+2}-\sqrt{x+3}.$

d) 
$$
y=\left\{ \begin{align}
& \frac{1}{x}\quad khi\ x\ge 1 \\
& \sqrt{x+1}\quad khi\ x<1 \\
\end{align} \right.
$$

a) Điều kiện xác định: ${{x}^{2}}+2x+3\ne 0$ đúng với mọi $x.$

Suy ra tập xác định của hàm số là: $\text{D}=\mathbb{R}.$

b) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x\ge 0 \\
x-\sqrt{x}-6\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
\begin{align}
& x\ge 0 \\
& \sqrt{x}\ne -2 \\
\end{align} \\
\sqrt{x}\ne 3 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge 0 \\
x\ne 9 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ 0;+\infty \right)\backslash \left\{ 9 \right\}.$

c) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x+2\ge 0 \\
x+3\ge 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge -2 \\
x\ge -3 \\
\end{matrix} \right.
$$
 $\Leftrightarrow x\ge -2.$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ -2;+\infty \right).$

d)

Khi $x\ge 1$ thì hàm số là $y=\frac{1}{x}$ luôn xác định với $x\ge 1.$

Khi $x<1$ thì hàm số là $y=\sqrt{x+1}$ xác định khi 
$$
\left\{ \begin{matrix}
x<1 \\
x+1\ge 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x<1 \\
x\ge -1 \\
\end{matrix} \right.
$$
 $\Leftrightarrow -1\le x<1.$

Do đó hàm số đã cho xác định khi $x\ge -1.$

Suy ra tập xác định của hàm số là $\text{D}=\left[ -1;+\infty \right).$

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Ví dụ 4. Cho hàm số $y=\frac{mx}{\sqrt{x-m+2}-1}$ với $m$ là tham số.

a) Tìm tập xác định của hàm số theo tham số $m.$

b) Tìm $m$ để hàm số xác định trên $\left( 0;1 \right).$

a) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x-m+2\ge 0 \\
\sqrt{x-m+2}\ne 1 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge m-2 \\
x\ne m-1 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ m-2;+\infty \right)\backslash \left\{ m-1 \right\}.$

b) Hàm số xác định trên $\left( 0;1 \right)$ khi và chỉ khi $\left( 0;1 \right)\subset \left[ m-2;m-1 \right)\cup \left( m-1;+\infty \right)$ 
$$
⇔ \left[ \begin{matrix}
\left( 0;1 \right)\subset \left[ m-2;m-1 \right) \\
\left( 0;1 \right)\subset \left( m-1;+\infty \right) \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{matrix}
m=2 \\
m-1\le 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{matrix}
m=2 \\
m\le 1 \\
\end{matrix} \right.
$$

Vậy $m\in \left( -\infty ;1 \right]\cup \left\{ 2 \right\}$ là giá trị cần tìm.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Ví dụ 5. Cho hàm số $y=\sqrt{2x-3m+4}+\frac{x}{x+m-1}$ với $m$ là tham số.

a) Tìm tập xác định của hàm số khi $m=1.$

b) Tìm $m$ để hàm số có tập xác định là $\left[ 0;+\infty \right).$

Điều kiện xác định: 
$$
\left\{ \begin{matrix}
2x-3m+4\ge 0 \\
x+m-1\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge \frac{3m-4}{2} \\
x\ne 1-m \\
\end{matrix} \right.
$$

a) Khi $m=1$, ta có điều kiện xác định: 
$$
\left\{ \begin{matrix}
x\ge -\frac{1}{2} \\
x\ne 0 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là $\text{D}=\left[ -\frac{1}{2};+\infty \right)\backslash \left\{ 0 \right\}.$

b)

Với $1-m\ge \frac{3m-4}{2}$ $\Leftrightarrow m\le \frac{6}{5}$ khi đó tập xác định của hàm số là: $\text{D}=\left[ \frac{3m-4}{2};+\infty \right)\backslash \left\{ 1-m \right\}$, do đó $m\le \frac{6}{5}$ không thỏa mãn yêu cầu bài toán.

Với $m>\frac{6}{5}$ khi đó tập xác định của hàm số là $\text{D}=\left[ \frac{3m-4}{2};+\infty \right).$

Do đó hàm số có tập xác định là $\left[ 0;+\infty \right)$ khi và chỉ khi $\frac{3m-4}{2}=0$ $\Leftrightarrow m=\frac{4}{3}$ (thỏa mãn).

Vậy $m=\frac{4}{3}$ là giá trị cần tìm.

## Bài tập
a. Đề bài

<!-- chunk:6 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 1. Tìm tập xác định của các hàm số sau:

a) $y=\frac{2\sqrt{x-1}}{\left| x \right|-2}.$

b) $y=\sqrt{x+2}-\frac{2}{\sqrt{x-1}}.$

c) $y=\frac{\sqrt[3]{x-1}}{{{x}^{2}}+x+1}.$

d) $y=x+\sqrt{{{x}^{2}}-4x+4}.$

e) $y=\frac{\sqrt[{}]{x+1}}{{{x}^{2}}-x-6}.$

f) 
$$
y=f(x)=\left\{ \begin{align}
& \frac{1}{2-x}\quad khi\ x\ge 1 \\
& \sqrt{2-x}\quad khi\ x<1 \\
\end{align} \right.
$$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 2. Tìm tập xác định của các hàm số sau:

a) $y=\sqrt{6-3x}-\sqrt{x-1}.$

b) $y=\frac{\sqrt{2-x}+\sqrt{x+2}}{x}.$

c) $y=\frac{\sqrt{3x-2}+6x}{\sqrt{4-3x}}.$

d) $y=\sqrt{6-x}+\frac{2x+1}{1+\sqrt{x-1}}.$

e) $y=\frac{2x+9}{\left( x+4 \right)\sqrt{x+3}}.$

f) $y=\frac{\sqrt{{{x}^{2}}-2x+3}}{x-3\sqrt{x}+2}.$

g) $f(x)=\frac{1}{\sqrt{1-\sqrt{1+4x}}}.$

h) $y=\frac{2{{x}^{2}}}{\sqrt{{{x}^{2}}-3x+2}}.$

<!-- chunk:8 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 3. Tìm giá trị của tham số $m$ để:

a) Hàm số $y=\frac{x+2m+2}{x-m}$ xác định trên $\left( -1;0 \right).$

b) Hàm số $y=\frac{\sqrt{x}}{\sqrt{x-m}+1}$ có tập xác định là $\left[ 0;+\infty \right).$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 4. Tìm giá trị của tham số $m$ để:

a) Hàm số $y=\sqrt{x-m+1}+\frac{2x}{\sqrt{-x+2m}}$ xác định trên $\left( -1;3 \right).$

b) Hàm số $y=\sqrt{x+m}+\sqrt{2x-m+1}$ xác định trên $\left( 0;+\infty \right).$

c) Hàm số $y=\sqrt{-x-2m+6}-\frac{1}{\sqrt{x+m}}$ xác định trên $\left( -1;0 \right).$

b. Hướng dẫn giải và đáp số

<!-- chunk:10 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 1.

a) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x\ge 1 \\
\left| x \right|\ne 2 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge 1 \\
x\ne \pm 2 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge 1 \\
x\ne 2 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $D=\left[ 1;+\infty \right)\backslash \left\{ 2 \right\}.$

b) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x+2\ge 0 \\
x-1>0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge -2 \\
x>1 \\
\end{matrix} \right.
$$
 $\Leftrightarrow x>1.$

Suy ra tập xác định của hàm số là: $D=\left( 1;+\infty \right).$

c) Điều kiện xác định: ${{x}^{2}}+x+1\ne 0$ $\Leftrightarrow {{\left( x+\frac{1}{2} \right)}^{2}}+\frac{3}{4}\ne 0$ (luôn đúng $\forall x$).

Suy ra tập xác định của hàm số là: $D=\mathbb{R}.$

d) Tập xác định của hàm số: $D=\mathbb{R}.$

e) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x+1\ge 0 \\
{{x}^{2}}-x-6\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge -1 \\
\begin{align}
& x\ne -2 \\
& x\ne 3 \\
\end{align} \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge -1 \\
x\ne 3 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $D=\left[ -1;+\infty \right)\backslash \left\{ 3 \right\}.$

f) Tập xác định của hàm số: $\text{D}=\mathbb{R}\backslash \left\{ 2 \right\}.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 2.

a) $D=\left[ 1;2 \right].$

b) $\text{D}=\left[ -2;2 \right]\backslash \left\{ 0 \right\}.$

c) $D=\left[ \frac{2}{3};\frac{4}{3} \right).$

d) $D=\left[ 1;6 \right].$

e) $\text{D}=\left( -3;+\infty \right).$

f) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
{{x}^{2}}-2x+3\ge 0 \\
x-3\sqrt{x}+2\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
{{\left( x-1 \right)}^{2}}+2\ge 0 \\
\left( \sqrt{x}-1 \right)\left( \sqrt{x}-2 \right)\ne 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ne 1 \\
x\ne 4 \\
\end{matrix} \right.
$$

Suy ra tập xác định của hàm số là: $\text{D}=\mathbb{R}\backslash \left\{ 1;4 \right\}.$

g) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
1-\sqrt{1+4x}>0 \\
1+4x\ge 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
1>1+4\text{x} \\
x\ge -\frac{1}{4} \\
\end{matrix} \right.
$$
 $\Leftrightarrow -\frac{1}{4}\le x<0.$

Suy ra tập xác định của hàm số là: $D=\left[ -\frac{1}{4};0 \right).$

h) Tập xác định của hàm số: $\text{D}=\left( -\infty ;1 \right)\cup \left( 2;+\infty \right)$

<!-- chunk:12 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 3.

a) Điều kiện xác định: $x\ne m.$

Hàm số xác định trên $\left( -1;0 \right)$ khi và chỉ khi $m\notin \left( -1;0 \right)$ 
$$
\Leftrightarrow \left[ \begin{matrix}
m\ge 0 \\
m\le -1 \\
\end{matrix} \right.
$$

b) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x\ge 0 \\
x\ge m \\
\end{matrix} \right.
$$

Nếu $m>0$ thì 
$$
\left\{ \begin{matrix}
x\ge 0 \\
x\ge m \\
\end{matrix} \right.
$$
 $\Leftrightarrow x\ge m$, suy ra tập xác định của hàm số là $D=\left[ m;+\infty \right)$ nên $m>0$ không thỏa mãn yêu cầu bài toán.

Nếu $m\le 0$ thì 
$$
\left\{ \begin{matrix}
x\ge 0 \\
x\ge m \\
\end{matrix} \right.
$$
 $\Leftrightarrow x\ge 0$, suy ra tập xác định của hàm số là $D=\left[ 0;+\infty \right).$

Vậy $m\le 0$ là giá trị cần tìm.

<!-- chunk:13 level:2 source:https://toanmath.com/2018/09/tim-tap-xac-dinh-cua-ham-so.html -->
## Bài toán 4.

a) $m\ge 2.$

b) $m\in \left[ 0;1 \right].$

c) $m\in \left[ 1;3 \right].$