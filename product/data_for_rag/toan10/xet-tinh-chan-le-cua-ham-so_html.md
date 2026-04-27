# Xét tính chẵn, lẻ của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp giải bài toán xét tính chẵn, lẻ của hàm số, đây là dạng toán thường gặp trong nội dung đại cương về hàm số thuộc chương trình Đại số 10 chương 2.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## A. PHƯƠNG PHÁP XÉT TÍNH CHẴN – LẺ CỦA HÀM SỐ
1. Khái niệm hàm số chẵn, hàm số lẻ
Cho hàm số $y=f\left( x \right)$ có tập xác định $D.$

• Hàm số $f$ được gọi là hàm số chẵn nếu với $\forall x\in D$ thì $-x\in D$ và $f\left( x \right)=f\left( x \right).$

• Hàm số $f$ được gọi là hàm số lẻ nếu với $\forall x\in D$ thì $-x\in D$ và $f\left( x \right)=-f\left( x \right).$

Chú ý: Một hàm số có thể không chẵn cũng không lẻ.

2. Đồ thị của hàm số chẵn, hàm số lẻ

• Đồ thị của hàm số chẵn nhận trục tung làm trục đối xứng.

• Đồ thị của hàm số lẻ nhận gốc toạ độ làm tâm đối xứng.

3. Phương pháp xét tính chẵn, lẻ của hàm số
Cho hàm số $y=f(x)$ xác định trên $D.$

• $f$ là hàm số chẵn 
$$
\Leftrightarrow \left\{ \begin{align}
& \forall x\in D\Rightarrow -x\in D \\
& f(-x)=f(x) \\
\end{align} \right.
$$

• $f$ là hàm số lẻ 
$$
\Leftrightarrow \left\{ \begin{align}
& \forall x\in D\Rightarrow -x\in D \\
& f(-x)=-f(x) \\
\end{align} \right.
$$

Các bước xét tính chẵn, lẻ của hàm số:

• Bước 1. Tìm tập xác định $D$ của hàm số.

• Bước 2. Kiểm tra:

+ Nếu $\forall x\in D$ $\Rightarrow -x\in D$ thì chuyển qua bước 3.

+ Nếu tồn tại ${{x}_{0}}\in D$ mà $-{{x}_{0}}\notin D$ thì kết luận hàm không chẵn cũng không lẻ.

• Bước 3. Xác định $f\left( -x \right)$ và so sánh với $f\left( x \right):$

+ Nếu $f\left( -x \right)$ = $f\left( x \right)$ thì kết luận hàm số là chẵn.

+ Nếu $f\left( -x \right)$ = $-f\left( x \right)$ thì kết luận hàm số là lẻ.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Ví dụ 1. Xét tính chẵn, lẻ của các hàm số sau:

a) $f(x)=3{{x}^{3}}+2\sqrt[3]{x}.$

b) $f(x)={{x}^{4}}+\sqrt{{{x}^{2}}+1}.$

c) $f\left( x \right)=\sqrt{x+5}+\sqrt{5-x}.$

d) $f(x)=\sqrt{2+x}+\frac{1}{\sqrt{2-x}}.$

a) Tập xác định của hàm số: $\text{D}=\mathbb{R}.$

Với mọi $x\in \mathbb{R}$ ta có $-x\in \mathbb{R}$ và $f(-x)$ $=3{{\left( -x \right)}^{3}}+2\sqrt[3]{-x}$ $=-\left( 3{{x}^{3}}+2\sqrt[3]{x} \right)$ $=-f(x).$

Do đó $f(x)=3{{x}^{3}}+2\sqrt[3]{x}$ là hàm số lẻ.

b) Tập xác định của hàm số: $\text{D}=\mathbb{R}.$

Với mọi $x\in \mathbb{R}$ ta có $-x\in \mathbb{R}$ và $f(-x)$ $={{\left( -x \right)}^{4}}+\sqrt{{{\left( -x \right)}^{2}}+1}$ $={{x}^{4}}+\sqrt{{{x}^{2}}+1}$ $=f(x).$

Do đó $f(x)={{x}^{4}}+\sqrt{{{x}^{2}}+1}$ là hàm số chẵn.

c) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
x+5\ge 0 \\
5-x\ge 0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge -5 \\
x\le 5 \\
\end{matrix} \right.
$$
 $\Leftrightarrow -5\le x\le 5.$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ -5;5 \right].$

Với mọi $x\in \left[ -5;5 \right]$ ta có $-x\in \left[ -5;5 \right]$ và $f(-x)$ $=\sqrt{\left( -x \right)+5}+\sqrt{5-\left( -x \right)}$ $=\sqrt{x+5}+\sqrt{5-x}$ $=f(x).$

Do đó $f\left( x \right)=\sqrt{x+5}+\sqrt{5-x}$ là hàm số chẵn.

d) Điều kiện xác định: 
$$
\left\{ \begin{matrix}
2+x\ge 0 \\
2-x>0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x\ge -2 \\
x<2 \\
\end{matrix} \right.
$$
 $\Leftrightarrow -2\le x<2.$

Suy ra tập xác định của hàm số là: $\text{D}=\left[ -2;2 \right).$

Ta có ${{x}_{0}}=-2\in \left[ -2;2 \right)$ nhưng $-{{x}_{0}}=2\notin \left[ -2;2 \right).$

Vậy hàm số $f(x)=\sqrt{2+x}+\frac{1}{\sqrt{2-x}}$ không chẵn và không lẻ.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Ví dụ 2. Xét tính chẵn, lẻ của các hàm số sau:

a) $f(x)={{x}^{4}}-4x+2.$

b) $f\left( x \right)=\left| \left| x+2 \right|-\left| x-2 \right| \right|.$

c) $f(x)=\frac{x+\sqrt{{{x}^{2}}+1}}{\sqrt{{{x}^{2}}+1}-x}-2{{x}^{2}}-1.$

d) 
$$
f(x)=\left\{ \begin{matrix}
-1\:khi\:x<0 \\
0\:khi\:x=0 \\
1\:khi\:x>0 \\
\end{matrix} \right.
$$

a) Tập xác định của hàm số: $D=\mathbb{R}.$

Ta có $f\left( -1 \right)=7$, $f\left( 1 \right)=-1$ 
$$
\Rightarrow \left\{ \begin{matrix}
f\left( -1 \right)\ne f\left( 1 \right) \\
f\left( -1 \right)\ne -f\left( 1 \right) \\
\end{matrix} \right.
$$

Vậy hàm số không chẵn và không lẻ.

b) Tập xác định của hàm số: $\text{D}=\mathbb{R}.$

Với mọi $x\in \mathbb{R}$ ta có $-x\in \mathbb{R}$ và $f(-x)=\left| \left| \left( -x \right)+2 \right|-\left| \left( -x \right)-2 \right| \right|$ $=\left| \left| x-2 \right|-\left| x+2 \right| \right|.$

Suy ra $f\left( -x \right)=f\left( x \right).$

Do đó $f\left( x \right)=\left| \left| x+2 \right|-\left| x-2 \right| \right|$ là hàm số chẵn.

c) Ta có $\sqrt{{{x}^{2}}+1}>\sqrt{{{x}^{2}}}=\left| x \right|\ge x$ $\Rightarrow \sqrt{{{x}^{2}}+1}-x\ne 0$ với mọi $x.$

Suy ra tập xác định của hàm số là: $D=\mathbb{R}.$

Mặt khác $\sqrt{{{x}^{2}}+1}>\sqrt{{{x}^{2}}}=\left| x \right|\ge -x$ $\Rightarrow \sqrt{{{x}^{2}}+1}+x\ne 0$, do đó $f(x)=\frac{{{\left( x+\sqrt{{{x}^{2}}+1} \right)}^{2}}}{\left( \sqrt{{{x}^{2}}+1}+x \right)\left( \sqrt{{{x}^{2}}+1}-x \right)}-2{{x}^{2}}-1$ $=2x\sqrt{{{x}^{2}}+1}.$

Với mọi $x\in \mathbb{R}$ ta có $-x\in \mathbb{R}$ và $f(-x)$ $=2\left( -x \right)\sqrt{{{\left( -x \right)}^{2}}+1}$ $=-2x\sqrt{{{x}^{2}}+1}$ $=-f\left( x \right).$

Do đó $f(x)=\frac{x+\sqrt{{{x}^{2}}+1}}{\sqrt{{{x}^{2}}+1}-x}-2{{x}^{2}}-1$ là hàm số lẻ.

d) Tập xác định của hàm số: $D=\mathbb{R}.$

Dễ thấy với mọi $x\in \mathbb{R}$ ta có $-x\in \mathbb{R}.$

Với mọi $x>0$ ta có $-x<0$ suy ra $f\left( -x \right)=-1$, $f\left( x \right)=1$ $\Rightarrow f\left( -x \right)=-f\left( x \right).$

Với mọi $x<0$ ta có $-x>0$ suy ra $f\left( -x \right)=1$, $f\left( x \right)=-1$ $\Rightarrow f\left( -x \right)=-f\left( x \right).$

Và $f\left( -0 \right)=-f\left( 0 \right)=0.$

Do đó với mọi $x\in \mathbb{R}$ ta có $f\left( -x \right)=-f\left( x \right).$

Vậy hàm số 
$$
f(x)=\left\{ \begin{matrix}
-1\:khi\:x<0 \\
0\:khi\:x=0 \\
1\:khi\:x>0 \\
\end{matrix} \right.
$$
 là hàm số lẻ.

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Ví dụ 3. Tìm $m$ để hàm số $f\left( x \right)=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)+\left( 2{{m}^{2}}-2 \right)x}{\sqrt{{{x}^{2}}+1}-m}$ là hàm số chẵn.

Điều kiện xác định: $\sqrt{{{x}^{2}}+1}\ne m.$

Giả sử hàm số $f(x)$ là hàm số chẵn suy ra $f\left( -x \right)=f\left( x \right)$ với mọi $x$ thỏa mãn điều kiện $\sqrt{{{x}^{2}}+1}\ne m.$

Ta có $f\left( -x \right)=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)-\left( 2{{m}^{2}}-2 \right)x}{\sqrt{{{x}^{2}}+1}-m}.$

Suy ra $f\left( -x \right)=f\left( x \right)$ $⇔ \frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)-\left( 2{{m}^{2}}-2 \right)x}{\sqrt{{{x}^{2}}+1}-m}$ $=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)+\left( 2{{m}^{2}}-2 \right)x}{\sqrt{{{x}^{2}}+1}-m}$ $\Leftrightarrow 2\left( 2{{m}^{2}}-2 \right)x=0$ với mọi $x$ thỏa mãn điều kiện xác định $\Leftrightarrow 2{{m}^{2}}-2=0$ $\Leftrightarrow m=\pm 1.$

+ Với $m=1$ ta có hàm số là $f\left( x \right)=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)}{\sqrt{{{x}^{2}}+1}-1}.$

Điều kiện xác định: $\sqrt{{{x}^{2}}+1}\ne 1\Leftrightarrow x\ne 0.$

Suy ra tập xác định của hàm số là: $\text{D}=\mathbb{R}\backslash \left\{ 0 \right\}.$

Dễ thấy với mọi $x\in \mathbb{R}\backslash \left\{ 0 \right\}$ ta có $-x\in \mathbb{R}\backslash \left\{ 0 \right\}$ và $f\left( -x \right)=f\left( x \right).$

Do đó $f\left( x \right)=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)}{\sqrt{{{x}^{2}}+1}-1}$ là hàm số chẵn.

+ Với $m=-1$ ta có hàm số là $f\left( x \right)=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)}{\sqrt{{{x}^{2}}+1}+1}.$

Tập xác định của hàm số: $\text{D}=\mathbb{R}.$

Dễ thấy với mọi $x\in \mathbb{R}$ ta có $-x\in \mathbb{R}$ và $f\left( -x \right)=f\left( x \right).$

Do đó $f\left( x \right)=\frac{{{x}^{2}}\left( {{x}^{2}}-2 \right)}{\sqrt{{{x}^{2}}+1}+1}$ là hàm số chẵn.

Vậy $m=\pm 1$ là giá trị cần tìm.

<!-- chunk:5 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 1. Xét tính chẵn, lẻ của các hàm số sau:

a) $f\left( x \right)=\frac{{{x}^{3}}+5x}{{{x}^{2}}+4}.$

b) $f\left( x \right)=\frac{{{x}^{2}}+5}{{{x}^{2}}-1}.$

c) $f\left( x \right)=\sqrt{x+1}-\sqrt{1-x}.$

d) $f\left( x \right)=\frac{x-5}{x-1}.$

e) $f\left( x \right)=3{{x}^{2}}-2x+1.$

f) $f\left( x \right)=\frac{{{x}^{3}}}{\left| x \right|-1}.$

g) $f(x)=\frac{\left| x-1 \right|+\left| x+1 \right|}{\left| 2x-1 \right|+\left| 2x+1 \right|}.$

h) $f(x)=\frac{\left| x+2 \right|+\left| x-2 \right|}{\left| x-1 \right|-\left| x+1 \right|}$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 3. Cho hàm số $y=f\left( x \right)$, $y=g\left( x \right)$ có cùng tập xác định $D$. Chứng minh rằng:

a) Nếu hai hàm số trên lẻ thì hàm số $y=f\left( x \right)+g\left( x \right)$ là hàm số lẻ.

b) Nếu hai hàm số trên một chẵn, một lẻ thì hàm số $y=f\left( x \right)g\left( x \right)$ là hàm số lẻ.

<!-- chunk:7 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 4.

a) Tìm $m$ để đồ thị hàm số sau nhận gốc tọa độ $O$ làm tâm đối xứng: $y={{x}^{3}}-({{m}^{2}}-9){{x}^{2}}+(m+3)x+m-3.$

b) Tìm $m$ để đồ thị hàm số sau nhận trục tung làm trục đối xứng: $y={{x}^{4}}-({{m}^{2}}-3m+2){{x}^{3}}+{{m}^{2}}-1.$

<!-- chunk:8 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 1.

a) Hàm số lẻ.

b) Hàm số chẵn.

c) Tập xác định của hàm số là $D=\left[ -1;1 \right]$ nên $\forall x\in D$ $\Rightarrow -x\in D.$

Ta có: $f\left( -x \right)$ $=\sqrt{1-x}-\sqrt{1+x}$ $=-f\left( x \right)$, $\forall x\in D.$

Vậy hàm số đã cho là hàm số lẻ.

d) Tập xác định của hàm số là: $D=\mathbb{R}\backslash \left\{ 1 \right\}.$

Ta có $x=-1\in D$ nhưng $-x=1\notin D.$

Do đó hàm số không chẵn và không lẻ.

e) Tập xác định của hàm số là: $D=\mathbb{R}$.

Ta có $f\left( 1 \right)=2$, $f\left( -1 \right)=6.$

Suy ra $f\left( -1 \right)\ne f\left( 1 \right)$, $f\left( -1 \right)\ne -f\left( 1 \right).$

Do đó hàm số không chẵn và không lẻ.

f) Tập xác định của hàm số là $D=\left( -\infty -1 \right)\cup \left( -1;1 \right)\cup \left( 1;+\infty \right)$ nên $\forall x\in D$ $\Rightarrow -x\in D.$

Ta có: $f\left( -x \right)$ $=\frac{{{\left( -x \right)}^{3}}}{\left| -x \right|-1}$ $=-\frac{{{x}^{3}}}{\left| x \right|-1}$ $=-f\left( x \right)$, $\forall x\in D.$

Vậy hàm số đã cho là hàm số lẻ.

g) Tập xác định của hàm số là $D=\mathbb{R}$ nên $\forall x\in D$ $\Rightarrow -x\in D.$

Ta có: $f(-x)$ $=\frac{\left| -x-1 \right|+\left| -x+1 \right|}{\left| -2x-1 \right|+\left| -2x+1 \right|}$ $=f\left( x \right)$, $\forall x\in D.$

Vậy hàm số đã cho là hàm số chẵn.

h) Điều kiện xác định: $\left| x-1 \right|\ne \left| x+1 \right|$ 
$$
\Leftrightarrow \left\{ \begin{matrix}
x-1\ne x+1 \\
x-1\ne -\left( x+1 \right) \\
\end{matrix} \right.
$$
 $\Leftrightarrow x\ne 0.$

Suy ra tập xác định của hàm số là $D=\mathbb{R}\backslash \left\{ 0 \right\}$, do đó $\forall x\in D$ $\Rightarrow -x\in D.$

Ta có: $f(-x)=\frac{\left| -x+2 \right|+\left| -x-2 \right|}{\left| -x-1 \right|-\left| -x+1 \right|}$ $=-f\left( x \right)$, $\forall x\in D.$

Vậy hàm số đã cho là hàm số lẻ.

<!-- chunk:9 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 3.

a) Ta có hàm số $y=f\left( x \right)+g\left( x \right)$ có tập xác định $\text{D}$.

Do hàm số $y=f\left( x \right)$, $y=g\left( x \right)$ lẻ nên $\forall x\in D$ $\Rightarrow -x\in D$ và $f\left( -x \right)=-f\left( x \right)$, $g\left( -x \right)=-g\left( x \right)$ suy ra $y\left( -x \right)=f\left( -x \right)+g\left( -x \right)$ $=-\left[ f\left( x \right)+g\left( x \right) \right]$ $=-y\left( x \right).$

Suy ra hàm số $y=f\left( x \right)+g\left( x \right)$ là hàm số lẻ.

b) Giả sử hàm số $y=f\left( x \right)$ chẵn, $y=g\left( x \right)$ lẻ.

Khi đó hàm số $y=f\left( x \right)g\left( x \right)$ có tập xác định là $D$ nên $\forall x\in D$ $\Rightarrow -x\in D.$

Ta có $y\left( -x \right)$ $=f\left( -x \right)g\left( -x \right)$ $=f\left( x \right)\left[ -g\left( x \right) \right]$ $=-f\left( x \right)g\left( x \right)$ $=-y\left( x \right).$

Do đó hàm số $y=f\left( x \right)g\left( x \right)$ lẻ.

<!-- chunk:10 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 4.

a) Tập xác định của hàm số: $D=\mathbb{R}$, suy ra $\forall x\in D$ $\Rightarrow -x\in D.$

Đồ thị hàm số đã cho nhận gốc tọa độ $O$ làm tâm đối xứng khi và chỉ khi nó là hàm số lẻ $\Leftrightarrow f\left( -x \right)=-f\left( x \right)$ $\Leftrightarrow {{\left( -x \right)}^{3}}-({{m}^{2}}-9){{\left( -x \right)}^{2}}+(m+3)\left( -x \right)+m-3$ $= – \left[ {{x^3} – ({m^2} – 9){x^2} + (m + 3)x + m – 3} \right]$ $\Leftrightarrow 2({m^2} – 9){x^2} – 2\left( {m – 3} \right) = 0$, $\forall x \in \mathbb{R}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{{m^2} – 9 = 0}\\
{m – 3 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = 3.$

b) Tập xác định của hàm số: $D=\mathbb{R}$, suy ra $\forall x\in D$ $\Rightarrow -x\in D.$

Đồ thị hàm số đã cho nhận trục tung làm trục đối xứng khi và chỉ khi nó là hàm số chẵn $\Leftrightarrow f\left( -x \right)=f\left( x \right)$ $\Leftrightarrow {{\left( -x \right)}^{4}}-({{m}^{2}}-3m+2){{\left( -x \right)}^{3}}+{{m}^{2}}-1$ $={{x}^{4}}-({{m}^{2}}-3m+2){{x}^{3}}+{{m}^{2}}-1$ $\Leftrightarrow 2({{m}^{2}}-3m+2){{x}^{3}}=0$, $\forall x\in \mathbb{R}$ $\Leftrightarrow {{m}^{2}}-3m+2=0$ 
$$
\Leftrightarrow \left[ \begin{matrix}
m=1 \\
m=2 \\
\end{matrix} \right.
$$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/09/xet-tinh-chan-le-cua-ham-so.html -->
## Bài toán 5. Tập xác định của hàm số: $D=\mathbb{R}.$

Với mọi $x\in D$ $\Rightarrow -x\in D.$

Ta có: $y\left( -x \right)$ $={{\left( -x \right)}^{2}}+\sqrt{3-\left( -x \right)}+\sqrt{3+\left( -x \right)}$ $={{x}^{2}}+\sqrt{3+x}+\sqrt{3-x}$ $=y\left( x \right).$

Do đó hàm số $y={{x}^{2}}+\sqrt{3-x}+\sqrt{3+x}$ là hàm số chẵn, nên nhận trục tung làm trục đối xứng.