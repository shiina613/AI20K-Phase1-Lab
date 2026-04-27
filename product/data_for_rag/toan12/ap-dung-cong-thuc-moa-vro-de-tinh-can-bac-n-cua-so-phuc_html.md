# Áp dụng công thức Moa-vrơ để tính căn bậc n của số phức

<!-- chunk:0 level:0 source:https://toanmath.com/2018/03/ap-dung-cong-thuc-moa-vro-de-tinh-can-bac-n-cua-so-phuc.html -->
Bài viết hướng dẫn cách áp dụng công thức Moa-vrơ (Moivre) để tính căn bậc $n$ của số phức thông qua quá trình thiết lập công thức tổng quát và các ví dụ minh họa đi kèm có lời giải chi tiết.

**Xem thêm:**

+ Viết số phức dưới dạng lượng giác

+ Tìm căn bậc hai của một số phức

Phương pháp

1. Tính căn bậc hai của số phức

Căn bậc hai của số phức $z$ là số phức $w$ thỏa ${w^2} = z$.

+ Căn bậc hai của $0$ bằng $0.$

+ Với $z \ne 0$ và $z = r(c{\rm{os}}\varphi + i \sin \varphi )$ với $r > 0.$

Đặt $w = R(c{\rm{os}}\theta + i \sin \theta )$ với $R > 0$ thì:

${{\rm{w}}^2} = z$ ⇔ ${R^2}(c{\rm{os}}2\theta + i \sin 2\theta ) = r(c{\rm{os}}\varphi + i \sin \varphi )$

$$
\Leftrightarrow \left\{ \begin{array}{l}
{R^2} = r\\
2\theta = \varphi + k2\pi , k \in Z
\end{array} \right.
$$

$$
\Leftrightarrow \left\{ \begin{array}{l}
R = \sqrt r \\
\theta = \frac{\varphi }{2} + k\pi , k \in Z
\end{array} \right.
$$

Từ đó suy ra: Số phức $z = r(c{\rm{os}}\varphi + i\sin \varphi )$ có $2$ căn bậc hai là: ${{\rm{w}}_1} = \sqrt r \left( {c{\rm{os}}\frac{\varphi }{2} + i\sin \frac{\varphi }{2}} \right)$ và ${{\rm{w}}_2} = \sqrt r \left( {c{\rm{os}}\left( {\frac{\varphi }{2} + \pi } \right) + i \sin \left( {\frac{\varphi }{2} + \pi } \right)} \right)$ $= – \sqrt r \left( {c{\rm{os}}\frac{\varphi }{2} + i\sin \frac{\varphi }{2}} \right).$

2. Tính căn bậc $n$ của số phức
Căn bậc $n$ của số phức $z$ là số phức $w$ thỏa ${w^n} = z$.

Với $z \ne 0$ và $z = r(c{\rm{os}}\varphi + i \sin \varphi )$ với $r > 0.$

Đặt $w = R(c{\rm{os}}\theta + i \sin \theta )$ với $R > 0$ thì:

${{\rm{w}}^n} = z \Leftrightarrow {R^n}(c{\rm{osn}}\theta + i {\mathop{\rm sinn}\nolimits} \theta )$ $= r(c{\rm{os}}\varphi + i \sin \varphi )$

$$
\Leftrightarrow \left\{ \begin{array}{l}
{R^n} = r\\
n\theta = \varphi + k2\pi , k \in Z
\end{array} \right.
$$

$$
\Leftrightarrow \left\{ \begin{array}{l}
R = \sqrt[n]{r}\\
\theta = \frac{\varphi }{n} + \frac{{k2\pi }}{n}, k \in Z
\end{array} \right.
$$

Bằng cách chọn $k = 0, 1, 2, …, n-1$ ta được $n$ căn bậc $n$ của $z$ là:

${w_1} = \sqrt[n]{r}\left( {\cos \frac{\varphi }{n} + i\sin \frac{\varphi }{n}} \right).$

${w_2}$ = $\sqrt[n]{r}\left( {\cos \left( {\frac{\varphi }{n} + \frac{{2\pi }}{n}} \right) + i\sin \left( {\frac{\varphi }{n} + \frac{{2\pi }}{n}} \right)} \right).$

…..

${w_n}$ = $\sqrt[n]{r}(\cos \left( {\frac{\varphi }{n} + \frac{{2\pi (n – 1)}}{n}} \right)$ $+ i\sin \left( {\frac{\varphi }{n} + \frac{{2\pi (n – 1)}}{n}} \right)).$

[ads]

<!-- chunk:1 level:3 source:https://toanmath.com/2018/03/ap-dung-cong-thuc-moa-vro-de-tinh-can-bac-n-cua-so-phuc.html -->
## Ví dụ 1.  Tìm căn bậc hai của số phức sau và viết dưới dạng lượng giác ${\rm{w}} = \frac{1}{2} + \frac{{\sqrt 3 }}{2}i.$

Ta có $w = \frac{1}{2} + \frac{{\sqrt 3 }}{2}i = \cos \frac{\pi }{3} + i\sin \frac{\pi }{3}.$

Đặt $z = r\left( {\cos \varphi + i\sin \varphi } \right)$ với $r > 0$ là một căn bậc hai của $w$, ta có:

${z^2} = w$ ⇔ ${r^2}\left( {\cos 2\varphi + i\sin 2\varphi } \right)$ $= \cos \frac{\pi }{3} + i\sin \frac{\pi }{3}$

$$
\Leftrightarrow \left\{ \begin{array}{l}
r = 1\\
2\varphi = \frac{\pi }{3} + k2\pi ,k \in Z
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
r = 1\\
\varphi = \frac{\pi }{6} + k\pi ,k \in Z
\end{array} \right.
$$

Vậy $w$ có hai căn bậc hai là: ${z_1} = \cos \frac{\pi }{6} + i\sin \frac{\pi }{6}$ và ${z_2} = \cos \frac{{7\pi }}{6} + i\sin \frac{{7\pi }}{6}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/03/ap-dung-cong-thuc-moa-vro-de-tinh-can-bac-n-cua-so-phuc.html -->
## Ví dụ 2. Tính căn bậc ba của số phức sau và viết dưới dạng lượng giác: $w = – 1 + i\sqrt 3 .$

Ta có: $w = – 1 + i\sqrt 3 = 2\left( { – \frac{1}{2} + i\frac{{\sqrt 3 }}{2}} \right)$ $= 2\left( {\cos \frac{{2\pi }}{3} + i\sin \frac{{2\pi }}{3}} \right).$

Suy ra $w$ có môđun $R = 2$ và một acgumen $\theta = \frac{{2\pi }}{3}.$

Do đó, căn bậc ba của $w$ là số phức $z$ có: môđun $r = \sqrt[3]{2}$ và một acgumen $\phi = \frac{\theta }{3} + \frac{{k2\pi }}{3} = \frac{{2\pi }}{9} + \frac{{k2\pi }}{3},k \in Z.$

Lấy $k = 0,1,2$ thì $\varphi$ có ba giá trị:

${\varphi _1} = \frac{{2\pi }}{9}$, ${\varphi _2} = \frac{{2\pi }}{9} + \frac{{2\pi }}{3} = \frac{{8\pi }}{9}$, ${\varphi _3} = \frac{{2\pi }}{9} + \frac{{4\pi }}{3} = \frac{{14\pi }}{9}.$

Vậy $w = – 1 + i\sqrt 3$ có $3$ căn bậc ba là: ${z_1} = \sqrt[3]{2}\left( {\cos \frac{{2\pi }}{9} + i\sin \frac{{2\pi }}{9}} \right)$, ${z_2} = \sqrt[3]{2}\left( {\cos \frac{{8\pi }}{9} + i\sin \frac{{8\pi }}{9}} \right)$, ${z_3} = \sqrt[3]{2}\left( {\cos \frac{{14\pi }}{9} + i\sin \frac{{14\pi }}{9}} \right).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/03/ap-dung-cong-thuc-moa-vro-de-tinh-can-bac-n-cua-so-phuc.html -->
## Ví dụ 3. Tính căn bậc bốn của số phức sau và viết dưới dạng lượng giác: $w = i.$

Ta có: $w = i = \cos \frac{\pi }{2} + i\sin \frac{\pi }{2}$ có môđun $R = 1$ và một acgumen $\theta = \frac{\pi }{2}.$

Suy ra căn bậc bốn của $w$ là số phức $z$ có: môđun $r = 1$ và một acgumen $\varphi = \frac{\theta }{4} + \frac{{k2\pi }}{4} = \frac{\pi }{8} + \frac{{k\pi }}{2},k \in Z.$

Lấy $k = 0,1,2,3$ ta có $4$ giá trị của $\varphi$: ${\varphi _1} = \frac{\pi }{8}$, ${\varphi _2} = \frac{\pi }{8} + \frac{\pi }{2} = \frac{{5\pi }}{8}$, ${\varphi _3} = \frac{\pi }{8} + \pi = \frac{{9\pi }}{8}$, ${\varphi _4} = \frac{\pi }{8} + \frac{{3\pi }}{2} = \frac{{13\pi }}{8}.$