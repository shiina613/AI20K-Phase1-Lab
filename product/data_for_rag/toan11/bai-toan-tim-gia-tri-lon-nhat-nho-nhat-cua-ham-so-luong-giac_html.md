# Bài toán tìm giá trị lớn nhất, nhỏ nhất của hàm số lượng giác

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số lượng giác.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 1: Tìm giá trị nhỏ nhất của biểu thức $A = \sin x + \sin \left( {x + \frac{{2\pi }}{3}} \right).$

A. $-1.$

B. $0.$

C. $-2.$

D. $\frac{{\sqrt 3 }}{2}.$

Chọn A.

Ta có $A = \sin x + \sin \left( {x + \frac{{2\pi }}{3}} \right)$ $= 2\sin \left( {x + \frac{\pi }{3}} \right)\cos \frac{\pi }{3}$ $= \sin \left( {x + \frac{\pi }{3}} \right).$

$– 1 \le \sin \left( {x + \frac{\pi }{3}} \right) \le 1$ $\Leftrightarrow – 1 \le A \le 1$, $\forall x \in R.$

Vậy $\mathop {\min }\limits_{x \in R} A = – 1$ khi $\sin \left( {x + \frac{\pi }{3}} \right) = – 1$ $\Leftrightarrow x = – \frac{{5\pi }}{6} + k2\pi$, $k \in Z.$

<!-- chunk:2 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 2: Tìm giá trị lớn nhất của biểu thức $A = {\sin ^4}x + {\cos ^4}x.$

A. $1.$

B. $0.$

C. $2.$

D. $\frac{1}{2}.$

Chọn A.

Ta có $A = {\sin ^4}x + {\cos ^4}x$ $= 1 – \frac{1}{2}{\sin ^2}2x.$

$0 \le {\sin ^2}2x \le 1$ $\Leftrightarrow \frac{1}{2} \le 1 – \frac{1}{2}{\sin ^2}2x \le 1$, $\forall x \in R.$

Vậy $\mathop {\max }\limits_{x \in R} A = 1$ khi ${\sin ^2}x = 1$ $\Leftrightarrow \cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 3: Tập giá trị của hàm số $y = \sin 2x + \sqrt 3 \cos 2x + 1$ là đoạn $[a;b].$ Tính tổng $T = a + b.$

A. $T = 1.$

B. $T = 2.$

C. $T = 0.$

D. $T = -1.$

Chọn B.

Cách 1: $y = \sin 2x + \sqrt 3 \cos 2x + 1$ $\Leftrightarrow \sin 2x + \sqrt 3 \cos 2x = y – 1.$

Để phương trình trên có nghiệm thì ${1^2} + {(\sqrt 3 )^2} \ge {(y – 1)^2}$ $\Leftrightarrow {y^2} – 2y – 3 \le 0$ $\Leftrightarrow – 1 \le y \le 3.$

Suy ra $y \in [ – 1;3].$ Vậy $T = – 1 + 3 = 2.$

Cách 2: $y = \sin 2x + \sqrt 3 \cos 2x + 1$ $= 2\sin \left( {2x + \frac{\pi }{3}} \right) + 1.$

Do $\sin \left( {2x + \frac{\pi }{3}} \right) \in [ – 1;1]$ nên $2\sin \left( {2x + \frac{\pi }{3}} \right) + 1 \in [ – 1;3].$

Vậy $– 1 \le y \le 3.$

Ta thấy $y = – 1$ khi $\sin \left( {2x + \frac{\pi }{3}} \right) = – 1$, $y = 3$ khi $\sin \left( {2x + \frac{\pi }{3}} \right) = 1.$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 4: Hằng ngày, mực nước của con kênh lên xuống theo thủy triều. Độ sâu $h$(m) của mực nước trong kênh tính theo thời gian $t$(h) được cho bởi công thức $h = 3\cos \left( {\frac{{\pi t}}{6} + \frac{\pi }{3}} \right) + 12.$ Khi nào mực nước của kênh là cao nhất với thời gian ngắn nhất?

A. $t = 22$(h).

B. $t = 15$(h).

C. $t = 14$(h).

D. $t = 10$(h).

Chọn D.

Ta có: $– 1 \le \cos \left( {\frac{\pi }{6}t + \frac{\pi }{3}} \right) \le 1$ $\Leftrightarrow 9 \le h \le 15.$ Do đó mực nước cao nhất của kênh là $15$m đạt được khi $\cos \left( {\frac{\pi }{6}t + \frac{\pi }{3}} \right) = 1$ $\Leftrightarrow \frac{\pi }{6}t + \frac{\pi }{3} = k2\pi$ $\Leftrightarrow t = – 2 + 12k.$

Vì $t > 0$ $\Leftrightarrow – 2 + 12k > 0$ $\Leftrightarrow k > \frac{1}{6}.$ Chọn số $k$ nguyên dương nhỏ nhất thoả $k > \frac{1}{6}$ là $k = 1$ $\Rightarrow t = 10.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 5: Gọi $M$ và $N$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = – 1 + 2\cos x[(2 – \sqrt 3 )\sin x + \cos x]$ trên $R.$ Biểu thức $M + N + 2$ có giá trị bằng?

A. $0.$

B. $4\sqrt {2 – \sqrt 3 } .$

C. $2.$

D. $\sqrt {2 + \sqrt 3 } + 2.$

Chọn C.

Ta có $y = – 1 + 2\cos x[(2 – \sqrt 3 )\sin x + \cos x]$ $= – 1 + 2(2 – \sqrt 3 )\sin x\cos x + 2{\cos ^2}x.$

$= (2 – \sqrt 3 )\sin 2x + \left( {2{{\cos }^2}x – 1} \right)$ $= (2 – \sqrt 3 )\sin 2x + \cos 2x.$

$= (\sqrt 6 – \sqrt 2 )\left[ {\frac{{\sqrt 6 – \sqrt 2 }}{4}\sin 2x + \frac{1}{{\sqrt 6 – \sqrt 2 }}\cos 2x} \right]$ $= (\sqrt 6 – \sqrt 2 )\sin (2x + \alpha )$ với $\frac{{\sqrt 6 – \sqrt 2 }}{4} = \cos \alpha$, $\frac{1}{{\sqrt 6 – \sqrt 2 }} = \sin \alpha .$

Suy ra $– \sqrt 6 + \sqrt 2 \le y \le \sqrt 6 – \sqrt 2 .$

Do đó $\mathop {\max }\limits_R y = \sqrt 6 – \sqrt 2 = M$, $\mathop {\min }\limits_R y = – \sqrt 6 + \sqrt 2 = N.$

Vậy $M + N + 2 = 2.$

<!-- chunk:6 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 6: Số giờ có ánh sáng của một thành phố X ở vĩ độ ${40^0}$ bắc trong ngày thứ $t$ của một năm không nhuận được cho bởi hàm số: $d(t) = 3\sin \left[ {\frac{\pi }{{182}}(t – 80)} \right] + 12$, $t \in Z$ và $0 < t \le 365.$ Vào ngày nào trong năm thì thành phố X có nhiều giờ ánh sáng nhất?

A. $262.$

B. $353.$

C. $80.$

D. $171.$

Chọn D.

Ta có: $d(t) = 3\sin \left[ {\frac{\pi }{{182}}(t – 80)} \right] + 12$ $\le 3 + 12 = 15.$

Dấu bằng xảy ra khi $\sin \left[ {\frac{\pi }{{182}}(t – 80)} \right] = 1$ $\Leftrightarrow \frac{\pi }{{182}}(t – 80) = \frac{\pi }{2} + k2\pi$ $(k \in Z).$

$\Leftrightarrow t = 171 + 364k.$

Mặt khác $t \in (0;365]$ nên $0 < 171 + 364k \le 365$ $\Leftrightarrow – \frac{{171}}{{364}} < k \le \frac{{194}}{{364}}.$

Mà $k \in Z$ nên $k = 0.$

Vậy $t = 171.$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 7: Hàm số $y = 2\cos 3x + 3\sin 3x – 2$ có tất cả bao nhiêu giá trị nguyên?

A. $7.$

B. $3.$

C. $5.$

D. $6.$

Chọn A.

Tập xác định: $D = R.$

$y = 2\cos 3x + 3\sin 3x – 2$ $= \sqrt {13} \left( {\frac{2}{{\sqrt {13} }}\cos 3x + \frac{3}{{\sqrt {13} }}\sin 3x} \right) – 2.$

$\Leftrightarrow y = \sqrt {13} \sin \left( {3x + \arccos \frac{3}{{\sqrt {13} }}} \right) – 2.$

Để hàm số $y$ có giá trị nguyên $\Leftrightarrow \sqrt {13} \sin \left( {3x + \arccos \frac{3}{{\sqrt {13} }}} \right)$ nguyên.

$\Leftrightarrow \sin \left( {3x + \arccos \frac{3}{{\sqrt {13} }}} \right) = \frac{n}{{\sqrt {13} }}$ (với $n$ là một số nguyên).

Mà: $\sin \left( {3x + \arccos \frac{3}{{\sqrt {13} }}} \right) \in [ – 1;1]$ $\Rightarrow – 1 \le \frac{n}{{\sqrt {13} }} \le 1$ $\Leftrightarrow – \sqrt {13} \le n \le \sqrt {13} .$

Mà: $n \in Z$ $\Rightarrow n = \{ 0; \pm 1; \pm 2 \pm 3\} .$

$\Rightarrow y$ có $7$ giá trị nguyên.

<!-- chunk:8 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 8: Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số sau $y = 2{\sin ^2}x + {\cos ^2}2x.$

A. $\max y = 4$, $\min y = \frac{3}{4}.$

B. $\max y = 3$, $\min y = 2.$

C. $\max y = 4$, $\min y = 2.$

D. $\max y = 3$, $\min y = \frac{3}{4}.$

Chọn D.

Đặt $t = {\sin ^2}x$, $0 \le t \le 1$ $\Rightarrow \cos 2x = 1 – 2t.$

$\Rightarrow y = 2t + {(1 – 2t)^2}$ $= 4{t^2} – 2t + 1$ $= {\left( {2t – \frac{1}{2}} \right)^2} + \frac{3}{4}.$

Cách 1: Do $0 \le t \le 1$ $\Rightarrow – \frac{1}{2} \le 2t – \frac{1}{2} \le \frac{3}{2}$ $\Rightarrow 0 \le {\left( {2t – \frac{1}{2}} \right)^2} \le \frac{9}{4}$ $\Rightarrow \frac{3}{4} \le y \le 3.$

Cách 2: Có $y’ = 8t – 2$ $\Rightarrow y’ = 0$ $\Leftrightarrow t = \frac{1}{4} \in [0;1].$

Ta có: $y(0) = 1$, $y\left( {\frac{1}{4}} \right) = \frac{3}{4}$, $y(1) = 3.$

Vậy:

$\max y = 3$ đạt được khi $x = \frac{\pi }{2} + k\pi .$

$\min y = \frac{3}{4}$ đạt được khi ${\sin ^2}x = \frac{1}{4}$ $\Leftrightarrow \frac{{1 – \cos 2x}}{2} = \frac{1}{4}$ $\Leftrightarrow \cos 2x = \frac{1}{2}$ $\Leftrightarrow 2x = \pm \frac{\pi }{3} + k2\pi$ $\Leftrightarrow x = \pm \frac{\pi }{6} + k\pi .$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 9: Gọi $M$ và $m$ lần lượt là GTLN và GTNN của hàm số $y = {\sin ^4}x + {\cos ^4}x + \sin 2x.$ Tổng $M + m$ là?

A. $\frac{{ – 3}}{2}.$

B. $– \frac{1}{2}.$

C. $\frac{3}{2}.$

D. $1.$

Chọn D.

Ta có: $y = {\sin ^4}x + {\cos ^4}x + \sin 2x$ $= 1 – \frac{1}{2}{\sin ^2}2x + \sin 2x$ $= – \frac{1}{2}{\sin ^2}2x + \sin 2x + 1.$

Đặt $t = \sin 2x$ $( – 1 \le t \le 1).$

$y = – \frac{1}{2}{t^2} + t + 1$ $( – 1 \le t \le 1)$ là parabol có đỉnh $I\left( { – \frac{b}{{2a}};y\left( {\frac{{ – b}}{{2a}}} \right)} \right)$ $\Rightarrow I\left( {1;\frac{3}{2}} \right)$ $\Rightarrow t = 1 \in [ – 1;1].$

$y( – 1) = – \frac{1}{2}$, $y(1) = \frac{3}{2}.$

Suy ra $M = \frac{3}{2}$, $m = \frac{{ – 1}}{2}.$

Vậy $M + m = 1.$

<!-- chunk:10 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 10: Cho hàm số $y = \frac{{\sin x – 2\cos x}}{{\sin x + \cos x + 3}}.$ Gọi $m$, $M$ lần lượt là giá trị nhỏ nhất và giá trị lớn nhất của hàm số đã cho. Tính $7m – 5M$ bằng?

A. $10.$

B. $1.$

C. $0.$

D. $-10.$

Chọn D.

Tập xác định: $D = R.$

Ta có: $y = \frac{{\sin x – 2\cos x}}{{\sin x + \cos x + 3}}$ $\Leftrightarrow (1 – y)\sin x – (y + 2)\cos x = 3y.$

Phương trình trên có nghiệm $\Leftrightarrow {(1 – y)^2} + {(y + 2)^2} \ge 9{y^2}.$

$\Leftrightarrow 7{y^2} – 2y – 5 \le 0$ $\Leftrightarrow – \frac{5}{7} \le y \le 1$ $\Rightarrow m = – \frac{5}{7}$, $M = 1.$

Vậy $7m – 5M = – 5 – 5 = – 10.$

<!-- chunk:11 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 11: Hàm số $y = \frac{{3\sin 4x – 4\left( {{{\sin }^4}x + {{\cos }^4}x} \right)}}{{2{{\cos }^2}2x – \sin 4x + 2}}$ có giá trị lớn nhất $M$ và giá trị nhỏ nhất $m.$ Khi đó tổng $M + m$ bằng?

A. $0.$

B. $– \frac{5}{7}.$

C. $– \frac{{10}}{7}.$

D. $\frac{3}{7}.$

Chọn C.

Tập xác định: $D = R.$

Ta có: $3\sin 4x – 4\left( {{{\sin }^4}x + {{\cos }^4}x} \right)$ $= 3\sin 4x – 4\left( {1 – 2{{\sin }^2}x{{\cos }^2}x} \right)$ $= 2{\sin ^2}2x + 3\sin 4x – 4$ $= 3\sin 4x – \cos 4x – 3.$

Xét mẫu thực: $2{\cos ^2}2x – \sin 4x + 2$ $= \cos 4x – \sin 4x + 3.$

Suy ra $y = \frac{{3\sin 4x – 4\left( {{{\sin }^4}x + {{\cos }^4}x} \right)}}{{2{{\cos }^2}2x – \sin 4x + 2}}$ $= \frac{{3\sin 4x – \cos 4x – 3}}{{\cos 4x – \sin 4x + 3}}.$

$\Leftrightarrow (3 + y)\sin x – (y + 1)\cos x = 3y + 3.$

Phương trình trên có nghiệm $\Leftrightarrow {(3 + y)^2} + {(y + 1)^2} \ge {(3y + 3)^2}.$

$\Leftrightarrow 7{y^2} + 10y – 1 \le 0$ $\Leftrightarrow \frac{{ – 5 – 4\sqrt 2 }}{7} \le y \le \frac{{ – 5 + 4\sqrt 2 }}{7}$ $\Rightarrow m + M = – \frac{{10}}{7}.$

<!-- chunk:12 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 12: Giá trị lớn nhất $M$, giá trị nhỏ nhất $m$ của hàm số $y = 2{\cos ^2}x – 2\sqrt 3 \sin x\cos x + 1$ là?

A. $M = 4$, $m = 0.$

B. $M = 3$, $m = 0.$

C. $M = 3$, $m = 1.$

D. $M = 4$, $m = 1.$

Chọn A.

Tập xác định: $D = R.$

Ta có: $y = 2{\cos ^2}x – 2\sqrt 3 \sin x\cos x + 1$ $= \cos 2x – \sqrt 3 \sin 2x + 2$ $= 2\left( {\frac{1}{2}\cos 2x – \frac{{\sqrt 3 }}{2}\sin 2x} \right) + 2$ $= 2\cos \left( {2x + \frac{\pi }{3}} \right) + 2.$

Mặt khác $0 \le 2\cos \left( {2x + \frac{\pi }{3}} \right) + 2 \le 4$, $\forall x \in R$ $\Leftrightarrow 0 \le y \le 4$, $\forall x \in R.$

Vậy:

Giá trị lớn nhất của hàm số là $M = 4$ khi $x = \frac{{ – \pi }}{6} + k\pi .$

Giá trị nhỏ nhất của hàm số là $m = 0$ khi $x = \frac{\pi }{3} + k\pi .$

<!-- chunk:13 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 13: Cho hàm số $y = \frac{{\sin x + 2\cos x + 1}}{{\sin x + \cos x + 2}}.$ Gọi $M$, $m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số. Tổng $M + m$ bằng?

A. $1.$

B. $-2.$

C. $-1.$

D. $2.$

Chọn C.

Tập xác định $D = R$ (do $\sin x + \cos x + 2 > 0$, $\forall x \in R$).

Xét phương trình: $y = \frac{{\sin x + 2\cos x + 1}}{{\sin x + \cos x + 2}}$ $\Leftrightarrow (1 – y)\sin x + (2 – y)\cos x + 1 – 2y = 0.$

Phương trình trên có nghiệm $\Leftrightarrow {(1 – y)^2} + {(2 – y)^2} \ge {(1 – 2y)^2}$ $\Leftrightarrow {y^2} + y – 2 \le 0$ $\Leftrightarrow – 2 \le y \le 1.$

Vậy $M = 1$, $m = – 2$ $\Rightarrow M + m = – 1.$

<!-- chunk:14 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 14: Giá trị lớn nhất của hàm số $y = \frac{{\cos x + 2\sin x + 3}}{{2\cos x – \sin x + 4}}$ là?

A. $3 – 2\sqrt 3 .$

B. $2.$

C. $-1.$

D. $0.$

Chọn B.

Xét phương trình $2\cos x – \sin x + 4 = 0$ $(1).$

Ta có: ${2^2} + {( – 1)^2} < {4^2}$ nên phương trình $(1)$ vô nghiệm, hay $2\cos x – \sin x + 4 \ne 0$, $\forall x \in R.$

Do đó hàm số đã cho có tập xác định $D = R.$

$y = \frac{{\cos x + 2\sin x + 3}}{{2\cos x – \sin x + 4}}$ $\Leftrightarrow (2y – 1)\cos x – (y + 2)\sin x = 3 – 4y$ $(2).$

Để tồn tại giá trị lớn nhất của hàm số ban đầu thì phương trình $(2)$ phải có nghiệm.

$\Leftrightarrow {(2y – 1)^2} + {(y + 2)^2} \ge {(4y – 3)^2}$ $\Leftrightarrow 11{y^2} – 24y + 4 \le 0$ $\Leftrightarrow \frac{2}{{11}} \le y \le 2.$

Vậy GTLN của hàm số đã cho là $2.$

<!-- chunk:15 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 15: Có bao nhiêu giá trị nguyên của tham số $m$ để giá trị lớn nhất của hàm số $y = \frac{{m\sin x + 1}}{{\cos x + 2}}$ nhỏ hơn $2.$

Chọn C.

Dễ thấy $\cos x \ne – 2$, $\forall x \in R$ nên hàm số có tập xác định là $D = R.$

Ta có $y = \frac{{m\sin x + 1}}{{\cos x + 2}}$ $\Leftrightarrow y\cos x + 2y = m\sin x + 1$ $\Leftrightarrow m\sin x – y\cos x = 2y – 1.$

Phương trình trên có nghiệm khi ${m^2} + {y^2} \ge {(2y – 1)^2}$ $\Leftrightarrow 3{y^2} – 4y + 1 – {m^2} \le 0.$

$\Leftrightarrow \frac{{2 – \sqrt {1 + 3{m^2}} }}{3} \le y \le \frac{{2 + \sqrt {1 + 3{m^2}} }}{3}$ $\Rightarrow {y_{\max }} = \frac{{2 + \sqrt {1 + 3{m^2}} }}{3} < 2$ $\Leftrightarrow \sqrt {1 + 3{m^2}} < 4$ $\Leftrightarrow {m^2} < 5.$

Do $m \in Z$ $\Rightarrow m \in \{ – 2; – 1;0;2;1\} .$ Vậy có $5$ giá trị của $m$ thỏa mãn yêu cầu bài toán.

<!-- chunk:16 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 16: Giả sử $M$ là giá trị lớn nhất và $m$ là giá trị nhỏ nhất của hàm số $y = \frac{{\sin x + 2\cos x + 1}}{{\sin x + \cos x + 2}}$ trên $R.$ Tìm $2M – 3m.$

A. $1 + \sqrt 2 .$

B. $0.$

C. $1.$

D. $8.$

Chọn D.

Ta có: $\sin x + \cos x + 2 = 0$ $\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = – 2$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4}} \right) = – \sqrt 2$ (vô nghiệm).

Do đó hàm số đã cho có tập xác định $D = R.$

Ta có $y = \frac{{\sin x + 2\cos x + 1}}{{\sin x + \cos x + 2}}$ $\Leftrightarrow (y – 1)\sin x + (y – 2)\cos x = 1 – 2y.$

Hàm số đạt giá trị lớn nhất, nhỏ nhất khi phương trình trên có nghiệm $\Leftrightarrow {(1 – 2y)^2} \le {(y – 1)^2} + {(y – 2)^2}.$

$\Leftrightarrow 2{y^2} + 2y – 4 \le 0$ $\Leftrightarrow – 2 \le y \le 1.$

Do đó $m = – 2$, $M = 1.$

Vậy $2M – 3m = 8.$

<!-- chunk:17 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 17: Gọi $M$, $m$ tương ứng là giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = \frac{{2\sin x + 2}}{{\cos x – 2}}.$ Khẳng định nào sau đây đúng?

A. $3m + M = 8.$

B. $3m + M = – 8.$

C. $3m + M = 0.$

D. $3m + M = – \frac{8}{3}.$

Chọn B.

Dễ thấy $\cos x \ne 2$, $\forall x \in R$ nên hàm số có tập xác định là $D = R.$

Ta có $y = \frac{{2\sin x + 2}}{{\cos x – 2}}$ $\Leftrightarrow y\cos x – 2\sin x = 2 + 2y.$

Để tồn tại giá trị lớn nhất và giá trị nhỏ nhất của hàm số ban đầu thì phương trình trên phải có nghiệm $\Leftrightarrow {y^2} + 4 \ge {(2 + 2y)^2}$ $\Leftrightarrow 3{y^2} + 8y \le 0$ $\Leftrightarrow – \frac{8}{3} \le y \le 0.$

Do đó 
$$
\left\{ {\begin{array}{l}
{M = 0}\\
{m = – \frac{8}{3}}
\end{array}} \right..
$$

Vậy $3m + M = – 8.$

<!-- chunk:18 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 18: Tập giá trị của hàm số $y = \sin 2x + \sqrt 3 \cos 2x + 1$ là đoạn $[a;b].$ Tính tổng $T = a + b.$

A. $T = 0.$

B. $T = -1.$

C. $T = 1.$

D. $T = 2.$

Chọn D

Cách 1: $y = \sin 2x + \sqrt 3 \cos 2x + 1$ $\Leftrightarrow \sin 2x + \sqrt 3 \cos 2x = y – 1.$

Để tồn tại giá trị lớn nhất và giá trị nhỏ nhất của hàm số ban đầu thì phương trình trên phải có nghiệm $\Leftrightarrow {1^2} + {(\sqrt 3 )^2} \ge {(y – 1)^2}$ $\Leftrightarrow {y^2} – 2y – 3 \le 0$ $\Leftrightarrow – 1 \le y \le 3.$

Suy ra $y \in [ – 1;3].$

Vậy $T = – 1 + 3 = 2.$

Cách 2: Ta có $y – 1 = \sin 2x + \sqrt 3 \cos 2x.$ Mặt khác áp dụng bất đẳng thức Bunhiacopski ta có:

${(y – 1)^2} = {(\sin 2x + \sqrt 3 \cos 2x)^2}$ $\le (1 + 3)\left( {{{\sin }^2}2x + {{\cos }^2}2x} \right) = 4$ $\Leftrightarrow – 2 \le y – 1 \le 2$ $\Leftrightarrow – 1 \le y \le 3.$

Vậy $T = – 1 + 3 = 2.$

Cách 3: $y = \sin 2x + \sqrt 3 \cos 2x + 1$ $= 2\sin \left( {2x + \frac{\pi }{3}} \right) + 1.$

Do $\sin \left( {2x + \frac{\pi }{3}} \right) \in [ – 1;1]$ nên $2\sin \left( {2x + \frac{\pi }{3}} \right) + 1 \in [ – 1;3].$

Vậy $– 1 \le y \le 3.$

<!-- chunk:19 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 19: Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = 3\sin x + 4\cos x – 1.$

A. $\max y = 6$, $\min y = – 4.$

B. $\max y = 8$, $\min y = – 6.$

C. $\max y = 4$, $\min y = – 6.$

D. $\max y = 6$, $\min y = – 8.$

Chọn C.

Ta có $y = 3\sin x + 4\cos x – 1$ $\Leftrightarrow 3\sin x + 4\cos x = y + 1$ $(*).$

Ta coi $(*)$ như là phương trình cổ điển với $a = 3$, $b = 4$, $c = y + 1.$

Phương trình $(*)$ có nghiệm khi và chỉ khi ${a^2} + {b^2} \ge {c^2}$ $\Leftrightarrow 9 + 16 \ge {(y + 1)^2}$ $\Leftrightarrow – 6 \le y \le 4.$

Vậy $\max y = 4$, $\min y = – 6.$

Chú ý:

Ta có thể áp dụng bất đẳng thức Bunhiacopski như sau:

$|y + 1| = |3\sin x + 4\cos x|$ $\le \sqrt {\left( {{3^2} + {4^2}} \right)\left( {{{\sin }^2}x + {{\cos }^2}x} \right)} = 5.$

<!-- chunk:20 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 20: Cho hàm số $y = \sqrt {1 + 2{{\sin }^2}x} + \sqrt {1 + 2{{\cos }^2}x} – 1.$ Gọi $m$, $M$ lần lượt là giá trị nhỏ nhất và giá trị lớn nhất của hàm số. Khi đó giá trị của $M + m$ bằng?

A. $\sqrt 3 + 2\sqrt 2 .$

B. $\sqrt 3 + \sqrt 2 – 1.$

C. $\sqrt 3 + 2\sqrt 2 – 1.$

D. $– \sqrt 3 + 3\sqrt 2 – 1.$

Chọn C.

Đặt $t = \sqrt {1 + 2{{\sin }^2}x} + \sqrt {1 + 2{{\cos }^2}x} .$

$\Rightarrow {t^2} = \left( {1 + 2{{\sin }^2}x} \right) + \left( {1 + 2{{\cos }^2}x} \right)$ $+ 2\sqrt {\left( {1 + 2{{\sin }^2}x} \right)\left( {1 + 2{{\cos }^2}x} \right)}$ $= 4 + 2\sqrt {3 + {{\sin }^2}2x} .$

$\Rightarrow t = \sqrt {4 + 2\sqrt {3 + {{\sin }^2}2x} }$ $\ge \sqrt {4 + 2\sqrt 3 } = 1 + \sqrt 3 .$

$\Rightarrow y = \sqrt {1 + 2{{\sin }^2}x} + \sqrt {1 + 2{{\cos }^2}x} – 1 \ge \sqrt 3 .$

Dấu bằng xảy ra khi $\sin 2x = 0$ $\Leftrightarrow x = \frac{{k\pi }}{2}.$ Khi đó $m = \sqrt 3 .$

Mặt khác: Áp dụng bất đẳng thức Cauchy – Schwarz ta có:

$\sqrt {1 + 2{{\sin }^2}x} + \sqrt {1 + 2{{\cos }^2}x}$ $\le \sqrt {\left( {{1^2} + {1^2}} \right)\left( {1 + 2{{\sin }^2}x + 1 + 2{{\cos }^2}x} \right)}$ $= 2\sqrt 2 .$

$\Rightarrow y = \sqrt {1 + 2{{\sin }^2}x} + \sqrt {1 + 2{{\cos }^2}x} – 1$ $\le 2\sqrt 2 – 1.$

Dấu bằng xảy ra khi ${\sin ^2}x = {\cos ^2}x$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = – \frac{\pi }{4} + k\pi }\\
{x = \frac{\pi }{4} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$ Khi đó $M = 2\sqrt 2 – 1.$

Vậy $M + m = \sqrt 3 + 2\sqrt 2 – 1.$

<!-- chunk:21 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 21: Tìm giá trị lớn nhất của hàm số $y = \frac{{2\sin x + 3\cos x + 1}}{{\sin x – \cos x + 2}}.$

A. $\frac{{3 + \sqrt {33} }}{2}.$

B. $\frac{{3 – \sqrt {33} }}{2}.$

C. $3.$

D. $\frac{1}{2}.$

Chọn A.

Ta có: $y = \frac{{2\sin x + 3\cos x + 1}}{{\sin x – \cos x + 2}}$ $\Leftrightarrow (y – 2)\sin x – (y + 3)\cos x = 1 – 2y.$

${(1 – 2y)^2}$ $= {[(y – 2)\sin x – (y + 3)\cos x]^2}$ $\le \left[ {{{(y – 2)}^2} + {{(y + 3)}^2}} \right]\left( {{{\sin }^2}x + {{\cos }^2}x} \right).$

$\Leftrightarrow 2{y^2} – 6y – 12 \le 0.$

$\Leftrightarrow \frac{{3 – \sqrt {33} }}{2} \le y \le \frac{{3 + \sqrt {33} }}{2}.$

<!-- chunk:22 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 22: Giá trị nhỏ nhất và giá trị lớn nhất của hàm số $f(x) = {\sin ^{2018}}x + {\cos ^{2018}}x$ lần lượt là:

A. $\frac{1}{{{2^{1008}}}}$ và $2.$

B. $\frac{1}{{{2^{1009}}}}$ và $1.$

C. $0$ và $1.$

D. $\frac{1}{{{2^{1008}}}}$ và $\$ 1.\Chọn D.

Đặt $a = {\sin ^2}x$, $b = {\cos ^2}x.$

Ta có: ${\sin ^{2018}}x + {\cos ^{2018}}x \le {\sin ^2}x + {\cos ^2}x = 1.$ Dấu bằng xảy ra $\Leftrightarrow x = k\frac{\pi }{2}.$

${\sin ^{2018}}x + {\cos ^{2018}}x$ $= 2\left( {\frac{{{a^{1009}} + {b^{1009}}}}{2}} \right)$ $\ge 2{\left( {\frac{{a + b}}{2}} \right)^{1009}} = \frac{1}{{{2^{1008}}}}.$

Dấu bằng xảy ra $\Leftrightarrow x = \frac{\pi }{4} + k\frac{\pi }{2}.$

Vậy giá trị nhỏ nhất bằng $\frac{1}{{{2^{1008}}}}$, giá trị lớn nhất bằng $1.$

<!-- chunk:23 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 23: Cho $x$, $y$ là các số thực thỏa mãn $\cos 2x + \cos 2y = 1.$ Giá trị nhỏ nhất của biểu thức $P = {\tan ^2}x + {\tan ^2}y$ bằng?

A. $\frac{1}{3}.$

B. $\frac{2}{3}.$

C. $\frac{8}{3}.$

D. $3.$

Chọn B.

Ta có: $P = \left( {\frac{1}{{{{\cos }^2}x}} – 1} \right) + \left( {\frac{1}{{{{\cos }^2}y}} – 1} \right)$ $= 2\left( {\frac{1}{{1 + \cos 2x}} + \frac{1}{{1 + \cos 2y}}} \right) – 2.$

Áp dụng BĐT cộng mẫu, ta được: $P \ge 2\left( {\frac{{{{(1 + 1)}^2}}}{{2 + \cos 2x + \cos 2y}}} \right) – 2$ $= 2.\frac{4}{{2 + 1}} – 2 = \frac{2}{3}.$

<!-- chunk:24 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 24: Cho hai số thực $x$, $y$ thuộc $\left( {0;\frac{\pi }{2}} \right)$ và thỏa mãn $\cos 2x + \cos 2y + 2\sin (x + y) = 2.$ Giá trị nhỏ nhất của $P = \frac{{{{\cos }^4}x}}{y} + \frac{{{{\cos }^4}y}}{x}$ bằng?

A. $\frac{2}{{3\pi }}.$

B. $\frac{3}{\pi }.$

C. $\frac{2}{\pi }.$

D. $\frac{5}{\pi }.$

Chọn C.

Ta có $\cos 2x + \cos 2y + 2\sin (x + y) = 2$ $\Leftrightarrow {\sin ^2}x + {\sin ^2}y = \sin (x + y).$

Suy ra $x + y = \frac{\pi }{2}.$

Áp dụng BĐT cộng mẫu $\frac{{{a^2}}}{m} + \frac{{{b^2}}}{n} \ge \frac{{{{(a + b)}^2}}}{{m + n}}$ ta được:

$P \ge \frac{{{{\left( {{{\cos }^2}x + {{\cos }^2}y} \right)}^2}}}{{x + y}}$ $= \frac{{{{\left[ {{{\cos }^2}x + {{\cos }^2}\left( {\frac{\pi }{2} – x} \right)} \right]}^2}}}{{x + y}}$ $= \frac{{{{\left[ {{{\cos }^2}x + {{\sin }^2}x} \right]}^2}}}{{x + y}}$ $= \frac{2}{\pi }.$

Dấu bằng xảy ra $\Leftrightarrow x = y = \frac{\pi }{4}.$

Nhận xét: Việc suy ra $x + y = \frac{\pi }{2}$ được chứng minh như sau:

Với $x$, $y \in \left( {0;\frac{\pi }{2}} \right)$ suy ra $\frac{\pi }{2} – x$, $\frac{\pi }{2} – y$ cùng thuộc $\left( {0;\frac{\pi }{2}} \right).$

Trên đoạn $\left[ {0;\frac{\pi }{2}} \right]$, hàm $y = \sin x$ đồng biến.

Nếu $x + y > \frac{\pi }{2}$
\Rightarrow \left\{ {\begin{array}{l}
{x > \frac{\pi }{2} – y \Rightarrow \sin x > \sin \left( {\frac{\pi }{2} – y} \right) = \cos y}\\
{y > \frac{\pi }{2} – x \Rightarrow \sin y > \sin \left( {\frac{\pi }{2} – x} \right) = \cos x}
\end{array}} \right..
$\Rightarrow {\sin ^2}x + {\sin ^2}y$ $= \sin x.\sin x + \sin y.\sin y$ $> \sin x.\cos y + \sin y.\cos x$ $= \sin (x + y)$: mâu thuẫn.

Tương tự cho $x + y < \frac{\pi }{2}.$

Trường hợp $x + y = \frac{\pi }{2}$: thỏa mãn.

<!-- chunk:25 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 25: Cho $a$, $b$, $c$ là các số thực thỏa mãn ${a^2} + {b^2} + {c^2} = 4.$ Tìm giá trị lớn nhất $M$ trong tất cả các hàm số $y = a + b\sqrt {\sin x} + c\sqrt {\cos x}$ với $x \in \left( {0;\frac{\pi }{4}} \right].$

A. $M = \sqrt {1 + \sqrt 2 } .$

B. $M = 1 + \sqrt 2 .$

C. $M = 2\sqrt {1 + \sqrt 2 } .$

D. $M = 2(1 + \sqrt 2 ).$

Chọn C.

Ta có ${(a + b\sqrt {\sin x} + c\sqrt {\cos x} )^2}$ $\le \left( {{a^2} + {b^2} + {c^2}} \right)(1 + \sin x + \cos x)$ $= 4\left[ {1 + \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right)} \right]$ $\le 4(1 + \sqrt 2 ).$

Suy ra $a + b\sqrt {\sin x} + c\sqrt {\cos x} \le 2\sqrt {1 + \sqrt 2 } .$

Dấu bằng xảy ra
\Leftrightarrow \left\{ {\begin{array}{l}
{a = \frac{b}{{\sqrt {\sin x} }} = \frac{c}{{\sqrt {\cos x} }}}\\
{{a^2} + {b^2} + {c^2} = 4}\\
{\sin \left( {x + \frac{\pi }{4}} \right) = 1}
\end{array}} \right.
$$
, $x \in \left( {0;\frac{\pi }{4}} \right]$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
\begin{array}{l}
a = \frac{{2\sqrt[4]{2}}}{{\sqrt {2 + \sqrt 2 } }}\\
b = c = \frac{2}{{\sqrt {2 + \sqrt 2 } }}
\end{array}\\
{x = \frac{\pi }{4}}
\end{array}} \right..
$$

<!-- chunk:26 level:2 source:https://toanmath.com/2019/09/bai-toan-tim-gia-tri-lon-nhat-nho-nhat-cua-ham-so-luong-giac.html -->
## Bài toán 26: Tập giá trị của hàm số $y = \sin 2x + \sqrt 3 \cos 2x + 1$ là đoạn $[a;b].$ Tính tổng $T = a + b.$

A. $T = 1.$

B. $T = 2.$

C. $T = 0.$

D. $T = -1.$

Chọn B.

Ta có $y – 1 = \sin 2x + \sqrt 3 \cos 2x.$

Mặt khác áp dụng bất đẳng thức Bunhiacopski ta có:

${(y – 1)^2}$ $= {(\sin 2x + \sqrt 3 \cos 2x)^2}$ $\le (1 + 3)\left( {{{\sin }^2}2x + {{\cos }^2}2x} \right) = 4$ $\Leftrightarrow – 2 \le y – 1 \le 2$ $\Leftrightarrow – 1 \le y \le 3.$

Vậy $T = – 1 + 3 = 2.$