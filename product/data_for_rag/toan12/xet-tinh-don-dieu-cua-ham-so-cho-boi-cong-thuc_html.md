# Xét tính đơn điệu của hàm số cho bởi công thức

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
Bài viết hướng dẫn phương pháp xét tính đơn điệu của hàm số cho bởi công thức trong chương trình Giải tích 12.

1. Phương pháp giải toán

Để tìm khoảng đơn điệu của hàm số $y = f(x)$ trên một khoảng, ta thực hiện các bước sau:

+ Bước 1. Tìm tập xác định.

+ Bước 2. Tính $f'(x).$ Tìm các điểm ${x_1}$, ${x_2}$ … ${x_n}$ trên $[a;b]$ là nghiệm của phương trình $f'(x) = 0$ hoặc $f'(x)$ không xác định.

+ Bước 3. Sắp xếp các điểm ${x_1}$, ${x_2}$ … ${x_n}$ theo thứ tự tăng dần và lập bảng biến thiên.

+ Bước 4. Nêu kết luận về các khoảng đồng biến, nghịch biến của hàm số.

2. Ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## Ví dụ 1. Tìm khoảng đồng biến, nghịch biến của hàm số $y = {x^3} – 3{x^2} + 1.$

Tập xác định: $D = R.$ Ta có $y’ = 3{x^2} – 6x.$

Khi đó $y’ = 0$ $\Leftrightarrow 3{x^2} – 6x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-1.png" alt="">

Hàm số đồng biến trên $( – \infty ;0)$ và $(2; + \infty ).$ Hàm số nghịch biến trên $(0;2).$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## Ví dụ 2. Tìm các khoảng đồng biến, nghịch biến của hàm số:

$y = – \frac{1}{4}{x^4} + 2{x^2} – 5.$

Ta có $y’ = – {x^3} + 4x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 2}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-2.png" alt="">

Do đó hàm số đồng biến trên $( – \infty ; – 2)$ và $(0;2).$

Hàm số nghịch biến trên $( – 2;0)$ và $(2; + \infty ).$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## Ví dụ 3. Tìm các khoảng đơn điệu của hàm số $y = \frac{{3x + 1}}{{ – x + 1}}.$

Tập xác định $D = R\backslash \{ 1\} .$

Ta có $y’ = \frac{4}{{{{( – x + 1)}^2}}} > 0$, $\forall x \in D.$

Do đó hàm số đồng biến trên các khoảng xác định $( – \infty ;1)$ và $(1; + \infty ).$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## Ví dụ 4. Tìm các khoảng đơn điệu của hàm số $y = \sqrt {2x – {x^2}} .$

Tập xác định $D = [0;2].$ Ta có $y’ = \frac{{1 – x}}{{\sqrt {2x – {x^2}} }}$, $y = 0$ $\Leftrightarrow x = 1.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-3.png" alt="">

Từ bảng biến thiên suy ra hàm số đồng biến trên $(0;1)$ và nghịch biến trên $(1;2).$

## Bài tập
## Bài 1. Hàm số $y = – {x^3} + 3x – 5$ đồng biến trên khoảng nào sau đây?

A. $(1; + \infty ).$

B. $( – 1;1).$

C. $( – \infty ; – 1).$

D. $( – \infty ;1).$

Ta có $y’ = – 3{x^3} + 3$, $y’ = 0$ $\Leftrightarrow x = \pm 1.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-4.png" alt="">

Từ bảng biến thiên kết luận hàm số đồng biến trên $(-1;1).$

> **Đáp án: B**

## Bài 2. Tìm tất cả các khoảng đồng biến của hàm số $y = \frac{x}{{{x^2} + 1}}.$

A. $( – 1;1).$

B. $(0; + \infty ).$

C. $( – \infty ; – 1)$ và $(1; + \infty ).$

D. $( – \infty ; + \infty ).$

Tập xác định $D = R.$

Ta có: $y’ = \frac{{1 – {x^2}}}{{{{\left( {{x^2} + 1} \right)}^2}}}$, $y’ = 0$ $\Leftrightarrow \frac{{1 – {x^2}}}{{{{\left( {{x^2} + 1} \right)}^2}}} = 0$ $\Leftrightarrow x = \pm 1.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-5.png" alt="">

Dựa vào bảng biến thiên, suy ra hàm số đồng biến trên khoảng $(-1;1).$

> **Đáp án: A**

Bài 3. Cho hàm số $y = – {x^3} + 3{x^2} + 9x + 4.$ Đồng biến trên khoảng nào sau đây?

A. $( – \infty ; – 3).$

B. $( – 1;3).$

C. $(3; + \infty ).$

D. $( – 3;1).$

Tập xác định: $D = R$, $y’ = – 3{x^2} + 6x + 9$ $\Rightarrow y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3}
\end{array}} \right..
$$

Do $y’ > 0$, $\forall x \in ( – 1;3)$ suy ra hàm số đồng biến trên khoảng $(-1;3).$

> **Đáp án: B**

## Bài 4. Cho hàm số $y = {x^2}\left( {6 – {x^2}} \right).$ Khẳng định nào sau đây là đúng?

<!-- chunk:5 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số đồng biến trên $( – \infty ;9).$

Ta có $y’ = – 4{x^3} + 12x$, $y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm \sqrt 3 }
\end{array}} \right..
$$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-6.png" alt="">

Từ bảng xét dấu $y’$ ta có hàm số đồng biến trên $( – \infty ; – \sqrt 3 )$ và $(0;\sqrt 3 ).$

> **Đáp án: A**

## Bài 5. Kết luận nào sau đây về tính đơn điệu của hàm số $y = \frac{{2x + 1}}{{x + 1}}$ là đúng?

<!-- chunk:6 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số đồng biến trên các khoảng $( – \infty ; – 1)$ và $( – 1; + \infty ).$

Ta có: $y’ = \frac{1}{{{{(x + 1)}^2}}} > 0$, $\forall x \ne – 1.$

Suy ra hàm số đồng biến trên các khoảng $( – \infty ; – 1)$ và $( – 1; + \infty ).$

> **Đáp án: D**

## Bài 6. Cho hàm số $y = \sqrt {{x^2} – 1} .$ Mệnh đề nào dưới đây đúng?

<!-- chunk:7 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số đồng biến trên $(1; + \infty ).$

Tập xác định: $( – \infty ; – 1] \cup [1; + \infty ).$

Ta có: $y’ = \frac{1}{{2\sqrt {{x^2} – 1} }}\left( {{x^2} – 1} \right)’$ $= \frac{x}{{\sqrt {{x^2} – 1} }}.$

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-7.png" alt="">

Từ bảng biến thiên của hàm số ta thấy hàm số đồng biến trên $(1; + \infty ).$

> **Đáp án: D**

## Bài 7. Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = {(x + 1)^2}(2 – x)(x + 3).$ Mệnh đề nào dưới đây đúng?

<!-- chunk:8 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số đồng biến trên khoảng $(-3;2).$

Ta có: $f'(x) = {(x + 1)^2}(2 – x)(x + 3) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 2}\\
{x = – 3}
\end{array}} \right.
$$
 (trong đó nghiệm $x = -1$ là nghiệm kép).

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc-8.png" alt="">

Hàm số đồng biến trên khoảng $(-3;2).$

> **Đáp án: D**

Lưu ý: Qua nghiệm bội bậc chẵn hàm số không đổi dấu. Ở đây $x = -1$ là nghiệm kép hay nghiệm bội bậc hai.

## Bài 8. Cho hàm số $f(x) = \sqrt {{x^2} + 2x + 2} + \sqrt {{x^2} – 2x + 2} .$ Mệnh đề nào dưới đây đúng?

A. $f(\sqrt[3]{4}) > f(\sqrt[4]{5}).$

B. $f(\sqrt[3]{4}) < f(\sqrt[4]{5}).$

C. $f(\sqrt[4]{5}) = 2f(\sqrt[3]{4}).$

D. $f(\sqrt[3]{4}) = f(\sqrt[4]{5}).$

Cách 1: Tập xác định: $D = R.$

Ta có: $f'(x)$ $= \frac{{x + 1}}{{\sqrt {{x^2} + 2x + 2} }} + \frac{{x – 1}}{{\sqrt {{x^2} – 2x + 2} }} > 0$, $\forall x > 1.$

Suy ra hàm số đồng biến trên $(1; + \infty ).$

Ta có: $\sqrt[3]{4} > \sqrt[4]{5} > 1$ $\Rightarrow f(\sqrt[3]{4}) > f(\sqrt[4]{5}).$

Cách 2: Dùng máy tính.

Ta có $f(x) = \sqrt {{x^2} + 2x + 2} + \sqrt {{x^2} – 2x + 2} .$

$f(\sqrt[3]{4})$ $= \sqrt {{{(\sqrt[3]{4})}^2} + 2.\sqrt[3]{4} + 2}$ $+ \sqrt {{{(\sqrt[3]{4})}^2} – 2.\sqrt[3]{4} + 2}$ $\approx 3,93368.$

$f(\sqrt[4]{5})$ $= \sqrt {{{(\sqrt[4]{5})}^2} + 2.\sqrt[4]{5} + 2}$ $+ \sqrt {{{(\sqrt[4]{5})}^2} – 2.\sqrt[4]{5} + 2}$ $\approx 3,804226.$

Vậy $f(\sqrt[3]{4}) > f(\sqrt[4]{5}).$

> **Đáp án: A**

## Bài 9. Hàm số nào sau đây thoả mãn với mọi ${x_1},{x_2} \in R$, ${x_1} > {x_2}$ thì $f\left( {{x_1}} \right) > f\left( {{x_2}} \right)$?

A. $f(x) = {x^4} + 2{x^2} + 1.$

B. $f(x) = \frac{{2x + 1}}{{x + 3}}.$

C. $f(x) = {x^3} + {x^2} + 1.$

D. $f(x) = {x^3} + {x^2} + 3x + 1.$

Vì ${x_1},{x_2} \in R$ suy ra tập xác định của hàm số là $D = R$ $\Rightarrow$ Loại đáp án B.

Vì $\forall {x_1},{x_2} \in R$, ${x_1} > {x_2}$ thì $f\left( {{x_1}} \right) > f\left( {{x_2}} \right)$ $\Rightarrow$ Hàm số đồng biến trên $R.$

Xét hàm số $f(x) = {x^4} + 2{x^2} + 1.$

Ta có $f'(x) = 4{x^3} + 4x$ $\Rightarrow f'(x) = 0$ $\Leftrightarrow x = 0.$

Suy ra $f'(x)$ đổi dấu qua $x = 0$ $\Rightarrow$ Hàm số không đồng biến trên $R$ nên hàm số ở đáp án A không thỏa mãn.

Xét hàm số $f(x) = {x^3} + {x^2} + 1.$

Ta có $f'(x) = 3{x^2} + 2x$ $\Rightarrow f'(x) = 0$ $\Leftrightarrow x = 0$ hoặc $x = – \frac{2}{3}$ $\Rightarrow f'(x)$ đổi dấu qua $x = 0$ hoặc $x = – \frac{2}{3}.$ Do đó hàm số không đồng biến trên $R$ nên hàm số ở đáp án C không thỏa mãn.

Xét hàm số $f(x) = {x^3} + {x^2} + 3x + 1.$

Ta có $f'(x) = 3{x^2} + 2x + 3 > 0$, $\forall x \in R$ nên hàm số đồng biến trên $R.$

> **Đáp án: D**

## Bài 10. Hàm số $y = \frac{{2x – 3}}{{\sqrt {{x^2} – 1} }}$ nghịch biến trên khoảng nào trong các khoảng dưới đây?

A. $( – \infty ; – 1)$ và $\left( {1;\frac{3}{2}} \right).$

B. $\left( {\frac{3}{2}; + \infty } \right).$

C. $\left( {1;\frac{3}{2}} \right).$

D. $( – \infty ; – 1).$

Tập xác định $D = ( – \infty ; – 1) \cup (1; + \infty ).$

Ta có $y’ = \frac{{3x – 2}}{{\sqrt {{{\left( {{x^2} – 1} \right)}^3}} }}$, $y’ = 0$ $\Leftrightarrow x = \frac{2}{3}.$

Nhận thấy $y’ < 0$ $\Rightarrow 3x – 2 < 0$ $\Leftrightarrow x < \frac{2}{3}.$

Từ tập xác định suy ra hàm số nghịch biến trên $( – \infty ; – 1).$

> **Đáp án: D**

## Bài tập
## Bài 1. Cho hàm số $y = f(x)$ có đạo hàm trên $R.$ Mệnh đề nào sau đây đúng?

<!-- chunk:9 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Nếu $f'(x) < 0$, $\forall x \in (a;b)$ thì $f(x)$ nghịch biến trên $(a;b).$

## Bài 2. Cho hàm số $f(x) = {x^4} + 2{x^2}.$ Khẳng định nào sau đây sai?

A. $f(2018) < f(2019).$

B. $f( – 2019) > f( – 2018).$

C. $f(e) < f(\pi ).$

D. $f( – 2019) < f(1).$

## Bài 3. Hàm số nào sau đây không đồng biến trên khoảng $( – \infty ; + \infty )$?

A. $f(x) = \frac{{x – 1}}{{x + 2}}.$

B. $g(x) = {x^3} + 3x.$

C. $h(x) = 2x + \cos x + 1.$

D. $k(x) = {x^5} + x.$

## Bài 4. Tìm khoảng đồng biến của hàm số $y = \sqrt {x – 3} + \sqrt {6 – x} .$

A. $( – \infty ;6).$

B. $(3; + \infty ).$

C. $\left( {\frac{9}{2};6} \right).$

D. $D.\left( {3;\frac{9}{2}} \right).$

## Bài 5. Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $(a;b).$ Tìm mệnh đề sai trong các mệnh đề sau.

<!-- chunk:10 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Nếu $f'(x) > 0$ với mọi $x \in (a;b)$ thì hàm số $y = f(x)$ đồng biến trên $(a;b).$

## Bài 6. Trong các hàm số sau, hàm số nào đồng biến trên khoảng $(1;3)$?

A. $y = {x^2} – 4x + 5.$

B. $y = \frac{{{x^2} – 4x + 8}}{{x – 2}}.$

C. $y = 2{x^2} – {x^4}.$

D. $y = \frac{{x – 3}}{{x – 1}}.$

## Bài 7. Cho hàm số $y = – {x^3} – 3{x^2} + 4.$ Mệnh đề nào dưới đây đúng?

<!-- chunk:11 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số đồng biến trên khoảng $( – 2;0).$

## Bài 8. Cho hàm số $y = {x^4} – 8{x^2} – 4.$ Các khoảng đồng biến của hàm số là:

A. $( – 2;0)$ và $(2; + \infty ).$

B. $( – \infty ; – 2)$ và $(2; + \infty ).$

C. $( – \infty ; – 2)$ và $(0;2).$

D. $( – 2;0)$ và $(0;2).$

## Bài 9. Cho hàm số $y = \sqrt {{x^2} – 1} .$ Mệnh đề nào dưới đây đúng?

<!-- chunk:12 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số nghịch biến trên khoảng $( – \infty ;0).$

## Bài 10. Cho hàm số $y = \frac{{2x + 1}}{{x + 1}}.$ Mệnh đề đúng là:

<!-- chunk:13 level:1 source:https://toanmath.com/2019/11/xet-tinh-don-dieu-cua-ham-so-cho-boi-cong-thuc.html -->
## D. Hàm số đồng biến trên tập $R.$

**ĐÁP ÁN BÀI TẬP TỰ LUYỆN**

1. D.

2. D.

3. A.

4. D.

5. A.

6. D.

7. D.

8. A.

9. C.

10. A.