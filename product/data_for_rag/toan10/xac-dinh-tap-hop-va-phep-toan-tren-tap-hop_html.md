# Xác định tập hợp và phép toán trên tập hợp

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
Bài viết trình bày lý thuyết và ví dụ minh họa có lời giải chi tiết các dạng toán xác định tập hợp và phép toán trên tập hợp.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
## A. TÓM TẮT LÝ THUYẾT

1. Tập hợp

• Tập hợp là một khái niệm cơ bản của toán học, không định nghĩa.

• Cách xác định tập hợp:

+ Liệt kê các phần tử: Viết các phần tử của tập hợp trong hai dấu móc $\left\{ {…} \right\}$.

+ Chỉ ra tính chất đăc trưng cho các phần tử của tập hợp.

• Tập rỗng: là tập hợp không chứa phần tử nào, kí hiệu $\emptyset .$

2. Tập hợp con
$A \subset B$ $\Leftrightarrow \left( {\forall x \in A \Rightarrow x \in B} \right).$

Các tính chất:

• $A \subset A,\forall A .$

• $\emptyset \subset A,\forall A .$

• $A \subset B,B \subset C$ $\Rightarrow A \subset C .$

3. Tập hợp bằng nhau
$A = B$ $\Leftrightarrow (A \subset B$ và $B \subset A)$ $\Leftrightarrow \left( {\forall x,x \in A \Leftrightarrow x \in B} \right) .$

4. Một số tập con của tập hợp số thực

<img link="data_for_rag/toan10/images/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop-1.png" alt="xac-dinh-tap-hop-va-phep-toan-tren-tap-hop-1">

5. Các phép toán tập hợp

• Giao của hai tập hợp: $A \cap B$ $\Leftrightarrow \left\{ {x|x \in A} \right.$ và $\left. {x \in B} \right\} .$

• Hợp của hai tập hợp: $A \cap B$ $\Leftrightarrow \left\{ {x|x \in A} \right.$ hoặc $\left. {x \in B} \right\} .$

• Hiệu của hai tập hợp: $A\backslash B$ $\Leftrightarrow \left\{ {x|x \in A} \right.$ và $\left. {x \notin B} \right\} .$

Phần bù: Cho $B \subset A$ thì ${C_A}B = A\backslash B .$

## B. VÍ DỤ MINH HỌA

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
## Ví dụ 1: Xác định các tập hợp sau bằng cách nêu tính chất đặc trưng:

$A = \left\{ {0;1;2;3;4} \right\}$

$B = \left\{ {0;4;8;12;16} \right\}$

$C = \left\{ {1;2;4;8;16} \right\}$

Ta có các tập hợp $A,B,C$ được viết dưới dạng nêu các tính chất đặc trưng là:

$A = \left\{ {x \in N|x \le 4} \right\}$

$B = \{ x \in N| x \vdots 4$ và $\left. {x \le 16} \right\}$

$C = \left\{ {{2^n}| n \le 4} \right.$ và $\left. {n \in N} \right\}$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
## Ví dụ 2: Cho tập hợp $A = \left\{ {x \in {\rm Z}|\frac{{{x^2} + 2}}{x} \in {\rm Z}} \right\}.$

a. Hãy xác định tập $A$ bằng cách liệt kê các phần tử.

b. Tìm tất cả các tập con của tập hợp $A$ mà số phần tử của nó nhỏ hơn $3.$

a. Ta có $\frac{{{x^2} + 2}}{x} = x + \frac{2}{x} \in {\rm Z}$ với $x \in {\rm Z}$ khi và chỉ khi $x$ là ước của $2$ hay $x \in \left\{ { – 2; – 1;1;2} \right\}.$

Vậy $A = \left\{ { – 2; – 1;1;2} \right\}.$

b. Tất cả các tập con của tập hợp $A$ mà số phần tử của nó nhỏ hơn $3$ là:

Tập không có phần tử nào: $\emptyset .$

Tập có một phần tử: $\left\{ { – 2} \right\}, \left\{ { – 1} \right\}, \left\{ 1 \right\}, \left\{ 2 \right\}.$

Tập có hai phần tử: $\left\{ { – 2; – 1} \right\}, \left\{ { – 2;1} \right\},$ $\left\{ { – 2;2} \right\}, \left\{ { – 1;1} \right\},$ $\left\{ { – 1;2} \right\}, \left\{ {1;2} \right\} .$

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
## Ví dụ 3: Cho $A = \left\{ { – 4; – 2; – 1;2;3;4} \right\}$ và $B = \left\{ {x \in {\rm Z}|\left| x \right| \le 4} \right\}$. Tìm tập hợp $X$ sao cho:

a. $X \subset B\backslash A.$

b. $A \subset X \subset B .$

c. $A \cup X = B$ với $X$ có đúng $4$ phần tử.

Ta có 
$$
\left\{ {\begin{array}{c}
{\left| x \right| \le 4}\\
{x \in {\rm Z}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{ – 4 \le x \le 4}\\
{x \in {\rm Z}}
\end{array}} \right.
$$
 $\Leftrightarrow x \in \left\{ { – 4; – 3; – 2; – 1;0;1;2;3;4} \right\}.$

Suy ra $B = \left\{ { – 4; – 3; – 2; – 1;0;1;2;3;4} \right\}.$

a. Ta có $B\backslash A = \left\{ { – 3;0;1} \right\}.$

Suy ra $X \subset B\backslash A$ thì các tập hợp $X$ là: $\emptyset ,\left\{ { – 3} \right\},\left\{ 0 \right\},\left\{ 1 \right\},\left\{ { – 3;0} \right\},$ $\left\{ { – 3;1} \right\},\left\{ {0;1} \right\},\left\{ { – 3;0;1} \right\} .$

b. Ta có $\left\{ { – 4; – 2; – 1;2;3;4} \right\}$ $\subset X \subset$ $\left\{ { – 4; – 3; – 2; – 1;0;1;2;3;4} \right\}$ suy ra tập hợp $X$ là:

$\left\{ { – 4; – 2; – 1;2;3;4} \right\}$, $\left\{ { – 4; – 2; – 3; – 1;2;3;4} \right\}$, $\left\{ { – 4; – 2; – 1;0;2;3;4} \right\}$, $\left\{ { – 4; – 2; – 1;1;2;3;4} \right\}$, $\left\{ { – 4; – 2; – 3; – 1;0;2;3;4} \right\}$, $\left\{ { – 4; – 2; – 3; – 1;1;2;3;4} \right\}$, $\left\{ { – 4; – 2; – 1;0;1;2;3;4} \right\}$, $\left\{ { – 4; – 3; – 2; – 1;0;1;2;3;4} \right\} .$

c. Ta có $A \cup X = B$ với $X$ có đúng $4$ phần tử khi đó tập hợp $X$ là: $\left\{ { – 4; – 3;0;1} \right\}$, $\left\{ { – 3; – 2;0;1} \right\}$, $\left\{ { – 3; – 1;0;1} \right\}$, $\left\{ { – 3;0;1;2} \right\}$ $\left\{ { – 3;0;1;3} \right\}$, $\left\{ { – 3;0;1;4} \right\} .$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
## Ví dụ 4: Cho các tập hợp:

$A =$ $\left\{ {x \in R|\left( {{x^2} + 7x + 6} \right)\left( {{x^2} – 4} \right) = 0} \right\}$

$B = \left\{ {x \in N|2x \le 8} \right\}$

a. Hãy viết lại các tập hợp $A, B, C$ dưới dạng liệt kê các phần tử.

b. Tìm $A \cup B$, $A \cap B$, $B\backslash C$, ${C_{A \cup B}}\left( {B\backslash C} \right) .$

c. Tìm $(A \cup C)\backslash B.$

a. Ta có: $\left( {{x^2} + 7x + 6} \right)\left( {{x^2} – 4} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} + 7x + 6 = 0\\
{x^2} – 4 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 1\\
x = – 6
\end{array} \right.
$$
 hoặc 
$$
\left[ {\begin{array}{c}
{x = – 2}\\
{x = 2}
\end{array}} \right.
$$

Vậy $A = \left\{ { – 6; – 2; – 1;2} \right\} .$

Ta có 
$$
\left\{ \begin{array}{l}
x \in N\\
2x \le 8
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \in N\\
x \le 4
\end{array} \right.
$$
 $\Leftrightarrow x \in \left\{ {0,1,2,3,4} \right\} .$

Vậy $B = \left\{ {0;1;2;3;4} \right\}.$

Ta có 
$$
\left\{ \begin{array}{l}
x \in Z\\
– 2 \le x \le 4
\end{array} \right.
$$
 $\Leftrightarrow x \in \left\{ { – 2, – 1,0,1,2,3,4} \right\} .$

Suy ra $C = \left\{ { – 3; – 1;1;3;5;7;9} \right\} .$

b. Ta có:

$A \cup B = \left\{ { – 6; – 2; – 1;0;1;2;3;4} \right\}.$

$A \cap B = \left\{ 2 \right\} .$

$B\backslash C = \left\{ {0;2;4} \right\}.$

${C_{A \cup B}}\left( {B\backslash C} \right) = \left( {A \cup B} \right)\backslash \left( {B\backslash C} \right)$ $= \left\{ { – 6; – 2; – 1;1;3} \right\}.$

c. Ta có: $A \cup C = \left\{ { – 6; – 3; – 2; – 1;1;2;3;5;7;9} \right\}.$

Suy ra  $(A \cup C)\backslash B = \left\{ { – 6; – 3; – 2; – 1;5;7;9} \right\}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/xac-dinh-tap-hop-va-phep-toan-tren-tap-hop.html -->
## Ví dụ 5: Cho các tập hợp $E = \{ {\rm{ }}x \in N|1 \le x < 7\}$, $A = \{ {\rm{ }}x \in N|$ $\left( {{x^2} – 9} \right)\left( {{x^2}-5x–6} \right) = 0\}$ và $B = {\rm{\{ }}x \in N|x$ là số nguyên tố nhỏ hơn $\left. 6 \right\}.$

a. Chứng minh rằng $A \subset E$ và $B \subset E .$

b. Tìm ${C_E}A$, ${C_E}B$, ${C_E}(A \cup B).$

c. Chứng minh rằng: $E\backslash (A \cap B)$ $= \left( {E\backslash A} \right) \cup \left( {{\rm{ }}E\backslash B} \right).$

a. Ta có ${\rm{E}} = \left\{ {1;2;3;4;5;6} \right\}$, $A = \left\{ {3;6} \right\}$ và $B = \left\{ {2;3;5} \right\}.$

Suy ra $A \subset E$ và $B \subset E .$

b. Ta có:

${C_E}A = E\backslash A = \left\{ {1;2;4;5} \right\}.$

${C_E}B = E\backslash B = \left\{ {1;4;6} \right\}.$

$A \cup B = \left\{ {2;3;5;6} \right\}$ $\Rightarrow {C_E}(A \cup B) = E\backslash \left( {A \cup B} \right) = \left\{ {1;4} \right\}.$

c. Ta có: $A \cap B = \left\{ 3 \right\}$ $\Rightarrow {C_E}(A \cap B) = E\backslash \left( {A \cap B} \right)$ $= \left\{ {1;2;4;5;6} \right\}.$

$E\backslash A = \left\{ {1;2;4;5} \right\}$, $E\backslash B = \left\{ {1;4;6} \right\}$ $\Rightarrow \left( {E\backslash A} \right) \cup \left( {{\rm{ }}E\backslash B} \right) = \left\{ {1;2;4;5;6} \right\}.$

Suy ra $E\backslash (A \cap B) = \left( {E\backslash A} \right) \cup \left( {{\rm{ }}E\backslash B} \right).$