# Diện tích hình phẳng giới hạn bởi ba đường cong

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
Bài viết hướng dẫn phương pháp ứng dụng tích phân để tính diện tích hình phẳng giới hạn bởi ba đường cong, đây là dạng toán thường gặp trong chương trình Giải tích 12 chương 3: Nguyên hàm – Tích phân và Ứng dụng.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## **I. PHƯƠNG PHÁP GIẢI TOÁN

****Cách 1**:

+ Tính hoành độ giao điểm của từng cặp đồ thị.

+ Chia diện tích hình phẳng thành tổng của các diện tích hình phẳng giới hạn bởi hai đồ thị.

**Cách 2**:

+ Vẽ các đồ thị trên cùng một hệ trục tọa độ.

+ Từ đồ thị chia diện tích hình phẳng thành tổng của các diện tích hình phẳng giới hạn bởi hai đồ thị.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 1: Gọi $S$ là diện tích hình phẳng giới hạn bởi đồ thị ba hàm số $y = f(x)$, $y = g(x)$, $y = h(x)$ (phần gạch chéo trong hình vẽ bên).

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong-1.png" alt="">

Khẳng định nào sau đây đúng?

A. $S = \int_a^b {[f(x) – g(x)]dx}$ $+ \int_b^c {[f(x) – h(x)]dx} .$

B. $S = \int_a^b {[f(x) – h(x)]dx}$ $+ \int_b^c {[g(x) – h(x)]dx} .$

C. $S = \int_a^b {[g(x) – h(x)]dx}$ $+ \int_b^c {[f(x) – h(x)]dx} .$

D. $S = \int_a^b {[f(x) – g(x)]dx}$ $+ \int_b^c {[g(x) – h(x)]dx} .$

Lời giải:

Từ đồ thị ta có:

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong-2.png" alt="">

$S = {S_1} + {S_2}$ $= \int_a^b {[g(x) – h(x)]dx}$ $+ \int_b^c {[f(x) – h(x)]dx} .$

> **Đáp án: C**

<!-- chunk:3 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 2: Diện tích hình phẳng giới hạn bởi các đường $y = – {x^2} + 3x$, $y = x + 1$, $y = – x + 4$ bằng:

A. $\frac{1}{{12}}.$

B. $\frac{1}{6}.$

C. $\frac{1}{4}.$

D. $\frac{1}{3}.$

Lời giải:

Tìm các hoành độ giao điểm:

$– {x^2} + 3x = x + 1$ $\Leftrightarrow – {x^2} + 2x – 1 = 0$ $\Leftrightarrow x = 1.$

$– {x^2} + 3x = – x + 4$ $\Leftrightarrow – {x^2} + 4x – 4 = 0$ $\Leftrightarrow x = 2.$

$x + 1 = – x + 4$ $\Leftrightarrow 2x – 3 = 0$ $\Leftrightarrow x = \frac{3}{2}.$

Diện tích:

$S = \int_1^{\frac{3}{2}} {\left| { – {x^2} + 3x – x – 1} \right|dx}$ $+ \int_{\frac{3}{2}}^2 {\left| { – {x^2} + 3x + x – 4} \right|dx}$ $= \int_1^{\frac{3}{2}} {{{(x – 1)}^2}} dx$ $+ \int_{\frac{3}{2}}^2 {{{(x – 2)}^2}} dx.$

$= \left. {\frac{{{{(x – 1)}^3}}}{3}} \right|_1^{\frac{3}{2}}$ $+ \left. {\frac{{{{(x – 2)}^3}}}{3}} \right|_{\frac{3}{2}}^2$ $= \frac{1}{{12}}.$

> **Đáp án: A**

<!-- chunk:4 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 3: Diện tích hình phẳng giới hạn bởi các đường $y = 2{x^2}$, $y = \frac{{{x^2}}}{4}$, $y = \frac{{54}}{x}$ bằng:

A. $\frac{{63}}{2} – 54\ln 2.$

B. $54\ln 2.$

C. $– \frac{{63}}{2} + 54\ln 2.$

D. $\frac{{63}}{4}.$

Lời giải:

Tìm các hoành độ giao điểm:

$2{x^2} = \frac{{{x^2}}}{4} \Leftrightarrow x = 0.$

$2{x^2} = \frac{{54}}{x} \Leftrightarrow x = 3.$

$\frac{{{x^2}}}{4} = \frac{{54}}{x} \Leftrightarrow x = 6.$

Diện tích:

$S = \int_0^3 {\left| {2{x^2} – \frac{{{x^2}}}{4}} \right|dx}$ $+ \int_3^6 {\left| {\frac{{54}}{x} – \frac{{{x^2}}}{4}} \right|dx}$ $= \left| {\int_0^3 {\left( {2{x^2} – \frac{{{x^2}}}{4}} \right)dx} } \right|$ $+ \left| {\int_3^6 {\left( {\frac{{54}}{x} – \frac{{{x^2}}}{4}} \right)dx} } \right|.$

$= \left| {\left. {\frac{{7{x^3}}}{{12}}} \right|_0^3} \right| + \left| {\left. {\left( {54\ln x – \frac{{{x^3}}}{{12}}} \right)} \right|_3^6} \right|$ $= 54\ln 2.$

> **Đáp án: B**

<!-- chunk:5 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 4: Diện tích hình phẳng giới hạn bởi các đường $y = {e^x}$, $y = 3$, $y = 1 – 2x$ bằng:

A. $5 – 3\ln 3.$

B. $3\ln 3 – 5.$

C. $3\ln 3 – 1.$

D. $S = 3\ln 3 + 2e – 5.$

Lời giải:

Tìm các hoành độ giao điểm:

${e^x} = 3 \Leftrightarrow x = \ln 3.$

$3 = 1 – 2x \Leftrightarrow x = – 1.$

${e^x} = 1 – 2x$ $\Leftrightarrow {e^x} + 2x – 1 = 0$ $\Leftrightarrow x = 0$ (vì $f(x) = {e^x} + 2x – 1$ đồng biến trên $R$ và $x=0$ là một nghiệm của phương trình ${e^x} + 2x – 1 = 0$).

Diện tích:

$S = \int_{ – 1}^0 {\left| {3 – (1 – 2x)} \right|dx}$ $+ \int_0^{\ln 3} {\left| {3 – {e^x}} \right|dx} .$

$= \left| {\int_{ – 1}^0 {(2 + 2x)dx} } \right|$ $+ \left| {\int_0^{\ln 3} {\left( {3 – {e^x}} \right)dx} } \right|.$

$= 3\ln 3 – 1.$

> **Đáp án: C**

<!-- chunk:6 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 5: Diện tích hình phẳng giới hạn bởi các đường $y = \sqrt x$, $y = 2 – x$, $y = 0$ bằng:

A. $\frac{4}{3}.$

B. $\frac{7}{6}.$

C. $\frac{1}{6} + \frac{{4\sqrt 2 }}{3}.$

D. $\frac{{13}}{3}.$

Lời giải:

Tìm các hoành độ giao điểm:

$\sqrt x = 2 – x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 2}\\
{x = {{(2 – x)}^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

$\sqrt x = 0 \Leftrightarrow x = 0.$

$2 – x = 0 \Leftrightarrow x = 2.$

Diện tích:

$S = \int_0^1 | \sqrt x – (2 – x)|dx$ $+ \int_1^2 | 2 – x|dx$ $= \left| {\int_0^1 {(\sqrt x – 2 + x)} dx} \right|$ $+ \left| {\int_1^2 {(2 – x)dx} } \right|.$

$= \left| {\left. {\left( {\frac{{2x\sqrt x }}{3} – 2x + \frac{{{x^2}}}{2}} \right)} \right|_0^1} \right|$ $+ \left| {\left. {\left( {2x – \frac{{{x^2}}}{2}} \right)} \right|_1^2} \right|$ $= \frac{4}{3}.$

> **Đáp án: A**

<!-- chunk:7 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 6: Diện tích hình phẳng giới hạn bởi parabol $(P):y = {x^2} – x – 2$ và các tiếp tuyến của $(P)$ tại các giao điểm của $(P)$ với trục hoành bằng:

A. ${\frac{{63}}{4}.}$

B. ${\frac{{63}}{8}.}$

C. ${\frac{{117}}{8}.}$

D. ${\frac{9}{4}.}$

Lời giải:

Viết các tiếp tuyến:

$y = {x^2} – x – 2$ $\Rightarrow y’ = 2x – 1.$

Phương trình hoành độ giao điểm của $(P)$ với $Ox:$

${x^2} – x – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 2 \Rightarrow y'(2) = 3}
\end{array}} \right..
$$

Tại $M( – 1;0)$, $y'( – 1) = – 3$, phương trình tiếp tuyến là: $y=-3x-3.$

Tại $N(2;0)$, $y'(2) = 3$, phương trình tiếp tuyến là: $y = 3x – 6.$

Tìm các hoành độ giao điểm:

${x^2} – x – 2 = – 3x – 3$ $\Leftrightarrow x = – 1.$

${x^2} – x – 2 = 3x – 6$ $\Leftrightarrow x = 2.$

$– 3x – 3 = 3x – 6$ $\Leftrightarrow x = \frac{1}{2}.$

Diện tích:

$S = \int_{ – 1}^{\frac{1}{2}} {\left| {{x^2} – x – 2 – ( – 3x – 3)} \right|dx}$ $+ \int_{\frac{1}{2}}^2 {\left| {{x^2} – x – 2 – (3x – 6)} \right|dx} .$

$= \int_{ – 1}^{\frac{1}{2}} {{{(x + 1)}^2}} dx$ $+ \int_{\frac{1}{2}}^2 {{{(x – 2)}^2}} dx$ $= \left. {\frac{{{{(x + 1)}^3}}}{3}} \right|_{ – 1}^{\frac{1}{2}}$ $+ \left. {\frac{{{{(x – 2)}^3}}}{3}} \right|_{\frac{1}{2}}^2$ $= \frac{9}{4}.$

> **Đáp án: D**

<!-- chunk:8 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 7: Hình phẳng giới hạn bởi đồ thị hàm số $y = 3x – {x^2}$ và
$$
y = \left\{ {\begin{array}{l}
{ – \frac{x}{2}}&{{\rm{khi}}\:\:x \le 2}\\
{x – 3}&{{\rm{khi}}\:\:x > 2}
\end{array}} \right.
$$
 có diện tích là:

A. $S = \frac{2}{3}.$

B. $S = \frac{8}{3}.$

C. $S = 4.$

D. $S = 6.$

Lời giải:

Tìm các hoành độ giao điểm:

<img link="data_for_rag/toan12/images/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong-3.png" alt="">

$3x – {x^2} = – \frac{x}{2}$ $(x \le 2)$ $\Leftrightarrow x = 0.$

$3x – {x^2} = x – 3$ $(x > 2)$ $\Leftrightarrow x = 3.$

$– \frac{x}{2} = x – 3 \Leftrightarrow x = 2.$

Diện tích:

$S = \int_0^2 {\left( {3x – {x^2} + \frac{x}{2}} \right)dx}$ $+ \int_2^3 {\left( {3x – {x^2} – x + 3} \right)dx} = 6.$

> **Đáp án: D**

<!-- chunk:9 level:3 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## Ví dụ 8: Gọi $S$ là diện tích hình phẳng giới hạn bởi các đường $y = \sqrt {3x}$, $y = 6 – x$ và trục $Ox.$ Khẳng định nào sau đây là đúng?

A. $S = \int_0^6 {(\sqrt {3x} – 6 + x)dx} .$

B. $S = \int_0^6 {\sqrt {3x} dx} + \int_0^6 {(6 – x)dx} .$

C. $S = \int_0^3 {\sqrt {3x} } dx + \int_3^6 {(6 – x)dx} .$

D. $S = \int_0^6 {(6 – x – \sqrt {3x} )dx} .$

Lời giải:

Tìm các hoành độ giao điểm:

$\sqrt {3x} = 6 – x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{6 – x \ge 0}\\
{3x = {{(6 – x)}^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 3.$

$\sqrt {3x} = 0$ $\Leftrightarrow x = 0.$

$6 – x = 0 \Leftrightarrow x = 6.$

Diện tích:

$S = \int_0^3 | \sqrt {3x} – 0|dx$ $+ \int_3^6 | 6 – x – 0|dx$ $= \int_0^3 {\sqrt {3x} } dx + \int_3^6 {(6 – x)dx} .$

> **Đáp án: C**

<!-- chunk:10 level:1 source:https://toanmath.com/2019/12/dien-tich-hinh-phang-gioi-han-boi-ba-duong-cong.html -->
## III. LUYỆN TẬP

1. ĐỀ BÀI

## Câu 1: Diện tích hình phẳng giới hạn bởi nhánh đường cong $y = {x^2}$ $(x \ge 0)$, đường thẳng $y = 3 – 2x$ và trục hoành bằng:

A. $\frac{5}{{12}}.$

B. $\frac{{23}}{{12}}.$

C. $\frac{7}{8}.$

D. $\frac{7}{{12}}.$

## Câu 2: Diện tích hình phẳng giới hạn bởi các đường $y = \sqrt {2x}$, $y = 4 – x$ và trục $Ox$ bằng:

A. $\frac{{17}}{3}.$

B. $\frac{{16}}{3}.$

C. $\frac{{14}}{3}.$

D. $\frac{{13}}{3}.$

## Câu 3: Diện tích hình phẳng giới hạn bởi các đường $y = {x^3}$, $y = 2 – x$ và $y = 0$ bằng:

A. ${\frac{3}{4}.}$

B. ${\frac{{11}}{4}.}$

C. ${\frac{7}{2}.}$

D. ${\frac{5}{2}.}$

## Câu 4: Gọi $S$ là diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y = {x^2}$, $y = \frac{{{x^2}}}{{27}}$, $y = \frac{{27}}{x}.$ Khẳng định nào sau đây là đúng?

A. $S = \int_0^3 {\left| {{x^2} – \frac{{{x^2}}}{{27}}} \right|dx}$ $+ \int_3^9 {\left| {\frac{{27}}{x} – \frac{{{x^2}}}{{27}}} \right|dx} .$

B. $S = \int_0^3 {\left| {{x^2} – \frac{{27}}{x}} \right|dx}$ $+ \int_3^9 {\left| {\frac{{27}}{x} – \frac{{{x^2}}}{{27}}} \right|dx} .$

C. $S = \int_0^3 {\left| {\frac{{27}}{x} – \frac{{{x^2}}}{{27}}} \right|dx}$ $+ \int_3^9 {\left| {\frac{{27}}{x} – {x^2}} \right|dx} .$

D. $S = \int_0^3 {\left| {{x^2} – \frac{{27}}{x}} \right|dx}$ $+ \int_3^9 {\left| {{x^2} – \frac{{{x^2}}}{{27}}} \right|dx} .$

## Câu 5: Cho diện tích hình phẳng giới hạn bởi hai nhánh đường cong $y = {x^2}$ $(x \ge 0)$, $y = 4{x^2}$ $(x \ge 0)$ và đường thẳng $y=4$ bằng?

A. ${\frac{8}{3}.}$

B. ${\frac{{14}}{3}.}$

C. $7.$

D. ${\frac{{17}}{3}}.$

**2. BẢNG ĐÁP ÁN**

**Câu** | 
1 | 
2 | 
3 | 
4 | 
5 | 

**Đáp án** | 
D | 
C | 
A | 
A | 
A | 

3. HƯỚNG DẪN GIẢI

## Câu 1: Phương trình hoành độ giao điểm:

${x^2} = 3 – 2x$ $(x \ge 0)$ $\Leftrightarrow x = 1.$

${x^2} = 0 \Leftrightarrow x = 0.$

$3 – 2x = 0 \Leftrightarrow x = \frac{3}{2}.$

Diện tích:

$S = \int_0^1 {\left| {{x^2} – 0} \right|dx}$ $+ \int_1^{\frac{3}{2}} | 3 – 2x – 0|dx$ $= \frac{7}{{12}}.$

> **Đáp án: D**

## Câu 2: Phương trình hoành độ giao điểm:

$\sqrt {2x} = 4 – x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le 4}\\
{2x = {{(4 – x)}^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 2.$

$\sqrt x = 0 \Leftrightarrow x = 0.$

$4 – x = 0 \Leftrightarrow x = 4.$

Diện tích:

$S = \int_0^2 | \sqrt {2x} – 0|dx$ $+ \int_2^4 | 4 – x – 0|dx$ $= \frac{{14}}{3}.$

> **Đáp án: C**

## Câu 3: Phương trình hoành độ giao điểm:

${x^3} = 0 \Leftrightarrow x = 0.$

$2 – x = 0 \Leftrightarrow x = 2.$

${x^3} = 2 – x \Leftrightarrow x = 1.$

Diện tích:

$S = \int_0^1 {\left| {{x^3} – 0} \right|dx}$ $+ \int_1^2 | 2 – x|dx = \frac{3}{4}.$

> **Đáp án: A**

## Câu 4: Phương trình hoành độ giao điểm:

${x^2} = \frac{{{x^2}}}{{27}} \Leftrightarrow x = 0.$

$\frac{{{x^2}}}{{27}} = \frac{{27}}{x} \Leftrightarrow x = 9.$

$\frac{{27}}{x} = {x^2} \Leftrightarrow x = 3.$

Diện tích: $S = \int_0^3 {\left| {{x^2} – \frac{{{x^2}}}{{27}}} \right|dx}$ $+ \int_3^9 {\left| {\frac{{27}}{x} – \frac{{{x^2}}}{{27}}} \right|dx} .$

> **Đáp án: A**

## Câu 5: Phương trình hoành độ giao điểm:

${x^2} = 4$ $(x \ge 0)$ $\Leftrightarrow x = 2.$

$4{x^2} = 4$ $(x \ge 0)$ $\Leftrightarrow x = 1.$

${x^2} = 4{x^2} \Leftrightarrow x = 0.$

Diện tích: $S = \int_0^1 {\left| {4{x^2} – {x^2}} \right|dx}$ $+ \int_1^2 {\left| {4 – {x^2}} \right|dx} = \frac{8}{3}.$

> **Đáp án: A**