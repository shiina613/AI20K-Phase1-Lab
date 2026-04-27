# Xác định vectơ pháp tuyến của mặt phẳng dựa vào tích có hướng

<!-- chunk:0 level:0 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
Bài viết hướng dẫn giải các bài toán có liên quan đến việc xác định vectơ pháp tuyến của mặt phẳng dựa vào tích có hướng trong chương trình Hình học 12 chương 3: Phương pháp tọa độ trong không gian Oxyz.

1. CÁC KẾT QUẢ CẦN LƯU Ý

Kết quả 1: Cho ba điểm $A$, $B$, $C$ phân biệt và không thẳng hàng cho trước. Lúc đó, mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\vec n = [\overrightarrow {AB} ,\overrightarrow {AC} ].$

Kết quả 2: Cho hai vectơ $\vec a$ và $\vec b$ không cùng phương cho trước.

Ta có: 
$$
\left\{ {\begin{array}{l}
{\vec c \bot \vec a}\\
{\vec c \bot \vec b}
\end{array}} \right.
$$
 $\Rightarrow$ chọn $\vec c = [\vec a,\vec b].$

Kết quả 3: Hai mặt phẳng $(\alpha )$, $(\beta )$ lần lượt có các vectơ pháp tuyến là ${\vec n_\alpha }$ và ${\vec n_\beta }.$

$(\alpha )//(\beta )$ $\Rightarrow {\vec n_\alpha }$ và ${\vec n_\beta }$ cùng phương.

$(\alpha ) \bot (\beta )$ $\Leftrightarrow {\vec n_\alpha } \bot {\vec n_\beta }.$

## Bài tập

<!-- chunk:1 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 1: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua ba điểm $A(1;1;2)$, $B(2;1;1)$ và $C(0;-1;3).$

A. $(P):x+y+z-4=0.$

B. $(P):x+2y+z-5=0.$

C. $(P):x+z-2=0.$

D. $(P):x+z-3=0.$

Lời giải:

Ta có $\overrightarrow {AB} = (1;0; – 1)$, $\overrightarrow {AC} = ( – 1; – 2;1).$

Mặt phẳng $(P)$ qua $A(1;1;2)$ và có một vectơ pháp tuyến là $\vec n = [\overrightarrow {AB} ,\overrightarrow {AC} ]$ $= ( – 2;0; – 2)$, có phương trình $(P): – 2(x – 1) + 0(y – 1) – 2(z – 2) = 0$ $\Leftrightarrow x + z – 3 = 0.$

> **Đáp án: D**

<!-- chunk:2 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 2: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(MNP)$ biết $M(1;0;1)$, $N(2;1;-1)$ và $P(0;1;2).$

A. $2x+z-3=0.$

B. $x+y+z-2=0.$

C. $3x + y + 2z-5=0.$

D. $3x +y +2z-1=0.$

Lời giải:

Ta có $\overrightarrow {MN} = (1;1; – 2)$, $\overrightarrow {MP} = ( – 1;1;1).$

Mặt phẳng $(MNP)$ qua $M(1;0;1)$ và có một vectơ pháp tuyến là $\vec n = [\overrightarrow {MN} ,\overrightarrow {MP} ] = (3;1;2)$ có phương trình:

$(MNP):3(x – 1) + 1(y – 0) + 2(z – 1) = 0$ $\Leftrightarrow 3x + y + 2z – 5 = 0.$

> **Đáp án: C**

<!-- chunk:3 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 3: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(1;0;1)$ và hai mặt phẳng $(P):x+y-2z=0$, $(Q):-x+y+z+5=0.$ Viết phương trình mặt phẳng $(\alpha )$ qua $A$, đồng thời vuông góc với hai mặt phẳng $(P)$ và $(Q).$

A. $x+ 2z-3=0.$

B. $2x+y – 2z-1=0.$

C. $3x + y + 2z – 4=0.$

D. $3x + y + 2z-5=0.$

Lời giải:

Mặt phẳng $(P)$ có một vectơ pháp tuyến là ${\vec n_P} = (1;1; – 2).$

Mặt phẳng $(Q)$ có một vectơ pháp tuyến là ${\vec n_Q} = ( – 1;1;1).$

Gọi ${\vec n_\alpha }$ là một vectơ pháp tuyến của $(\alpha ).$ Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_\alpha } \bot {{\vec n}_p}}\\
{{{\vec n}_\alpha } \bot {{\vec n}_Q}}
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_\alpha } = \left[ {{{\vec n}_P},{{\vec n}_Q}} \right] = (3;1;2).$

Mặt phẳng $(\alpha )$ qua $A(1;0;1)$ và có một vectơ pháp tuyến là ${\vec n_\alpha } = (3;1;2)$, có phương trình $(\alpha ):3(x – 1) + 1(y – 0) + 2(z – 1) = 0$ $\Leftrightarrow 3x + y + 2z – 5 = 0.$

> **Đáp án: D**

<!-- chunk:4 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 4: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $H(1;1;2)$ và hai mặt phẳng $(P):x-z+1=0$, $(Q):-x-2y+z+1=0.$ Viết phương trình mặt phẳng $(\alpha )$ qua $H$, đồng thời vuông góc với hai mặt phẳng $(P)$ và $(Q).$

A. $x + 2z – 3=0.$

B. $x+z-3=0.$

C. $x + z + 3 = 0.$

D. $3x + y + 2z – 5 = 0.$

Lời giải:

Mặt phẳng $(P)$ có một vectơ pháp tuyến là ${\vec n_p} = (1;0; – 1).$

Mặt phẳng $(Q)$ có một vectơ pháp tuyến là ${\vec n_Q} = ( – 1; – 2;1).$

Gọi ${\vec n_\alpha }$ là một vectơ pháp tuyến của $(\alpha ).$ Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_\alpha } \bot {{\vec n}_P}}\\
{{{\vec n}_\alpha } \bot {{\vec n}_Q}}
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_\alpha } = \left[ {{{\vec n}_P},{{\vec n}_Q}} \right] = ( – 2;0; – 2).$

Mặt phẳng $(\alpha )$ qua $H(1;1;2)$ và có một vectơ pháp tuyến là ${\vec n_\alpha } = ( – 2;0; – 2)$ có phương trình $(\alpha ): – 2(x – 1) + 0(y – 1) – 2(z – 2) = 0$ $\Leftrightarrow x + z – 3 = 0.$

> **Đáp án: B**

<!-- chunk:5 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 5: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(1;3;2)$, $B( – 1;1;0)$ và mặt phẳng $(\alpha ):x – 4y – z + 10 = 0.$ Viết phương trình mặt phẳng $(P)$ qua hai điểm $A$, $B$ và vuông góc với mặt phẳng $(\alpha ).$

A. $x + 2z – 3 = 0.$

B. $3x + 2y – 5z + 1 = 0.$

C. $3x + 2y – 5z – 2 = 0.$

D. $3x + y + 2z – 5 = 0.$

Lời giải:

Mặt phẳng $(\alpha )$ có một vectơ pháp tuyến là ${\vec n_\alpha } = (1; – 4; – 1)$ và $\overrightarrow {AB} = ( – 2; – 2; – 2).$

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot {{\vec n}_\alpha }}\\
{{{\vec n}_P} \bot \overrightarrow {AB} }
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_P} = \left[ {{{\vec n}_\alpha },\overrightarrow {AB} } \right] = (6;4; – 10).$

Mặt phẳng $(P)$ qua $B(-1;1;0)$ và có một vectơ pháp tuyến là ${\vec n_P} = (6;4; – 10)$, có phương trình:

$(P):6(x + 1) + 4(y – 1) – 10(z – 0) = 0$ $\Leftrightarrow 3x + 2y – 5z + 1 = 0.$

> **Đáp án: B**

<!-- chunk:6 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 6: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $A(1;2;1)$, $B( – 1;4; – 1)$ và song song với trục $Ox.$

A. $x + 2y + z – 8 = 0.$

B. $y + z – 5 = 0.$

C. $y + z – 3 = 0.$

D. $3x + y + z – 1 = 0.$

Lời giải:

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot \vec i = (1;0;0)}\\
{{{\vec n}_P} \bot \overrightarrow {AB} = ( – 2;2; – 2)}
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_P} = [\vec i,\overrightarrow {AB} ] = (0;2;2).$

Mặt phẳng $(P)$ qua $A(1;2;1)$ và có một vectơ pháp tuyến là ${\vec n_P} = (0;2;2)$ có phương trình $(P):0(x – 1) + 2(y – 2) + 2(z – 1) = 0$ $\Leftrightarrow y + z – 3 = 0$ (thỏa do $O \notin (P)$).

> **Đáp án: C**

<!-- chunk:7 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 7: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $A(1;2;1)$, $B(-1;4;-1)$ và vuông góc với mặt phẳng $(Oyz).$

A. $x + 2y + z – 8 = 0.$

B. $y + z – 4 = 0.$

C. $y + z – 3 = 0.$

D. $x + y + z – 4 = 0.$

Lời giải:

Mặt phẳng $(Oyz):$ $x = 0$ có một vectơ pháp tuyến là $\vec n = (1;0;0)$ và $\overrightarrow {AB} = ( – 2;2; – 2).$

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot \vec n}\\
{{{\vec n}_P} \bot \overrightarrow {AB} }
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_P} = [\vec n,\overrightarrow {AB} ] = (0;2;2).$

Mặt phẳng $(P)$ qua $A(1;2;1)$ và có một vectơ pháp tuyến là ${\vec n_P} = (0;2;2)$, có phương trình $(P):0(x – 1) + 2(y – 2) + 2(z – 1) = 0$ $\Leftrightarrow y + z – 3 = 0.$

> **Đáp án: C**

<!-- chunk:8 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 8: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $M(1;2;3)$, $N(-1;1;5)$ và song song với trục $Oz.$

A. $x + z – 4 = 0.$

B. $x – 2y + 3 = 0.$

C. $x – 2y + 5 = 0.$

D. $x + 2z – 7 = 0.$

Lời giải:

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot \vec k = (0;0;1)}\\
{{{\vec n}_P} \bot \overrightarrow {MN} = ( – 2; – 1;2)}
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_p} = [\vec k,\overrightarrow {MN} ] = (1; – 2;0).$

Mặt phẳng $(P)$ qua $M(1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_P} = (1; – 2;0)$, có phương trình $(P):1(x – 1) – 2(y – 2) + 0(z – 3) = 0$ $\Leftrightarrow x – 2y + 3 = 0$ (thỏa do $O \notin (P)$).

> **Đáp án: B**

<!-- chunk:9 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 9: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $M(1;2;3)$, $N(-1;1;5)$ và vuông góc với mặt phẳng $(Oxy).$

A. $x + z – 4 = 0.$

B. $x + 2z – 7 = 0.$

C. $x – 2y + 5 = 0.$

D. $x – 2y + 3 = 0.$

Lời giải:

Mặt phẳng $(Oxy):$ $z = 0$ có một vectơ pháp tuyến là $\vec n = (0;0;1)$ và $\overrightarrow {MN} = ( – 2; – 1;2).$

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot \vec n}\\
{{{\vec n}_P} \bot \overrightarrow {MN} }
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_P} = [\vec n,\overrightarrow {MN} ] = (1; – 2;0).$

Mặt phẳng $(P)$ qua $M(1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_P} = (1; – 2;0)$, có phương trình $(P):1(x – 1) – 2(y – 2) + 0(z – 3) = 0$ $\Leftrightarrow x – 2y + 3 = 0.$

> **Đáp án: D**

<!-- chunk:10 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 10: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua điểm $A(1;2;1)$, vuông góc với mặt phẳng $(\alpha ): – 2x + 2y – 2z + 1 = 0$ và song song với trục $Ox.$

A. $x + 2y + z – 8 = 0.$

B. $y + z – 3 = 0.$

C. $y + z – 1 = 0.$

D. $3x + y + z – 1 = 0.$

Lời giải:

Mặt phẳng $(\alpha )$ có một vectơ pháp tuyến là $\vec n = ( – 2;2; – 2).$

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot \vec i = (1;0;0)}\\
{{{\vec n}_P} \bot \vec n}
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${{{\vec n}_P} = [\vec i,\vec n] = (0;2;2)}.$

Mặt phẳng $(P)$ qua $A(1;2;1)$ và có một vectơ pháp tuyến là ${\vec n_P} = (0;2;2)$, có phương trình $(P):0(x – 1) + 2(y – 2) + 2(z – 1) = 0$ $\Leftrightarrow y + z – 3 = 0$ (thỏa do $O \notin (P)$).

> **Đáp án: B**

<!-- chunk:11 level:3 source:https://toanmath.com/2020/02/xac-dinh-vecto-phap-tuyen-cua-mat-phang-dua-vao-tich-co-huong.html -->
## Ví dụ 11: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua điểm $A(1;2;3)$, vuông góc với mặt phẳng $(\alpha ): – 2x + 2y – 2z + 1 = 0$ và vuông góc với mặt phẳng $(Oyz).$

A. $x+2y +z-8=0.$

B. $y +z-5=0.$

C. $y +z-1=0.$

D. $3x+y+z-1=0.$

Lời giải:

Mặt phẳng $(Oyz):x = 0$ có một vectơ pháp tuyến là $\vec n = (1;0;0).$

Mặt phẳng $(\alpha )$ có một vectơ pháp tuyến là ${\vec n_\alpha } = ( – 2;2; – 2).$

Gọi ${\vec n_P}$ là một vectơ pháp tuyến của $(P).$

Ta có: 
$$
\left\{ {\begin{array}{l}
{{{\vec n}_P} \bot \vec n}\\
{{{\vec n}_P} \bot {{\vec n}_\alpha }}
\end{array}} \right.
$$
 $\Rightarrow$ chọn ${\vec n_P} = \left[ {\vec n,{{\vec n}_\alpha }} \right] = (0;2;2).$

Mặt phẳng $(P)$ qua $A(1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_P} = (0;2;2)$, có phương trình $(P):0(x – 1) + 2(y – 2) + 2(z – 3) = 0$ $\Leftrightarrow y + z – 5 = 0$ (thỏa do $O \notin (P)$).

> **Đáp án: B**

## Bài tập
1. ĐỀ BÀI
## Câu 1: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(ABC)$ biết $A(1;3;2)$, $B(2;-1;1)$ và $C(-1;1;0).$

A. $x + 2z – 3 = 0.$

B. $2x + y – 2z – 1 = 0.$

C. $3x + 2y – 5z + 4 = 0.$

D. $3x + 2y – 5z + 1 = 0.$

## Câu 2: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $K(-1;1;0)$ và hai mặt phẳng $(\alpha ):x – 4y – z = 0$, $(\beta ): – 2x – 2y – 2z + 1 = 0.$ Viết phương trình mặt phẳng $(P)$ qua $K$, đồng thời vuông góc với hai mặt phẳng $(\alpha )$ và $(\beta ).$

A. $x – 2y + 3 = 0.$

B. $3x + 2y – 5z + 1 = 0.$

C. $3x + 2y – 5z – 2 = 0.$

D. $3x + y + 2z – 5 = 0.$

## Câu 3: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(1;1;2)$, $B(2;1;1)$ và mặt phẳng $(\alpha ): – x – 2y + z + 9 = 0.$ Viết phương trình mặt phẳng $(P)$ qua hai điểm $A$, $B$ và vuông góc với mặt phẳng $(\alpha ).$

A. $(P):x + y + z – 4 = 0.$

B. $(P):x + z – 3 = 0.$

C. $(P):x + z – 2 = 0.$

D. $(P):x + 2y + z – 5 = 0.$

## Câu 4: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $A(1;0;2)$, $B(3;-1;1)$ và song song với trục $Oy.$

A. $x+ 2z-3=0.$

B. $y +z-5=0.$

C. $y +z-1=0.$

D. $x + 2z – 5 = 0.$

## Câu 5: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $A(1;0;2)$, $B(3;-1;1)$ và vuông góc với mặt phẳng $(Oxz).$

A. $x + 2z-3=0.$

B. $y +z-5=0.$

C. $y +z-1=0.$

D. $x + 2z-5=0.$

## Câu 6: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua điểm $A(1;0;2)$, vuông góc với mặt phẳng $(\alpha ):2x – y – z + 7 = 0$ và song song với trục $Oy.$

A. $x + 2z – 3=0.$

B. $y + z-5=0.$

C. $y +z-1=0.$

D. $x+2z -5=0.$

## Câu 7: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua hai điểm $A(1;0;2)$, vuông góc với mặt phẳng $(\alpha ):2x – y – z + 7 = 0$ và vuông góc với mặt phẳng $(Oxz).$

A. $x + 2z-3=0.$

B. $y +z-5=0.$

C. $y +z-1=0.$

D. $x + 2z-5=0.$

## Câu 8: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua điểm $A(-1;1;5)$, vuông góc với mặt phẳng $(\alpha ): – 2x – y + 2z + 11 = 0$ và vuông góc với mặt phẳng $(Oxy).$

A. $x+z–4=0.$

B. $x + 2z – 7 = 0.$

C. $x-2y+5=0.$

D. $x – 2y +3=0.$

## Câu 9: Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng $(P)$ qua điểm $A(-1;1;5)$, vuông góc với mặt phẳng $(\alpha ): – 2x – y + 2z + 11 = 0$ và song song với trục $Oz.$

A. $x+z-4=0.$

B. $x + 2z-7 =0.$

C. $x – 2y +5=0.$

D. $x – 2y +3=0.$

## Câu 10: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $M(1;0;1)$, $N(2;1;-1)$ và mặt phẳng $(\alpha ): – x + y + z + 5 = 0.$ Viết phương trình mặt phẳng $(P)$ qua hai điểm $M$, $N$ và vuông góc với mặt phẳng $(\alpha ).$

A. $2x+z-3=0.$

B. $x+y+z-2=0.$

C. $3x + y + 2z -5=0.$

D. $3x +y + 2z-1=0.$

**2. BẢNG ĐÁP ÁN**

**Câu** | 
1 | 
2 | 
3 | 
4 | 
5 | 

**Đáp án** | 
D | 
B | 
B | 
D | 
D | 

**Câu** | 
6 | 
7 | 
8 | 
9 | 
10 | 

**Đáp án** | 
D | 
D | 
D | 
D | 
C |