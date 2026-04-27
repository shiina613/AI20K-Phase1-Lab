# Điều kiện để đường thẳng tiếp xúc với đồ thị hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm điều kiện của tham số để đường thẳng tiếp xúc với đồ thị hàm số trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN
Sử dụng điều kiện tiếp xúc của đường thẳng với đồ thị hàm số:

+ Đường thẳng $y = ax + b$ tiếp xúc với đồ thị hàm số $y = f(x)$ khi và chỉ khi hệ phương trình 
$$
\left\{ {\begin{array}{l}
{f(x) = ax + b}\\
{f'(x) = a}
\end{array}} \right.
$$
 có nghiệm.

+ Khi đó, đường thẳng $y = ax + b$ là tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm $M\left( {{x_0};{y_0}} \right)$ khi ${x_0}$ và $a$ là nghiệm của hệ phương trình 
$$
\left\{ {\begin{array}{l}
{f\left( {{x_0}} \right) = a{x_0} + b}\\
{f’\left( {{x_0}} \right) = a}
\end{array}} \right..
$$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## Ví dụ 1. Cho hàm số $y = {x^3} – 3{x^2} + m – 1$ có đồ thị $(C).$ Tìm $m$ để đường thẳng $d:y = m(x – 2) + m – 5$ là tiếp tuyến của đồ thị $(C).$

$d$ là tiếp tuyến của $(C)$ khi và chỉ khi hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{{x^3} – 3{x^2} + m – 1 = m(x – 2) + m – 5}\\
{3{x^2} – 6x = m}
\end{array}} \right..
$$

Ta có ${x^3} – 3{x^2} + 3{x^2} – 6x – 1$ $= \left( {3{x^2} – 6x} \right)(x – 2)$ $+ 3{x^2} – 6x – 5.$

$\Leftrightarrow 2{x^3} – 9{x^2} + 12x – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{1}{2} \Rightarrow m = – \frac{9}{4}}\\
{x = 2 \Rightarrow m = 0}
\end{array}} \right..
$$

Vậy có hai giá trị của $m$ cần tìm là $m = – \frac{9}{4}$ và $m = 0.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## Ví dụ 2. Tìm $m$ để tiếp tuyến của đồ thị hàm số $(C):y = \frac{{2x + m}}{{x – 1}}$ tại điểm có hoành độ bằng $2$ chắn hai trục tọa độ tạo thành một tam giác có diện tích bằng $\frac{1}{2}.$

Tập xác định: $D = R\backslash \{ 1\} .$

Ta có $y’ = \frac{{ – 2 – m}}{{{{(x – 1)}^2}}}.$

Với ${x_0} = 2$ $\Rightarrow {y_0} = 4 + m$, $y'(2) = – 2 – m.$

Phương trình tiếp tuyến:

$y = ( – 2 – m)(x – 2) + 4 + m$ hay $y = – (2 + m)x + 8 + 3m.$

Tiếp tuyến cắt hai trục tọa độ tại $A\left( {\frac{{8 + 3m}}{{2 + m}};0} \right)$ và $B(0;8 + 3m)$ $(m \ne – 2).$

Khi đó $OA = \left| {\frac{{8 + 3m}}{{2 + m}}} \right|$, $OB = \left| {8 + 3m} \right|.$

Theo giả thiết ${S_{\Delta OAB}} = \frac{1}{2}$ $\Leftrightarrow \frac{1}{2}\left| {\frac{{8 + 3m}}{{2 + m}}} \right|.\left| {8 + 3m} \right| = \frac{1}{2}.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{{{(8 + 3m)}^2} = 2 + m}\\
{{{(8 + 3m)}^2} = – 2 – m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{9{m^2} + 47m + 62 = 0\:\:{\rm{(vô\:nghiệm)}}}\\
{9{m^2} + 49m + 66 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = – 3}\\
{m = – \frac{{22}}{9}}
\end{array}} \right..
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## Ví dụ 3. Cho hàm số $y = {x^3} – 6{x^2} + 3(m + 2)x + 4m – 5$ có đồ thị $(C).$ Tìm $m$ sao cho trên $(C)$ có đúng hai điểm có hoành độ lớn hơn $1$ sao cho tiếp tuyến tại mỗi điểm đó vuông góc với đường thẳng $\Delta 😡 + 2y + 3 = 0.$

Ta có $y’ = 3{x^2} – 12x + 3(m + 2).$

Gọi $M\left( {{x_0};{y_0}} \right)$ là tọa độ tiếp điểm.

Hệ số góc của tiếp tuyến tại $M:$ $k = 3x_0^2 – 12{x_0} + 3(m + 2).$

Hệ số góc của $\Delta$ là $– \frac{1}{2}.$

Do tiếp tuyến vuông góc với $\Delta$ nên:

$k = 3x_0^2 – 12{x_0} + 3(m + 2) = 2$ $\Leftrightarrow 3x_0^2 – 12{x_0} + 3m + 4 = 0$ $(1).$

Yêu cầu bài toán $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ lớn hơn $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 36 – 3(3m + 3) > 0}\\
{\left( {{x_1} – 1} \right) + \left( {{x_2} – 1} \right) > 0}\\
{\left( {{x_1} – 1} \right)\left( {{x_2} – 1} \right) > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{27 – 9m > 0}\\
{\left( {{x_1} + {x_2}} \right) – 2 > 0}\\
{{x_1}{x_2} – \left( {{x_1} + {x_2}} \right) + 1 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 3}\\
{4 – 2 > 0}\\
{3m + 4 – 4 + 1 > 0}
\end{array}} \right..
$$

$\Leftrightarrow – \frac{1}{3} < m < 3.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## Ví dụ 4. Cho hàm số $y = {x^3} + m{x^2} + 1$ có đồ thị $(C).$ Đường thẳng $\Delta :y = – x + 1$ cắt $(C)$ tại ba điểm phân biệt $A$, $B$, $C(0;1).$ Tìm $m$ sao cho tiếp tuyến của $(C)$ tại $A$ và $B$ vuông góc với nhau.

Ta có $y’ = 3{x^2} + 2mx$ $= x(3x + 2m).$

Phương trình hoành độ giao điểm:

${x^3} + m{x^2} + 1 = – x + 1$ $\Leftrightarrow x\left( {{x^2} + mx + 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{{x^2} + mx + 1 = 0}
\end{array}} \right..
$$

$\Delta$ cắt $(C)$ tại ba điểm phân biệt khi phương trình ${x^2} + mx + 1 = 0$ có hai nghiệm phân biệt khác $0.$

$\Leftrightarrow \Delta = {m^2} – 4 > 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m < – 2}\\
{m > 2}
\end{array}} \right..
$$

Khi đó $A$, $B$ có hoành độ lần lượt là 
$$
\left\{ {\begin{array}{l}
{{x_A} = \frac{{ – m + \sqrt {{m^2} – 4} }}{2}}\\
{{x_B} = \frac{{ – m – \sqrt {{m^2} – 4} }}{2}}
\end{array}} \right..
$$

Suy ra 
$$
\left\{ {\begin{array}{l}
{y{‘_A} = \frac{{ – m + \sqrt {{m^2} – 4} }}{2}\left[ {3\left( {\frac{{ – m + \sqrt {{m^2} – 4} }}{2}} \right) + 2m} \right]}\\
{y{‘_B} = \frac{{ – m – \sqrt {{m^2} – 4} }}{2}\left[ {3\left( {\frac{{ – m – \sqrt {{m^2} – 4} }}{2}} \right) + 2m} \right]}
\end{array}} \right..
$$

Theo giả thiết $y’\left( {{x_A}} \right)y’\left( {{x_B}} \right) = – 1.$

$\Leftrightarrow (m + 3\sqrt {{m^2} – 4} )(m – 3\sqrt {{m^2} – 4} ) = – 4$ $\Leftrightarrow – 8{m^2} + 40 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = \sqrt 5 }\\
{m = – \sqrt 5 }
\end{array}} \right..
$$

<!-- chunk:6 level:1 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Cho hàm số $y = \frac{{2x – 3}}{{x – 1}}$ có đồ thị $(C).$ Tìm các giá trị của $m$ để đường thẳng $y = 2x + m$ tiếp xúc với đồ thị hàm số $(C).$

A. $\forall m \in R.$

B. $m = \sqrt 8 .$

C. $m = \pm 2\sqrt 2 .$

D. $m \ne 1.$

Ta có $y’ = \frac{1}{{{{(x – 1)}^2}}}.$

Đường thẳng $y = 2x + m$ tiếp xúc với đồ thị hàm số $(C)$ khi hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{\frac{{2x – 3}}{{x – 1}} = 2x + m}\\
{\frac{1}{{{{(x – 1)}^2}}} = 2}
\end{array}} \right..
$$

Giải hệ phương trình ta được 
$$
\left\{ {\begin{array}{l}
{x = 1 + \frac{{\sqrt 2 }}{2}}\\
{m = – 2\sqrt 2 }
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{x = 1 – \frac{{\sqrt 2 }}{2}}\\
{m = 2\sqrt 2 }
\end{array}} \right..
$$

> **Đáp án: C**

## Bài 2. Đường thẳng $y = m$ tiếp xúc với đồ thị $(C):y = – 2{x^4} + 4{x^2} – 1$ tại hai điểm phân biệt. Tìm tung độ tiếp điểm.

A. $1.$

B. $-1.$

C. $0.$

D. $3.$

Phân tích: Ta nhận thấy $(C)$ là đồ thị hàm số trùng phương có ba điểm cực trị. Do đó, đường thẳng tiếp xúc với $(C)$ tại hai điểm phân biệt khi đường thẳng đó tiếp xúc với $(C)$ tại hai điểm cực trị có cùng tung độ.

Ta có $y’ = – 8{x^3} + 8x$, $y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

Khi đó đồ thị hàm số có hai điểm cực đại là $A(1;1)$, $B(-1;1).$

Đường thẳng $y = m$ tiếp xúc với $(C)$ tại hai điểm phân biệt khi $y = m$ là tiếp tuyến của $(C)$ tại hai điểm cực đại của $(C).$

Suy ra $m = 1$ và tung độ hai tiếp điểm là $1.$

> **Đáp án: A**

## Bài 3. Cho hàm số $y = \frac{{x + 1}}{{x + 2}}$ có đồ thị $(C)$ và đường thẳng $d:y = – 2x + m – 1$ ($m$ là tham số thực). Gọi ${k_1}$, ${k_2}$ là hệ số góc của tiếp tuyến tại giao điểm của $d$ và $(C).$ Tính giá trị của ${k_1}{k_2}.$

A. $3.$

B. $4.$

C. $\frac{1}{4}.$

D. $2.$

Ta có $y’ = \frac{1}{{{{(x + 2)}^2}}}.$

Hoành độ giao điểm của $d$ và $(C)$ là nghiệm của phương trình:

$\frac{{x + 1}}{{x + 2}} = – 2x + m – 1$ $\Leftrightarrow 2{x^2} + (6 – m)x + 3 – 2m = 0$ $(1).$

Phương trình $(1)$ luôn có hai nghiệm phân biệt khác $-2.$

Gọi ${x_1}$, ${x_2}$ là hai nghiệm phân biệt của phương trình $(1).$

Theo định lý Vi-ét 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{{m – 6}}{2}}\\
{{x_1}{x_2} = \frac{{3 – 2m}}{2}}
\end{array}} \right..
$$

Khi đó ${k_1}{k_2} = \frac{1}{{{{\left( {{x_1} + 2} \right)}^2}}}.\frac{1}{{{{\left( {{x_2} + 2} \right)}^2}}}.$

$= \frac{1}{{{{\left[ {{x_1}{x_2} + 2\left( {{x_1} + {x_2}} \right) + 4} \right]}^2}}}$ $= \frac{1}{{{{\left( {\frac{{3 – 2m}}{2} + m – 6 + 4} \right)}^2}}}$ $= 4.$

> **Đáp án: B**

## Bài 4. Cho hàm số $y = {x^4} – 2{m^2}{x^2} + 2m + 1.$ Tìm các giá trị của $m$ để tiếp tuyến của đồ thị hàm số tại giao điểm của đồ thị và đường thẳng $x = 1$ song song với đường thẳng $y = -12x + 2.$ A. $m = 4.$

B. $m = \pm 2.$

C. $m = -2.$

D. $m = 2.$

Ta có $y’ = 4{x^3} – 4{m^2}x.$

Với $x = 1$ $\Rightarrow y = 2 + 2m – 2{m^2}.$

Hệ số góc của tiếp tuyến của đồ thị hàm số tại điểm $A\left( {1;2 + 2m – 2{m^2}} \right)$ là $y'(1) = 4 – 4{m^2}.$

Tiếp tuyến song song với đường thẳng $y = -12x + 2$ nên:

$4 – 4{m^2} = – 12$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 2}\\
{m = – 2}
\end{array}} \right..
$$

Với $m = 2$ ta có $A(1;-2).$

Phương trình tiếp tuyến là $y = -12(x – 1) – 2$ hay $y = -12x + 10.$

Với $m = -2$, ta có $A(1;-10).$

Phương trình tiếp tuyến là $y = -12(x – 1) – 10$ hay $y = -12x + 2$ (loại).

> **Đáp án: D**

Lưu ý: Với những bài toán có liên quan đến yếu tố song song, ta cần kiểm tra xem giá trị $m$ có thỏa mãn hay không.

## Bài 5. Tìm các giá trị của $m$ để hàm số $y = m{x^3} – 3m{x^2} – 3x + 2$ nghịch biến trên $R$ và đồ thị của nó không có tiếp tuyến song song với trục hoành.

A. $– 1 < m < 0.$

B. $– 1 \le m \le 0.$

C. $– 1 \le m < 0.$

D. $– 1 < m \le 0.$

Ta có $y’ = 3m{x^2} – 6mx – 3.$

Với $m = 0$, ta có $y = -3x + 2.$ Hàm số nghịch biến trên $R$ và đồ thị không có tiếp tuyến (thỏa mãn).

Với $m \ne 0.$

Hàm số nghịch biến trên $R$ và tiếp tuyến của đồ thị không song song với trục hoành khi $y’ < 0$ với mọi $x \in R.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 0}\\
{\Delta {‘_{y’}} = 9{m^2} + 9m < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 0}\\
{ – 1 < m < 0}
\end{array}} \right..
$$

Vậy giá trị $m$ thỏa mãn bài toán là $– 1 < m \le 0.$

> **Đáp án: D**

## Bài 6. Tìm các giá trị của $m$ để đồ thị hàm số $y = {x^3} – 3mx + m + 1$ tiếp xúc với trục hoành.

A. $m = 1.$

B. $m = \pm 1.$

C. $m = -1.$

D. $m \ne 1.$

Ta có $y’ = 3{x^2} – 3m.$

Đồ thị hàm số tiếp xúc với trục hoành khi hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{{x^3} – 3mx + m + 1 = 0}\\
{3{x^2} – 3m = 0}
\end{array}} \right..
$$

Giải hệ phương trình ta được 
$$
\left\{ {\begin{array}{l}
{x = 1}\\
{m = 1}
\end{array}} \right..
$$

> **Đáp án: A**

## Bài 7. Cho hàm số $y = \frac{{x + 2}}{{x – 1}}$ có đồ thị $(C)$ và điểm $A(0;m).$ Tìm tập hợp $S$ các giá trị của tham số $m$ để từ $A$ kẻ được hai tiếp tuyến đến $(C)$ sao cho hai tiếp điểm tương ứng nằm hai phía trục hoành.

A. $S = \left( { – 2;\frac{3}{2}} \right)\backslash \{ 1\} .$

B. $S = ( – 2; + \infty ).$

C. $S = ( – 2; + \infty )\backslash \{ 1\} .$

D. $S = \left( { – \frac{2}{3}; + \infty } \right)\backslash \{ 1\} .$

Ta có $y’ = \frac{{ – 3}}{{{{(x – 1)}^2}}}.$

Phương trình đường thẳng qua $A(0;m)$ có hệ số góc $k$ là $\Delta :y = kx + m.$

Đường thẳng $\Delta$ là tiếp tuyến của $(C)$ khi hệ phương trình 
$$
\left\{ {\begin{array}{l}
{\frac{{x + 2}}{{x – 1}} = kx + m}\\
{\frac{{ – 3}}{{{{(x – 1)}^2}}} = k}
\end{array}} \right.
$$
 $(I)$ có nghiệm.

Ta có $(I)$ suy ra $\frac{{x + 2}}{{x – 1}} = \frac{{ – 3}}{{{{(x – 1)}^2}}}x + m$ $\Leftrightarrow (m – 1){x^2} – 2(m + 2)x + m + 2 = 0$ $(1).$

Để kẻ được hai tiếp tuyến thì $(1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 3m + 6 > 0}\\
{m \ne 1}\\
{m – 1 – 2(m + 2) + m + 2 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m > – 2}\\
{m \ne 1}
\end{array}} \right..
$$

Khi đó $(1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}.$

Theo định lí Vi-ét ta có 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{{2m + 4}}{{m – 1}}}\\
{{x_1}{x_2} = \frac{{m + 2}}{{m – 1}}}
\end{array}} \right..
$$

Hai tiếp điểm tương ứng nằm hai phía trục hoành khi $y\left( {{x_1}} \right).y\left( {{x_2}} \right) < 0.$

$\Leftrightarrow \frac{{{x_1} + 2}}{{{x_1} – 1}}.\frac{{{x_2} + 2}}{{{x_2} – 1}} < 0$ $\Leftrightarrow \frac{{{x_1}{x_2} + 2\left( {{x_1} + {x_2}} \right) + 4}}{{{x_1}{x_2} – \left( {{x_1} + {x_2}} \right) + 1}} < 0$ $\Leftrightarrow \frac{{9m + 6}}{{ – 3}} < 0$ $\Leftrightarrow m > – \frac{2}{3}.$

Vậy 
$$
\left\{ {\begin{array}{l}
{m > – \frac{2}{3}}\\
{m \ne 1}
\end{array}} \right..
$$

> **Đáp án: D**

## Bài 8. Cho hàm số $y = – {x^3} + m{x^2} + mx + 1$ có đồ thị $(C).$ Có bao nhiêu giá trị của $m$ để tiếp tuyến có hệ số góc lớn nhất của $(C)$ đi qua gốc tọa độ $O$?

A. $2.$

B. $1.$

C. $3.$

D. $4.$

Ta có $y’ = – 3{x^2} + 2mx + m$ $= – 3{\left( {x – \frac{m}{3}} \right)^2} + \frac{{{m^2}}}{3} + m$ $\le \frac{{{m^2}}}{3} + m.$

Dấu bằng xảy ra khi $x = \frac{m}{3}$ $\Rightarrow y = \frac{{2{m^3}}}{{27}} + \frac{{{m^2}}}{3} + 1.$

Khi đó tiếp tuyến của $(C)$ tại $M$ là $y = \left( {\frac{{{m^2}}}{3} + m} \right)\left( {x – \frac{m}{3}} \right)$ $+ \frac{{2{m^3}}}{{27}} + \frac{{{m^2}}}{3} + 1.$

Tiếp tuyến đi qua gốc tọa độ $O$ nên:

$0 = \left( {\frac{{{m^2}}}{3} + m} \right)\left( { – \frac{m}{3}} \right)$ $+ \frac{{2{m^3}}}{{27}} + \frac{{{m^2}}}{3} + 1$ $\Leftrightarrow m = 3.$

Có một giá trị $m = 3$ thỏa bài toán.

> **Đáp án: B**

## Bài 9. Cho hàm số $y = {x^3} – 2{x^2} + (m – 1)x + 2m$ có đồ thị là $\left( {{C_m}} \right).$ Tìm $m$ để tiếp tuyến có hệ số góc nhỏ nhất của đồ thị $\left( {{C_m}} \right)$ vuông góc với đường thẳng $\Delta :y = 3x + 2018.$

A. $m = \frac{7}{3}.$

B. $m = 1.$

C. $m = 2.$

D. $m = – \frac{1}{3}.$

Ta có $y’ = 3{x^2} – 4x + m – 1$ $= {\left( {x\sqrt 3 – \frac{2}{{\sqrt 3 }}} \right)^2} + m – \frac{7}{3}$ $\ge m – \frac{7}{3}.$

Dấu bằng xảy ra khi $x = \frac{2}{3}.$

Tiếp tuyến $d$ của $\left( {{C_m}} \right)$ có hệ số góc nhỏ nhất là $m – \frac{7}{3}.$

Theo giả thiết $d \bot \Delta$ nên $\left( {m – \frac{7}{3}} \right).3 = – 1$ $\Leftrightarrow m = 2.$

> **Đáp án: C**

## Bài 10. Gọi $S$ là tập tất cả các giá trị thực của tham số $m$ sao cho đường thẳng $d:y = mx – m – 3$ cắt đồ thị $(C):y = 2{x^3} – 3{x^2} – 2$ tại ba điểm phân biệt $A$, $B$, $I(1;-3)$ mà tiếp tuyến với $(C)$ tại $A$ và tại $B$ vuông góc với nhau. Tính tổng các phần tử của $S.$

A. $-1.$

B. $1.$

C. $2.$

D. $5.$

Ta có $y’ = 6{x^2} – 6x.$

Xét phương trình hoành độ giao điểm của $(C)$ và $(d):$

$2{x^3} – 3{x^2} – 2 = mx – m – 3$ $\Leftrightarrow (x – 1)\left( {2{x^2} – x – m – 1} \right) = 0$ $(*).$

Đường thẳng $(d)$ cắt đồ thị $(C)$ tại ba điểm phân biệt khi và chỉ khi $(*)$ có ba nghiệm phân biệt.

$\Leftrightarrow 2{x^2} – x – m – 1 = 0$ có hai nghiệm phân biệt $x \ne 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = 1 + 4.2(m + 1) > 0}\\
{{{2.1}^2} – 1 – m – 1 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m > \frac{{ – 9}}{8}}\\
{m \ne 0}
\end{array}} \right..
$$

Khi đó $d$ cắt $(C)$ tại ba điểm $A$, $B$, $I(1;-3)$ với $A$, $B$ có hoành độ lần lượt ${x_1}$, ${x_2}$ là nghiệm của phương trình $2{x^2} – x – m – 1 = 0.$

Theo định lý Vi-et ta có 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{1}{2}}\\
{{x_1}{x_2} = – \frac{{m + 1}}{2}}
\end{array}} \right..
$$

Hệ số góc của tiếp tuyến của $(C)$ tại $A$, $B$ lần lượt là: ${k_1} = 6x_1^2 – 6{x_1}$, ${k_2} = 6x_2^2 – 6{x_2}.$

Do tiếp tuyến với $(C)$ tại $A$ và tại $B$ vuông góc với nhau nên ${k_1}.{k_2} = – 1.$

$\Leftrightarrow \left( {6x_1^2 – 6{x_1}} \right)\left( {6x_2^2 – 6{x_2}} \right) = – 1.$

$\Leftrightarrow 36{\left( {{x_1}{x_2}} \right)^2} – 36{x_1}{x_2}\left( {{x_1} + {x_2}} \right)$ $+ 36{x_1}{x_2} + 1 = 0.$

$\Leftrightarrow 36{\left( { – \frac{{m + 1}}{2}} \right)^2} – 36\left( { – \frac{{m + 1}}{2}} \right)\frac{1}{2}$ $+ 36\left( { – \frac{{m + 1}}{2}} \right) + 1 = 0.$

$\Leftrightarrow 9{m^2} + 9m + 1 = 0.$

Phương trình có hai nghiệm phân biệt và có $S = -1.$

> **Đáp án: A**

<!-- chunk:7 level:1 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Đường thẳng $x + y = 2m$ là tiếp tuyến của đường cong $y = – {x^3} + 2x + 4$ khi $m$ bằng:

A. $-3$ hoặc $1.$

B. $1$ hoặc $3.$

C. $-1$ hoặc $3.$

D. $-3$ hoặc $-1.$

## Bài 2. Có bao nhiêu giá trị của tham số $m$ để đường thẳng $y = 3x + m$ là tiếp tuyến của đồ thị hàm số $y = {x^3} + 2$?

A. $0.$

B. $1.$

C. $2.$

D. $3.$

## Bài 3. Gọi $S$ là tập hợp các giá trị của $m$ sao cho đồ thị hàm số $y = {x^3} – 3{x^2} + 3mx + 3m + 4$ tiếp xúc với trục hoành. Tính tổng các phần tử của $S.$

A. $\frac{3}{2}.$

B. $1.$

C. $\frac{9}{4}.$

D. $\frac{{15}}{4}.$

## Bài 4. Tìm giá trị của $m$ để đường thẳng $y = 6x + m$ là tiếp tuyến của đường cong $y = {x^3} + 3x – 1.$

A. 
$$
\left[ {\begin{array}{l}
{m = – 3}\\
{m = 1}
\end{array}} \right..
$$

B. 
$$
\left[ {\begin{array}{l}
{m = 1}\\
{m = 3}
\end{array}} \right..
$$

C. 
$$
\left[ {\begin{array}{l}
{m = – 1}\\
{m = 3}
\end{array}} \right..
$$

D. 
$$
\left[ {\begin{array}{l}
{m = – 1}\\
{m = – 3}
\end{array}} \right..
$$

## Bài 5. Tìm các giá trị của $m$ để hai đường $y = \frac{{2{x^2} + mx + 2 – m}}{{x + m – 1}}$ và $y = x – 1$ tiếp xúc nhau?

A. $m \ne 2.$

B. $m = 1.$

C. $m = 2.$

D. $m \in R.$

## Bài 6. Tìm các giá trị của $m$ để hai đường $y = 2x – m + 1$ và $y = {x^2} + 5$ tiếp xúc nhau?

A. $m = 0.$

B. $m = 1.$

C. $m = 3.$

D. $m = -3.$

## Bài 7. Gọi $S$ là tập các giá trị của tham số $m$ để đồ thị hàm số $y = {x^4} – 2{x^2} + m – 2$ có đúng một tiếp tuyến song song với trục $Ox.$ Tìm tổng các phần tử của $S.$

A. $-2.$

B. $5.$

C. $-5.$

D. $3.$

## Bài 8. Cho hàm số $y = \frac{1}{3}{x^3} – 2m{x^2} + 8(m – 1)x + 2$ ($m$ là tham số) có đồ thị là $\left( {{C_m}} \right).$ Tìm tất cả giá trị $m$ sao cho tồn tại hai điểm $A$, $B$ nằm trên $\left( {{C_m}} \right)$ sao cho tiếp tuyến của $\left( {{C_m}} \right)$ tại $A$ và $B$ cùng song song với đường thẳng $y = 1 – 4x.$

A. $m = 1.$

B. $m \ne 1.$

C. $m \le 1.$

D. $m \ge 1.$

## Bài 9. Cho hàm số $y = f(x) = – {x^3} + 6{x^2} + 2$ có đồ thị $(C)$ và điểm $M(m;2).$ Gọi $S$ là tập các giá trị thực của $m$ để qua $M$ kẻ được đúng hai tiếp tuyến với đồ thị $(C).$ Tổng các phần tử của $S$ là:

A. $\frac{{12}}{3}.$

B. $\frac{{20}}{3}.$

C. $\frac{{19}}{3}.$

D. $\frac{{23}}{3}.$

## Bài 10. Cho hàm số $y = {x^3} – 3{x^2} + 4$ có đồ thị $(C).$ Gọi $S$ là tập hợp tất cả các giá trị thực của $k$ để đường thẳng $y = k(x – 2)$ cắt đồ thị $(C)$ tại ba điểm phân biệt $M(2;0)$, $N$, $P$ sao cho các tiếp tuyến của $(C)$ tại $N$ và $P$ vuông góc với nhau. Tính tổng tất cả các phần tử của tập $S.$

A. $2.$

B. $-1.$

C. $-2.$

D. $1.$

## Bài 11. Cho hàm số $y = \frac{{x – 1}}{{x + 2}}$, gọi $d$ là tiếp tuyến với đồ thị hàm số tại điểm có hoành độ bằng $m – 2.$ Biết đường thẳng $d$ cắt tiệm cận đứng của đồ thị hàm số tại điểm $A\left( {{x_1};{y_1}} \right)$ và cắt tiệm cận ngang của đồ thị hàm số tại điểm $B\left( {{x_2};{y_2}} \right).$ Gọi $S$ là tập hợp các số $m$ sao cho ${x_2} + {y_1} = – 5.$ Tính tổng bình phương các phần tử của $S.$

A. $0.$

B. $4.$

C. $10.$

D. $9.$

## Bài 12. Cho hàm số $y = {x^4} – 2m{x^2} + m$ có đồ thị $(C)$ với $m$ là tham số thực. Gọi $A$ là điểm thuộc đồ thị $(C)$ có hoành độ bằng $1.$ Tìm $m$ để tiếp tuyến $\Delta$ với đồ thị $(C)$ tại $A$ cắt đường tròn $(\gamma ):{x^2} + {(y – 1)^2} = 4$ tạo thành một dây cung có độ dài nhỏ nhất.

A. $\frac{{16}}{{13}}$.

B. ${ – \frac{{13}}{{16}}}$.

C. ${\frac{{13}}{{16}}}$.

D. $– \frac{{16}}{{13}}$.

<!-- chunk:8 level:1 source:https://toanmath.com/2019/11/dieu-kien-de-duong-thang-tiep-xuc-voi-do-thi-ham-so.html -->
## **V. ĐÁP ÁN BÀI TẬP TỰ LUYỆN

**1. B.

2. C.

3. C.

4. A.

5. D.

6. D.

7. B.

8. B.

9. B.

10. C.

11. C.

12. C.