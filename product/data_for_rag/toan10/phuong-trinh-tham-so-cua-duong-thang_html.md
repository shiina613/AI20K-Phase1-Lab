# Phương trình tham số của đường thẳng

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
Bài viết tóm tắt lý thuyết và hướng dẫn phương pháp giải một số dạng toán liên quan đến phương trình tham số của đường thẳng trong chương trình Hình học 10 chương 3.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## A. KIẾN THỨC CẦN NẮM
1. Vectơ chỉ phương và phương trình tham số của đường thẳng

a. Định nghĩa vectơ chỉ phương

Cho đường thẳng $\Delta$ Vectơ $\overrightarrow u \ne \vec 0$ gọi là vectơ chỉ phương (VTCP) của đường thẳng $\Delta$ nếu giá của nó song song hoặc trùng với $\Delta .$

Nhận xét:

+ Nếu $\overrightarrow u$ là VTCP của $\Delta$ thì $k\overrightarrow u$ $(k \ne 0)$ cũng là VTCP của $\Delta .$

+ VTPT và VTCP vuông góc với nhau. Do vậy nếu $\Delta$ có VTCP $\overrightarrow u = (a;b)$ thì $\vec n = ( – b;a)$ là một VTPT của $\Delta .$

b. Phương trình tham số của đường thẳng

Cho đường thẳng $\Delta$ đi qua ${M_0}\left( {{x_0};{y_0}} \right)$ và $\overrightarrow u = (a;b)$ là VTCP.

Khi đó $M(x;y) \in \Delta$ $\Leftrightarrow \overrightarrow {M{M_0}} = t\vec u$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = {x_0} + at}\\
{y = {y_0} + bt}
\end{array}} \right.
$$
, $t \in R$ $(*).$

Hệ $(*)$ gọi là phương trình tham số của đường thẳng $\Delta$, $t$ gọi là tham số.

Nhận xét: Nếu $\Delta$ có phương trình tham số là $(*)$ khi đó:

$A \in \Delta$ $\Leftrightarrow A\left( {{x_0} + at;{y_0} + bt} \right).$

2. Phương trình chính tắc của đường thẳng

Cho đường thẳng $\Delta$ đi qua ${M_0}\left( {{x_0};{y_0}} \right)$ và $\overrightarrow u = (a;b)$ (với $a \ne 0$, $b \ne 0$) là vectơ chỉ phương thì phương trình $\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b}$ được gọi là phương trình chính tắc của đường thẳng $\Delta .$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## B. CÁC DẠNG TOÁN VÀ PHƯƠNG PHÁP GIẢI
DẠNG TOÁN 1: VIẾT PHƯƠNG TRÌNH THAM SỐ VÀ CHÍNH TẮC CỦA ĐƯỜNG THẲNG.

1. PHƯƠNG PHÁP GIẢI
Để viết phương trình tham số của đường thẳng $\Delta$ ta cần xác định:

+ Điểm $A\left( {{x_0};{y_0}} \right) \in \Delta .$

+ Một vectơ chỉ phương $\vec u(a;b)$ của $\Delta .$

Khi đó phương trình tham số của $\Delta$ là 
$$
\left\{ {\begin{array}{l}
{x = {x_0} + at}\\
{y = {y_0} + bt}
\end{array}} \right.
$$
, $t \in R.$

Để viết phương trình chính tắc của đường thẳng $\Delta$ ta cần xác định:

+ Điểm $A\left( {{x_0};{y_0}} \right) \in \Delta .$

+ Một vectơ chỉ phương $\vec u(a;b)$, $ab \ne 0$ của $\Delta .$

Khi đó phương trình chính tắc của $\Delta$ là $\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b}$ (trường hợp $ab = 0$ thì đường thẳng không có phương trình chính tắc).

Chú ý:

+ Nếu hai đường thẳng song song với nhau thì chúng có cùng VTCP và VTPT.

+ Hai đường thẳng vuông góc với nhau thì VTCP của đường thẳng này là VTPT của đường thẳng kia và ngược lại.

+ Nếu $\Delta$ có VTCP $\vec u = (a;b)$ thì $\vec n = ( – b;a)$ là một VTPT của $\Delta .$

2. CÁC VÍ DỤ

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 1: Cho điểm $A(1;-3)$ và $B(-2;3).$ Viết phương trình tham số của đường thẳng $\Delta$ trong mỗi trường hợp sau:

a) $\Delta$ đi qua $A$ và nhận vectơ $\overrightarrow n (1;2)$ làm vectơ pháp tuyến.

b) $\Delta$ đi qua gốc tọa độ và song song với đường thẳng $AB.$

c) $\Delta$ là đường trung trực của đoạn thẳng $AB.$

a) Vì $\Delta$ nhận vectơ $\vec n(1;2)$ làm vectơ pháp tuyến nên VTCP của $\Delta$ là $\overrightarrow u ( – 2;1).$

Vậy phương trình tham số của đường thẳng $\Delta$ là: 
$$
\Delta :\left\{ {\begin{array}{l}
{x = 1 – 2t}\\
{y = – 3 + t}
\end{array}} \right..
$$

b) Ta có $\overrightarrow {AB} ( – 3;6)$ mà $\Delta$ song song với đường thẳng $AB$ nên nhận $\overrightarrow u ( – 1;2)$ làm VTCP.

Vậy phương trình tham số của đường thẳng $\Delta$ là: 
$$
\Delta :\left\{ {\begin{array}{l}
{x = – t}\\
{y = 2t}
\end{array}} \right..
$$

c) Vì $\Delta$ là đường trung trực của đoạn thẳng $AB$ nên nhận $\overrightarrow {AB} ( – 3;6)$ làm VTPT và đi qua trung điểm $I$ của đoạn thẳng $AB.$

Ta có $I\left( { – \frac{1}{2};0} \right)$ và $\Delta$ nhận $\overrightarrow u ( – 1;2)$ làm VTCP nên phương trình tham số của đường thẳng $\Delta$ là: 
$$
\Delta :\left\{ {\begin{array}{l}
{x = – \frac{1}{2} – t}\\
{y = 2t}
\end{array}} \right..
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 2: Viết phương trình tổng quát, tham số, chính tắc (nếu có) của đường thẳng $\Delta$ trong mỗi trường hợp sau:

a) $\Delta$ đi qua điểm $A(3;0)$ và $B(1;3).$

b) $\Delta$ đi qua $N(3;4)$ và vuông góc với đường thẳng 
$$
d’:\left\{ {\begin{array}{l}
{x = 1 – 3t}\\
{y = 4 + 5t}
\end{array}} \right..
$$

a) Đường thẳng $\Delta$ đi qua hai điểm $A$ và $B$ nên nhận $\overrightarrow {AB} = ( – 2;3)$ làm vectơ chỉ phương, do đó phương trình tham số là: 
$$
\left\{ {\begin{array}{l}
{x = 3 – 2t}\\
{y = 3t}
\end{array}} \right.
$$
, phương trình chính tắc là: $\frac{{x – 3}}{{ – 2}} = \frac{y}{3}$, phương trình tổng quát là: $3(x – 3) = – 2y$ hay $3x + 2y – 9 = 0.$

b) $\Delta \bot d’$ nên VTCP của $d’$ cũng là VTPT của $\Delta$ nên đường thẳng $\Delta$ nhận $\overrightarrow u ( – 3;5)$ làm VTPT và $\vec v( – 5; – 3)$ làm VTCP, do đó đó phương trình tổng quát là: $– 3(x – 3) + 5(y – 4) = 0$ hay $3x – 5y + 11 = 0$, phương trình tham số là: 
$$
\left\{ {\begin{array}{l}
{x = 3 – 5t}\\
{y = 4 – 3t}
\end{array}} \right.
$$
, phương trình chính tắc là: $\frac{{x – 3}}{{ – 5}} = \frac{{y – 4}}{{ – 3}}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 3: Cho tam giác $ABC$ có $A(-2;1)$, $B(2;3)$ và $C(1;-5).$

a) Viết phương trình đường thẳng chứa cạnh $BC$ của tam giác.

b) Viết phương trình đường thẳng chứa đường trung tuyến $AM.$

c) Viết phương trình đường thẳng đi qua hai điểm $D$, $G$ với $D$ là chân đường phân giác trong góc $A$ và $G$ là trọng tâm của $\Delta ABC.$

a) Ta có $\overrightarrow {BC} ( – 1; – 8)$ suy ra đường thẳng chứa cạnh $BC$ có phương trình là: 
$$
\left\{ {\begin{array}{l}
{x = 2 – t}\\
{y = 3 – 8t}
\end{array}} \right..
$$

b) $M$ là trung điểm của $BC$ nên $M\left( {\frac{3}{2}; – 1} \right)$ do đó đường thẳng chứa đường trung tuyến $AM$ nhận $\overrightarrow {AM} \left( {\frac{7}{2}; – 2} \right)$ làm VTCP.

Nên có phương trình là 
$$
\left\{ {\begin{array}{c}
{x = – 2 + \frac{7}{2}t}\\
{y = 1 – 2t}
\end{array}} \right..
$$

c) Gọi $D\left( {{x_D};{y_D}} \right)$ là chân đường phân giác hạ từ $A$ của tam giác $ABC.$

Ta có $\overrightarrow {BD} = \frac{{AB}}{{AC}}\overrightarrow {DC} .$

Mà $AB = \sqrt {{{( – 2 – 2)}^2} + {{(3 – 1)}^2}} = 2\sqrt 5$ và $AC = \sqrt {{{(1 + 2)}^2} + {{( – 5 – 1)}^2}} = 3\sqrt 5 .$

Suy ra:

$\overrightarrow {BD} = \frac{{AB}}{{AC}}\overrightarrow {DC} = \frac{2}{3}\overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_D} – 2 = \frac{2}{3}\left( {1 – {x_D}} \right)}\\
{{y_D} – 3 = \frac{2}{3}\left( { – 5 – {y_D}} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_D} = \frac{8}{5}}\\
{{y_D} = \frac{{ – 1}}{5}}
\end{array}} \right.
$$
 $\Rightarrow D\left( {\frac{8}{5}; – \frac{1}{5}} \right).$

$G\left( {\frac{1}{3}; – \frac{1}{3}} \right)$ là trọng tâm của tam giác $ABC.$

Ta có $\overrightarrow {DG} \left( { – \frac{{19}}{{15}}; – \frac{2}{{15}}} \right)$ suy ra đường thẳng $DG$ nhận $\overrightarrow u = (19;2)$ làm VTCP, nên có phương trình là: 
$$
\left\{ {\begin{array}{l}
{x = \frac{1}{3} + 19t}\\
{y = – \frac{1}{3} + 2t}
\end{array}} \right..
$$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 4: Cho tam giác $ABC$ biết $AB:x + y – 1 = 0$, $AC:x – y + 3 = 0$ và trọng tâm $G(1;2).$ Viết phương trình đường thẳng chứa cạnh $BC.$

Ta có tọa độ điểm $A$ là nghiệm của hệ: 
$$
\left\{ {\begin{array}{l}
{x + y – 1 = 0}\\
{x – y + 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – 1}\\
{y = 2}
\end{array}} \right.
$$
 $\Rightarrow A( – 1;2).$

Gọi $M(x;y)$ là trung điểm của $BC.$

Vì $G$ là trọng tâm nên $\overrightarrow {AG} = 2.\overrightarrow {GM}$, $\overrightarrow {AG} (2;0)$, $\overrightarrow {GM} (x – 1;y – 2).$

Suy ra 
$$
\left\{ {\begin{array}{l}
{2 = 2.(x – 1)}\\
{0 = 2.(y – 2)}
\end{array}} \right.
$$
 $\Rightarrow M(2;2).$

$B\left( {{x_B};{y_B}} \right) \in AB$ $\Rightarrow {x_B} + {y_B} – 1 = 0$ $\Rightarrow {y_B} = 1 – {x_B}$, do đó $B\left( {{x_B};1 – {x_B}} \right).$

$C\left( {{x_C};{y_C}} \right) \in AC$ $\Rightarrow {x_C} – {y_C} + 3 = 0$ $\Rightarrow {y_C} = {x_C} + 3$, do đó $C\left( {{x_C};{x_C} + 3} \right).$

Mà $M$ là trung điểm của $BC$ nên ta có:

$$
\left\{ {\begin{array}{l}
{{x_M} = \frac{{{x_B} + {x_C}}}{2}}\\
{{y_M} = \frac{{{y_B} + {y_C}}}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_B} + {x_C} = 4}\\
{{x_C} – {x_B} = 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{{x_B} = 2}\\
{{x_C} = 2}
\end{array}} \right..
$$

Vậy $B(2; – 1)$, $C(2;5)$ $\Rightarrow \overrightarrow {BC} (0;6)$ suy ra phương trình đường thẳng $BC$ là 
$$
\left\{ {\begin{array}{l}
{x = 2}\\
{y = – 1 + 6t}
\end{array}} \right..
$$

## Bài tập
## Bài 1: Cho điểm $A(2;-2)$ và $B(0;1).$ Viết phương trình tham số của đường thẳng $\Delta$ trong mỗi trường hợp sau:

a) $\Delta$ đi qua $A$ và nhận vectơ $\overrightarrow u (1;2)$ làm vectơ chỉ phương.

b) $\Delta$ đi qua $A$ và nhận vectơ $\vec n(4;2)$ làm vectơ pháp tuyến.

c) $\Delta$ đi qua $C(1;1)$ và song song với đường thẳng $AB.$

d) $\Delta$ là đường trung trực của đoạn thẳng $AB.$

a) Phương trình tham số của đường thẳng $\Delta$ là 
$$
\Delta :\left\{ {\begin{array}{l}
{x = 2 + t}\\
{y = – 2 + 2t}
\end{array}} \right..
$$

b) Vì $\Delta$ nhận vectơ $\vec n(4;2)$ làm vectơ pháp tuyến nên VTCP của $\Delta$ là $\overrightarrow u ( – 1;2).$

Vậy phương trình tham số của đường thẳng $\Delta$ là 
$$
\Delta :\left\{ {\begin{array}{l}
{x = 2 – t}\\
{y = – 2 + 2t}
\end{array}} \right..
$$

c) Ta có $\overrightarrow {AB} ( – 2;3)$ mà $\Delta$ song song với đường thẳng $AB$ nên nhận $\overrightarrow u ( – 2;3)$ làm VTCP.

Vậy phương trình tham số của đường thẳng $\Delta$ là 
$$
\Delta :\left\{ {\begin{array}{l}
{x = 1 – 2t}\\
{y = 1 + 3t}
\end{array}} \right..
$$

d) Vì $\Delta$ là đường trung trực của đoạn thẳng $AB$ nên nhận $\overrightarrow {AB} ( – 2;3)$ làm VTPT và đi qua trung điểm $I$ của đoạn thẳng $AB.$

Ta có: $I\left( {1;\frac{1}{2}} \right)$ và $\Delta$ nhận $\overrightarrow u (3;2)$ làm VTCP nên phương trình tham số của đường thẳng $\Delta$ là: 
$$
\Delta :\left\{ {\begin{array}{l}
{x = 1 + 3t}\\
{y = \frac{1}{2} + 2t}
\end{array}} \right..
$$

## Bài 2: Viết phương trình tổng quát, tham số, chính tắc (nếu có) của đường thẳng $\Delta$ trong mỗi trường hợp sau:

a) $\Delta$ đi qua điểm $A(3;0)$ và $B(-1;0).$

b) $\Delta$ đi qua $M(1;2)$ và vuông góc với đường thẳng $d:x – 3y – 1 = 0.$

c) $\Delta$ đi qua gốc tọa độ và song song với đường thẳng 
$$
\Delta ‘:\left\{ {\begin{array}{l}
{x = 1 + 3t}\\
{y = 2t}
\end{array}} \right..
$$

a) Đường thẳng $\Delta$ đi qua hai điểm $A$ và $B$ nên nhận $\overrightarrow {AB} = ( – 4;0)$ làm vectơ chỉ phương, do đó phương trình tham số là: 
$$
\left\{ {\begin{array}{l}
{x = 3 – 4t}\\
{y = 0}
\end{array}} \right..
$$

Phương trình chính tắc không có, phương trình tổng quát là $y = 0.$

b) $\Delta \bot d$ nên VTPT của $d$ cũng là VTCP của $\Delta$ nên đường thẳng $\Delta$ nhận $\overrightarrow u (1; – 3)$ làm VTCP, nên phương trình tham số là: 
$$
\left\{ {\begin{array}{c}
{x = 1 + t}\\
{y = 2 – 3t}
\end{array}} \right.
$$
, phương trình chính tắc là: $\frac{{x – 1}}{1} = \frac{{y – 2}}{{ – 3}}$, phương trình tổng quát là $3x + y – 5 = 0.$

c) $\Delta //\Delta ‘$ nên VTCP của $\Delta ‘$ cũng là VTCP của $\Delta$, nên đường thẳng $\Delta$ nhận $\overrightarrow u (3;2)$ làm VTCP, nên phương trình tham số là: 
$$
\left\{ {\begin{array}{l}
{x = 3t}\\
{y = 2t}
\end{array}} \right.
$$
, phương trình chính tắc là $\frac{x}{3} = \frac{y}{2}$, phương trình tổng quát là $2x – y = 0.$

## Bài 3: Cho tam giác $ABC$ có $A(2;-1)$, $B(-2;-3)$ và $C(-1;5).$

a) Viết phương trình đường thẳng chứa cạnh của tam giác.

b) Viết phương trình đường thẳng chứa đường trung tuyến $AM.$

c) Viết phương trình đường thẳng đi qua trung điểm $AB$ và trọng tâm của tam giác $ABC.$

a) Ta có $\overrightarrow {AB} ( – 4; – 2)$ suy ra đường thẳng chứa cạnh $BC$ có phương trình là:

$$
\left\{ {\begin{array}{l}
{x = – 2 – 4t}\\
{y = – 3 – 2t}
\end{array}} \right..
$$

$\overrightarrow {BC} (1;8)$ suy ra đường thẳng chứa cạnh $BC$ có phương trình là 
$$
\left\{ {\begin{array}{c}
{x = – 2 + t}\\
{y = – 3 + 8t}
\end{array}} \right..
$$

$\overrightarrow {CA} (3; – 6)$ suy ra đường thẳng chứa cạnh $BC$ có phương trình là 
$$
\left\{ {\begin{array}{l}
{x = 2 + 3t}\\
{y = – 1 – 6t}
\end{array}} \right..
$$

b) $M$ là trung điểm của $BC$ nên $M\left( { – \frac{3}{2};1} \right)$ do đó đường thẳng chứa đường trung tuyến $AM$ nhận $\overrightarrow {AM} \left( { – \frac{7}{2};2} \right)$ làm VTCP nên có phương trình là: 
$$
\left\{ {\begin{array}{l}
{x = 2 – \frac{7}{2}t}\\
{y = – 1 + 2t}
\end{array}} \right..
$$

c) Trung điểm của $AB$ là $I(0; – 2)$, trọng tâm của tam giác $ABC$ là $G\left( { – \frac{1}{3};\frac{1}{3}} \right).$ Khi đó ta có $\overrightarrow {IG} \left( { – \frac{1}{3};\frac{7}{3}} \right)$ do đó 
$$
IG:\left\{ {\begin{array}{l}
{x = – t}\\
{y = – 2 + 7t}
\end{array}} \right..
$$

## Bài 4: Cho tam giác $ABC$ biết $A(1;4)$, $B(3;-1)$ và $C(6;-2).$

a) Viết phương trình đường thẳng chứa các cạnh $AB.$

b) Viết phương trình đường cao $AH.$

c) Viết phương trình đường trung tuyến $AM$ của tam giác.

d) Viết phương trình đường trung trực cạnh $BC.$

e) Viết phương trình đường thẳng đi qua trọng tâm của tam giác và song song với trục hoành.

f) Viết phương trình đường thẳng đi qua trung điểm $BC$ và vuông góc với trục tung.

g) Viết phương trình đường thẳng đi qua $A$ và tạo với hai trục tọa độ một tam giác cân đỉnh là gốc tọa độ.

h) Viết phương trình đường thẳng qua $C$ và chia tam giác thành hai phần, phần chứa điểm $A$ có diện tích gấp đối phần chứa điểm $B.$

a) $AB:5x + 2y – 13 = 0.$

b) $AH:3x – y + 1 = 0.$

c) Vì $M$ là trung điểm của $BC$ nên $M = \left( {\frac{9}{2}; – \frac{3}{2}} \right)$, $\overrightarrow {AM} = (7; – 11)$ $\Rightarrow AM:11x + 7y – 39 = 0.$

d) $3x – y – 12 = 0.$

e) Trọng tâm của tam giác $G = \left( {\frac{{10}}{3};\frac{1}{3}} \right)$, suy ra đường thẳng cần tìm là $y = \frac{1}{3}.$

f) Đường thẳng đi qua $M$ và vuông góc với trục tung có dạng là: $y = – \frac{3}{2}.$

g) $x + y – 5 = 0.$

h) Lấy $K \in AB$ sao cho $AK = 2BK$ $\to K = \left( {\frac{7}{3};\frac{2}{3}} \right).$

Khi đó $\overrightarrow {CK} = ( – 11;8)$ $\to CK:8x + 11y – 26 = 0.$

## Bài 5: Viết phương trình đường thẳng qua $M(3;2)$ và cắt tia $Ox$ tại $A$, tia $Oy$ tại $B$ sao cho:

a) $OA + OB = 12.$

b) Diện tích tam giác $OAB$ bằng $12.$

Gọi $A(a;0)$, $B(0;b)$ ($a > 0$, $b > 0$).

Phương trình $\Delta$ cần tìm có dạng: $\frac{x}{a} + \frac{y}{b} = 1.$

Mặt khác $OA = a$, $OB = b.$

a) ${\Delta _1}:x + 3y – 9 = 0$, ${\Delta _2}:2x + y – 8 = 0.$

b) $\Delta :2x + 3y – 12 = 0.$

## Bài 6: Cho hình bình hành hai cạnh có phương trình: $3x – y – 2 = 0$ và $x + y – 2 = 0.$ Viết phương trình hai cạnh còn lại biết tâm hình bình hành là $I(3;1).$

Gọi $AB:3x – y – 2 = 0$, $AD:x + y – 2 = 0.$

Khi đó $A(1;1)$ $\Rightarrow C(5;1)$, $CD:3x – y – 14 = 0$, $AD:x + y – 6 = 0.$

## Bài 7: Cho tam giác $ABC$ có trung điểm của $AB$ là $I(1;3)$, trung điểm $AC$ là $J( – 3;1).$ Điểm $A$ thuộc $Oy$ và đường $BC$ qua gốc tọa độ $O.$ Tìm tọa độ điểm $A$, phương trình $BC$ và đường cao vẽ từ $B.$

$A(0;a)$ $\Rightarrow B(2;6 – a)$, $C( – 6;2 – a).$

$BC$ đi qua gốc tọa độ nên $\overrightarrow {OB}$ và $\overrightarrow {OC}$ cùng phương, suy ra $2(2 – a) = (6 – a)( – 6)$ $\Leftrightarrow a = 5.$

DẠNG TOÁN 2: XÁC ĐỊNH TỌA ĐỘ ĐIỂM THUỘC ĐƯỜNG THẲNG.

1. PHƯƠNG PHÁP GIẢI

Để xác định tọa độ điểm thuộc đường thẳng ta dựa vào nhận xét sau:

+ Điểm $A$ thuộc đường thẳng 
$$
\Delta :\left\{ {\begin{array}{l}
{x = {x_0} + at}\\
{y = {y_0} + b{t^\prime }}
\end{array}} \right.
$$
, $t \in R$ (hoặc $\Delta :\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b}$) có dạng: $A\left( {{x_0} + at;{y_0} + bt} \right).$

Điểm $A$ thuộc đường thẳng $\Delta :ax + by + c = 0$ (điều kiện ${a^2} + {b^2} \ne 0$) có dạng: $A\left( {t;\frac{{ – at – c}}{b}} \right)$ với $b \ne 0$ hoặc $A\left( {\frac{{ – bt – c}}{a};t} \right)$ với $a \ne 0.$

2. CÁC VÍ DỤ

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 1: Cho đường thẳng $\Delta :3x – 4y – 12 = 0.$

a) Tìm tọa độ điểm $A$ thuộc $\Delta$ và cách gốc tọa độ một khoảng bằng $4.$

b) Tìm điểm $B$ thuộc $\Delta$ và cách đều hai điểm $E(5;0)$, $F(3;-2).$

c) Tìm tọa độ hình chiếu của điểm $M(1;2)$ lên đường thẳng $\Delta.$

a) Dễ thấy $M(0;-3)$ thuộc đường thẳng $\Delta$ và $\overrightarrow u (4;3)$ là một vectơ chỉ phương của $\Delta$ nên có phương trình tham số là 
$$
\left\{ {\begin{array}{l}
{x = 4t}\\
{y = – 3 + 3t}
\end{array}} \right..
$$

Điểm $A$ thuộc $\Delta$ nên tọa độ của điểm $A$ có dạng $A(4t; – 3 + 3t)$, suy ra:

$OA = 4$ $\Leftrightarrow \sqrt {{{(4t)}^2} + {{( – 3 + 3t)}^2}} = 4$ $\Leftrightarrow 25{t^2} – 18t – 7 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = \frac{{ – 7}}{{25}}}
\end{array}} \right..
$$

Vậy ta tìm được hai điểm là ${A_1}(4;0)$ và ${A_2}\left( {\frac{{ – 28}}{{25}};\frac{{ – 96}}{{25}}} \right).$

b) Vì $B \in \Delta$ nên $B(4t; – 3 + 3t).$

Điểm $B$ cách đều hai điểm $E(5;0)$, $F(3;-2)$ suy ra:

$E{B^2} = F{B^2}$ $\Leftrightarrow {(4t – 5)^2} + {(3t – 3)^2}$ $= {(4t – 3)^2} + {(3t – 1)^2}$ $\Leftrightarrow t = \frac{6}{7}.$

Suy ra $B\left( {\frac{{24}}{7}; – \frac{3}{7}} \right).$

c) Gọi $H$ là hình chiếu của $M$ lên $\Delta$ khi đó $H \in \Delta$ nên $H(4t; – 3 + 3t).$

Ta có $\overrightarrow u (4;3)$ là vectơ chỉ phương của $\Delta$ và vuông góc với $\overrightarrow {HM} (4t – 1;3t – 5)$ nên $\overrightarrow {HM} .\overrightarrow u = 0$ $\Leftrightarrow 4(4t – 1) + 3(3t – 5) = 0$ $\Leftrightarrow t = \frac{{19}}{{25}}.$

Suy ra $H\left( {\frac{{76}}{{25}}; – \frac{{18}}{{25}}} \right).$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 2: Cho hai đường thẳng $\Delta: x – 2y + 6 = 0$ và
$$
\Delta ‘:\left\{ {\begin{array}{c}
{x = – 1 – t}\\
{y = t}
\end{array}} \right..
$$

a) Xác định tọa độ điểm đối xứng với điểm $A(-1;0)$ qua đường thẳng $\Delta .$

b) Viết phương trình đường thẳng đối xứng với $\Delta ‘$ qua $\Delta .$

a) Gọi $H$ là hình chiếu của $A$ lên $\Delta$, khi đó $H(2t – 6;t).$

Ta có $\overrightarrow u (2;1)$ là vectơ chỉ phương của $\Delta$ và vuông góc với $\overrightarrow {AH} (2t – 5;t)$ nên:

$\overrightarrow {AH} .\overrightarrow u = 0$ $\Leftrightarrow 2(2t – 5) + t = 0$ $\Leftrightarrow t = 2$ $\Rightarrow H( – 2;2).$

$A’$ là điểm đối xứng với $A$ qua $\Delta$ suy ra $H$ là trung điểm của $AA’$, do đó:

$$
\left\{ {\begin{array}{l}
{{x_{A’}} = 2{x_H} – {x_A}}\\
{{y_{A’}} = 2{y_H} – {y_A}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_{A’}} = – 3}\\
{{y_{A’}} = 4}
\end{array}} \right..
$$

Vậy điểm cần tìm là $A'( – 3;4).$

b) Thay 
$$
\left\{ {\begin{array}{l}
{x = – 1 – t}\\
{y = t}
\end{array}} \right.
$$
 vào phương trình $\Delta$ ta được: $– 1 – t – 2t + 6 = 0$ $\Leftrightarrow t = \frac{5}{3}$, suy ra giao điểm của $\Delta$ và $\Delta ‘$ là $K\left( { – \frac{8}{3};\frac{5}{3}} \right).$

Dễ thấy điểm $A$ thuộc đường thẳng $\Delta ‘$ do đó đường thẳng đối xứng với $\Delta ‘$ qua $\Delta$ đi qua điểm $A’$ và điểm $K$ do đó nhận $\overrightarrow {A’K} = \left( {\frac{1}{3}; – \frac{7}{3}} \right) = \frac{1}{3}(1; – 7)$, nên có phương trình là: 
$$
\left\{ {\begin{array}{l}
{x = – 3 + t}\\
{y = 4 – 7t}
\end{array}} \right..
$$

Nhận xét: Để tìm tọa độ hình chiếu $H$ của $A$ lên $\Delta$ ta có thể làm cách khác như sau: ta có đường thẳng $AH$ nhận $\overrightarrow u (2;1)$ làm VTPT nên có phương trình là: $2x + y + 2 = 0$, do đó tọa độ $H$ là nghiệm của hệ:

$$
\left\{ {\begin{array}{l}
{x – 2y + 6 = 0}\\
{2x + y + 2 = 0}
\end{array}} \right.
$$
 $\Rightarrow H( – 2;2).$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 3: Cho tam giác $ABC$ vuông ở $A.$ Biết $A(-1;4)$, $B(1;-4)$, đường thẳng $BC$ đi qua điểm $K\left( {\frac{7}{3};2} \right).$ Tìm toạ độ đỉnh $C.$

Ta có $\overrightarrow {BK} \left( {\frac{4}{3};6} \right)$ suy ra đường thẳng $BC$ nhận $\overrightarrow u (2;9)$ làm VTCP.

Nên có phương trình là: 
$$
\left\{ {\begin{array}{c}
{x = 1 + 2t}\\
{y = – 4 + 9t}
\end{array}} \right..
$$

$C \in BC$ $\Rightarrow C(1 + 2t; – 4 + 9t).$

Tam giác $ABC$ vuông tại $A$ nên $\overrightarrow {AB} .\overrightarrow {AC} = 0$, $\overrightarrow {AB} (2; – 8)$, $\overrightarrow {AC} (2 + 2t; – 8 + 9t)$ suy ra $2(2 + 2t) – 8(9t – 8) = 0$ $\Leftrightarrow t = 1.$

Vậy $C(3;5).$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 4: Cho hình bình hành $ABCD.$ Biết $I\left( {\frac{7}{2};\frac{5}{2}} \right)$ là trung điểm của cạnh $CD$, $D\left( {3;\frac{3}{2}} \right)$ và đường phân giác góc $\widehat {BAC}$ có phương trình là $\Delta: x – y + 1 = 0.$ Xác định tọa độ đỉnh $B.$

Cách 1: Điểm $I$ là trung điểm của $CD$ nên 
$$
\left\{ {\begin{array}{l}
{{x_C} = 2{x_I} – {x_D} = 4}\\
{{y_C} = 2{x_I} – {y_D} = \frac{7}{2}}
\end{array}} \right.
$$
 $\Rightarrow C\left( {4;\frac{7}{2}} \right).$

Vì $A \in \Delta$ nên tọa độ điểm $A$ có dạng $A(a;a + 1).$

Mặt khác $ABCD$ là hình bình hành tương đương với $\overrightarrow {DA}$, $\overrightarrow {DC}$ không cùng phương và $\overrightarrow {AB} = \overrightarrow {DC} .$

$\overrightarrow {AB} = \overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_B} – a = 4 – 3}\\
{{y_B} – a – 1 = \frac{7}{2} – \frac{3}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_B} = a + 1}\\
{{y_B} = a + 3}
\end{array}} \right.
$$
 $\Rightarrow B(a + 1;a + 3).$

$\overrightarrow {DA}$, $\overrightarrow {DC}$ không cùng phương khi và chỉ khi $\frac{{a – 3}}{1} \ne \frac{{a + 1 – \frac{3}{2}}}{2}$ $\Leftrightarrow a \ne \frac{{11}}{2}.$

Đường thẳng $\Delta$ là phân giác góc $\widehat {BAC}$ nhận vectơ $\overrightarrow u = (1;1)$ làm vectơ chỉ phương nên $\cos (\overrightarrow {AB} ;\overrightarrow u )$ $= \cos (\overrightarrow {AC} ;\overrightarrow u )$ $\Leftrightarrow \frac{{\overrightarrow {AB} .\overrightarrow u }}{{|\overrightarrow {AB} ||\overrightarrow u |}} = \frac{{\overrightarrow {AC} .\overrightarrow u }}{{|\overrightarrow {AC} ||\overrightarrow u |}}$ $(*).$

Có $\overrightarrow {AB} (1;2)$, $\overrightarrow {AC} \left( {4 – a;\frac{5}{2} – a} \right)$ nên:

$(*) \Leftrightarrow \frac{3}{{\sqrt 5 }} = \frac{{\frac{{13}}{2} – 2a}}{{\sqrt {{{(4 – a)}^2} + {{\left( {\frac{5}{2} – a} \right)}^2}} }}$ $\Leftrightarrow 2{a^2} – 13a + 11 = 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 1}\\
{a = \frac{{11}}{2}\:{\rm{(loại)}}}
\end{array}} \right..
$$

Vậy tọa độ điểm $B(2;4).$

Cách 2: Ta có $C\left( {4;\frac{7}{2}} \right).$

Đường thẳng $d$ đi qua $C$ vuông góc với $\Delta$ nhận $\overrightarrow u = (1;1)$ làm vectơ pháp tuyến nên có phương trình là:

$1.(x – 4) + 1.\left( {y – \frac{7}{2}} \right) = 0$ hay $2x + 2y – 15 = 0.$

Tọa độ giao điểm $H$ của $\Delta$ và $d$ là nghiệm của hệ:

$$
\left\{ {\begin{array}{l}
{x – y + 1 = 0}\\
{2x + 2y – 15 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{{13}}{4}}\\
{y = \frac{{17}}{4}}
\end{array}} \right.
$$
 $\Rightarrow H\left( {\frac{{13}}{4};\frac{{17}}{4}} \right).$

Gọi $C’$ là điểm đối xứng với $C$ qua $\Delta$ thì khi đó $C’$ thuộc đường thẳng chứa cạnh $AB$ và $H$ là trung điểm của $CC’$ do đó:

$$
\left\{ {\begin{array}{l}
{{x_{C’}} = 2{x_H} – {x_C}}\\
{{y_{C’}} = 2{y_H} – {y_C}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_{C’}} = \frac{5}{2}}\\
{{y_{C’}} = 5}
\end{array}} \right.
$$
 $\Rightarrow C’\left( {\frac{5}{2};5} \right).$

Suy ra đường thẳng chứa cạnh $AB$ đi qua $C’$ và nhận $\overrightarrow {DC} = (1;2)$ làm vectơ chỉ phương nên có phương trình là: 
$$
\left\{ {\begin{array}{l}
{x = \frac{5}{2} + t}\\
{y = 5 + 2t}
\end{array}} \right..
$$

Thay $x$, $y$ từ phương trình đường thẳng chứa cạnh $AB$ vào phương trình đường thẳng $\Delta$ ta được: $\frac{5}{2} + t – 5 – 2t + 1 = 0$ $\Leftrightarrow t = – \frac{3}{2}$ suy ra $A(1;2).$

$ABCD$ là hình bình hành nên $\overrightarrow {AB} = \overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_B} – 1 = 1}\\
{{y_B} – 2 = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_B} = 2}\\
{{y_B} = 4}
\end{array}} \right..
$$

Suy ra $B(2;4).$

Chú ý: Bài toán có liên quan đến đường phân giác thì ta thường sử dụng nhận xét: “$\Delta$ là đường phân giác của góc tạo bởi hai đường thẳng cắt nhau ${\Delta _1}$ và ${\Delta _2}$ khi đó điểm đối xứng với điểm $M \in {\Delta _1}$ qua $\Delta$ thuộc ${\Delta _2}$”.

<!-- chunk:11 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tham-so-cua-duong-thang.html -->
## Ví dụ 5: Cho đường thẳng $d:x – 2y – 2 = 0$ và hai điểm $A(0;1)$ và $B(3;4).$ Tìm tọa độ điểm $M$ trên $d$ sao cho $|\overrightarrow {MA} + 2\overrightarrow {MB} |$ là nhỏ nhất.

$M \in d$ $\Rightarrow M(2t + 2;t)$, $\overrightarrow {MA} ( – 2t – 2;1 – t)$, $\overrightarrow {MB} (1 – 2t;4 – t).$

Do đó $MA + 2MB = ( – 6t; – 3t + 9).$

Suy ra $|\overrightarrow {MA} + 2\overrightarrow {MB} |$ $= \sqrt {{{( – 6t)}^2} + {{( – 3t + 9)}^2}}$ $= \sqrt {45\left( {t – \frac{3}{5}} \right) + \frac{{314}}{5}}$ $\ge \sqrt {\frac{{314}}{5}} .$

$|\overrightarrow {MA} + 2\overrightarrow {MB} |$ nhỏ nhất khi và chỉ khi $t = \frac{3}{5}$ do đó $M\left( {\frac{{16}}{5};\frac{3}{5}} \right)$ là điểm cần tìm.

## Bài tập
## Bài 1: Cho hai đường thẳng ${d_1}:x – y = 0$ và ${d_2}:2x + y – 1 = 0.$ Tìm toạ độ các đỉnh hình vuông $ABCD$ biết rằng đỉnh $A$ thuộc ${d_1}$, đỉnh $C$ thuộc ${d_2}$ và các đỉnh $B$, $D$ thuộc trục hoành.

$A \in {d_1}$, $C \in {d_2}$, $B$, $D$ thuộc trục hoành suy ra:

$A(a;a)$, $C(c;1 – 2c)$, $B(b;0)$, $D(d;0).$

Vì $ABCD$ là hình vuông và $B$, $D$ thuộc trục hoành nên $A$ và $C$ đối xứng nhau qua trục hoành, do đó 
$$
\left\{ {\begin{array}{l}
{a = c}\\
{a = 2c – 1}
\end{array}} \right.
$$
 $\Leftrightarrow a = c = 1.$ Suy ra $A(1;1)$, $C(1;-1).$

$ABCD$ là hình vuông suy ra $BA \bot BC$ và trung điểm của $AC$ trùng với trung điểm của $BD.$

$BA \bot BC$ $\Rightarrow \overrightarrow {BA} .\overrightarrow {BC} = 0$ $\Leftrightarrow {(1 – b)^2} – 1 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{b = 0}\\
{b = 2}
\end{array}} \right.
$$
 $(1).$

Trung điểm của $AC$ trùng trung điểm của $BD$ nên $b + d = 2$ $(2).$

Từ $(1)$ và $(2)$ ta có: 
$$
\left\{ {\begin{array}{l}
{b = 0}\\
{d = 2}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{b = 2}\\
{d = 0}
\end{array}} \right..
$$

Vậy có hai hình vuông thỏa mãn có tọa độ các đỉnh là: $A(1;1)$, $B(2;0)$, $C(1; – 1)$, $D(0;0)$ và $A(1;1)$, $B(0;0)$, $C(1; – 1)$, $D(2;0).$

## Bài 2: Cho điểm $A(2;2)$ và các đường thẳng ${d_1}:x + y – 2 = 0$ và ${d_2}:x + y – 8 = 0.$ Tìm toạ độ các điểm $B$ và $C$ lần lượt thuộc ${d_1}$ và ${d_2}$ sao cho tam giác $ABC$ vuông cân tại $A.$

$B \in {d_1}$, $C \in {d_2}$ nên tọa độ $B$, $C$ có dạng $B(a;2 – a)$, $C(b;8 – b).$

$\overrightarrow {AB} = (a – 2; – a)$, $\overrightarrow {AC} (b – 2;6 – b).$

Tam giác $ABC$ vuông cân tại $A$ nên:

$$
\left\{ {\begin{array}{l}
{AB = AC}\\
{\overrightarrow {AB} .\overrightarrow {AC} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{{(a – 2)}^2} + {a^2} = {{(b – 2)}^2} + {{(6 – b)}^2}}\\
{(a – 2)(b – 2) – a(6 – b) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{(a – 1)(b – 4) = 2}\\
{{{(a – 1)}^2} – {{(b – 4)}^2} = 3}
\end{array}} \right..
$$

Giải hệ này dễ dàng tìm được 
$$
\left\{ {\begin{array}{l}
{a = – 1}\\
{b = 3}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{a = 3}\\
{b = 5}
\end{array}} \right..
$$

Từ đó $B( – 1;3)$, $C(3;5)$ hoặc $B(3; – 1)$, $C(5;3).$

## Bài 3: Tam giác $ABC$ biết $A(2;-1)$ và phương trình hai đường phân giác trong của góc $B$ và góc $C$ lần lượt là: $\Delta: x – 2y + 1 = 0$, $\Delta ‘:2x – 3y + 6 = 0.$ Xác định tọa độ $B$ và $C.$

Điểm $A'(0;3) \in BC$ là điểm đối xứng $A$ qua $\Delta$, $A”(0;2) \in BC$ là điểm đổi xứng $A$ qua $\Delta ‘.$

Ta có $BC: x = 0$ suy ra $B\left( {0;\frac{1}{2}} \right)$ và $C\left( {0;\frac{5}{3}} \right).$

## Bài 4: Cho đường thẳng $\Delta: x – 2y + 3 = 0$ và hai điểm $A(2;5)$ và $B(-4;5).$ Tìm tọa độ điểm $M$ trên $\Delta$ sao cho: a) $2M{A^2} + M{B^2}$ đạt giá trị nhỏ nhất.

b) $MA + MB$ đạt giá trị nhỏ nhất.

c) $|MA – MB|$ đạt giá trị lớn nhất.

a) $M \in \Delta$ $\Rightarrow M(2t – 3;t)$ suy ra:

$2M{A^2} + M{B^2}$ $= 15{t^2} – 66t + 126$ $= 15{\left( {t – \frac{{11}}{5}} \right)^2} + \frac{{267}}{5}$ $\ge \frac{{267}}{5}.$

Dấu bằng xảy ra $\Leftrightarrow t = \frac{{11}}{5}$ $\Rightarrow M\left( {\frac{7}{5};\frac{{11}}{5}} \right).$

b) Dễ thấy $A$, $B$ cùng phía với $\Delta .$ Gọi $A’$ là điểm đối xứng $A$ qua $\Delta$ $\Rightarrow A'(4;1).$

Ta có $MA + MB$ $= MA’ + MB \ge A’B$, dấu “$=$” xảy ra:

$\Leftrightarrow M \in A’B$ $\Leftrightarrow M = A’B \cap \Delta$ $\Rightarrow M\left( {\frac{3}{2};\frac{9}{4}} \right).$

c) Lấy $A’$ như câu b suy ra: $|MA – MB|$ $= \left| {MA’ – MB} \right|$ $\le A’B$, dấu “$=$” xảy ra:

$\Leftrightarrow M = A’B \cap \Delta$ $\Rightarrow M\left( {\frac{3}{2};\frac{9}{4}} \right).$

## Bài 5: Viết phương trình đường thẳng $\Delta ‘$ đối xứng với đường thẳng $\Delta$ qua điểm $I$ biết:

a) $I( – 3;1)$, $\Delta :2x + y – 3 = 0.$

b) $I( – 1;3)$, 
$$
\Delta :\left\{ {\begin{array}{l}
{x = 2 – t}\\
{y = – 1 – 2t}
\end{array}} \right..
$$

a) $d(I;\Delta ) = \frac{{8\sqrt 5 }}{5}$, $\Delta ‘//\Delta$ $\Rightarrow \Delta ‘:2x + y + c = 0.$

$d(I;\Delta )$ $= d\left( {I;\Delta ‘} \right)$ $\Leftrightarrow \frac{{8\sqrt 5 }}{5} = \frac{{|c – 5|}}{{\sqrt 5 }}$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{c = – 3\:{\rm{(loại)}}}\\
{c = 13}
\end{array}} \right..
$$

Vậy $\Delta ‘:2x + y + 13 = 0.$

b) $\Delta ‘:2x – y + 15 = 0.$

## Bài 6: Cho hình vuông tâm $I(2;3)$ và $AB:x – 2y – 1 = 0.$ Viết phương trình các cạnh còn lại và các đường chéo.

$DC:x – 2y + 9 = 0.$

$BC:2x + y – 2 = 0.$

$AD:2x + y – 12 = 0.$

$AC:x + 3y – 11 = 0.$

$BD:3x – y – 3 = 0.$

## Bài 7: Cho tam giác $ABC$ vuông tại $A$ biết phương trình cạnh $BC$ là $\sqrt 3 x – y – \sqrt 3 = 0$, điểm $A$, $B$ thuộc trục hoành. Xác định toạ độ trọng tâm $G$ của tam giác $ABC$ biết bán kính đường tròn nội tiếp tam giác $ABC$ bằng $2.$

Dễ thấy $B(1;0).$ Vì $C \in \Delta$ $\Rightarrow C(a;\sqrt 3 (a – 1)).$

$A$, $B$ thuộc trục hoành và tam giác $ABC$ vuông nên $A(a;0).$

$\overrightarrow {AB} = (a – 1;0)$, $\overrightarrow {AC} = (0;\sqrt 3 (a – 1))$, $ABC$ là tam giác khi và chỉ khi $\overrightarrow {AB}$, $\overrightarrow {AC}$ không cùng phương hay $a \ne 1.$

Theo công thức tính diện tích tam giác ta có ${S_{ABC}} = pr = \frac{1}{2}AB.AC.$

Suy ra: $2(AB + BC + CA) = AB.AC.$

Mặt khác: $AB = |a – 1|$, $BC = 2|a – 1|$, $CA = \sqrt 3 |a – 1|.$

Nên ta có $2(3 + \sqrt 3 )|a – 1| = \sqrt 3 {(a – 1)^2}$ suy ra $a = 1$ (loại), $a = 3 + 2\sqrt 3$ hoặc $a = – 1 – 2\sqrt 3 .$

Vậy có hai trường hợp xảy ra ta tìm được tọa độ trọng tâm trong hai trường hợp đó là: ${G_1}\left( {\frac{{7 + 4\sqrt 3 }}{3};\frac{{2\sqrt 3 + 6}}{3}} \right)$, ${G_2}\left( {\frac{{ – 1 – 4\sqrt 3 }}{3};\frac{{ – 2\sqrt 3 – 6}}{3}} \right).$

Nhận xét:

Cách khác: Gọi $I$ là tâm đường tròn nội tiếp $\Delta ABC.$

Vì $r = 2$ $\Rightarrow {y_I} = \pm 2.$

Từ phương trình đường thẳng $BC$ suy ra $\widehat B = {60^0}$, do đó:

$BI:y = \frac{{x – 1}}{{\sqrt 3 }}$ $\Rightarrow {x_I} = 1 \pm 2\sqrt 3$ 
$$
\Rightarrow \left[ {\begin{array}{c}
{{x_A} = {x_C} = 3 + 2\sqrt 3 }\\
{{x_A} = {x_C} = – 1 – 2\sqrt 3 }
\end{array}} \right..
$$

Từ phương trình $BC$ ta suy ra được ${y_C}$ do đó tìm được tọa độ ba đỉnh rồi suy ra tọa độ trọng tâm.

## Bài 8: Cho tam giác $ABC$ có $C(-2;0)$, đường phân giác trong góc $A$ có phương trình là $5x + y – 3 = 0$ và thỏa mãn $\overrightarrow {AB} = 2\overrightarrow {OM}$ với $M(2;3).$ Tìm tọa độ điểm $A$, $B.$

$A(a;3 – 5a)$ $\Rightarrow B(4 + a;9 – 5a)$, $\vec u( – 1;5)$, $\overrightarrow {AB} (4;6)$, $\overrightarrow {AC} ( – 2 – a;5a – 3).$

$\cos (\overrightarrow {AB} ;\overrightarrow u )$ $= \cos (\overrightarrow {AC} ;\overrightarrow u )$ $\Leftrightarrow \frac{{26}}{{\sqrt {{4^2} + {6^2}} }}$ $= \frac{{26a – 13}}{{\sqrt {{{(2 + a)}^2} + {{(5a – 3)}^2}} }}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = 0}\\
{a = 1}
\end{array}} \right..
$$

Chỉ có trường hợp $a = 1 \Rightarrow B(5;4).$

## Bài 9: Cho tam giác $ABC$ cân tại $A$ có đỉnh $A(6;6)$, đường thẳng đi qua trung điểm của các cạnh $AB$ và $AC$ có phương trình $x + y – 4 = 0.$ Tìm tọa độ các đỉnh $B$ và $C$, biết điểm $\frac{\alpha }{{{a^2}}} + \frac{\beta }{{{a^{\prime 2}}}} = \frac{\alpha }{{{b^2}}} – \frac{\beta }{{{b^{\prime 2}}}} = k > 0$, $\alpha + \beta > 0$ nằm trên đường cao đi qua đỉnh $C$ của tam giác đã cho.

<img link="data_for_rag/toan10/images/phuong-trinh-tham-so-cua-duong-thang.png" alt="">

Gọi $H’$ là chân đường cao xuất phát từ đỉnh $A$, $H$ là giao điểm của đường thẳng $\Delta$ và $AH.$

Vì $H \in \Delta$ nên $H(a;4 – a).$

$\overrightarrow {AH} .\overrightarrow u = 0$ $\Leftrightarrow – 1(a – 6) + 1( – 2 – a) = 0$ $\Leftrightarrow a = 2$ $\Rightarrow H(2;2)$ (trong đó $\overrightarrow u ( – 1;1)$ là vectơ chỉ phương của $\Delta$).

$H$ là trung điểm của đoạn thẳng $AH’$ nên $H'( – 2; – 2).$

Đường thẳng chứa cạnh $BC$ đi qua $H$ nhận $\overrightarrow u$ làm vectơ chỉ phương nên 
$$
BC:\left\{ {\begin{array}{l}
{x = – 2 – t}\\
{y = – 2 + t}
\end{array}} \right..
$$

Gọi $B( – 2 – t;t – 2)$ $\Rightarrow C(t – 2; – 2 – t).$

$E$ nằm trên đường cao đi qua đỉnh $C$ nên $\overrightarrow {EC} .\overrightarrow {AB} = 0.$

Hay $(t – 3)( – 8 – t) + (1 – t)(t – 8) = 0$ $\Leftrightarrow {t^2} – 2t – 8 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{t = 4}\\
{t = – 2}
\end{array}} \right..
$$

Vậy $B( – 6;2)$, $C(2; – 6)$ hoặc $B(0; – 4)$, $C( – 4;0).$

## Bài 10: Cho tam giác $ABC$ có diện tích $S = \frac{3}{2}$, tọa độ các đỉnh $A(2; – 3)$, $B(3; – 2)$ và trọng tâm $G$ của tam giác nằm trên đường thẳng có phương trình $3x – y – 8 = 0.$ Tìm tọa độ đỉnh $C.$

$I$ là trung điểm $AB$ thì $I\left( {\frac{5}{2}; – \frac{5}{2}} \right).$

${S_{GAB}} = \frac{1}{2}$ $\Rightarrow GH = \frac{{{S_{GAB}}}}{{AB}} = \frac{1}{{\sqrt 2 }}$, $G(a;8 – 3a).$

$AB:x – y – 5 = 0$, $d(G;AB) = GH$ từ đó suy ra $C( – 2; – 10)$ hoặc $C(1;1).$

## Bài 11: Cho điểm $M(1;1)$ và hai đường thẳng: ${d_1}:3x – y – 5 = 0$, ${d_2}:x + y – 4 = 0.$ Viết phương trình tổng quát của đường thẳng $d$ đi qua $M$ và cắt ${d_1}$, ${d_2}$ lần lượt tại $A$, $B$ sao cho $2MA – 3MB = 0.$

$A \in {d_1}$ $\Rightarrow A\left( {{x_1};3{x_1} – 5} \right).$

$B \in {d_2}$ $\Rightarrow B\left( {{x_2};4 – {x_2}} \right).$

Vì $A$, $B$, $M$ thẳng hàng và $2MA = 3MB$ 
$$
\Rightarrow \left[ {\begin{array}{l}
{2\overrightarrow {MA} = 3\overrightarrow {MB} \:(1)}\\
{2\overrightarrow {MA} = – 3\overrightarrow {MB} \:(2)}
\end{array}} \right..
$$

Ta có $\overrightarrow {MA} = \left( {{x_1} – 1;3{x_1} – 6} \right)$, $\overrightarrow {MB} = \left( {{x_2} – 1;3 – {x_2}} \right).$

$(1) \Leftrightarrow 2\left( {{x_1} – 1;3{x_1} – 6} \right)$ $= 3\left( {{x_2} – 1;3 – {x_2}} \right)$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_1} = \frac{5}{2}}\\
{{x_2} = 2}
\end{array}} \right..
$$

Suy ra $A\left( {\frac{5}{2};\frac{5}{2}} \right)$, $B(2;2).$

Suy ra phương trình $d:x – y = 0.$

$(2) \Leftrightarrow 2\left( {{x_1} – 1;3{x_1} – 6} \right)$ $= – 3\left( {{x_2} – 1;3 – {x_2}} \right)$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_1} = 1}\\
{{x_2} = 1}
\end{array}} \right..
$$

Suy ra $A(1;-2)$, $B(1;3).$

Suy ra phương trình $d: x – 1 = 0.$

## Bài 12: Cho tam giác $ABC$, phương trình các đường thẳng chứa đường cao và đường trung tuyến kẻ từ đỉnh $A$ lần lượt là $x – 2y – 13 = 0$ và $13x – 6y – 9 = 0.$ Tìm tọa độ các đỉnh $B$ và $C$ biết tâm đường tròn ngoại tiếp tam giác $ABC$ là $I(-5;1).$

Ta có $A(-3;-8).$

Gọi $M$ là trung điểm $BC$ $\Rightarrow IM//AH.$

Ta suy ra phương trình $IM:x – 2y + 7 = 0.$

Suy ra tọa độ $M$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{x – 2y + 7 = 0}\\
{13x – 6y – 9 = 0}
\end{array}} \right.
$$
 $\Rightarrow M(3;5).$

Phương trình đường thẳng $BC:2(x – 3) + y – 5 = 0$ $\Leftrightarrow 2x + y – 11 = 0.$

$B \in BC$ $\Rightarrow B(a;11 – 2a).$

Khi đó $IA = IB$ $\Leftrightarrow {a^2} – 6a + 8 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = 4}\\
{a = 2}
\end{array}} \right..
$$

Từ đó suy ra $B(4;3)$, $C(2;7)$ hoặc $B(2;7)$, $C(4;3).$

## Bài 13: Xác định tọa độ các đỉnh của tam giác $ABC$ biết $M(1;4)$, $N(-1;3)$ là trung điểm của $BC$, $CA$ và $H\left( {\frac{1}{3}; – \frac{5}{3}} \right)$ là trực tâm tam giác $ABC.$

Từ giả thiết suy ra: $MN \bot CH$, $\overrightarrow {NM} (2;1)$ 
$$
\Rightarrow CH:\left\{ {\begin{array}{l}
{x = – t}\\
{y = – 1 + 2t}
\end{array}} \right..
$$

Gọi $C( – t; – 1 + 2t)$ $\Rightarrow A(t – 2;7 – 2t)$ $\Rightarrow \overrightarrow {HA} \left( {t – \frac{7}{3};\frac{{26}}{3} – 2t} \right)$, $\overrightarrow {CM} (t + 1;5 – 2t).$

Do đó $\overrightarrow {HA} .\overrightarrow {CM} = 0$ $\Leftrightarrow \left( {t – \frac{7}{3}} \right)(t + 1) + \left( {\frac{{26}}{3} – 2t} \right)(5 – 2t) = 0.$

$\Leftrightarrow 15{t^2} – 86t + 123 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 3}\\
{t = \frac{{41}}{{15}}}
\end{array}} \right..
$$

Do đó $C( – 3;5)$, $B(5;3)$, $A(1;1)$ hoặc $C\left( { – \frac{{41}}{{15}};\frac{{67}}{{15}}} \right)$, $B\left( {\frac{{71}}{{15}};\frac{{53}}{{15}}} \right)$, $A\left( {\frac{{11}}{{15}};\frac{{23}}{{15}}} \right).$