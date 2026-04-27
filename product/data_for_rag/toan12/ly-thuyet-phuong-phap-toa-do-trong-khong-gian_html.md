# Lý thuyết phương pháp tọa độ trong không gian

<!-- chunk:0 level:0 source:https://toanmath.com/2019/03/ly-thuyet-phuong-phap-toa-do-trong-khong-gian.html -->
Bài viết tổng hợp lý thuyết phương pháp tọa độ trong không gian Oxyz, bao gồm các định nghĩa, tính chất và công thức thường sử dụng trong giải toán.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/03/ly-thuyet-phuong-phap-toa-do-trong-khong-gian.html -->
## I. Tọa độ trong không gian.

1) Hệ trục tọa độ trong không gian $Oxyz$.

Hệ gồm ba trục $Ox$, $Oy$, $Oz$ đôi một vuông góc được gọi là hệ trục tọa độ vuông góc trong không gian.

Điểm $O$ gọi là gốc của hệ tọa độ, trục $Ox$ là trục hoành, $Oy$ là trục tung và $Oz$ là trục cao.

Véctơ đơn vị trên các trục $Ox$, $Oy$, $Oz$ lần lượt là $\vec i$, $\vec j$, $\vec k$, ta có: $\left| {\vec i} \right| = \left| {\vec j} \right| = \left| {\vec k} \right| = 1$, $\vec i.\vec j = \vec j.\vec k = \vec k.\vec i = 0.$

Xét điểm $M$ thỏa mãn $\overrightarrow {OM} = x.\vec i + y.\vec j + z.\vec k$ thì $M(x; y; z).$ Ngược lại điểm $M(x; y; z)$ thì $\overrightarrow {OM} = x.\vec i + y.\vec j + z.\vec k.$

Với véctơ $\overrightarrow u$ trong hệ tọa độ $Oxyz$ luôn tồn tại duy nhất bộ $(x; y; z)$ thỏa $\vec u = x.\vec i + y.\vec j + z.\vec k.$ Tọa độ $\overrightarrow u$ là $(x; y; z).$

2) Tọa độ véctơ – Tọa độ điểm.

Cho $\overrightarrow a = ({x_1};{y_1};{z_1})$, $\overrightarrow b = ({x_2};{y_2};{z_2})$ và số thực $k.$ Khi đó:

$\overrightarrow a \pm \overrightarrow b = ({x_1} \pm {x_2};{y_1} \pm {y_2}).$

$k\overrightarrow a = (k{x_1};k{y_1};k{z_1}).$

$\overrightarrow a //\overrightarrow b$ $\Leftrightarrow \overrightarrow a = k\overrightarrow b$ $\Leftrightarrow \frac{{{x_1}}}{{{x_2}}} = \frac{{{y_1}}}{{{y_2}}} = \frac{{{z_1}}}{{{z_2}}} = k$ $\Rightarrow \overrightarrow a = \overrightarrow b$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_1} = {x_2}\\
{y_1} = {y_2}\\
{z_1} = {z_2}
\end{array} \right.
$$

Chú ý: Nếu ${x_2} = 0$ $\left( {{y_2} = 0, {z_2} = 0} \right)$ thì ${x_1} = 0$ $\left( {{y_1} = 0,{z_1} = 0} \right).$

$\left| {\overrightarrow a } \right| = \sqrt {x_1^2 + y_1^2 + z_1^2} .$

$\overrightarrow a .\overrightarrow b = {x_1}{x_2} + {y_1}{y_2} + {z_1}{z_2}.$

$\overrightarrow a \bot \overrightarrow b$ $\Leftrightarrow {x_1}{x_2} + {y_1}{y_2} + {z_1}{z_2} = 0.$

$\cos (\overrightarrow a ,\overrightarrow b ) = \frac{{\overrightarrow a .\overrightarrow b }}{{\left| {\overrightarrow a } \right|\left| {\overrightarrow b } \right|}}.$

Cho $A = ({x_A};{y_A};{z_A})$, $B = ({x_B};{y_B};{z_B})$, $C({x_C};{y_C};{z_C})$, $D({x_D};{y_D};{z_D}).$

Khi đó:

$\overrightarrow {AB} = ({x_B} – {x_A};{y_B} – {y_A};{z_B} – {z_A}).$

$AB = \left| {\overrightarrow {AB} } \right|$ $= \sqrt {{{({x_B} – {x_A})}^2} + {{({y_B} – {y_A})}^2} + {{({z_B} – {z_A})}^2}} .$

Trung điểm $I$ của đoạn $AB$: $I = \left( {\frac{{{x_A} + {x_B}}}{2};\frac{{{y_A} + {y_B}}}{2};\frac{{{z_A} + {z_B}}}{2}} \right).$

Trọng tâm $G$ của $\Delta ABC$: $G\left( {\frac{{{x_A} + {x_B} + {x_C}}}{3};\frac{{{y_A} + {y_B} + {y_C}}}{3};\frac{{{z_A} + {z_B} + {z_C}}}{3}} \right).$

Trọng tâm $G$ của tứ diện $ABCD$: $G\left( {\frac{{{x_A} + {x_B} + {x_C} + {x_D}}}{4};\frac{{{y_A} + {y_B} + {y_C} + {y_D}}}{4};\frac{{{z_A} + {z_B} + {z_C} + {z_D}}}{4}} \right).$

3) Tích có hướng của hai véc tơ và ứng dụng.

a) Định nghĩa: Cho $\overrightarrow a = \left( {{x_1};{y_1};{z_1}} \right)$ và $\overrightarrow b = \left( {{x_2};{y_2};{z_2}} \right)$, ta có:

$$
\left[ {\overrightarrow a ,\overrightarrow b } \right] = \left( {\left| \begin{array}{l}
{y_1}{\rm{ }}{z_1}\\
{y_2}{\rm{ }}{z_2}
\end{array} \right|;\left| \begin{array}{l}
{z_1}{\rm{ }}{x_1}\\
{z_2}{\rm{ }}{x_2}
\end{array} \right|;\left| \begin{array}{l}
{x_1}{\rm{ }}{y_1}\\
{x_2}{\rm{ }}{y_2}
\end{array} \right|} \right).
$$

b) Các tính chất:

$\overrightarrow a$ cùng phương $\overrightarrow b$ $\Leftrightarrow \left[ {\overrightarrow a ,\overrightarrow b } \right] = \overrightarrow 0 .$

$\left[ {\overrightarrow a ,\overrightarrow b } \right] \bot \overrightarrow a$ và $\left[ {\overrightarrow a ,\overrightarrow b } \right] \bot \overrightarrow b .$

$\left| {\left[ {\overrightarrow a ,\overrightarrow b } \right]} \right| = \left| {\overrightarrow a } \right|.\left| {\overrightarrow b } \right|.\sin (\overrightarrow a ,\overrightarrow b ).$

c) Các ứng dụng của tích có hướng:

Diện tích tam giác: ${S_{\Delta ABC}} = \frac{1}{2}\left| {\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right]} \right|.$

Thể tích:

+ Hình hộp ${V_{ABCD.A’B’C’D’}} = \left| {\left[ {\overrightarrow {AB} ,\overrightarrow {AD} } \right].\overrightarrow {AA’} } \right|.$

+ Tứ diện ${V_{ABCD}} = \frac{1}{6}\left| {\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right].\overrightarrow {AD} } \right|.$

d) Điều kiện 3 véctơ đồng phẳng:

$\overrightarrow a$, $\overrightarrow b$, $\overrightarrow c$ đồng phẳng $\Leftrightarrow \left[ {\overrightarrow a ,\overrightarrow b } \right].\overrightarrow c = 0.$

$A$, $B$, $C$, $D$ đồng phẳng $\Leftrightarrow \left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right].\overrightarrow {AD} = 0.$

4) Phương trình mặt cầu.

Mặt cầu $(S)$ tâm $I(a;b;c)$, bán kính $R$ có phương trình: ${(x – a)^2} + {(y – b)^2} + {(z – c)^2} = {R^2}.$

Phương trình này có thể được biểu diễn cách khác như sau: ${x^2} + {y^2} + {z^2} – 2ax – 2by – 2cz + d = 0$, với $d = {a^2} + {b^2} + {c^2} – {R^2}$ 
$$
\Rightarrow \left\{ \begin{array}{l}
{a^2} + {b^2} + {c^2} – d > 0\\
R = \sqrt {{a^2} + {b^2} + {c^2} – d}
\end{array} \right.
$$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/03/ly-thuyet-phuong-phap-toa-do-trong-khong-gian.html -->
## II. Phương trình mặt phẳng.

1) Véctơ pháp tuyến.

a) Định nghĩa: Cho mặt phẳng $(\alpha ).$ Véctơ $\overrightarrow n \ne \overrightarrow 0$ gọi là véctơ pháp tuyến (VTPT) của mặt phẳng $(\alpha )$ nếu giá của $\overrightarrow n$ vuông góc với $(\alpha )$, kí hiệu $\overrightarrow n \bot (\alpha ).$

b) Chú ý:

Nếu $\overrightarrow n$ là VTPT của $(\alpha )$ thì $k.\overrightarrow n$ $(k \ne 0)$ cũng là VTPT của $(\alpha ).$ Vậy mặt phẳng $(\alpha )$ có vô số VTPT.

Nếu hai véctơ $\overrightarrow a$, $\overrightarrow b$ (không cùng phương) có giá song song (hoặc nằm trên) $(\alpha )$ thì $\overrightarrow n = \left[ {\overrightarrow a ,\overrightarrow b } \right]$ là một VTPT của mặt phẳng $(\alpha ).$

Nếu ba điểm $A$, $B$, $C$ phân biệt không thẳng hàng thì véctơ $\overrightarrow n = \left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right]$ là một VTPT của mặt phẳng $\left( {ABC} \right).$

2) Phương trình tổng quát của mặt phẳng.

Cho mặt phẳng $(\alpha )$ đi qua $M({x_0};{y_0};{z_0})$, có $\overrightarrow n = (A;B;C)$ là một VTPT. Khi đó phương trình tổng quát của $(\alpha )$ có dạng: $A(x – {x_0}) + B(y – {y_0}) + C(z – {z_0}) = 0.$

Nếu $(\alpha )$: $Ax + By + Cz + D = 0$ thì $\overrightarrow n = (A;B;C)$ là một VTPT của $(\alpha ).$

Nếu $A(a;0;0)$, $B(0;b;0)$, $C(0;0;c)$, $abc \ne 0$ thì phương trình của $(ABC)$ có dạng: $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ và được gọi là phương trình theo đoạn chắn của $(\alpha ).$

3) Vị trí tương đối của hai mặt phẳng.

Cho hai mặt phẳng $(P)$: $Ax + By + Cz + D = 0$ và $(Q)$: $A’x + B’y + C’z + D’ = 0.$

$(P)$ cắt $(Q)$ $\Leftrightarrow A:B:C \ne A’:B’:C’.$

$(P)//(Q)$ $\Leftrightarrow \frac{A}{{A’}} = \frac{B}{{B’}} = \frac{C}{{C’}} \ne \frac{D}{{D’}}.$

$(P) \equiv (Q)$ $\Leftrightarrow \frac{A}{{A’}} = \frac{B}{{B’}} = \frac{C}{{C’}} = \frac{D}{{D’}}.$

$(P) \bot (Q)$ $\Leftrightarrow AA’ + BB’ + CC’ = 0.$

4) Khoảng cách từ một điểm đến một mặt phẳng.

Khoảng cách từ $M\left( {{x_0};{y_0};{z_0}} \right)$ đến mặt phẳng $(P)$: $Ax + By + Cz + D = 0$ là: $d(M,(P)) = \frac{{\left| {A{x_0} + B{y_0} + C{z_0} + D} \right|}}{{\sqrt {{A^2} + {B^2} + {C^2}} }}.$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/03/ly-thuyet-phuong-phap-toa-do-trong-khong-gian.html -->
## III. Phương trình đường thẳng trong không gian.

1) Phương trình tham số của đường thẳng.

a) Véctơ chỉ phương của đường thẳng:

Cho đường thẳng $\Delta .$ Véctơ $\overrightarrow u \ne \overrightarrow 0$ gọi là véctơ chỉ phương (VTCP) của đường thẳng $\Delta$ nếu giá của nó song song hoặc trùng với $\Delta .$

Chú ý:

Nếu $\overrightarrow u$ là VTCP của $\Delta$ thì $k.\overrightarrow u$ $(k \ne 0)$ cũng là VTCP của $\Delta .$

Nếu đường thẳng $\Delta$ đi qua hai điểm $A$ và $B$ thì $\overrightarrow {AB}$ là một VTCP của $\Delta .$

Nếu $\Delta$ là giao tuyến của hai mặt phẳng $(P)$ và $(Q)$ thì $\left[ {\overrightarrow {{n_P}} ,\overrightarrow {{n_Q}} } \right] = \overrightarrow {{u_\Delta }}$ là một VTCP của $\Delta$ (trong đó $\overrightarrow {{n_P}}$, $\overrightarrow {{n_Q}}$ lần lượt là VTPT của $(P)$ và $(Q).$

b) Phương trình tham số của đường thẳng:

Cho đường thẳng $\Delta$ đi qua $M({x_0};{y_0};{z_0})$ và có VTCP $\overrightarrow u = (a;b;c).$ Khi đó phương trình đường thẳng $\Delta$ có dạng: 
$$
\left\{ \begin{array}{l}
x = {x_0} + at\\
y = {y_0} + bt\\
z = {z_0} + ct
\end{array} \right.
$$
 $t \in R.$

Phương trình này gọi là phương trình tham số của đường thẳng $\Delta$, $t$ gọi là tham số.

Chú ý: Cho đường thẳng $\Delta$ có phương trình 
$$
\left\{ \begin{array}{l}
x = {x_0} + at\\
y = {y_0} + bt\\
z = {z_0} + ct
\end{array} \right.
$$
 $t \in R$, khi đó:

$\overrightarrow u = (a;b;c)$ là một VTCP của $\Delta .$

$M \in \Delta$ $\Leftrightarrow M({x_0} + at;{y_0} + bt;{z_0} + ct).$

2) Phương trình chính tắc.

Cho đường thẳng $\Delta$ đi qua $M({x_0};{y_0};{z_0})$ và có VTCP $\overrightarrow u = (a;b;c)$ với $abc \ne 0.$ Khi đó phương trình đường thẳng $\Delta$ có dạng: $\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b} = \frac{{z – {z_0}}}{c}.$

Phương trình này gọi là phương trình chính tắc của đường thẳng $\Delta .$

3) Vị trí tương đối giữa hai đường thẳng.

Cho hai đường thẳng $d$: $\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b} = \frac{{z – {z_0}}}{c}$ đi qua $M({x_0};{y_0};{z_0})$ có VTCP $\overrightarrow {{u_d}} = (a;b;c)$ và $d’$ $\frac{{x – x_0^,}}{{a’}} = \frac{{y – y_0^,}}{{b’}} = \frac{{z – z_0^,}}{{c’}}$ đi qua $M'(x_0^,;y_0^,;z_0^,)$ có VTCP $\overrightarrow {{u_{d’}}} = (a’;b’;c’).$

Nếu $[\overrightarrow {{u_d}} ,\overrightarrow {{u_{d’}}} ]\overrightarrow {MM’} = 0$ $\Rightarrow d$ và $d’$ đồng phẳng. Khi đó xảy ra ba trường hợp:

i) $d$ và $d’$ cắt nhau $\Leftrightarrow [\overrightarrow u ,\overrightarrow {u’} ] \ne \overrightarrow 0$ và tọa độ giao điểm là nghiệm của hệ: 
$$
\left\{ \begin{array}{l}
\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b} = \frac{{z – {z_0}}}{c}\\
\frac{{x – x_0^,}}{{a’}} = \frac{{y – y_0^,}}{{b’}} = \frac{{z – z_0^,}}{{c’}}
\end{array} \right.
$$

ii) $d//d’$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
[\overrightarrow u ,\overrightarrow {u’} ] = \overrightarrow 0 \\
[\overrightarrow u ,\overrightarrow {MM’} ] \ne \overrightarrow 0
\end{array} \right.
$$

iii) $d \equiv d’$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
[\overrightarrow u ,\overrightarrow {u’} ] = \overrightarrow 0 \\
[\overrightarrow u ,\overrightarrow {MM’} ] = \overrightarrow 0
\end{array} \right.
$$

Nếu $[\overrightarrow u ,\overrightarrow {u’} ]\overrightarrow {MM’} \ne 0$ $\Rightarrow$ $d$ và $d’$ chéo nhau.

4) Vị trí tương đối giữa đường thẳng và mặt phẳng.

Cho mặt phẳng $(\alpha )$: $Ax + By + Cz + D = 0$ có $\overrightarrow n = (A;B;C)$ là VTPT và đường thẳng $\Delta$: $\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b} = \frac{{z – {z_0}}}{c}$ có $\overrightarrow u = (a;b;c)$ là VTCP và đi qua ${M_0}({x_0};{y_0};{z_0}).$

$\Delta$ cắt $(\alpha )$ $\Leftrightarrow \overrightarrow n$ và $\overrightarrow u$ không cùng phương $\Leftrightarrow Aa + Bb + Cc \ne 0.$ Khi đó tọa độ giao điểm là nghiệm của hệ: 
$$
\left\{ \begin{array}{l}
Ax + By + Cz + D = 0\\
\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b} = \frac{{z – {z_0}}}{c}
\end{array} \right.
$$

$\Delta //(\alpha )$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\overrightarrow n \bot \overrightarrow u \\
{M_0} \notin (\alpha )
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
Aa + Bb + Cc = 0\\
A{x_0} + B{y_0} + C{z_0} + D \ne 0
\end{array} \right.
$$

$\Delta \subset (\alpha )$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\overrightarrow n \bot \overrightarrow u \\
{M_0} \in (\alpha )
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
Aa + Bb + Cc = 0\\
A{x_0} + B{y_0} + C{z_0} + D = 0
\end{array} \right.
$$

$\Delta \bot (\alpha )$ $\Leftrightarrow \overrightarrow n$ và $\overrightarrow u$ cùng phương $\Leftrightarrow \overrightarrow n = k.\overrightarrow u .$

5) Khoảng cách.

a) Khoảng cách từ một điểm đến một đường thẳng:

Cho đường thẳng $\Delta$ đi qua ${M_0}$, có VTCP $\overrightarrow u$ và điểm $M \notin \Delta .$ Khi đó để tính khoảng cách từ $M$ đến $\Delta$ ta có các cách sau:

+ Cách 1: Sử dụng công thức: $d(M,\Delta ) = \frac{{\left| {[\overrightarrow {{M_0}M} ,\overrightarrow u ]} \right|}}{{\left| {\overrightarrow u } \right|}} .$

+ Cách 2: Lập phương trình mặt phẳng $\left( P \right)$ đi qua $M$ vuông góc với $\Delta .$ Tìm giao điểm $H$ của $(P)$ với $\Delta .$ Khi đó độ dài $MH$ là khoảng cách cần tìm.

b) Khoảng cách giữa hai đường thẳng chéo nhau:

Cho hai đường thẳng chéo nhau $\Delta$ đi qua ${M_0}$ có VTCP $\overrightarrow u$ và $\Delta’$ đi qua ${M_0}’$ có VTCP $\overrightarrow {u’} .$ Khi đó khoảng cách giữa hai đường thẳng $\Delta$ và $\Delta’$ được tính theo các cách sau:

+ Cách 1: Sử dụng công thức: $d(\Delta ,\Delta’) = \frac{{\left| {\left[ {\overrightarrow u ,\overrightarrow {u’} } \right].\overrightarrow {{M_0}M{‘_0}} } \right|}}{{\left| {\left[ {\overrightarrow u ,\overrightarrow {u’} } \right]} \right|}}.$

+ Cách 2: Tìm đoạn vuông góc chung $MN.$ Khi đó độ dài $MN$ là khoảng cách cần tìm.

+ Cách 3: Lập phương trình $\left( P \right)$ đi qua $\Delta$ và song song với $\Delta’ .$ Khi đó khoảng cách cần tìm là khoảng cách từ một điểm bất kì trên $\Delta’$ đến $(P).$

<!-- chunk:4 level:1 source:https://toanmath.com/2019/03/ly-thuyet-phuong-phap-toa-do-trong-khong-gian.html -->
## IV. Góc.

1) Góc giữa hai đường thẳng.

Cho hai đưòng thẳng $\Delta$ $\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b} = \frac{{z – {z_0}}}{c}$ có VTCP $\overrightarrow u = (a;b;c)$ và đường thẳng $\Delta’$: $\frac{{x – {x_0}’}}{{a’}} = \frac{{y – {y_0}’}}{{b’}} = \frac{{z – {z_0}’}}{{c’}}$ có VTCP $\overrightarrow {u’} = (a’;b’;c’).$ Đặt $\alpha = \left( {\Delta ,\Delta’} \right)$, khi đó: $\cos \alpha = \left| {\cos \left( {\overrightarrow u ,\overrightarrow {u’} } \right)} \right|$ $= \frac{{\left| {aa’ + bb’ + cc’} \right|}}{{\sqrt {{a^2} + {b^2} + {c^2}} .\sqrt {a{‘^2} + b{‘^2} + c{‘^2}} }}.$

2) Góc giữa đường thẳng và mặt phẳng.

Cho mặt phẳng $(\alpha )$: $Ax + By + Cz + D = 0$ có $\overrightarrow n = \left( {A;B;C} \right)$ là VTPT và đường thẳng $\Delta$: $\frac{{x – {x_o}}}{a} = \frac{{y – {y_o}}}{b} = \frac{{z – {z_o}}}{c}$ có $\overrightarrow u = (a;b;c)$ là VTCP. Gọi $\varphi$ là góc giữa mặt phẳng $(\alpha )$ và đường thẳng $\Delta$, khi đó ta có: $\sin \varphi = \left| {\cos \left( {\overrightarrow n ,\overrightarrow u } \right)} \right|$ $= \frac{{\left| {Aa + Bb + Cc} \right|}}{{\sqrt {{A^2} + {B^2} + {C^2}} \sqrt {{a^2} + {b^2} + {c^2}} }}.$

3) Góc giữa hai mặt phẳng.

Cho hai mặt phẳng $(\alpha )$: $Ax + By + Cz + D = 0$ có VTPT $\overrightarrow {{n_1}} = (A;B;C)$ và $\beta )$: $A’x + B’y + C’z + D’ = 0$ có VTPT $\overrightarrow {{n_2}} = \left( {A’;B’;C’} \right).$

Gọi $\varphi$ là góc giữa hai mặt phẳng (${0^0} \le \varphi \le {90^0}$). Khi đó: $\cos \varphi = \left| {\cos \left( {\overrightarrow {{n_1}} ,\overrightarrow {{n_2}} } \right)} \right|$ $= \frac{{\left| {AA’ + BB’ + CC’} \right|}}{{\sqrt {{A^2} + {B^2} + {C^2}} \sqrt {A{‘^2} + B{‘^2} + C{‘^2}} }}.$