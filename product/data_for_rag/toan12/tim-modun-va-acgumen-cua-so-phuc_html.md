# Tìm môđun và acgumen của số phức

<!-- chunk:0 level:0 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
Bài viết hướng dẫn tìm môđun và acgumen của một số phức bất kỳ, đây là một dạng toán căn bản trong chương trình Giải tích 12 chương 4 mà học sinh cần nắm vững, ngoài ra bài viết còn cung cấp một số ví dụ nâng cao và mở rộng của dạng toán này. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu số phức trên TOANMATH.com.

Phương pháp: Nhìn chung các bài tập này có cách giải như sau:

Giả sử ta cần tìm một acgumen của số phức $z$. Ta cần biến đổi sao cho $z$ có dạng $z = r\left( {\cos \varphi + i\sin \varphi } \right).$

1. Với $z = a + bi, (a,b \in R)$ ta có mô đun của $z$ là $r = \sqrt {{a^2} + {b^2}}$, và $1$ acgumen của $z$ là $\varphi$ thỏa  $c{\rm{os}}\varphi = \frac{{{a^2}}}{{\sqrt {{a^2} + {b^2}} }}$; $\sin \varphi = \frac{{{b^2}}}{{\sqrt {{a^2} + {b^2}} }}.$

2. Với $z = r(c{\rm{os}}\varphi + i\sin \varphi )$ thì $z$ có mô đun là $r$ và $1$ acgumen của $z$ là $\varphi.$

3. Với $z = r(\cos \varphi – i \sin \varphi )$ $= r\left[ {c{\rm{os}}( – \varphi ) + i \sin ( – \varphi )} \right].$

4. Với $z = r(\sin \varphi + i c{\rm{os}}\varphi )$ $= r\left[ {c{\rm{os}}(\frac{\pi }{2} – \varphi ) + i \sin (\frac{\pi }{2} – \varphi )} \right].$

Các ví dụ điển hình thường gặp:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 1. Cho số phức $z = 1 – \sin \varphi + i\cos \varphi ,$ $0 < \varphi < \frac{\pi }{2}.$ Tìm một acgumen của số phức $z$.

$z = 1 – \sin \varphi + i\cos \varphi$ $= 1 – \cos \left( {\frac{\pi }{2} – \varphi } \right) + i\sin \left( {\frac{\pi }{2} – \varphi } \right)$

$= 2{\sin ^2}\left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right)$ $+ 2i\sin \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right)\cos \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right)$

$= 2\sin \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right)$ $\left[ {\sin \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right) + i\cos \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right)} \right]$

$= 2\sin \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right)$ $\left[ {\cos \left( {\frac{\pi }{4} + \frac{\varphi }{2}} \right) + i\sin \left( {\frac{\pi }{4} + \frac{\varphi }{2}} \right)} \right].$

Do $0 < \varphi < \frac{\pi }{2}$ nên $2\sin \left( {\frac{\pi }{4} – \frac{\varphi }{2}} \right) > 0.$ Vậy, một acgumen của $z$ là $\frac{\pi }{4} + \frac{\varphi }{2}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 2. Cho số phức $z$ có mô đun bằng $1$ và $\varphi$ là một acgumen của $z.$
a. Tìm một acgumen của $\frac{{\overline z }}{z}.$

b. Tìm một acgumen của $\overline z + z$ nếu $\cos \varphi \ne 0.$

Từ giả thiết suy ra $z = \cos \varphi + isin\varphi .$

a. Ta có

$\frac{{\overline z }}{z} = \frac{{\cos \varphi – i\sin \varphi }}{{\cos \varphi + i\sin \varphi }}$ $= \frac{{\cos \left( { – \varphi } \right) + i\sin \left( { – \varphi } \right)}}{{\cos \varphi + i\sin \varphi }}$ $= \cos \left( { – 2\varphi } \right) + i\sin \left( { – 2\varphi } \right).$

Vậy một acgumen của $z$ là $– 2\varphi .$

b. Ta có: $\overline z + z = 2\cos \varphi .$

+ Nếu $\cos \varphi > 0$ thì $\overline z + z = 2\cos \varphi$ $= 2\cos \varphi \left( {\cos 0 + i\sin 0} \right).$ Lúc đó $0$ là một acgumen của $\overline z + z.$

+ Nếu $\cos \varphi < 0$ thì $\overline z + z = – 2\cos \varphi .( – 1)$ $= – 2\cos \varphi \left( {\cos \pi + i\sin \pi } \right).$ Lúc đó $\pi$ là một acgumen của $\overline z + z.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 3. Tìm môđun và một acgumen của các số phức sau:

a. $z = 1 + \cos \frac{\pi }{4} + i\sin \frac{\pi }{4}.$

b. $z = 1 + \cos \frac{\pi }{3} – i\sin \frac{\pi }{3}.$

c. $z = 1 – \cos \frac{{2\pi }}{5} + i\sin \frac{{2\pi }}{5}.$

d. $z = – 1 – \sin \frac{\pi }{3} + i\sin \frac{\pi }{6}.$

e. $z = – 1 + \sin \frac{\pi }{6} – i\sin \frac{\pi }{6}.$

a. $z = 1 + \cos \frac{\pi }{4} + i\sin \frac{\pi }{4}$ $= 2{\cos ^2}\frac{\pi }{8} + 2i\sin \frac{\pi }{8}\cos \frac{\pi }{8}.$

Vậy 
$$
\left\{ \begin{array}{l}
r = 2\cos \frac{\pi }{8}\\
\varphi = \frac{\pi }{8}
\end{array} \right.
$$

b. $z = 1 + \cos \frac{\pi }{3} – i\sin \frac{\pi }{3}$ $= 2{\cos ^2}\frac{\pi }{6} + 2i\sin \frac{\pi }{6}.\cos \frac{\pi }{6}$

$= 2\cos \frac{\pi }{6}\left( {\cos \frac{\pi }{6} – i\sin \frac{\pi }{6}} \right)$ $= 2\cos \frac{\pi }{6}\left[ {\cos \left( { – \frac{\pi }{6}} \right) + i\sin \left( { – \frac{\pi }{6}} \right)} \right].$

Vậy 
$$
\left\{ \begin{array}{l}
r = 2\cos \frac{\pi }{6} = \sqrt 3 \\
\varphi = – \frac{\pi }{6}
\end{array} \right.
$$

c. $z = 1 – \cos \frac{{2\pi }}{5} + i\sin \frac{{2\pi }}{5}$ $= 2{\sin ^2}\frac{\pi }{5} + 2i\sin \frac{\pi }{5}.\cos \frac{\pi }{5}$

$= 2\sin \frac{\pi }{5}\left( {\sin \frac{\pi }{5} + i\cos \frac{\pi }{5}} \right)$ $= 2\sin \frac{\pi }{5}\left( {\cos \frac{{3\pi }}{{10}} + i\sin \frac{{3\pi }}{{10}}} \right).$

Vậy 
$$
\left\{ \begin{array}{l}
r = 2\sin \frac{\pi }{5}\\
\varphi = \frac{{3\pi }}{{10}}
\end{array} \right.
$$

d. $z = – 1 – \sin \frac{\pi }{3} + i\sin \frac{\pi }{6}$ $= – 1 – \cos \frac{\pi }{6} + 2i\sin \frac{\pi }{6}$

$= – 2{\cos ^2}\frac{\pi }{{12}} + 2i\sin \frac{\pi }{{12}}\cos \frac{\pi }{{12}}$ $= 2\cos \frac{\pi }{{12}}\left( { – \cos \frac{\pi }{{12}} + i\sin \frac{\pi }{{12}}} \right)$ $= 2\cos \frac{\pi }{{12}}\left( {\cos \frac{{11\pi }}{{12}} + i\sin \frac{{11\pi }}{{12}}} \right).$

Vậy 
$$
\left\{ \begin{array}{l}
r = 2\cos \frac{\pi }{{12}}\\
\varphi = \frac{{11\pi }}{{12}}
\end{array} \right.
$$

e. $z = – 1 + \sin \frac{\pi }{6} – i\sin \frac{\pi }{6}$ $= – 1 + \cos \frac{\pi }{3} – i\sin \frac{\pi }{3}$

$= – 2{\sin ^2}\frac{\pi }{6} – 2i\sin \frac{\pi }{6}.\cos \frac{\pi }{6}$ $= 2\sin \frac{\pi }{6}\left( { – \sin \frac{\pi }{6} – i\cos \frac{\pi }{6}} \right)$

$= 2.\frac{1}{2}\left( {\sin \frac{{7\pi }}{6} + i\cos \frac{{7\pi }}{6}} \right)$ $= \cos \left( { – \frac{{2\pi }}{3}} \right) + i\sin \left( { – \frac{{2\pi }}{3}} \right).$

Vậy 
$$
\left\{ \begin{array}{l}
r = 1\\
\varphi = – \frac{{2\pi }}{3}
\end{array} \right.
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 4.  Tìm môđun và một acgumen của các số phức sau:

a. $z = 1 + \frac{1}{{\sqrt 2 }} – \frac{1}{{\sqrt 2 }}i.$

b. $z = 2 – \sqrt 2 – i\sqrt 2 .$

c. $z = 2\sqrt 3 + 3 + i\sqrt 3.$

d. $z = \frac{{\sqrt 3 }}{3} – \frac{2}{3} + \frac{1}{3}i.$

Ta kí hiệu $r$ và $\varphi$ lần lượt là môđun và acgumen của số phức $z$, ta có:

a. $z = 1 + \frac{1}{{\sqrt 2 }} – \frac{1}{{\sqrt 2 }}i$ $= 1 + \cos \frac{\pi }{4} – i\sin \frac{\pi }{4}$

$= 2{\cos ^2}\frac{\pi }{8} – 2i\sin \frac{\pi }{8}.\cos \frac{\pi }{8}$ $= 2\cos \frac{\pi }{8}\left( {\cos \frac{\pi }{8} – i\sin \frac{\pi }{8}} \right)$

$= 2\cos \frac{\pi }{8}\left[ {\cos \left( { – \frac{\pi }{8}} \right) + i\sin \left( { – \frac{\pi }{8}} \right)} \right].$

Vậy 
$$
\left\{ \begin{array}{l}
r = 2\cos \frac{\pi }{8}\\
\varphi = – \frac{\pi }{8}
\end{array} \right.
$$

b. $z = 2 – \sqrt 2 – i\sqrt 2$ $= 2\left( {1 – \frac{{\sqrt 2 }}{2} – \frac{{i\sqrt 2 }}{2}} \right)$ $= 2\left( {1 – \cos \frac{\pi }{4} – i\sin \frac{\pi }{4}} \right)$

$= 2\left( {2{{\sin }^2}\frac{\pi }{8} – 2i\sin \frac{\pi }{8}.\cos \frac{\pi }{8}} \right)$ $= 4\sin \frac{\pi }{8}\left( {\sin \frac{\pi }{8} – i\cos \frac{\pi }{8}} \right)$

$= 4\sin \frac{\pi }{8}\left( {\cos \frac{{3\pi }}{8} – i\sin \frac{{3\pi }}{8}} \right)$ $= 4\sin \frac{\pi }{8}\left[ {\cos \left( { – \frac{{3\pi }}{8}} \right) + i\sin \left( { – \frac{{3\pi }}{8}} \right)} \right].$

Vậy 
$$
\left\{ \begin{array}{l}
r = 4\sin \frac{\pi }{8}\\
\varphi = – \frac{{3\pi }}{8}
\end{array} \right.
$$

c. $z = 2\sqrt 3 + 3 + i\sqrt 3$ $= 2\sqrt 3 \left( {1 + \frac{{\sqrt 3 }}{2} + \frac{1}{2}i} \right)$ $= 2\sqrt 3 \left( {1 + \cos \frac{\pi }{6} + i\sin \frac{\pi }{6}} \right)$

$= 2\sqrt 3 \left( {2{{\cos }^2}\frac{\pi }{{12}} + 2i\sin \frac{\pi }{{12}}.\cos \frac{\pi }{{12}}} \right)$ $= 4\sqrt 3 \cos \frac{\pi }{{12}}\left( {\cos \frac{\pi }{{12}} + i\sin \frac{\pi }{{12}}} \right).$

Vậy 
$$
\left\{ \begin{array}{l}
r = 4\sqrt 3 \cos \frac{\pi }{{12}}\\
\varphi = \frac{\pi }{{12}}
\end{array} \right.
$$

d. $z = \frac{{\sqrt 3 }}{3} – \frac{2}{3} + \frac{1}{3}i$ $= – \frac{2}{3} + \frac{{\sqrt 3 }}{3} + \frac{1}{3}i$ $= \frac{2}{3}\left( { – 1 + \frac{{\sqrt 3 }}{2} + \frac{1}{2}i} \right)$

$= \frac{2}{3}\left( { – 2{{\sin }^2}\frac{\pi }{{12}} + 2i\sin \frac{\pi }{{12}}.\cos \frac{\pi }{{12}}} \right)$ $= \frac{4}{3}\sin \frac{\pi }{{12}}\left( { – \sin \frac{\pi }{{12}} + i\cos \frac{\pi }{{12}}} \right)$

$= \frac{4}{3}\sin \frac{\pi }{{12}}\left( {\sin \left( { – \frac{\pi }{{12}}} \right) + i\cos \left( { – \frac{\pi }{{12}}} \right)} \right)$ $= \frac{4}{3}\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right).$

Vậy 
$$
\left\{ \begin{array}{l}
r = \frac{4}{3}\sin \frac{\pi }{{12}}\\
\phi = \frac{{7\pi }}{{12}}
\end{array} \right.
$$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 5.  Gọi ${z_1}, {z_2}$ là hai nghiệm của phương trình ${z^2} – 2iz – 4 = 0$, ${z_1}$ có phần thực âm. Tính môđun và acgumen của các số phức sau:

a. $w = z_1^2.{z_2}.$

b. $w = \frac{{{z_1}}}{{{z_2} – 2}}.$

c. $w = \left( {{z_1} – 2} \right)\left( {{z_2} – 2} \right).$

d. $w = \overline {{z_1}.} \left( {2 – \overline {{z_2}} } \right).$

Ta gọi $r$ và $\varphi$ lần lượt là môđun và acgumen của số phức $w.$

Giải phương trình: ${z^2} – 2iz – 4 = 0$ ta được  $2$ nghiệm là:

${z_1} = – \sqrt 3 + i = 2\left( { – \frac{{\sqrt 3 }}{2} + \frac{1}{2}i} \right)$ $= 2\left( {\cos \frac{{5\pi }}{6} + i\sin \frac{{5\pi }}{6}} \right)$ (vì ${z_1}$ có phần thực âm).

${z_2} = \sqrt 3 + i = 2\left( {\frac{{\sqrt 3 }}{2} + \frac{1}{2}i} \right)$ $= 2\left( {\cos \frac{\pi }{6} + i\sin \frac{\pi }{6}} \right).$

a. Ta có: $z_1^2 = 4\left( {\cos \frac{{5\pi }}{3} + i\sin \frac{{5\pi }}{3}} \right)$, ${z_2} = 2\left( {\cos \frac{\pi }{6} + i\sin \frac{\pi }{6}} \right).$

Suy ra: $w = z_1^2.{z_2}$ $= 4.2.\left[ {\cos \left( {\frac{{5\pi }}{3} + \frac{\pi }{6}} \right) + i\sin \left( {\frac{{5\pi }}{3} + \frac{\pi }{6}} \right)} \right]$ $= 8\left( {\cos \frac{{11\pi }}{6} + i\sin \frac{{11\pi }}{6}} \right).$

Vậy $w$ có môđun và một acgumen là: 
$$
\left\{ \begin{array}{l}
r = 8\\
\varphi = \frac{{11\pi }}{6}
\end{array} \right.
$$

b. Ta có

${z_2} – 2 = \sqrt 3 + i – 2$ $= 2\left( { – 1 + \frac{{\sqrt 3 }}{2} + \frac{1}{2}i} \right)$ $= 2\left( { – 1 + \cos \frac{\pi }{6} + i\sin \frac{\pi }{6}} \right)$

$= 2\left( { – 2{{\sin }^2}\frac{\pi }{{12}} + 2i\sin \frac{\pi }{{12}}.\cos \frac{\pi }{{12}}} \right)$ $= 4\sin \frac{\pi }{{12}}\left( { – \sin \frac{\pi }{{12}} + i\cos \frac{\pi }{{12}}} \right)$

$= 4\sin \frac{\pi }{{12}}\left[ {\sin \left( { – \frac{\pi }{{12}}} \right) + i\sin \left( { – \frac{\pi }{{12}}} \right)} \right]$ $= 4\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right).$

Suy ra: $w = \frac{{{z_1}}}{{{z_2} – 2}}$ $= \frac{{2\left( {\cos \frac{{5\pi }}{6} + i\sin \frac{{5\pi }}{6}} \right)}}{{4\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right)}}$

$= \frac{1}{{2\sin \frac{\pi }{{12}}}}\left[ {\cos \left( {\frac{{5\pi }}{6} – \frac{{7\pi }}{{12}}} \right) + i\sin \left( {\frac{{5\pi }}{6} – \frac{{7\pi }}{{12}}} \right)} \right]$

$= \frac{1}{{2\sin \frac{\pi }{{12}}}}\left( {\cos \frac{{3\pi }}{{12}} + i\sin \frac{{3\pi }}{{12}}} \right)$ $= \frac{1}{{2\sin \frac{\pi }{{12}}}}\left( {\cos \frac{\pi }{4} + i\sin \frac{\pi }{4}} \right).$

Vậy $w = \frac{{{z_1}}}{{{z_2} – 2}}$ có môđun và acgumen là
\left\{ \begin{array}{l}
r = \frac{1}{{2\sin \frac{\pi }{{12}}}}\\
\varphi = \frac{\pi }{4}
\end{array} \right.
c. Ta có ${z_2} – 2$ $= 4\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right)$ (theo câu b) và:

${z_1} – 2 = – \sqrt 3 + i – 2$ $= 2\left( { – 1 – \frac{{\sqrt 3 }}{2} + \frac{1}{2}i} \right)$ $= 2\left( { – 1 – \cos \frac{\pi }{6} + i\sin \frac{\pi }{6}} \right)$

$= 2\left( { – 2{{\cos }^2}\frac{\pi }{{12}} + 2i\sin \frac{\pi }{{12}}.\cos \frac{\pi }{{12}}} \right)$ $= 4\cos \frac{\pi }{{12}}\left( { – \cos \frac{\pi }{{12}} + i\sin \frac{\pi }{{12}}} \right)$

$= 4\cos \frac{\pi }{{12}}\left( {\cos \frac{{11\pi }}{{12}} + i\sin \frac{{11\pi }}{{12}}} \right).$

Suy ra:

$w = \left( {{z_1} – 2} \right)\left( {{z_2} – 2} \right)$ $= 4\cos \frac{\pi }{{12}}\left( {\cos \frac{{11\pi }}{{12}} + i\sin \frac{{11\pi }}{{12}}} \right)$.$4\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right)$

$= 16.\sin \frac{\pi }{{12}}.\cos \frac{\pi }{{12}}\left[ {\cos \left( {\frac{{11\pi }}{{12}} + \frac{{7\pi }}{{12}}} \right) + i\sin \left( {\frac{{11\pi }}{{12}} + \frac{{7\pi }}{{12}}} \right)} \right]$

$= 8.\sin \frac{\pi }{6}.\left( {\cos \frac{{18\pi }}{{12}} + i\sin \frac{{18\pi }}{{12}}} \right)$ $= 8\sin \frac{\pi }{6}\left( {\cos \frac{{3\pi }}{2} + i\sin \frac{{3\pi }}{2}} \right)$

$= 4\cos \frac{\pi }{{12}}\left( {\cos \frac{{3\pi }}{2} + i\sin \frac{{3\pi }}{2}} \right).$

Vậy $w = \left( {{z_1} – 2} \right)\left( {{z_2} – 2} \right)$ có môđun và một acgumen là: 
$$
\left\{ \begin{array}{l}
r = 4\\
\varphi = \frac{{3\pi }}{2}
\end{array} \right.
$$

Cách khác: Trong trường hợp này, ta có thể áp dụng công thức Vi-et:

${z_1} + {z_2} = 2i, {z_1}{z_2} = – 4.$

Ta có:

$w = \left( {{z_1} – 2} \right)\left( {{z_2} – 2} \right)$ $= {z_1}.{z_2} – 2\left( {{z_1} + {z_2}} \right) + 4$ $= – 4 – 2.2i + 4 = – 4i$

$= 4\left( {0 – i} \right)$ $= 4\left( {\cos \frac{{3\pi }}{2} + i\sin \frac{{3\pi }}{2}} \right).$

d. $w = \overline {{z_1}} .\left( {2 – \overline {{z_2}} } \right)$ $\Rightarrow \overline w = \overline {\overline {{z_1}} .\left( {2 – \overline {{z_2}} } \right)}$ $= {z_1}.\left( {2 – {z_2}} \right) = – {z_1}.\left( {{z_2} – 2} \right)$

Với $– {z_1} = – 2\left( {\cos \frac{{5\pi }}{6} + i\sin \frac{{5\pi }}{6}} \right)$ $= 2\left( { – \cos \frac{{5\pi }}{6} – i\sin \frac{{5\pi }}{6}} \right)$

$= 2\left[ {\cos \left( {\frac{{5\pi }}{6} – \pi } \right) + i\sin \left( {\frac{{5\pi }}{6} – \pi } \right)} \right]$ $= 2\left[ {\cos \left( { – \frac{\pi }{6}} \right) + i\sin \left( { – \frac{\pi }{6}} \right)} \right]$ và ${z_2} – 2$ $= 4\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right).$

Suy ra:

$\overline w = – {z_1}.\left( {{z_2} – 2} \right)$ $= 2\left[ {\cos \left( { – \frac{\pi }{6}} \right) + i\sin \left( { – \frac{\pi }{6}} \right)} \right]$.$4\sin \frac{\pi }{{12}}\left( {\cos \frac{{7\pi }}{{12}} + i\sin \frac{{7\pi }}{{12}}} \right)$

$= 8\sin \frac{\pi }{{12}}$.$\left[ {\cos \left( { – \frac{\pi }{6} + \frac{{7\pi }}{{12}}} \right) + i\sin \left( { – \frac{\pi }{6} + \frac{{7\pi }}{{12}}} \right)} \right]$ $= 8\sin \frac{\pi }{{12}}.\left( {\cos \frac{{5\pi }}{{12}} + i\sin \frac{{5\pi }}{{12}}} \right)$

$\Rightarrow w = 8\sin \frac{\pi }{{12}}$.$\left( {\cos \frac{{5\pi }}{{12}} – i\sin \frac{{5\pi }}{{12}}} \right)$

$= 8\sin \frac{\pi }{{12}}$.$\left[ {\cos \left( { – \frac{{5\pi }}{{12}}} \right) + i\sin \left( { – \frac{{5\pi }}{{12}}} \right)} \right].$

Vậy $w = \overline {{z_1}} .\left( {2 – \overline {{z_2}} } \right)$ có môđun và acgumen là: 
$$
\left\{ \begin{array}{l}
r = 8\sin \frac{\pi }{{12}}\\
\varphi = – \frac{{5\pi }}{{12}}
\end{array} \right.
$$

[ads]

<!-- chunk:6 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 6. Tìm môđun và một acgumen của số phức $z$ thỏa mãn phương trình: $\frac{{1 + {z^2}}}{{1 – {z^2}}} = i$.

Ta có: $\frac{{1 + {z^2}}}{{1 – {z^2}}} = i$ $\Leftrightarrow 1 + {z^2} = i – i{z^2}$ $\Leftrightarrow \left( {1 + i} \right){z^2} = – 1 + i$ $\Leftrightarrow {z^2} = \frac{{ – 1 + i}}{{1 + i}}.$

${z^2} = \frac{{ – \left( {1 – i} \right)\left( {1 – i} \right)}}{{\left( {1 + i} \right)\left( {1 – i} \right)}}$ $= \frac{{ – \left( {1 + {i^2} – 2i} \right)}}{{1 + 1}} = i$ $= \cos \frac{\pi }{2} + i\sin \frac{\pi }{2}.$

$\Rightarrow \left| z \right| = 1$. Đặt $z = \cos \varphi + i\sin \varphi$ $\Rightarrow {z^2} = \cos 2\varphi + i\sin 2\varphi .$

Ta có:

${z^2} = \cos \frac{\pi }{2} + i\sin \frac{\pi }{2}$ $\Leftrightarrow \cos 2\varphi + i\sin 2\varphi$ $= \cos \frac{\pi }{2} + i\sin \frac{\pi }{2}$

$\Leftrightarrow 2\varphi = \frac{\pi }{2} + k2\pi$ $\Leftrightarrow \varphi = \frac{\pi }{4} + k\pi .$

Chọn $k = 0, 1$ ta được ${\varphi _1} = \frac{\pi }{4}, {\varphi _2} = \frac{{5\pi }}{4}.$

Vậy có $2$ số phức $z$ thỏa mãn: $\frac{{1 + {z^2}}}{{1 – {z^2}}} = i$ là:

${z_1}$ có môđun $r = 1$, một acgumen là ${\varphi _1} = \frac{\pi }{4}$ và ${z_2}$ có môđun $r = 1$, một acgumen là $\varphi = \frac{{5\pi }}{4}$.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 7.  Trong các acgumen của số phức ${\left( {1 – \sqrt 3 i} \right)^8}$, tìm acgumen có số đo dương nhỏ nhất.

Ta có: $1 – \sqrt 3 i = 2\left( {\frac{1}{2} – \frac{{\sqrt 3 }}{2}i} \right)$ $= 2\left( {\cos \frac{{ – \pi }}{6} + i\sin \frac{{ – \pi }}{3}} \right).$

Theo công thức Moivre ta có: $z = {2^8}\left( {\cos \frac{{ – 8\pi }}{3} + i\sin \frac{{ – 8\pi }}{3}} \right)$. Từ đó suy ra $z$ có các họ acgumen là: $– \frac{{8\pi }}{3} + 2k\pi , k \in R$. Ta thấy với $k = 2$ thì acgumen dương nhỏ nhất của $z$ là $\frac{{4\pi }}{3}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 8. Tìm acgumen âm lớn nhất của số phức $z = {\left( {1 + i\sqrt 3 } \right)^{10}}.$

$z = {\left( {1 + i\sqrt 3 } \right)^{10}}$ $= {2^{10}}{\left( {\frac{1}{2} + i\frac{{\sqrt 3 }}{2}} \right)^{10}}$ $= {2^{10}}{\left( {cos\frac{\pi }{3} + i.\sin \frac{\pi }{3}} \right)^{10}}.$

Áp dụng công thức Moivre, ta có:

$z = {2^{10}}\left( {cos\frac{{10\pi }}{3} + i.\sin \frac{{10\pi }}{3}} \right)$ $= {2^{10}}\left( {cos\frac{{4\pi }}{3} + i.\sin \frac{{4\pi }}{3}} \right).$

Các acgumen của $z$ đều có dạng $\frac{{4\pi }}{3} + k2\pi \left( {k \in Z} \right)$. Ta có $\frac{{4\pi }}{3} + k2\pi < 0 \Leftrightarrow k < – \frac{2}{3}$ hay $k \in \left\{ {…, – 4, – 3, – 2, – 1} \right\}.$

Acgumen âm lớn nhất của $z$ tương ứng với $k = – 1.$

Vậy acgumen cần tìm của $z$ là $– \frac{{2\pi }}{3}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 9. Giải phương trình sau trên tập hợp số phức ${\left( {z + i} \right)^4} + 1 = i\sqrt 3 .$

Ta có: ${\left( {z + i} \right)^4}$ $= – 1 + i\sqrt 3 \Leftrightarrow {\left( {z + i} \right)^4}$ $= 2\left( {\cos \frac{{2\pi }}{3} + i\sin \frac{{2\pi }}{3}} \right)$ $\left( 1 \right).$

Giả sử $z + i = r\left( {\cos \varphi + i\sin \varphi } \right)$, $r \in {R^ + }$ $\Rightarrow {\left( {z + i} \right)^4}$ $= {r^4}\left( {\cos 4\varphi + i\sin 4\varphi } \right)$ $\left( 2 \right).$

Từ $(1)$ và $(2)$ suy ra: 
$$
\left\{ \begin{array}{l}
{r^4} = 2\\
\cos 4\varphi = \cos \frac{{2\pi }}{3}\\
\sin 4\varphi = \sin \frac{{2\pi }}{3}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
r = \sqrt[4]{2}\\
\varphi = \frac{\pi }{6} + \frac{{k\pi }}{2} \left( {k \in Z} \right)
\end{array} \right.
$$

Cho $k = 0, \pm 1, – 2$ ta nhận được các giá trị acgumen tương ứng của số phức $z + i$ là ${\varphi _1} = \frac{\pi }{6}$, ${\varphi _2} = \frac{{2\pi }}{3}$, ${\varphi _3} = – \frac{\pi }{3}$, ${\varphi _4} = – \frac{{5\pi }}{6}.$

Từ đó phương trình đã cho có $4$ nghiệm lần lượt là:

$z + i = \sqrt[4]{2}\left( {\cos \frac{\pi }{6} + i\sin \frac{\pi }{6}} \right)$ hay $z = \frac{{\sqrt[4]{{18}}}}{2} + \left( {\frac{{\sqrt[4]{2}}}{2} – 1} \right)i.$

$z + i = \sqrt[4]{2}\left( {\cos \frac{{2\pi }}{3} + i\sin \frac{{2\pi }}{3}} \right)$ hay $z = – \frac{{\sqrt[4]{2}}}{2} + \left( {\frac{{\sqrt[4]{{18}}}}{2} – 1} \right)i.$

$z + i$ $= \sqrt[4]{2}\left( {\cos \left( { – \frac{\pi }{3}} \right) + i\sin \left( { – \frac{\pi }{3}} \right)} \right)$ hay $z = \frac{{\sqrt[4]{2}}}{2} – \left( {\frac{{\sqrt[4]{{18}}}}{2} + 1} \right)i.$

$z + i$ $= \sqrt[4]{2}\left( {\cos \left( { – \frac{{5\pi }}{6}} \right) + i\sin \left( { – \frac{{5\pi }}{6}} \right)} \right)$ hay $z = – \frac{{\sqrt[4]{{18}}}}{2} – \left( {\frac{{\sqrt[4]{2}}}{2} + 1} \right)i.$

Nhận xét: Dạng lượng giác luôn phát huy được ưu thế của mình khi xử lí các biểu thức lũy thừa bậc cao của số phức.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 10. Gọi ${z_1}, {z_2}$ là nghiệm của phương trình ${z^2} – \left( {2{\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}}} \right)z + 1 = 0$. Tìm số $n$ nguyên dương nhỏ nhất sao cho ${z_1}^n + {z_2}^n = 1.$

Đặt ${z^2} – \left( {2{\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}}} \right)z + 1 = 0$ $(1)$. Biệt thức của $(1)$ là:

$\Delta’ = {\mathop{\rm co}\nolimits} {s^2}\frac{{5\pi }}{{21}} – 1$ $= – {\sin ^2}\frac{{5\pi }}{{21}} = {\left( {i{{\sin }^2}\frac{{5\pi }}{{21}}} \right)^2}.$

Vậy $(1)$ có các nghiệm là ${z_1} = {\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}} – i\sin \frac{{5\pi }}{{21}}$ và ${z_2} = {\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}} + i\sin \frac{{5\pi }}{{21}}.$

${z_1}^n + {z_2}^n = 1$ $\Leftrightarrow {\left( {{\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}} – i\sin \frac{{5\pi }}{{21}}} \right)^n}$ $+ {\left( {{\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}} + i\sin \frac{{5\pi }}{{21}}} \right)^n} = 1$

$\Leftrightarrow {\left[ {{\mathop{\rm co}\nolimits} s\left( { – \frac{{5\pi }}{{21}}} \right) + i\sin \left( {\frac{{5\pi }}{{21}}} \right)} \right]^n}$ $+ {\left( {{\mathop{\rm co}\nolimits} s\frac{{5\pi }}{{21}} + i\sin \frac{{5\pi }}{{21}}} \right)^n} = 1$

$\Leftrightarrow {\mathop{\rm co}\nolimits} s\left( { – \frac{{n5\pi }}{{21}}} \right) – i\sin \left( { – \frac{{n5\pi }}{{21}}} \right)$ $+ {\mathop{\rm co}\nolimits} s\frac{{n5\pi }}{{21}} + i\sin \frac{{n5\pi }}{{21}} = 1$

$\Leftrightarrow cos\left( { – \frac{{n5\pi }}{{21}}} \right) + {\mathop{\rm co}\nolimits} s\frac{{n5\pi }}{{21}} = 1$ $\Leftrightarrow 2{\mathop{\rm co}\nolimits} s\frac{{n5\pi }}{{21}} = 1$

$\Leftrightarrow {\mathop{\rm co}\nolimits} s\frac{{n5\pi }}{{21}} = {\mathop{\rm co}\nolimits} s\frac{\pi }{3}$ $\Leftrightarrow \frac{{n5\pi }}{{21}} = \pm \frac{\pi }{3} + k2\pi$ $\Leftrightarrow n = \pm \frac{7}{5} + \frac{{42k}}{5} \left( {k \in Z} \right) \left( * \right).$

Vì $n$ là số nguyên nhỏ nhất nên từ $(*)$ suy ra: $n = 7.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/04/tim-modun-va-acgumen-cua-so-phuc.html -->
## Ví dụ 11. Cho số phức $z$ thỏa mãn $z + \sqrt 2 i$ có một acgument bằng một acgument của $z + \sqrt 2$ cộng với $\frac{\pi }{4}$. Tìm giá trị lớn nhất của biểu thức $T = \left| {z + 1} \right| + \left| {z + i} \right|.$

Đặt $z = a + bi\left( {a,b \in R} \right)$. Khi đó $z + \sqrt 2 i$ có một acgument bằng acgument của $z + \sqrt 2$ cộng với $\frac{\pi }{4}$ nên $\frac{{z + \sqrt 2 i}}{{z + \sqrt 2 }} = r\left( {cos\frac{\pi }{4} + i.\sin \frac{\pi }{4}} \right)$ với $r > 0.$

$\frac{{z + \sqrt 2 i}}{{z + \sqrt 2 }} = \frac{{a + \left( {b + \sqrt 2 } \right)i}}{{a + \sqrt 2 + bi}}$ $= \frac{{a\left( {a + \sqrt 2 } \right) + b\left( {b + \sqrt 2 } \right)}}{{{{\left( {a + \sqrt 2 } \right)}^2} + {b^2}}}$ $+ \frac{{\left( {a + \sqrt 2 } \right)\left( {b + \sqrt 2 } \right) – ab}}{{{{\left( {a + \sqrt 2 } \right)}^2} + {b^2}}} – i.$

Suy ra $\frac{{a\left( {a + \sqrt 2 } \right) + b\left( {b + \sqrt 2 } \right)}}{{{{\left( {a + \sqrt 2 } \right)}^2} + {b^2}}}$ $= \frac{{\left( {a + \sqrt 2 } \right)\left( {b + \sqrt 2 } \right) – ab}}{{{{\left( {a + \sqrt 2 } \right)}^2} + {b^2}}} – i > 0$

$$
\Leftrightarrow \left\{ \begin{array}{l}
{a^2} + {b^2} = 2\\
{\left( {a + 2} \right)^2} + {b^2} \ne 0\\
a + b + \sqrt 2 > 0
\end{array} \right. \left( * \right).
$$

Ta có: $T = \left| {z + 1} \right| + \left| {z + i} \right|$ $= \left| {a + 1 + bi} \right| + \left| {a + \left( {b + 1} \right)i} \right|$

$= \sqrt {{{\left( {a + 1} \right)}^2} + {b^2}} + \sqrt {{a^2} + {{\left( {b + 1} \right)}^2}}$ $= \sqrt {3 + 2a} + \sqrt {3 + 2b}$ do $(*).$

Áp dụng bất đẳng thức Cosi,ta được:

${T^2} \le 2\left( {6 + 2a + 2b} \right)$ $\le 2\left( {6 + 2\sqrt {{a^2} + {b^2}} } \right) = 20.$

Suy ra $T \le 2\sqrt 5$, đẳng thức xảy ra khi $a = b = 1.$

Vậy, giá trị lớn nhất của $T$ là: $2\sqrt 5$, đạt khi $z = 1 + i.$