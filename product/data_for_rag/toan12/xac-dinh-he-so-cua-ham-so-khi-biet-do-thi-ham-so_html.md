# Xác định hệ số của hàm số khi biết đồ thị hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
Bài viết hướng dẫn phương pháp giải bài toán xác định hệ số của hàm số khi biết đồ thị hàm số trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN
Để xác định hệ số của một hàm số thì cần phải có kĩ năng nhận dạng tốt đồ thị của ba hàm số thường gặp: hàm số bậc ba, hàm số trùng phương, hàm số phân thức hữu tỉ. Cần phải nhớ hình dạng cơ bản của đồ thị hàm số, các điểm cực trị, tính đồng biến nghịch biến thể hiện trên đồ thị hàm số, giới hạn cơ bản của hàm số cho trong đề bài: $\mathop {\lim }\limits_{x \to + \infty } y$, $\mathop {\lim }\limits_{x \to – \infty } y$, tiệm cận của đồ thị hàm số, giao điểm của đồ thị với các trục tọa độ.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## Ví dụ 1. Cho hàm số $f(x) = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ. Hãy xác định dấu của các hệ số $a$, $b$, $c$, $d$ của đa thức đã cho.

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-1.png" alt="">

Từ đồ thị hàm số ta có $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$, $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$ nên $a > 0.$

Đồ thị hàm số cắt trục tung tại điểm có tung độ âm nên $d < 0.$

Ta có $y’ = 3a{x^2} + 2bx + c.$

Đồ thị hàm số có hai điểm cực trị nằm về hai phía đối với trục tung nên $y’ = 0$ có hai nghiệm trái dấu ${x_1} < 0 < {x_2}.$ Suy ra $ac < 0$ $\Rightarrow c < 0.$

Mặt khác từ đồ thị ta thấy ${x_1} + {x_2} > 0.$ Do đó $\frac{{ – 2b}}{{3a}} > 0$ $\Rightarrow b < 0.$

Vậy ta có $a > 0$, $b < 0$, $c < 0$, $d < 0.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## Ví dụ 2. Cho hàm số $f(x) = a{x^4} + b{x^2} + c$ có đồ thị như hình vẽ. Hãy xác định dấu của các hệ số $a$, $b$, $c$ của đa thức đã cho.

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-2.png" alt="">

Từ đồ thị ta có $\mathop {\lim }\limits_{x \to + \infty } y = \mathop {\lim }\limits_{x \to – \infty } y = + \infty$ $\Rightarrow a > 0.$

Đồ thị hàm số cắt trục tung tại điểm có tung độ âm nên $c < 0.$

Ta có $f'(x) = 4a{x^3} + 2bx = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{{x^2} = – \frac{b}{{2a}}}
\end{array}} \right..
$$

Đồ thị hàm số có ba điểm cực trị nên $– \frac{b}{{2a}} > 0$ $\Rightarrow b < 0.$

Vậy $a > 0$, $b < 0$, $c < 0.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## Ví dụ 3. Cho hàm số $f(x) = \frac{{ax + b}}{{cx + d}}$ có đồ thị như hình vẽ. Hãy xác định dấu của $ad – bc$, $bd$, $ab$, $ac$, $cd.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-3.png" alt="">

Ta có $f'(x) = \frac{{ad – bc}}{{{{(cx + d)}^2}}}.$

Dựa vào đồ thị, ta thấy hàm số đồng biến trên mỗi khoảng xác định nên $ad – bc > 0.$

Đồ thị hàm số có đường tiệm cận đứng $x = – \frac{d}{c}$ nằm bên phải trục tung nên $– \frac{d}{c} > 0$ hay $cd < 0.$

Đồ thị hàm số có đường tiệm cận ngang $y = \frac{a}{c}$ nằm trên trục hoành nên $\frac{a}{c} > 0$ hay $ac > 0.$

Đồ thị hàm số cắt trục hoành tại điểm $A\left( { – \frac{b}{a};0} \right)$ có hoành độ dương nên $– \frac{b}{a} > 0$ hay $ab < 0.$

Đồ thị hàm số cắt trục tung tại điểm $B\left( {0;\frac{b}{d}} \right)$ có tung độ dương nên $\frac{b}{d} > 0$ hay $bd > 0.$

Vậy $ad – bc > 0$, $bd > 0$, $ab < 0$, $ac > 0$, $cd < 0.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## Ví dụ 4. Cho hàm số $f(x) = a{x^4} + b{x^2} + c$ có đồ thị như hình vẽ bên. Tính giá trị của biểu thức $P = a + 2b + 3c.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-4.png" alt="">

Ta có $f'(x) = 4a{x^3} + 2bx = 0.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;2)$ nên $c = 2.$

Đồ thị hàm số có điểm cực trị là $B(1;-1)$ nên ta có 
$$
\left\{ {\begin{array}{l}
{a + b + c = – 1}\\
{4a + 2b = 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{a = 3}\\
{b = – 6}
\end{array}} \right..
$$

Vậy $P = a + 2b + 3c$ $= 3 + 2.( – 6) + 3.2 = – 3.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## Ví dụ 5. Cho hàm số $f(x) = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên dưới. Tính giá trị biểu thức $P = 3a + 2b + c – 4d.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-5.png" alt="">

Ta có $f'(x) = 3a{x^2} + 2bx + c.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;5)$ nên $d = 5.$

Hàm số có hai điểm cực trị $x = – 1$, $x = 3$ và $f(3) = – 4$ nên:

$$
\left\{ {\begin{array}{l}
{3a – 2b + c = 0}\\
{27a + 6b + c = 0}\\
{27a + 9b + 3c + d = – 4}
\end{array}} \right..
$$

Giải hệ trên ta được $a = \frac{1}{3}$, $b = – 1$, $c = – 3.$

Vậy $P = 3a + 2b + c – 4d$ $= 1 – 2 – 3 – 20 = – 24.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## Ví dụ 6. Cho hàm số $y = \frac{{ax + b}}{{cx – 2}}$ có đồ thị như hình vẽ bên dưới. Tính giá trị biểu thức $P = a – 3b + 2c.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-6.png" alt="">

Đồ thị hàm số cắt trục tung tại điểm $A(0; – 1)$ nên $\frac{b}{{ – 2}} = – 1$ $\Leftrightarrow b = 2.$0

Đồ thị hàm số có tiệm cận đứng $x = 2$ nên $\frac{2}{c} = 2$ $\Leftrightarrow c = 1.$

Đồ thị hàm số có tiệm cận ngang $y = 2$ nên $\frac{a}{c} = 2$ $\Leftrightarrow a = 2c = 2.$

Vậy $P = a – 3b + 2c$ $= 2 – 3.2 + 2 = – 2.$

<!-- chunk:8 level:1 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Mệnh đề nào dưới đây đúng?

A. $a < 0$, $b>0$, $c>0$, $d<0.$

B. $a < 0$, $b<0$, $c>0$, $d<0.$

C. $a>0$, $b<0$, $c<0$, $d > 0.$

D. $a<0$, $b>0$, $c<0$, $d<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-7.png" alt="">

Dựa vào hình dáng đồ thị, ta thấy đây là đồ thị hàm số bậc ba có hệ số $a < 0.$

Đồ thị cắt trục tung tại điểm $A(0;d)$ có tung độ âm nên $d < 0.$

Ta có $y’ = 3a{x^2} + 2bx + c.$

Đồ thị có hai điểm cực trị nằm về hai phía đối với trục hoành nên $y’ = 0$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ trái dấu nhau. Suy ra ${x_1}{x_2} = \frac{c}{{3a}} < 0$ $\Rightarrow c > 0.$

Dễ thấy ${x_1} + {x_2} > 0$ hay $– \frac{{2b}}{{3a}} > 0$ $\Rightarrow b > 0.$

> **Đáp án: A**

## Bài 2. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ biết $a$, $b$, $c$, $d \in R$, $b \ne 0$ có đồ thị như hình vẽ bên. Mệnh đề nào dưới đây đúng?

A. $a > 0$, $b < 0$, $c < 0$, $d > 0.$

B. $a > 0$, $b < 0$, $c > 0$, $d < 0.$

C. $a > 0$, $b > 0$, $c > 0$, $d < 0.$

D. $a < 0$, $b < 0$, $c > 0$, $d < 0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-8.png" alt="">

Ta có $y’ = 3a{x^2} + 2bx + c$ có $\Delta ‘ = {b^2} – 3ac.$

Dựa vào hình dáng đồ thị, ta thấy đây là đồ thị hàm số bậc ba có hệ số $a>0$ và $\Delta ‘ = 0$ hay ${b^2} – 3ac = 0$ $\Leftrightarrow 3ac = {b^2} > 0$ $\Rightarrow c > 0.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;d)$ có tung độ âm nên $d < 0.$

Ta có $y’ = 0$ có nghiệm kép $x = – \frac{b}{{3a}} > 0$ $\Rightarrow b < 0.$

> **Đáp án: B**

## Bài 3. Đường cong hình bên là đồ thị hàm số $y = a{x^4} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng? A. $a<0$, $b>0$, $c>0.$

B. $a<0$, $b<0$, $c>0.$

C. $a>0$, $b<0$, $c<0.$

D. $a>0$, $b<0$, $c>0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-9.png" alt="">

Dựa vào hình dáng đồ thị, đây là đồ thị hàm số trùng phương có hệ số $a < 0.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;c)$ có tung độ dương nên $c > 0.$

Đồ thị hàm số có ba điểm cực trị nên $ab < 0$ $\Rightarrow b > 0.$

> **Đáp án: A**

## Bài 4. Đường cong hình bên là đồ thị hàm số $y = a{x^4} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực và $b \ne 0.$ Mệnh đề nào dưới đây đúng?

A. $a<0$, $b>0$, $c>0.$

B. $a <0$, $b<0$, $c>0.$

C. $a>0$, $b>0$, $c<0.$

D. $a>0$, $b<0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-10.png" alt="">

Dựa vào hình dáng đồ thị, đây là đồ thị hàm số trùng phương có hệ số $a > 0.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;c)$ có tung độ âm nên $c <0.$

Đồ thị hàm số có một điểm cực trị nên $ab > 0$ $\Rightarrow b > 0.$

> **Đáp án: C**

## Bài 5. Đường cong hình bên là đồ thị hàm số $y = \frac{{ax + b}}{{x + c}}$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $a>0$, $b>0$, $c<0.$

B. $a<0$, $b>0$, $c<0.$

C. $a>0$, $b<0$, $c<0.$

D. $a<0$, $b>0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-11.png" alt="">

Đồ thị hàm số có tiệm cận đứng $x = 2$ $\Rightarrow – c = 2$ $\Leftrightarrow c = – 2 < 0.$

Đồ thị hàm số có tiệm cận ngang $y = a$ nằm phía trên trục hoành nên $a>0.$

Đồ thị hàm số cắt trục tung tại điểm $A\left( {0;\frac{b}{c}} \right)$ có tung độ âm nên $\frac{b}{c} < 0$ $\Rightarrow b > 0.$

> **Đáp án: A**

## Bài 6. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = 2a + b – c + d.$

A. $P=-7.$

B. $P=-5.$

C. $P = \frac{{13}}{3}.$

D. $P = 6.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-12.png" alt="">

Ta có $y’ = 3a{x^2} + 2bx + c.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;1)$ nên $d=1.$

Hàm số có hai điểm cực trị $x =1$, $x = – \frac{5}{3}$ và có đồ thị đi qua điểm $B(1;4)$ nên:

$$
\left\{ {\begin{array}{l}
{3a + 2b + c = 0}\\
{\frac{{25}}{3}a – \frac{{10}}{3}b + c = 0}\\
{a + b + c + 1 = 4}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = – 1}\\
{b = – 1}\\
{c = 5}
\end{array}} \right..
$$

Vậy $P = 2a + b – c + d = – 7.$

> **Đáp án: A**

## Bài 7. Cho hàm số $y = a{x^4} + b{x^2} + c$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = 2a + b – c.$

A. $P = 2.$

B. $P=-2.$

C. $P = \frac{3}{2}.$

D. $P=0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-13.png" alt="">

Ta có $y’ = 4a{x^3} + 2bx.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;-2)$ nên $c = -2.$

Đồ thị hàm số có điểm cực trị $B\left( {1; – \frac{5}{2}} \right)$ nên 
$$
\left\{ {\begin{array}{l}
{4a + 2b = 0}\\
{a + b – 2 = – \frac{5}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = \frac{1}{2}}\\
{b = – 1}
\end{array}} \right..
$$

Vậy $P = 2a + b – c$ $= 1 – 1 + 2 = 2.$

> **Đáp án: A**

## Bài 8. Cho hàm số $y = \frac{{ax + b}}{{x – c}}$ có đồ thị như hình vẽ bên dưới. Tính giá trị biểu thức $P = 2a + 3b – 5c.$

A. $P = 11.$

B. $P = -2.$

C. $P = 5.$

D. $P = -7.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-14.png" alt="">

Đồ thị hàm số có tiệm cận đứng $x = 0$ và tiệm cận ngang $y = 1$ nên $a = 1$ và $c = 0.$

Đồ thị cắt trục hoành tại điểm $A(3;0)$ $\Rightarrow y(3) = \frac{{3a + b}}{3} = 0$ $\Leftrightarrow b = – 3a = – 3.$

Vậy $P = 2a + 3b – 5c$ $= 2 – 9 = – 7.$

> **Đáp án: D**

## Bài 9. Đường cong hình bên là đồ thị hàm số $y = a{x^3} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $(6a + c)(b – 7c) < 0.$

B. $(a + 2c)(b – c) > 0.$

C. $(3a + c)(b – 2a) > 0.$

D. $(a + 4c)(a + 3c – b) < 0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-15.png" alt="">

Dựa vào hình dáng đồ thị, đây là đồ thị hàm số bậc ba có hệ số $a < 0.$

Đồ thị hàm số cắt trục tung tại điểm $A(0;c)$ có tung độ âm nên $c<0.$

Ta có $y’ = 3a{x^2} + 2bx$ $= x(3ax + 2b).$

Hàm số đạt cực trị tại điểm $x = – \frac{{2b}}{{3a}} > 0$ $\Rightarrow b > 0.$

Do đó $(6a + c)(b – 7c) < 0.$

> **Đáp án: A**

## Bài 10. Đường cong hình bên là đồ thị hàm số $y = \frac{{ax + 4}}{{bx + c}}$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $(a + 3b)(2a – c) < 0.$

B. $(3a + b)(3c – b) > 0.$

C. $( – 4b + c)(c – a) < 0.$

D. $(2a + 3b)(a – 5c) > 0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-16.png" alt="">

Đồ thị hàm số cắt trục tung tại điểm $A\left( {0;\frac{4}{c}} \right)$ nên $\frac{4}{c} = – 2$ $\Rightarrow c = – 2.$

Đồ thị hàm số có tiệm cận $x = – \frac{c}{b}$ nằm phía bên phải trục tung và tiệm cận ngang $y = \frac{a}{b}$ nằm phía trên trục hoành.

Suy ra $– \frac{c}{b} > 0$ và $\frac{a}{b} > 0$ hay $a > 0$ và $b > 0.$

Do đó $(2a + 3b)(a – 5c) > 0.$

> **Đáp án: D**

<!-- chunk:9 level:1 source:https://toanmath.com/2019/11/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so.html -->
## IV. BÀI TẬP TỰ LUYỆN

## Bài 1. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Mệnh đề nào dưới đây đúng?

A. $a<0$, $b>0$, $c>0$, $d<0.$

B. $a<0$, $b<0$, $c>0$, $d<0.$

C. $a>0$, $b<0$, $c<0$, $d >0.$

D. $a>0$, $b>0$, $c<0$, $d >0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-17.png" alt="">

## Bài 2. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Mệnh đề nào dưới đây đúng?

A. $(a – 2b)(a + c)(a + d) > 0.$

B. $(2a + c – 2b)(a + 3d) < 0.$

C. $(b – a – 5c)(b – d) < 0.$

D. $(3c – b)(4a + d)(b – d) > 0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-18.png" alt="">

## Bài 3. Đường cong hình bên là đồ thị hàm số $y = a{x^3} + b{x^2} + cx + d$ với $a$, $b$, $c$, $d$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $a>0$, $b<0$, $c<0$, $d = 0.$

B. $a<0$, $b>0$, $c<0$, $d = 0.$

C. $a>0$, $b>0$, $c<0$, $d = 0.$

D. $a>0$, $b>0$, $c<0$, $d<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-19.png" alt="">

## Bài 4. Đường cong hình bên là đồ thị hàm số $y = a{x^3} + b{x^2} + cx + d$ với $a$, $b$, $c$, $d$ là các số thực và $c \ne 0$. Mệnh đề nào dưới đây đúng?

A. $a>0$, $b<0$, $c<0$, $d <0.$

B. $a<0$, $b>0$, $c>0$, $d <0.$

C. $a<0$, $b>0$, $c<0$, $d<0.$

D. $a<0$, $b<0$, $c<0$, $d<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-20.png" alt="">

## Bài 5. Đường cong hình bên là đồ thị hàm số $y = a{x^4} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực và $b \ne 0.$ Mệnh đề nào dưới đây đúng?

A. $a<0$, $b>0$, $c>0.$

B. $a <0$, $b<0$, $c > 0.$

C. $a > 0$, $b>0$, $c<0.$

D. $a>0$, $b<0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-21.png" alt="">

## Bài 6. Đường cong hình bên là đồ thị hàm số $y = a{x^4} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $a < 0$, $b>0$, $c<0.$

B. $a < 0$, $b <0$, $c<0.$

C. $a <0$, $b>0$, $c>0.$

D. $a > 0$, $b <0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-22.png" alt="">

## Bài 7. Đường cong hình bên là đồ thị hàm số $y = a{x^4} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $(a – b)(a – c) < 0.$

B. $(2c – 1)(3a – b) > 0.$

C. $(b – a)\left( {{b^2} – c} \right) > 0.$

D. $(3a + 1)(b + 5c) < 0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-23.png" alt="">

## Bài 8. Đường cong hình bên là đồ thị hàm số $y = \frac{{ax + 6}}{{bx + c}}$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $a>0$, $b>0$, $c>0.$

B. $a > 0$, $b>0$, $c<0.$

C. $a<0$, $b<0$, $c<0.$

D. $a<0$, $b>0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-24.png" alt="">

## Bài 9. Đường cong hình bên là đồ thị hàm số $y = \frac{{ax + b}}{{cx – 5}}$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $a>0$, $b>0$, $c>0.$

B. $a>0$, $b<0$, $c<0.$

C. $a<0$, $b>0$, $c>0.$

D. $a<0$, $b<0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-25.png" alt="">

## Bài 10. Đường cong hình bên là đồ thị hàm số $y = \frac{{3x + a}}{{bx + c}}$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $a>0$, $b>0$, $c>0.$

B. $a>0$, $b>0$, $c<0.$

C. $a<0$, $b>0$, $c<0.$

D. $a<0$, $b<0$, $c<0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-26.png" alt="">

## Bài 11. Đường cong hình bên là đồ thị hàm số $y = a{x^4} + b{x^2} + c$ với $a$, $b$, $c$ là các số thực. Mệnh đề nào dưới đây đúng?

A. $(3a – b + 2c)\left( {{b^2} – 4ac – 4} \right) > 0.$

B. $(b – 2a – 3c)\left( {{b^2} – 4ac – 2} \right) < 0.$

C. $(a – b + 5c)\left[ {7 – 2\left( {{b^2} – 4ac} \right)} \right] < 0.$

D. $(a – b + c)\left( {{b^2} – 4ac + 12} \right) > 0.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-27.png" alt="">

## Bài 12. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = \frac{{3a + b}}{{c – d}}.$

A. $P = 2.$

B. $P = – \frac{3}{5}.$

C. $P = \frac{7}{{11}}.$

D. $P = – 3.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-28.png" alt="">

## Bài 13. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = (a + 2b)(c + 3d) – 5.$

A. $P = 6.$

B. $P = \frac{{11}}{2}.$

C. $P = – 4.$

D. $P = – 5.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-29.png" alt="">

## Bài 14. Cho hàm số $y = a{x^4} + b{x^2} + c$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = (4a + 2)(4b + c).$

A. $P = 30.$

B. $P=-6.$

C. $P= -3.$

D. $P = 12.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-30.png" alt="">

## Bài 15. Cho hàm số $y = \frac{{ax – 1}}{{bx + c}}$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = – 4a + b + 2c.$

A. $P=-5.$

B. $P=-9.$

C. $P = 7.$

D. $P = 11.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-31.png" alt="">

## Bài 16. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = a + b + 3c + 4d.$

A. $P = -9.$

B. $P = 12.$

C. $P = 5.$

D. $P=-5.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-32.png" alt="">

## Bài 17. Cho hàm số $y = a{x^3} + b{x^2} + cx + d$ có đồ thị như hình vẽ bên. Tính giá trị biểu thức $P = (3a + 2b)(c + 3d).$

A. $P = 6.$

B. $P=-20.$

C. $P = -5.$

D. $P=15.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-33.png" alt="">

## Bài 18. Cho hàm số $y = \frac{{ax + b}}{{x + c}}$ có đồ thị như hình vẽ, với $a$, $b$, $c$ là các số nguyên. Tính giá trị biểu thức $T = a – 3b + 2c.$

A. $T = 12.$

B. $T = -7.$

C. $T = 10.$

D. $T = -9.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-34.png" alt="">

## Bài 19. Cho hàm số $y = – 2{x^3} + b{x^2} + cx + d$ có đồ thị như hình bên. Khẳng định nào sau đây đúng?

A. ${bcd = – 144.}$

B. ${{c^2} < {b^2} + {d^2}.}$

C. ${b + c + d = 1.}$

D. ${b + d < c.}$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-35.png" alt="">

## Bài 20. Cho hàm số $y = \frac{{x – a}}{{bx + c}}$ có đồ thị như hình vẽ bên. Tính giá trị của biểu thức $P = a + b + c.$

A. $P = -3.$

B. $P = 1.$

C. $P = 5.$

D. $P = 2.$

<img link="data_for_rag/toan12/images/xac-dinh-he-so-cua-ham-so-khi-biet-do-thi-ham-so-36.png" alt="">